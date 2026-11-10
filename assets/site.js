/* 1) Parametry kampanii (utm_*, fbclid, gclid) z adresu strony doklejane do linków
      Naffy i do linków oznaczonych data-utm, żeby atrybucja przetrwała przejście do zakupu.
   2) Licznik sekund kuli oddechu na stronie głównej, zsynchronizowany z animacją CSS. */
(function () {
  var KEEP = /^(utm_[a-z]+|fbclid|gclid|ttclid)$/;

  function carryCampaign() {
    var params = new URLSearchParams(location.search);
    var keep = [];
    params.forEach(function (v, k) { if (KEEP.test(k)) keep.push([k, v]); });
    if (!keep.length) return;
    document.querySelectorAll('a[href*="naffy.io"], a[data-utm]').forEach(function (a) {
      try {
        var u = new URL(a.getAttribute('href'), location.href);
        keep.forEach(function (p) { if (!u.searchParams.has(p[0])) u.searchParams.set(p[0], p[1]); });
        a.href = u.toString();
      } catch (e) { /* zostaw link bez zmian */ }
    });
  }

  function breathCounter() {
    var orb = document.querySelector('.breath__orb');
    var phase = document.querySelector('.breath__phase');
    var count = document.querySelector('.breath__count');
    if (!orb || !phase || !count || !orb.getAnimations) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var anim = orb.getAnimations()[0];
    if (!anim) return;
    var IN = 4000, CYCLE = 10000, last = '';
    function tick() {
      var t = (Number(anim.currentTime) || 0) % CYCLE;
      var inhale = t < IN;
      var left = Math.ceil(((inhale ? IN : CYCLE) - t) / 1000);
      var label = inhale ? 'wdech' : 'wydech';
      var key = label + left;
      if (key !== last) { phase.textContent = label; count.textContent = String(left); last = key; }
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  // Pasek zakupu na telefonie znika, gdy widać już główny przycisk „Kup”.
  function buybar() {
    var bar = document.querySelector('.buybar');
    var targets = document.querySelectorAll('#kup, .closer');
    if (!bar || !targets.length || !('IntersectionObserver' in window)) return;
    var visible = new Set();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) visible.add(e.target); else visible.delete(e.target); });
      bar.classList.toggle('is-hidden', visible.size > 0);
    });
    targets.forEach(function (t) { io.observe(t); });
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () { carryCampaign(); breathCounter(); buybar(); });
})();
