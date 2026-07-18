/* Ketonemia glossary filter.
   Client-side only: no network, no storage, no tracking.
   Content is static HTML; this script only filters what is already on the page. */
(function () {
  "use strict";
  var input = document.getElementById("glossary-search");
  if (!input) return;
  var terms = Array.prototype.slice.call(document.querySelectorAll(".glossary-term"));
  var countEl = document.getElementById("glossary-count");
  var emptyEl = document.getElementById("glossary-empty");
  var total = terms.length;

  function apply() {
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    terms.forEach(function (t) {
      var hay = (t.getAttribute("data-search") || t.textContent || "").toLowerCase();
      var match = q === "" || hay.indexOf(q) !== -1;
      t.hidden = !match;
      if (match) shown++;
    });
    if (countEl) {
      var label = shown + (shown === 1 ? " term" : " terms");
      countEl.textContent = q ? label + " matching “" + input.value.trim() + "”" : total + " terms";
    }
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  input.addEventListener("input", apply);
})();
