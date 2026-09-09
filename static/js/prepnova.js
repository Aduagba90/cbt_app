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

    /* ---------- Copy-to-clipboard buttons ---------- */
    document.querySelectorAll("[data-copy]").forEach(function (b) {
      b.addEventListener("click", function () {
        var txt = b.getAttribute("data-copy"), orig = b.innerHTML;
        var done = function () { b.innerHTML = '<i class="bi bi-check2 me-1"></i>' + (b.getAttribute("data-copied") || "Copied!"); setTimeout(function () { b.innerHTML = orig; }, 1800); };
        if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(txt).then(done, function () { window.prompt("Copy this link:", txt); }); }
        else { window.prompt("Copy this link:", txt); }
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

/* ===== Landing motion pack ===== */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.addEventListener("DOMContentLoaded", function () {
    /* ---------- Rotating headline word (all words share one grid cell → no layout shift) ---------- */
    document.querySelectorAll("[data-rotate]").forEach(function (box) {
      var words = box.querySelectorAll(".pn-rotate-word");
      if (words.length < 2 || reduce) return;
      var i = 0;
      setInterval(function () {
        var cur = words[i];
        cur.classList.remove("on"); cur.classList.add("out");
        setTimeout(function () {
          cur.classList.remove("out");
          i = (i + 1) % words.length;
          words[i].classList.add("on");
        }, 280);
      }, 2600);
    });

    /* ---------- Countdown (days) ---------- */
    document.querySelectorAll("[data-countdown]").forEach(function (el) {
      var d = new Date(el.getAttribute("data-countdown") + "T00:00:00");
      if (isNaN(d)) return;
      var days = Math.max(0, Math.ceil((d - new Date()) / 86400000));
      el.textContent = days;
    });

    /* ---------- Try a real question ---------- */
    var box = document.getElementById("pnTry");
    if (box) {
      var src = box.getAttribute("data-src"), q = null, right = 0, total = 0, lastId = 0;
      var $ = function (n) { return box.querySelector("[data-try='" + n + "']"); };
      var load = function () {
        box.classList.add("loading");
        $("explanation").hidden = true;
        fetch(src + "?skip=" + lastId, { credentials: "same-origin" }).then(function (r) { return r.json(); }).then(function (j) {
          box.classList.remove("loading");
          if (!j || !j.ok) { $("text").textContent = "Create a free account to practise thousands of questions."; $("options").innerHTML = ""; return; }
          q = j; lastId = j.id;
          $("subject").textContent = j.subject;
          $("difficulty").textContent = j.difficulty || "";
          $("text").textContent = j.text;
          var opts = $("options"); opts.innerHTML = "";
          ["A", "B", "C", "D"].forEach(function (k) {
            var b = document.createElement("button");
            b.type = "button"; b.className = "pn-try-opt"; b.setAttribute("data-key", k);
            b.innerHTML = '<span class="key"></span><span class="txt"></span>';
            b.querySelector(".key").textContent = k;
            b.querySelector(".txt").textContent = j.options[k] || "";
            b.addEventListener("click", function () { answer(k, b); });
            opts.appendChild(b);
          });
        }).catch(function () { box.classList.remove("loading"); $("text").textContent = "Could not load a question right now. Please try again."; });
      };
      var answer = function (k, btn) {
        if (!q) return;
        var buttons = box.querySelectorAll(".pn-try-opt");
        buttons.forEach(function (b) { b.disabled = true; });
        total += 1;
        var ok = k === q.answer;
        if (ok) { right += 1; btn.classList.add("correct"); }
        else {
          btn.classList.add("wrong");
          var c = box.querySelector(".pn-try-opt[data-key='" + q.answer + "']");
          if (c) c.classList.add("correct");
        }
        var exp = $("explanation");
        exp.innerHTML = "<b></b> <span></span>";
        exp.querySelector("b").textContent = ok ? "Correct! " : "Not quite — the answer is " + q.answer + ". ";
        exp.querySelector("span").textContent = q.explanation || "";
        exp.hidden = false;
        $("score").textContent = "Score: " + right + " / " + total;
        if (navigator.vibrate && !ok) navigator.vibrate(60);
      };
      $("next").addEventListener("click", load);
      if ("IntersectionObserver" in window) {
        var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { load(); o.disconnect(); } }); }, { rootMargin: "200px" });
        o.observe(box);
      } else { load(); }
    }

    /* ---------- Mobile slider dots ---------- */
    document.querySelectorAll("[data-slider]").forEach(function (track) {
      var dots = track.parentElement.querySelector("[data-slider-dots]");
      var slides = track.querySelectorAll(".pn-slide");
      if (!dots || slides.length < 2) return;
      slides.forEach(function (_, i) { var d = document.createElement("span"); if (i === 0) d.className = "on"; dots.appendChild(d); });
      var update = function () {
        var idx = Math.round(track.scrollLeft / (slides[0].offsetWidth + 16));
        dots.querySelectorAll("span").forEach(function (d, i) { d.classList.toggle("on", i === idx); });
      };
      track.addEventListener("scroll", update, { passive: true });
      /* gentle auto-advance on phones until the user touches it */
      if (!reduce && window.matchMedia("(max-width: 767.98px)").matches) {
        var stopped = false, n = 0;
        var timer = setInterval(function () {
          if (stopped) { clearInterval(timer); return; }
          n = (n + 1) % slides.length;
          track.scrollTo({ left: slides[n].offsetLeft - track.offsetLeft, behavior: "smooth" });
        }, 4500);
        ["touchstart", "pointerdown", "wheel"].forEach(function (ev) { track.addEventListener(ev, function () { stopped = true; }, { passive: true, once: true }); });
      }
    });

    /* ---------- Sticky mobile CTA after the hero ---------- */
    var cta = document.querySelector("[data-sticky-cta]");
    var hero = document.querySelector(".pn-hero");
    if (cta && hero) {
      var tryBox = document.getElementById("pnTry");
      var onS = function () {
        var past = window.scrollY > hero.offsetHeight - 80;
        var nearEnd = window.innerHeight + window.scrollY > document.body.scrollHeight - 300;
        /* hide while the interactive question card is on screen so it never covers an answer */
        var overTry = false;
        if (tryBox) { var r = tryBox.getBoundingClientRect(); overTry = r.top < window.innerHeight && r.bottom > 0; }
        var show = past && !nearEnd && !overTry;
        cta.classList.toggle("show", show);
        document.body.classList.toggle("has-sticky-cta", show);
      };
      onS();
      window.addEventListener("scroll", onS, { passive: true });
    }
  });
})();
