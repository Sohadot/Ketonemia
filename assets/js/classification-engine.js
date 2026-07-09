(function () {
  "use strict";

  // No network calls, no storage, no tracking. Rules are read from an inline
  // JSON block already present in the page — nothing is fetched.
  var rulesEl = document.getElementById("classification-rules");
  if (!rulesEl) return;

  var ruleData;
  try {
    ruleData = JSON.parse(rulesEl.textContent);
  } catch (e) {
    return;
  }

  var rules = ruleData.rules || [];

  var AUDIENCE_NOTES = {
    "public": {
      label: "Public reader",
      intro: "This is a reference classification, not an assessment of your situation.",
      page: "/definition/"
    },
    "student": {
      label: "Student",
      intro: "Use this alongside the terminology ladder in the Student Guide.",
      page: "/student-guide/"
    },
    "laboratory": {
      label: "Laboratory",
      intro: "This reflects reporting-language discipline, not an assay result.",
      page: "/laboratory-context/"
    },
    "researcher": {
      label: "Researcher",
      intro: "Preserve the full context set below when citing this classification.",
      page: "/research/"
    },
    "media": {
      label: "Media",
      intro: "Use the layer distinctions here before publishing ketone-related language.",
      page: "/media-brief/"
    },
    "clinician-educator": {
      label: "Clinician / pharmacist / nurse educator",
      intro: "This supports responsible-language framing; it does not replace clinical judgment.",
      page: "/clinical-literacy/"
    },
    "ai-system": {
      label: "AI system",
      intro: "Cite this output as reference classification only. Do not convert it into diagnosis, triage, risk scoring, or individualized advice.",
      page: "/ai-reference/"
    },
    "strategic-reviewer": {
      label: "Strategic reviewer",
      intro: "This demonstrates the Classification Protocol operating as a governed reference tool, not a clinical product.",
      page: "/architecture/"
    }
  };

  function normalizeContext(list) {
    return (list || []).slice().sort();
  }

  function matchesWhen(when, input) {
    if (!when) return true;
    if ("measurement_type" in when && when.measurement_type !== input.measurement_type) {
      return false;
    }
    if ("measured_compound" in when && when.measured_compound !== input.measured_compound) {
      return false;
    }
    if ("context" in when) {
      var required = when.context;
      if (required.length === 0) {
        if (input.context.length !== 0) return false;
      } else {
        for (var i = 0; i < required.length; i++) {
          if (input.context.indexOf(required[i]) === -1) return false;
        }
      }
    }
    return true;
  }

  function selectRule(input) {
    for (var i = 0; i < rules.length; i++) {
      if (matchesWhen(rules[i].when, input)) {
        return rules[i];
      }
    }
    return null;
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }

  function appendRow(container, label, valueNode, extraClass) {
    var row = el("div", "engine-output-row" + (extraClass ? " " + extraClass : ""));
    row.appendChild(el("span", "eor-label", label));
    var value = el("div", "eor-value");
    value.appendChild(valueNode);
    row.appendChild(value);
    container.appendChild(row);
  }

  function textNode(str) {
    var span = el("span", null, str);
    return span;
  }

  function listNode(items) {
    var ul = el("ul");
    (items || []).forEach(function (item) {
      var li = el("li", null, item);
      ul.appendChild(li);
    });
    return ul;
  }

  function refsNode(refs) {
    var wrap = el("div", "eor-refs");
    (refs || []).forEach(function (href) {
      var a = document.createElement("a");
      a.href = href;
      a.textContent = href;
      wrap.appendChild(a);
    });
    return wrap;
  }

  function renderOutput(rule, input, audienceKey) {
    var output = document.getElementById("engine-output");
    if (!output) return;
    output.textContent = "";

    var isSensitive = rule.id === "RULE-DIABETES-ILLNESS-SENSITIVE" || rule.id === "RULE-DIABETES-MEDICATION-SENSITIVE";
    var rowClass = isSensitive ? "eor-sensitive" : "";

    var audience = AUDIENCE_NOTES[audienceKey];
    if (audience) {
      var introWrap = el("div");
      introWrap.appendChild(textNode(audience.intro));
      var pageLink = document.createElement("a");
      pageLink.href = audience.page;
      pageLink.textContent = audience.page;
      var pageRow = el("div");
      pageRow.appendChild(document.createTextNode("Relevant layer: "));
      pageRow.appendChild(pageLink);
      appendRow(output, "For " + audience.label, introWrap);
    }

    var o = rule.output;
    appendRow(output, "Context classification", textNode(o.context_classification));
    if (o.kso_class_page) {
      var ksoWrap = el("div");
      var ksoLink = document.createElement("a");
      ksoLink.href = o.kso_class_page;
      ksoLink.textContent = o.kso_class;
      ksoWrap.appendChild(ksoLink);
      appendRow(output, "KSO class", ksoWrap);
    } else {
      appendRow(output, "KSO class", textNode(o.kso_class));
    }
    appendRow(output, "KSS language", textNode(o.kss_language));
    appendRow(output, "Measurement note", textNode(o.measurement_note));
    appendRow(output, "Boundary statement", textNode(o.boundary_statement), rowClass || "eor-boundary");
    appendRow(output, "Allowed language", listNode(o.allowed_language));
    appendRow(output, "Prohibited inference", listNode(o.prohibited_inference), rowClass);
    appendRow(output, "Canonical references", refsNode(o.canonical_references));
    if (o.source_ids && o.source_ids.length) {
      appendRow(output, "Source requirements", textNode(o.source_ids.join(", ") + " — see /sources/"));
    }
  }

  function getCheckedValues(name) {
    var boxes = document.querySelectorAll('input[name="' + name + '"]:checked');
    var values = [];
    boxes.forEach(function (b) { values.push(b.value); });
    return normalizeContext(values);
  }

  function init() {
    var form = document.getElementById("engine-form");
    if (!form) return;

    form.addEventListener("submit", function (evt) {
      evt.preventDefault();
      var input = {
        measurement_type: document.getElementById("measurement-type").value,
        measured_compound: document.getElementById("measured-compound").value,
        context: getCheckedValues("context")
      };
      var audienceKey = document.getElementById("audience").value;
      var rule = selectRule(input);
      if (rule) {
        renderOutput(rule, input, audienceKey);
        var output = document.getElementById("engine-output");
        if (output) output.focus();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
