/* PrepNova CBT — shared front-end behaviours (no external dependencies besides Bootstrap) */
(function () {
  "use strict";

  /* ---------- Toasts (flash messages) ---------- */
  function toast(message, type) {
    var wrap = document.querySelector(".pn-toast-wrap");
    if (!wrap) {
      wrap = document.createElement("div");
      wrap.className = "pn-toast-wrap";
      document.body.appendChild(wrap);
    }
    var el = document.createElement("div");
    el.className = "pn-toast " + (type || "info");
    var icon = { success: "bi-check-circle-fill", danger: "bi-x-circle-fill", warning: "bi-exclamation-triangle-fill", info: "bi-info-circle-fill" }[type] || "bi-info-circle-fill";
    el.innerHTML = '<i class="bi ' + icon + '"></i><span></span>';
    el.querySelector("span").textContent = message;
    wrap.appendChild(el);
    setTimeout(function () {
      el.style.transition = "opacity .4s ease, transform .4s ease";
      el.style.opacity = "0";
      el.style.transform = "translateY(-6px)";
      setTimeout(function () { el.remove(); }, 420);
    }, 4200);
  }
  window.pnToast = toast;

  document.addEventListener("DOMContentLoaded", function () {
    /* Flash messages rendered server-side as data attributes */
    document.querySelectorAll("[data-pn-flash]").forEach(function (n) {
      toast(n.getAttribute("data-pn-flash"), n.getAttribute("data-pn-flash-type") || "info");
      n.remove();
    });

    /* ---------- Password visibility toggles ---------- */
    document.querySelectorAll("[data-toggle-password]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var input = document.getElementById(btn.getAttribute("data-toggle-password"));
        if (!input) return;
        var show = input.type === "password";
        input.type = show ? "text" : "password";
        btn.innerHTML = show ? '<i class="bi bi-eye-slash"></i>' : '<i class="bi bi-eye"></i>';
        btn.setAttribute("aria-label", show ? "Hide password" : "Show password");
      });
    });

    /* ---------- Password strength meter ---------- */
    document.querySelectorAll("[data-strength-for]").forEach(function (meter) {
      var input = document.getElementById(meter.getAttribute("data-strength-for"));
      var bar = meter.querySelector("span");
      var label = document.querySelector("[data-strength-label='" + meter.getAttribute("data-strength-for") + "']");
      if (!input || !bar) return;
      input.addEventListener("input", function () {
        var v = input.value, s = 0;
        if (v.length >= 8) s++;
        if (/[A-Z]/.test(v)) s++;
        if (/[a-z]/.test(v)) s++;
        if (/\d/.test(v)) s++;
        if (/[^A-Za-z0-9]/.test(v)) s++;
        var pct = v.length === 0 ? 0 : Math.max(15, s * 20);
        var colors = ["#dc2626", "#dc2626", "#f59e0b", "#f59e0b", "#16a34a", "#0b7a4b"];
        var names = ["Too weak", "Weak", "Fair", "Good", "Strong", "Very strong"];
        bar.style.width = pct + "%";
        bar.style.backgroundColor = colors[s];
        if (label) label.textContent = v.length ? names[s] : "";
      });
    });

    /* ---------- Reveal on scroll ---------- */
    var reveals = document.querySelectorAll(".reveal");
    if (reveals.length && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
        });
      }, { threshold: 0.12 });
      reveals.forEach(function (r) { io.observe(r); });
    } else {
      reveals.forEach(function (r) { r.classList.add("in"); });
    }

    /* ---------- Landing nav scroll state ---------- */
    var lnav = document.querySelector(".pn-landing-nav");
    if (lnav) {
      var onScroll = function () { lnav.classList.toggle("scrolled", window.scrollY > 30); };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }

    /* ---------- Animated counters ---------- */
    document.querySelectorAll("[data-count]").forEach(function (el) {
      var target = parseFloat(el.getAttribute("data-count")) || 0;
      var suffix = el.getAttribute("data-suffix") || "";
      var started = false;
      var run = function () {
        if (started) return; started = true;
        var start = null, dur = 1200;
        var step = function (ts) {
          if (!start) start = ts;
          var p = Math.min(1, (ts - start) / dur);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased).toLocaleString() + suffix;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      };
      if ("IntersectionObserver" in window) {
        var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { run(); o.disconnect(); } }); }, { threshold: 0.4 });
        o.observe(el);
      } else { run(); }
    });

    /* ---------- Confirm dialogs for destructive forms/links ---------- */
    document.querySelectorAll("[data-confirm]").forEach(function (el) {
      el.addEventListener("click", function (ev) {
        if (!window.confirm(el.getAttribute("data-confirm"))) { ev.preventDefault(); ev.stopImmediatePropagation(); }
      });
    });

    /* ---------- Prevent double submission ---------- */
    document.querySelectorAll("form[data-once]").forEach(function (f) {
      f.addEventListener("submit", function () {
        var btn = f.querySelector("[type=submit]");
        if (btn && !btn.disabled) {
          btn.disabled = true;
          btn.dataset.orig = btn.innerHTML;
          btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>' + (btn.getAttribute("data-loading") || "Please wait…");
        }
      });
    });

    /* ---------- Auto-dismiss alerts ---------- */
    document.querySelectorAll(".alert[data-autodismiss]").forEach(function (a) {
      setTimeout(function () { a.style.transition = "opacity .4s"; a.style.opacity = "0"; setTimeout(function () { a.remove(); }, 400); }, 6000);
    });

    /* ---------- Bootstrap tooltips ---------- */
    if (window.bootstrap) {
      document.querySelectorAll("[data-bs-toggle='tooltip']").forEach(function (t) { new bootstrap.Tooltip(t); });
    }

    /* ---------- Phone number formatting (Nigeria) ---------- */
    document.querySelectorAll("input[data-ng-phone]").forEach(function (inp) {
      inp.addEventListener("input", function () {
        inp.value = inp.value.replace(/[^\d+]/g, "").slice(0, 14);
      });
    });
  });

  /* ---------- Simple client-side fetch helper (CSRF aware) ---------- */
  window.pnFetch = function (url, options) {
    options = options || {};
    options.headers = options.headers || {};
    var meta = document.querySelector('meta[name="csrf-token"]');
    if (meta) options.headers["X-CSRFToken"] = meta.getAttribute("content");
    options.credentials = "same-origin";
    return fetch(url, options);
  };
})();
