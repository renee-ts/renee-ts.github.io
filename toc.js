// Table of contents behaviour:
//  - bold the entry for the section/subsection currently being read;
//  - expand the subsections of the top-level section being read
//    (the collapsing itself is CSS, wide screens only);
//  - clicking a top-level section jumps to it and expands its subsections.
document.addEventListener("DOMContentLoaded", function () {
  var toc = document.getElementById("TOC");
  if (!toc) return;
  var links = Array.prototype.slice.call(toc.querySelectorAll("a[href^='#']"));
  if (!links.length) return;

  var headings = links.map(function (a) {
    return document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
  });
  // Top-level <li> that each link belongs to.
  var sections = Array.prototype.slice.call(toc.querySelectorAll(":scope > ul > li"));
  var sectionOf = links.map(function (a) {
    return sections.find(function (li) { return li.contains(a); });
  });

  // A section opened by clicking stays open until the reader scrolls into
  // a different section (needed for short final sections that can never
  // scroll up to the "reading" line).
  var clicked = null;
  var activeAtClick; // section the reader was in right after the click

  function currentIndex() {
    var atBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
    if (atBottom) return headings.length - 1;
    // The current heading is the last one that has scrolled past the top third.
    var cutoff = window.innerHeight / 3;
    var active = -1;
    for (var i = 0; i < headings.length; i++) {
      if (headings[i] && headings[i].getBoundingClientRect().top <= cutoff) active = i;
    }
    return active;
  }

  function update() {
    var active = currentIndex();
    var activeSection = active >= 0 ? sectionOf[active] : null;

    if (clicked) {
      // First update after the jump: remember where the click landed us.
      if (activeAtClick === undefined) activeAtClick = activeSection;
      else if (activeSection !== activeAtClick && activeSection !== clicked) clicked = null;
    }

    links.forEach(function (a, i) { a.classList.toggle("active", i === active); });
    sections.forEach(function (li) {
      li.classList.toggle("open", li === activeSection || li === clicked);
    });

    // Keep the active entry visible if the ToC itself scrolls.
    if (active >= 0 && toc.scrollHeight > toc.clientHeight) {
      var top = links[active].offsetTop; // #TOC is position:fixed, so it's the offsetParent
      if (top < toc.scrollTop || top > toc.scrollTop + toc.clientHeight - 40) {
        toc.scrollTop = top - toc.clientHeight / 2;
      }
    }
  }

  sections.forEach(function (li) {
    var a = li.querySelector(":scope > a");
    if (!a) return;
    a.addEventListener("click", function () {
      clicked = li;
      activeAtClick = undefined;
      li.classList.add("open");
      // The browser jumps to the section after this handler returns.
      setTimeout(update, 0);
    });
  });

  var ticking = false;
  window.addEventListener("scroll", function () {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(function () { update(); ticking = false; });
    }
  }, { passive: true });
  window.addEventListener("resize", update);
  update();
});
