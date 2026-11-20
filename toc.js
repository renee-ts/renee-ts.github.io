document.addEventListener("DOMContentLoaded", function () {
  var toc = document.getElementById("TOC");
  if (!toc) return;
  var links = Array.prototype.slice.call(toc.querySelectorAll("a[href^='#']"));
  if (!links.length) return;

  var headings = links.map(function (a) {
    return document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
  });
  var sections = Array.prototype.slice.call(toc.querySelectorAll(":scope > ul > li"));
  var sectionOf = links.map(function (a) {
    return sections.find(function (li) { return li.contains(a); });
  });

  var clicked = null;
  var activeAtClick;

  function currentIndex() {
    var atBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
    if (atBottom) return headings.length - 1;
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
      if (activeAtClick === undefined) activeAtClick = activeSection;
      else if (activeSection !== activeAtClick && activeSection !== clicked) clicked = null;
    }

    links.forEach(function (a, i) { a.classList.toggle("active", i === active); });
    sections.forEach(function (li) {
      li.classList.toggle("open", li === activeSection || li === clicked);
    });

    if (active >= 0 && toc.scrollHeight > toc.clientHeight) {
      var top = links[active].offsetTop;
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
