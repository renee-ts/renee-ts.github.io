document.addEventListener("DOMContentLoaded", function () {
  var bar = document.querySelector(".progress-bar");
  if (!bar) return;

  function update() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var progress = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 1;
    bar.style.transform = "scaleX(" + progress + ")";
  }

  var ticking = false;
  function schedule() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { update(); ticking = false; });
  }

  window.addEventListener("scroll", schedule, { passive: true });
  window.addEventListener("resize", schedule);
  window.addEventListener("load", update);
  update();
});
