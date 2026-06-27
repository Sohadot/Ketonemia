$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")

$requiredFiles = @(
    "README.md",
    "FOUNDATION_DOCTRINE.md",
    "ASSET_THESIS.md",
    "CATEGORY_LANGUAGE.md",
    "KETONEMIA_SIGNAL_ONTOLOGY.md",
    "KETONEMIA_STATE_STANDARD.md",
    "CLINICAL_BOUNDARY.md",
    "CLAIM_POLICY.md",
    "SOURCE_POLICY.md",
    "INTERFACE_THESIS.md",
    "BUYER_LOGIC.md",
    "MONETIZATION_BOUNDARY.md",
    "AI_REFERENCE_POLICY.md",
    "SEO_GOVERNANCE.md",
    "INTERNAL_LINKING_POLICY.md",
    "QUALITY_GATE.md",
    "DECISION_LOG.md",
    "ROADMAP.md"
)

$failures = New-Object System.Collections.Generic.List[string]

function Add-Failure {
    param([string]$Message)
    $failures.Add($Message) | Out-Null
}

function Get-RepoPath {
    param([string]$RelativePath)
    Join-Path $root $RelativePath
}

foreach ($file in $requiredFiles) {
    if (-not (Test-Path -LiteralPath (Get-RepoPath $file) -PathType Leaf)) {
        Add-Failure "Missing required governance file: $file"
    }
}

$readmePath = Get-RepoPath "README.md"
if (Test-Path -LiteralPath $readmePath -PathType Leaf) {
    $readme = Get-Content -LiteralPath $readmePath -Raw

    foreach ($file in $requiredFiles | Where-Object { $_ -ne "README.md" }) {
        if ($readme -notmatch [regex]::Escape("]($file)")) {
            Add-Failure "README.md does not link to required file: $file"
        }
    }

    foreach ($mustMention in @("CLINICAL_BOUNDARY.md", "CLAIM_POLICY.md", "SOURCE_POLICY.md")) {
        if ($readme -notmatch [regex]::Escape($mustMention)) {
            Add-Failure "README.md does not mention required boundary/policy file: $mustMention"
        }
    }
}

$decisionLogPath = Get-RepoPath "DECISION_LOG.md"
if (Test-Path -LiteralPath $decisionLogPath -PathType Leaf) {
    $decisionLog = Get-Content -LiteralPath $decisionLogPath -Raw
    if ($decisionLog -notmatch "DEC-001") {
        Add-Failure "DECISION_LOG.md must contain DEC-001."
    }
    if ($decisionLog -notmatch "Blood Ketone Intelligence Infrastructure" -and $decisionLog -notmatch "blood ketone intelligence infrastructure") {
        Add-Failure "DECISION_LOG.md must contain the Sprint 0 positioning decision."
    }
}

$clinicalBoundaryPath = Get-RepoPath "CLINICAL_BOUNDARY.md"
if (-not (Test-Path -LiteralPath $clinicalBoundaryPath -PathType Leaf)) {
    Add-Failure "CLINICAL_BOUNDARY.md is missing."
}

foreach ($policyFile in @("SOURCE_POLICY.md", "CLAIM_POLICY.md")) {
    if (-not (Test-Path -LiteralPath (Get-RepoPath $policyFile) -PathType Leaf)) {
        Add-Failure "$policyFile is missing."
    }
}

$riskyPhrasePatterns = @(
    "\bdiagnose\b",
    "\btreat\b",
    "you are safe",
    "you have DKA",
    "medical advice"
)

$allowedContextPatterns = @(
    "\bnot\b",
    "\bno\b",
    "\bwithout\b",
    "\bavoid\b",
    "\bprohibit",
    "\bmust not\b",
    "\bdoes not\b",
    "\bdo not\b",
    "\bnever\b",
    "\breplace\b",
    "\bboundary\b",
    "\beducational\b",
    "\bclaim policy\b",
    "\bprohibited\b",
    "\brather than\b"
)

$markdownFiles = Get-ChildItem -LiteralPath $root -Recurse -File -Filter "*.md" |
    Where-Object { $_.FullName -notmatch "\\.git\\" }

foreach ($file in $markdownFiles) {
    $lines = Get-Content -LiteralPath $file.FullName
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $contextStart = [Math]::Max(0, $i - 10)
        $contextEnd = [Math]::Min($lines.Count - 1, $i + 1)
        $contextWindow = ($lines[$contextStart..$contextEnd] -join " ")

        foreach ($pattern in $riskyPhrasePatterns) {
            if ($line -match $pattern) {
                $hasAllowedContext = $false
                foreach ($allowed in $allowedContextPatterns) {
                    if ($contextWindow -match $allowed) {
                        $hasAllowedContext = $true
                        break
                    }
                }

                if (-not $hasAllowedContext) {
                    $relative = Resolve-Path -LiteralPath $file.FullName -Relative
                    Add-Failure "Risky phrase lacks boundary context: $relative line $($i + 1): $line"
                }
            }
        }
    }
}

$linkPattern = [regex]'\[[^\]]+\]\(([^)]+)\)'
foreach ($file in $markdownFiles) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($match in $linkPattern.Matches($content)) {
        $target = $match.Groups[1].Value

        if ($target -match "^[a-zA-Z][a-zA-Z0-9+.-]*:" -or $target.StartsWith("#") -or $target.StartsWith("/")) {
            continue
        }

        $targetWithoutAnchor = ($target -split "#")[0]
        if ([string]::IsNullOrWhiteSpace($targetWithoutAnchor)) {
            continue
        }

        $decodedTarget = [uri]::UnescapeDataString($targetWithoutAnchor)
        $baseDir = Split-Path -Parent $file.FullName
        $candidate = Join-Path $baseDir $decodedTarget

        if (-not (Test-Path -LiteralPath $candidate)) {
            $relative = Resolve-Path -LiteralPath $file.FullName -Relative
            Add-Failure "Broken internal Markdown link in ${relative}: $target"
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Host "Foundation integrity gate failed:" -ForegroundColor Red
    foreach ($failure in $failures) {
        Write-Host " - $failure" -ForegroundColor Red
    }
    exit 1
}

Write-Host "Foundation integrity gate passed." -ForegroundColor Green
Write-Host "Checked $($requiredFiles.Count) required files and $($markdownFiles.Count) Markdown files."
