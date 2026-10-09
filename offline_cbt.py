"""
PrepNova Offline — JAMB CBT Simulator
=====================================
Builds a single self-contained HTML file: the full JAMB mock-exam experience
embedded with real questions from the live bank. The buyer downloads it once
and can then run timed JAMB mocks on any device with a browser — no network,
no data, no account. Scores, resume state and history live in localStorage on
the buyer's device only.

Used by app.pdf_download (paid shop orders) and /offline_free (subscribers).
"""

import io
import json
from datetime import datetime

ENGLISH_SUBJECT = "Use of English"
SUBJECT_CAP = 500          # max questions embedded per subject
TEMPLATE_TOKEN = "__PN_DATA__"


# ---------------------------------------------------------------------------
# Question bank loading
# ---------------------------------------------------------------------------

def _load_bank(conn):
    """Return (subjects, passages) ready for JSON embedding.

    subjects: [{"n": "Use of English", "q": [[stem, a, b, c, d, ans, expl, pid], ...]}, ...]
              English first, then the other active JAMB subjects.
    passages: {"<pid>": "<passage_text>"} for every passage referenced.
    """
    names = [r[0] for r in conn.execute(
        "SELECT DISTINCT s.subject_name FROM subjects s "
        "JOIN questions_v2 q ON q.subject_id = s.id "
        "WHERE s.exam_type = 'JAMB' AND q.status = 'Active' "
        "ORDER BY s.subject_name").fetchall()]
    subjects, others, pids = [], [], set()
    for name in names:
        rows = conn.execute(
            "SELECT q.question_text, q.option_a, q.option_b, q.option_c, q.option_d, "
            "q.correct_answer, COALESCE(q.explanation, ''), q.passage_id "
            "FROM questions_v2 q JOIN subjects s ON s.id = q.subject_id "
            "WHERE s.exam_type = 'JAMB' AND s.subject_name = ? AND q.status = 'Active' "
            "ORDER BY RANDOM() LIMIT ?", (name, SUBJECT_CAP)).fetchall()
        pack = []
        for r in rows:
            ans = (r[5] or "").strip().upper()
            if ans not in ("A", "B", "C", "D"):
                continue
            pid = r[7]
            pack.append([r[0], r[1], r[2], r[3], r[4], ans, r[6], pid])
            if pid is not None:
                pids.add(pid)
        if len(pack) < 40:      # not enough to run a 40-question paper offline
            continue
        (subjects if name == ENGLISH_SUBJECT else others).append({"n": name, "q": pack})
    subjects += others
    if not subjects or subjects[0]["n"] != ENGLISH_SUBJECT:
        raise RuntimeError("JAMB Use of English bank missing — cannot build offline pack")
    passages = {}
    for pid in pids:
        row = conn.execute("SELECT passage_text FROM passages WHERE id = ?", (pid,)).fetchone()
        if row and row[0]:
            passages[str(pid)] = row[0]
    return subjects, passages


def build_offline_jamb_html(conn, site_url, buyer_name="", buyer_ref=""):
    """Build the complete single-file simulator as a BytesIO (text/html)."""
    subjects, passages = _load_bank(conn)
    data = {
        "title": "PrepNova Offline — JAMB CBT Simulator",
        "built": datetime.utcnow().strftime("%d %B %Y"),
        "site": site_url,
        "buyer": {"name": (buyer_name or "PrepNova student").strip()[:60],
                  "ref": (buyer_ref or "").strip()[:40]},
        "english": ENGLISH_SUBJECT,
        "subjects": subjects,
        "passages": passages,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")          # never terminate the <script> block
    html = _TEMPLATE.replace(TEMPLATE_TOKEN, payload)
    return io.BytesIO(html.encode("utf-8"))


# ---------------------------------------------------------------------------
# The single-file app (all CSS + JS inline; zero external requests)
# ---------------------------------------------------------------------------

_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>PrepNova Offline — JAMB CBT Simulator</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{--pri:#0b7a4b;--pri600:#096640;--pri50:#e9f7f0;--gold:#f2b705;--navy:#0f1f3d;--navy2:#14285a;
--ink:#1f2937;--mut:#6b7280;--line:#e5e7eb;--bg:#f4f6f9;--card:#fff;--ok:#16a34a;--warn:#f59e0b;--bad:#dc2626;--info:#0284c7}
html{-webkit-text-size-adjust:100%}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55;min-height:100vh}
button{font:inherit;cursor:pointer;touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.pn-top{background:linear-gradient(135deg,var(--navy) 0%,var(--navy2) 100%);color:#fff;padding:12px 16px;display:flex;align-items:center;gap:12px;position:sticky;top:0;z-index:40;box-shadow:0 2px 10px rgba(15,31,61,.25)}
.pn-logo{width:38px;height:38px;border-radius:10px;background:var(--pri);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:15px;flex:none;box-shadow:inset 0 -2px 0 rgba(0,0,0,.25)}
.pn-top .t{font-weight:700;font-size:1rem;line-height:1.2}
.pn-top .s{font-size:.75rem;opacity:.75}
.pill{display:inline-flex;align-items:center;gap:5px;background:rgba(242,183,5,.16);border:1px solid rgba(242,183,5,.55);color:#ffd75e;font-size:.68rem;font-weight:700;letter-spacing:.4px;padding:3px 9px;border-radius:999px;white-space:nowrap}
.pn-top .timer{margin-left:auto;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.25);padding:6px 12px;border-radius:10px;font-weight:700;font-variant-numeric:tabular-nums;font-size:1rem}
.pn-top .timer.low{background:var(--bad);border-color:var(--bad);animation:blink 1s step-end infinite}
@keyframes blink{50%{opacity:.55}}
.pn-top .submit-top{background:var(--gold);color:var(--navy);border:none;font-weight:800;padding:8px 14px;border-radius:10px;font-size:.85rem}
.wrap{max-width:1060px;margin:0 auto;padding:18px 14px 60px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;box-shadow:0 1px 3px rgba(15,31,61,.06);margin-bottom:16px}
.h1{font-size:1.45rem;font-weight:800;letter-spacing:-.02em}
.h2{font-size:1.05rem;font-weight:800;margin-bottom:12px}
.mut{color:var(--mut)}.small{font-size:.82rem}
.hero{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;border-radius:16px;padding:26px 22px;margin-bottom:16px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(242,183,5,.25),transparent 70%)}
.hero .h1{color:#fff}
.hero p{opacity:.85;margin-top:6px;max-width:560px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.stat{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);padding:6px 12px;border-radius:999px;font-size:.78rem;font-weight:600}
.stat b{color:var(--gold)}
.mode-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.mode{border:2px solid var(--line);border-radius:12px;padding:14px;cursor:pointer;background:#fff}
.mode.on{border-color:var(--pri);background:var(--pri50)}
.mode .mt{font-weight:800;font-size:.95rem}
.mode .md{font-size:.78rem;color:var(--mut);margin-top:2px}
.subj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.subj{border:2px solid var(--line);border-radius:10px;padding:9px 10px;font-size:.85rem;font-weight:600;text-align:left;background:#fff;color:var(--ink)}
.subj.on{border-color:var(--pri);background:var(--pri50);color:var(--pri600)}
.subj.lock{border-style:dashed;opacity:.75;cursor:default;background:var(--pri50);border-color:var(--pri);color:var(--pri600)}
.btn{border:none;border-radius:10px;font-weight:700;padding:12px 18px;font-size:.95rem}
.btn.main{background:var(--pri);color:#fff}
.btn.main:disabled{background:#cbd5e1;cursor:not-allowed}
.btn.gold{background:var(--gold);color:var(--navy)}
.btn.ghost{background:#fff;color:var(--ink);border:1.5px solid var(--line)}
.btn.danger{background:#fff;color:var(--bad);border:1.5px solid #fca5a5}
.btn.sm{padding:8px 12px;font-size:.83rem}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.resume{border-left:5px solid var(--gold)}
.hist{display:flex;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}
.hist:last-child{border-bottom:none}
.hist .sc{font-weight:800;font-size:1.05rem;color:var(--pri);margin-left:auto;white-space:nowrap}
.tag{display:inline-block;font-size:.68rem;font-weight:700;padding:2px 8px;border-radius:999px;background:var(--pri50);color:var(--pri600);white-space:nowrap}
.tag.navy{background:#e8edf9;color:var(--navy)}
.tabs{display:flex;gap:8px;overflow-x:auto;padding:4px 2px;margin-bottom:12px;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tab{border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:7px 14px;font-size:.83rem;font-weight:700;color:var(--mut);white-space:nowrap}
.tab.on{background:var(--navy);border-color:var(--navy);color:#fff}
.exam-grid{display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start}
.qhead{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px}
.qnum{font-weight:700;font-size:.9rem}
.pbar{height:5px;background:var(--line);border-radius:99px;overflow:hidden;margin-bottom:14px}
.pbar i{display:block;height:100%;background:var(--pri);border-radius:99px;transition:width .2s}
.passage{background:#f8fafc;border:1px solid var(--line);border-left:4px solid var(--info);border-radius:10px;padding:12px 14px;font-size:.9rem;white-space:pre-wrap;margin-bottom:14px;max-height:300px;overflow:auto}
.stem{font-size:1rem;font-weight:600;margin-bottom:16px;white-space:pre-wrap}
.opt{display:flex;gap:12px;align-items:flex-start;width:100%;text-align:left;border:2px solid var(--line);background:#fff;border-radius:12px;padding:12px 14px;margin-bottom:10px;font-size:.95rem;transition:border-color .1s}
.opt .key{flex:none;width:30px;height:30px;border-radius:8px;background:var(--bg);border:1px solid var(--line);font-weight:800;display:flex;align-items:center;justify-content:center;font-size:.85rem}
.opt.sel{border-color:var(--pri);background:var(--pri50)}
.opt.sel .key{background:var(--pri);color:#fff;border-color:var(--pri)}
.qact{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px;justify-content:space-between}
.qact .l,.qact .r{display:flex;gap:8px;flex-wrap:wrap}
.flag-on{color:var(--warn);border-color:var(--warn)!important}
.palette{position:sticky;top:76px}
.pal-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;box-shadow:0 1px 3px rgba(15,31,61,.06)}
.pal-sum{display:flex;gap:14px;margin:8px 0 12px;font-size:.78rem}
.pal-sum b{display:block;font-size:1.05rem}
.pal-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(38px,1fr));gap:6px;max-height:300px;overflow:auto;padding:2px}
.pal{position:relative;border:1.5px solid var(--line);background:#fff;border-radius:8px;height:34px;font-size:.78rem;font-weight:700;color:var(--mut)}
.pal.ans{background:var(--pri);border-color:var(--pri);color:#fff}
.pal.flag{background:var(--warn);border-color:var(--warn);color:#fff}
.pal.ans.flag{background:var(--warn);border-color:var(--warn);color:#fff}
.pal.ans.flag::after{content:"";position:absolute;right:4px;top:4px;width:6px;height:6px;border-radius:50%;background:var(--pri)}
.pal.cur{box-shadow:0 0 0 3px var(--navy);border-color:var(--navy)}
.legend{display:flex;flex-wrap:wrap;gap:10px;font-size:.7rem;color:var(--mut);margin-top:10px}
.legend i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:4px;vertical-align:-1px;background:#fff;border:1.5px solid var(--line)}
.legend i.a{background:var(--pri);border-color:var(--pri)}
.legend i.f{background:var(--warn);border-color:var(--warn)}
.legend i.c{box-shadow:0 0 0 2px var(--navy);border-color:var(--navy)}
.pal-toggle{display:none;position:fixed;right:14px;bottom:14px;z-index:45;background:var(--navy);color:#fff;border:none;border-radius:999px;padding:12px 18px;font-weight:800;box-shadow:0 6px 20px rgba(15,31,61,.4)}
.overlay{position:fixed;inset:0;background:rgba(15,31,61,.55);z-index:60;display:flex;align-items:center;justify-content:center;padding:16px}
.modal{background:#fff;border-radius:16px;padding:22px;max-width:420px;width:100%;max-height:86vh;overflow:auto}
.score-big{font-size:2.6rem;font-weight:800;color:var(--pri);line-height:1}
.score-big small{font-size:1.1rem;color:var(--mut);font-weight:700}
.sbar{margin:12px 0}
.sbar .lbl{display:flex;justify-content:space-between;font-size:.82rem;font-weight:600;margin-bottom:4px}
.sbar .tr{height:10px;background:var(--line);border-radius:99px;overflow:hidden}
.sbar .tr i{display:block;height:100%;border-radius:99px}
.band-hi{background:var(--ok)}.band-mid{background:var(--warn)}.band-lo{background:var(--bad)}
.rv-item{border:1px solid var(--line);border-radius:12px;padding:14px;margin-bottom:12px}
.rv-q{font-weight:600;margin:6px 0 10px;white-space:pre-wrap}
.rv-opt{display:flex;gap:10px;align-items:flex-start;border:1.5px solid var(--line);border-radius:10px;padding:8px 10px;margin-bottom:6px;font-size:.88rem}
.rv-opt .k{font-weight:800;flex:none}
.rv-opt.ok{border-color:var(--ok);background:#f0fdf4}
.rv-opt.bad{border-color:var(--bad);background:#fef2f2}
.rv-opt.mute{opacity:.6}
.expl{background:var(--pri50);border-left:4px solid var(--pri);border-radius:8px;padding:10px 12px;font-size:.85rem;margin-top:8px}
.expl b{color:var(--pri600)}
.fchip{border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;font-size:.8rem;font-weight:700;color:var(--mut)}
.fchip.on{background:var(--navy);border-color:var(--navy);color:#fff}
.calc-disp{background:var(--navy);color:#fff;border-radius:10px;padding:14px;text-align:right;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums;margin-bottom:12px;min-height:56px;overflow:hidden}
.calc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.calc-grid button{border:1px solid var(--line);background:#fff;border-radius:10px;padding:12px 0;font-size:1.05rem;font-weight:600}
.calc-grid button.op{background:var(--pri50);color:var(--pri600);font-weight:800}
.calc-grid button.eq{background:var(--pri);color:#fff;font-weight:800}
.wm{text-align:center;color:var(--mut);font-size:.72rem;padding:18px 10px 0}
.howto li{margin:6px 0 6px 18px;font-size:.88rem}
.notice{border-radius:12px;padding:12px 14px;font-size:.88rem;margin-bottom:14px}
.notice.ok{background:var(--pri50);border:1px solid #b6e4cd;color:var(--pri700,#075334)}
.notice.warn{background:#fffbeb;border:1px solid #fde68a;color:#92400e}
@media(max-width:900px){
.exam-grid{grid-template-columns:1fr}
.palette{position:fixed;left:0;right:0;bottom:0;top:auto;z-index:50;padding:0;transform:translateY(105%);transition:transform .22s}
.palette.open{transform:translateY(0)}
.pal-card{border-radius:18px 18px 0 0;max-height:70vh;overflow:auto;box-shadow:0 -8px 30px rgba(15,31,61,.25)}
.pal-toggle{display:block}
.pal-close{display:block}
}
@media(min-width:901px){.pal-close{display:none}}
@media(max-width:560px){
.mode-grid{grid-template-columns:1fr}
.h1{font-size:1.2rem}
.qact{justify-content:flex-start}
.pn-top .s{display:none}
}
@media print{
.pn-top,.pal-toggle,.qact,.no-print,.overlay{display:none!important}
body{background:#fff}
.card,.hero{box-shadow:none;border:1px solid #ccc}
.palette{display:none}
}
</style>
</head>
<body>
<div id="app"></div>
<script>
(function () {
"use strict";
var PN = __PN_DATA__;
var SUB = {};
PN.subjects.forEach(function (s) { SUB[s.n] = s; });
var SHORT = { "Use of English": "English", "Christian Religious Studies": "CRS",
  "Islamic Religious Studies": "IRS", "Agricultural Science": "Agric", "Literature in English": "Literature" };
function short(n) { return SHORT[n] || n; }
var TOTAL_Q = PN.subjects.reduce(function (a, s) { return a + s.q.length; }, 0);

/* ---------- storage (localStorage with in-memory fallback) ---------- */
var MEM = {}, HAS_LS = false;
try { localStorage.setItem("__pn", "1"); localStorage.removeItem("__pn"); HAS_LS = true; } catch (e) {}
function sGet(k) { if (HAS_LS) { try { return localStorage.getItem(k); } catch (e) {} } return (k in MEM) ? MEM[k] : null; }
function sSet(k, v) { MEM[k] = v; if (HAS_LS) { try { localStorage.setItem(k, v); } catch (e) {} } }
function sDel(k) { delete MEM[k]; if (HAS_LS) { try { localStorage.removeItem(k); } catch (e) {} } }
var KEY_S = "pnOffState", KEY_H = "pnOffHist", KEY_L = "pnOffLast";

/* ---------- tiny DOM helpers (textContent only — safe) ---------- */
var appEl = document.getElementById("app");
function h(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt !== undefined) e.textContent = txt; return e; }
function btn(cls, txt, fn, title) { var b = h("button", cls, txt); b.type = "button"; if (title) b.title = title; if (fn) b.addEventListener("click", fn); return b; }
function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function pad(n) { return (n < 10 ? "0" : "") + n; }
function fmt(sec) { sec = Math.max(0, Math.round(sec)); var hh = Math.floor(sec / 3600), mm = Math.floor((sec % 3600) / 60), ss = sec % 60; return (hh ? hh + ":" + pad(mm) : mm) + ":" + pad(ss); }
function escDate(iso) { try { return new Date(iso).toLocaleString([], { dateStyle: "medium", timeStyle: "short" }); } catch (e) { return iso; } }
function num(n) { try { return n.toLocaleString(); } catch (e) { return "" + n; } }

/* ---------- shared chrome ---------- */
var state = null, timerId = null, inExam = false, calcOpen = false;
function stopTimer() { if (timerId) { clearInterval(timerId); timerId = null; } }
function topbar(subtitle, withTimer, submitFn) {
  var bar = h("div", "pn-top");
  bar.appendChild(h("div", "pn-logo", "PN"));
  var tw = h("div"); tw.style.minWidth = "0";
  tw.appendChild(h("div", "t", "PrepNova Offline"));
  if (subtitle) tw.appendChild(h("div", "s", subtitle));
  bar.appendChild(tw);
  bar.appendChild(h("span", "pill", "WORKS OFFLINE"));
  if (withTimer) {
    var t = h("div", "timer", "--:--"); t.id = "timerEl"; bar.appendChild(t);
    if (submitFn) bar.appendChild(btn("submit-top", "Submit", submitFn));
  } else {
    var b = btn("submit-top", "Home", goHome); b.style.marginLeft = "auto"; bar.appendChild(b);
  }
  return bar;
}
function watermark() {
  var w = h("div", "wm", "Licensed to " + PN.buyer.name + (PN.buyer.ref ? " · " + PN.buyer.ref : "") +
    " · PrepNova CBT · built " + PN.built);
  return w;
}
function modal(build) {
  var ov = h("div", "overlay");
  var m = h("div", "modal");
  build(m, function () { appEl.removeChild(ov); });
  ov.appendChild(m);
  ov.addEventListener("click", function (e) { if (e.target === ov) appEl.removeChild(ov); });
  appEl.appendChild(ov);
  return ov;
}

/* ---------- home ---------- */
function goHome() { stopTimer(); inExam = false; state = null; renderHome(); }

function renderHome() {
  appEl.textContent = "";
  appEl.appendChild(topbar("JAMB CBT Simulator", false));
  var wrap = h("div", "wrap");

  var hero = h("div", "hero");
  hero.appendChild(h("div", "h1", "The JAMB mock exam that lives in this file"));
  hero.appendChild(h("p", null, "Downloaded once — now it works anywhere: bus, village, midnight, flight mode. " +
    "Pick your subjects and practise under real exam conditions, with instant marking and explained answers."));
  var chips = h("div", "chips");
  [num(TOTAL_Q) + " real questions", (PN.subjects.length - 1) + " subjects + English", "Scored over 400", "No network needed"]
    .forEach(function (t) { var c = h("span", "stat"); var parts = t.match(/^(\D*)(\d[\d,]*)(.*)$/); if (parts) { c.appendChild(document.createTextNode(parts[1])); c.appendChild(h("b", null, parts[2])); c.appendChild(document.createTextNode(parts[3])); } else c.textContent = t; chips.appendChild(c); });
  hero.appendChild(chips);
  wrap.appendChild(hero);

  /* resume */
  var saved = null;
  try { saved = JSON.parse(sGet(KEY_S) || "null"); } catch (e) { saved = null; }
  if (saved && saved.qs && saved.qs.length) {
    var rc = h("div", "card resume");
    rc.appendChild(h("div", "h2", "You have an exam in progress"));
    var done = saved.qs.filter(function (e) { return e.sel; }).length;
    var rem = Math.max(0, Math.round((saved.endsAt - Date.now()) / 1000));
    rc.appendChild(h("div", "small mut", done + " of " + saved.qs.length + " answered · " + fmt(rem) + " remaining"));
    var rr = h("div", "row"); rr.style.marginTop = "10px";
    rr.appendChild(btn("btn main", "Continue exam", function () { state = saved; renderExam(); }));
    rr.appendChild(btn("btn ghost", "Discard it", function () {
      modal(function (m, close) {
        m.appendChild(h("div", "h2", "Discard this exam?"));
        m.appendChild(h("p", "small mut", "Your answers in this attempt will be lost."));
        var r2 = h("div", "row"); r2.style.marginTop = "14px";
        r2.appendChild(btn("btn danger", "Yes, discard", function () { sDel(KEY_S); close(); renderHome(); }));
        r2.appendChild(btn("btn ghost", "Keep it", close));
        m.appendChild(r2);
      });
    }));
    rc.appendChild(rr);
    wrap.appendChild(rc);
  }

  /* setup card */
  var card = h("div", "card");
  card.appendChild(h("div", "h2", "Set up your exam"));
  var mode = "full";
  var mg = h("div", "mode-grid");
  var mFull = h("div", "mode on"), mDrill = h("div", "mode");
  mFull.appendChild(h("div", "mt", "Full JAMB mock")); mFull.appendChild(h("div", "md", "English + 3 subjects · 180 questions · 120 minutes · scored /400"));
  mDrill.appendChild(h("div", "mt", "Single-subject drill")); mDrill.appendChild(h("div", "md", "One subject · 40 questions · 40 minutes · instant feedback"));
  mg.appendChild(mFull); mg.appendChild(mDrill);
  card.appendChild(mg);

  var picked = [];
  var fullBox = h("div"); fullBox.style.marginTop = "16px";
  var drillBox = h("div"); drillBox.style.marginTop = "16px"; drillBox.style.display = "none";
  var engRow = h("div", "subj-grid"); engRow.style.marginBottom = "8px";
  engRow.appendChild(h("button", "subj lock", "Use of English — compulsory"));
  var counter = h("div", "small mut"); counter.style.margin = "8px 0";
  var grid = h("div", "subj-grid");
  var startBtn = btn("btn main", "Start full mock", function () { startAttempt("full", [PN.english].concat(picked)); }); startBtn.style.marginTop = "14px"; startBtn.disabled = true;
  var electives = PN.subjects.filter(function (s) { return s.n !== PN.english; });
  electives.forEach(function (s) {
    var b = btn("subj", short(s.n) + " · " + s.q.length, function () {
      var i = picked.indexOf(s.n);
      if (i >= 0) { picked.splice(i, 1); b.className = "subj"; }
      else { if (picked.length >= 3) return; picked.push(s.n); b.className = "subj on"; }
      counter.textContent = picked.length + " of 3 subjects selected";
      startBtn.disabled = picked.length !== 3;
    });
    b.title = s.n;
    grid.appendChild(b);
  });
  counter.textContent = "0 of 3 subjects selected";
  fullBox.appendChild(h("div", "small", "Your combination:"));
  fullBox.appendChild(engRow); fullBox.appendChild(grid); fullBox.appendChild(counter); fullBox.appendChild(startBtn);

  var dsel = h("div", "subj-grid"); var drillSub = PN.english;
  var startDrillBtn = btn("btn main", "Start drill", function () { startAttempt("drill", [drillSub]); });
  startDrillBtn.style.marginTop = "14px";
  PN.subjects.forEach(function (s) {
    var b = btn("subj" + (s.n === PN.english ? " on" : ""), short(s.n), function () {
      drillSub = s.n;
      Array.prototype.forEach.call(dsel.children, function (c) { c.className = "subj"; });
      b.className = "subj on";
    });
    b.title = s.n;
    dsel.appendChild(b);
  });
  drillBox.appendChild(h("div", "small", "Choose a subject (English drill is 60 questions · 60 minutes):"));
  drillBox.appendChild(dsel); drillBox.appendChild(startDrillBtn);

  mFull.addEventListener("click", function () { mode = "full"; mFull.className = "mode on"; mDrill.className = "mode"; fullBox.style.display = ""; drillBox.style.display = "none"; });
  mDrill.addEventListener("click", function () { mode = "drill"; mDrill.className = "mode on"; mFull.className = "mode"; drillBox.style.display = ""; fullBox.style.display = "none"; });
  card.appendChild(fullBox); card.appendChild(drillBox);
  wrap.appendChild(card);

  /* history */
  var hist = [];
  try { hist = JSON.parse(sGet(KEY_H) || "[]"); } catch (e) { hist = []; }
  if (hist.length) {
    var hc = h("div", "card");
    var ht = h("div", "h2", "Your past attempts (saved on this device)");
    var clear = btn("btn ghost sm", "Clear history", function () {
      modal(function (m, close) {
        m.appendChild(h("div", "h2", "Clear attempt history?"));
        var r2 = h("div", "row"); r2.style.marginTop = "14px";
        r2.appendChild(btn("btn danger", "Clear", function () { sDel(KEY_H); close(); renderHome(); }));
        r2.appendChild(btn("btn ghost", "Cancel", close));
        m.appendChild(r2);
      });
    });
    clear.style.marginLeft = "auto";
    var hr = h("div", "row"); hr.appendChild(ht); hr.appendChild(clear); hc.appendChild(hr);
    hist.slice().reverse().forEach(function (a) {
      var row = h("div", "hist");
      row.appendChild(h("span", "tag " + (a.m === "full" ? "navy" : ""), a.m === "full" ? "Full mock" : "Drill"));
      row.appendChild(h("span", "small mut", a.subs.map(short).join(" · ")));
      var sc = h("span", "sc", a.m === "full" ? (a.j + "/400" + (a.auto ? " · time up" : "")) : (a.c + "/" + a.t));
      row.appendChild(sc);
      row.appendChild(h("span", "small mut", a.p + "% · " + escDate(a.d)));
      hc.appendChild(row);
    });
    wrap.appendChild(hc);
  }

  /* how to use */
  var how = h("div", "card");
  how.appendChild(h("div", "h2", "How to use this file"));
  var ul = h("ul", "howto");
  ["Open it in Chrome on your phone or computer — it also works with network switched off completely.",
   "Everything is inside this one file: questions, timer, marking and explanations. No data charges, ever.",
   "Your exam progress, scores and history are saved on this device only. Don't delete the file.",
   "Every attempt picks fresh questions, so you can retake mocks again and again.",
   "Tell a friend: " + (PN.site || "prepnova.pythonanywhere.com")].forEach(function (t) { var li = h("li", null, t); ul.appendChild(li); });
  how.appendChild(ul);
  wrap.appendChild(how);

  wrap.appendChild(watermark());
  appEl.appendChild(wrap);
}

/* ---------- attempt lifecycle ---------- */

function startAttempt(mode, subs) {
  var qs = [];
  subs.forEach(function (sub) {
    var n = (mode === "full") ? (sub === PN.english ? 60 : 40) : (sub === PN.english ? 60 : 40);
    var idxs = [];
    for (var i = 0; i < SUB[sub].q.length; i++) idxs.push(i);
    shuffle(idxs).slice(0, n).forEach(function (qi) { qs.push({ s: sub, i: qi, sel: null, flag: false }); });
  });
  var minutes = mode === "full" ? 120 : (subs[0] === PN.english ? 60 : 40);
  state = { mode: mode, subs: subs.slice(), qs: qs, idx: 0, startedAt: Date.now(), endsAt: Date.now() + minutes * 60000 };
  sSet(KEY_S, JSON.stringify(state));
  sSet(KEY_L, JSON.stringify({ mode: mode, subs: subs }));
  renderExam();
}

function saveState() { if (state) sSet(KEY_S, JSON.stringify(state)); }

/* ---------- exam room ---------- */
function renderExam() {
  inExam = true;
  appEl.textContent = "";
  var title = state.mode === "full" ? "JAMB Mock — " + state.subs.map(short).join(" · ")
                                   : "Drill — " + short(state.subs[0]);
  appEl.appendChild(topbar(title, true, confirmSubmit));
  var wrap = h("div", "wrap");

  var tabs = h("div", "tabs");
  state.subs.forEach(function (sub) {
    var t = btn("tab", short(sub), function () { jumpToSubject(sub); });
    t.dataset.sub = sub;
    tabs.appendChild(t);
  });
  wrap.appendChild(tabs);

  var grid = h("div", "exam-grid");
  var qc = h("div", "card qcard"); qc.id = "qcard";
  var pal = h("div", "palette"); pal.id = "palette";
  grid.appendChild(qc); grid.appendChild(pal);
  wrap.appendChild(grid);

  var pt = btn("pal-toggle", "Palette", function () { pal.classList.add("open"); });
  wrap.appendChild(pt);
  appEl.appendChild(wrap);

  renderQ(); renderPalette();
  stopTimer();
  timerId = setInterval(tick, 1000); tick();
}

function cur() { return state.qs[state.idx]; }
function curQ(e) { e = e || cur(); return SUB[e.s].q[e.i]; }

function jumpToSubject(sub) {
  for (var i = 0; i < state.qs.length; i++) if (state.qs[i].s === sub) { state.idx = i; saveState(); renderQ(); renderPalette(); return; }
}
function jump(i) { state.idx = Math.max(0, Math.min(state.qs.length - 1, i)); saveState(); renderQ(); renderPalette(); }

function renderQ() {
  var qc = document.getElementById("qcard"); if (!qc) return;
  qc.textContent = "";
  var e = cur(), q = curQ(e);
  var head = h("div", "qhead");
  head.appendChild(h("div", "qnum", "Question " + (state.idx + 1) + " of " + state.qs.length));
  head.appendChild(h("span", "tag", short(e.s)));
  qc.appendChild(head);
  var pb = h("div", "pbar"); var pbi = h("i"); pbi.style.width = Math.round(100 * (state.idx + 1) / state.qs.length) + "%"; pb.appendChild(pbi); qc.appendChild(pb);
  if (q[7] != null && PN.passages[String(q[7])]) qc.appendChild(h("div", "passage", PN.passages[String(q[7])]));
  qc.appendChild(h("div", "stem", q[0]));
  ["A", "B", "C", "D"].forEach(function (k) {
    var o = btn("opt" + (e.sel === k ? " sel" : ""));
    o.appendChild(h("span", "key", k));
    o.appendChild(h("span", null, q[{ A: 1, B: 2, C: 3, D: 4 }[k]]));
    o.addEventListener("click", function () { select(k); });
    o.dataset.k = k;
    qc.appendChild(o);
  });
  var act = h("div", "qact");
  var L = h("div", "l"), R = h("div", "r");
  L.appendChild(btn("btn ghost sm", "← Previous", function () { jump(state.idx - 1); }));
  L.appendChild(btn("btn ghost sm", "Clear", function () { e.sel = null; saveState(); renderQ(); renderPalette(); }));
  var fb = btn("btn ghost sm flag-on" + (e.flag ? "" : " ghost-off"), e.flag ? "⚑ Flagged" : "Flag for review", function () { e.flag = !e.flag; saveState(); renderQ(); renderPalette(); });
  if (!e.flag) fb.className = "btn ghost sm";
  L.appendChild(fb);
  R.appendChild(btn("btn ghost sm", "Calculator", openCalc));
  R.appendChild(btn("btn main sm", "Save & Next →", function () { jump(state.idx + 1); }));
  act.appendChild(L); act.appendChild(R);
  qc.appendChild(act);
  qc.appendChild(h("div", "small mut", "Answers save automatically on this device. Keyboard: A–D select · ← → move · F flag · X calculator."));
  /* tabs active state */
  Array.prototype.forEach.call(document.querySelectorAll(".tab"), function (t) {
    t.className = "tab" + (t.dataset.sub === e.s ? " on" : "");
  });
  var pal = document.getElementById("palette");
  if (pal) pal.classList.remove("open");
}

function select(k) { cur().sel = (cur().sel === k ? null : k); saveState(); renderQ(); renderPalette(); }

function renderPalette() {
  var pal = document.getElementById("palette"); if (!pal) return;
  pal.textContent = "";
  var c = h("div", "pal-card");
  c.appendChild(h("h4", null, "Question palette"));
  var ans = state.qs.filter(function (e) { return e.sel; }).length;
  var flg = state.qs.filter(function (e) { return e.flag; }).length;
  var sum = h("div", "pal-sum");
  sum.appendChild(h("div", null)).appendChild(h("b", null, ans));
  sum.firstChild.appendChild(h("small", "mut", "Answered"));
  var s2 = h("div"); s2.appendChild(h("b", null, flg)); s2.appendChild(h("small", "mut", "Flagged")); sum.appendChild(s2);
  var s3 = h("div"); s3.appendChild(h("b", null, state.qs.length - ans)); s3.appendChild(h("small", "mut", "Left")); sum.appendChild(s3);
  c.appendChild(sum);
  var g = h("div", "pal-grid");
  state.qs.forEach(function (e, i) {
    var cls = "pal" + (e.sel ? " ans" : "") + (e.flag ? " flag" : "") + (i === state.idx ? " cur" : "");
    var b = btn(cls, String(i + 1), function () { jump(i); });
    b.setAttribute("aria-label", "Question " + (i + 1));
    g.appendChild(b);
  });
  c.appendChild(g);
  var lg = h("div", "legend");
  [["a", "Answered"], ["f", "Flagged"], ["", "Not answered"], ["c", "Current"]].forEach(function (p) {
    var sp = h("span"); sp.appendChild(h("i", p[0])); sp.appendChild(document.createTextNode(" " + p[1])); lg.appendChild(sp);
  });
  c.appendChild(lg);
  c.appendChild(btn("btn gold", "Submit exam", confirmSubmit)).style.marginTop = "12px";
  c.lastChild.style.width = "100%";
  var pc = btn("btn ghost sm pal-close", "Close", function () { pal.classList.remove("open"); });
  pc.style.marginTop = "10px"; pc.style.width = "100%";
  c.appendChild(pc);
  pal.appendChild(c);
  var pt = document.querySelector(".pal-toggle");
  if (pt) pt.textContent = "Palette " + ans + "/" + state.qs.length;
}

function tick() {
  var t = document.getElementById("timerEl"); if (!t || !state) return;
  var rem = (state.endsAt - Date.now()) / 1000;
  t.textContent = fmt(rem);
  t.className = "timer" + (rem <= 300 ? " low" : "");
  if (rem <= 0) doSubmit(true);
}

/* ---------- calculator ---------- */
function openCalc() {
  if (calcOpen) return; calcOpen = true;
  var acc = null, op = null, cur_ = "0", fresh = true;
  modal(function (m, close) {
    m.appendChild(h("div", "h2", "Calculator"));
    var d = h("div", "calc-disp", "0");
    m.appendChild(d);
    function show() { d.textContent = cur_.length > 14 ? cur_.slice(0, 14) : cur_; }
    function press(k) {
      if (k >= "0" && k <= "9") { cur_ = (fresh || cur_ === "0") ? k : cur_ + k; fresh = false; }
      else if (k === ".") { if (fresh) { cur_ = "0."; fresh = false; } else if (cur_.indexOf(".") < 0) cur_ += "."; }
      else if (k === "C") { acc = null; op = null; cur_ = "0"; fresh = true; }
      else if (k === "⌫") { cur_ = cur_.length > 1 ? cur_.slice(0, -1) : "0"; }
      else if (k === "=") {
        if (op !== null && acc !== null) {
          var a = parseFloat(acc), b = parseFloat(cur_), r = null;
          if (op === "+") r = a + b; else if (op === "−") r = a - b;
          else if (op === "×") r = a * b; else if (op === "÷") r = (b === 0 ? null : a / b);
          cur_ = (r === null || !isFinite(r)) ? "Error" : String(Math.round(r * 1e8) / 1e8);
          acc = null; op = null; fresh = true;
        }
      } else { /* operator */
        if (op !== null && acc !== null && !fresh) { press("="); }
        acc = cur_; op = k; fresh = true;
      }
      show();
    }
    var g = h("div", "calc-grid");
    ["C", "⌫", "÷", "7", "8", "9", "×", "4", "5", "6", "−", "1", "2", "3", "+", "0", ".", "="].forEach(function (k) {
      var b = btn(k === "=" ? "eq" : ("0123456789.".indexOf(k) >= 0 ? "" : "op"), k, function () { press(k); });
      g.appendChild(b);
    });
    m.appendChild(g);
    var cl = btn("btn ghost", "Close", function () { close(); calcOpen = false; });
    cl.style.marginTop = "12px"; cl.style.width = "100%";
    m.appendChild(cl);
  });
}

/* ---------- submit + grade ---------- */
function confirmSubmit() {
  modal(function (m, close) {
    m.appendChild(h("div", "h2", "Submit exam?"));
    var nAns = state.qs.filter(function (e) { return e.sel; }).length;
    state.subs.forEach(function (sub) {
      var t = state.qs.filter(function (e) { return e.s === sub; }).length;
      var a = state.qs.filter(function (e) { return e.s === sub && e.sel; }).length;
      m.appendChild(h("div", "small", short(sub) + ": " + a + " of " + t + " answered"));
    });
    if (nAns < state.qs.length) {
      var w = h("div", "notice warn");
      w.style.marginTop = "12px";
      w.textContent = (state.qs.length - nAns) + " question(s) unanswered — they will score zero.";
      m.appendChild(w);
    }
    var r = h("div", "row"); r.style.marginTop = "14px";
    r.appendChild(btn("btn main", "Submit now", function () { close(); doSubmit(false); }));
    r.appendChild(btn("btn ghost", "Keep writing", close));
    m.appendChild(r);
  });
}

function doSubmit(auto) {
  if (!state) return;
  stopTimer(); inExam = false;
  var per = {}, totalC = 0;
  state.qs.forEach(function (e) {
    var q = curQ(e);
    var p = per[e.s] || (per[e.s] = { c: 0, t: 0 });
    p.t++;
    if (e.sel && e.sel === q[5]) { p.c++; totalC++; }
  });
  var jamb = 0;
  if (state.mode === "full") Object.keys(per).forEach(function (s) { jamb += Math.round(100 * per[s].c / per[s].t); });
  var g = { mode: state.mode, subs: state.subs.slice(), qs: state.qs.slice(), per: per,
            correct: totalC, total: state.qs.length, jamb: jamb,
            pct: Math.round(100 * totalC / state.qs.length),
            used: Math.round((Math.min(Date.now(), state.startedAt + 7200000) - state.startedAt) / 1000), auto: auto };
  var hist = [];
  try { hist = JSON.parse(sGet(KEY_H) || "[]"); } catch (e) { hist = []; }
  hist.push({ d: new Date().toISOString(), m: g.mode, subs: g.subs, j: g.jamb, p: g.pct, c: g.correct, t: g.total, auto: g.auto });
  if (hist.length > 20) hist = hist.slice(-20);
  sSet(KEY_H, JSON.stringify(hist));
  sDel(KEY_S);
  state = null;
  renderResults(g);
}

/* ---------- results ---------- */
function renderResults(g) {
  appEl.textContent = "";
  var sub = g.mode === "full" ? "Result — " + g.subs.map(short).join(" · ") : "Drill result — " + short(g.subs[0]);
  appEl.appendChild(topbar(sub, false));
  var wrap = h("div", "wrap");
  var card = h("div", "card");
  if (g.auto) { var n = h("div", "notice warn"); n.textContent = "Time up — the exam was submitted automatically."; card.appendChild(n); }
  var sc = h("div", "score-big");
  if (g.mode === "full") {
    sc.appendChild(document.createTextNode(g.jamb));
    sc.appendChild(h("small", null, " / 400"));
  } else {
    sc.appendChild(document.createTextNode(g.correct));
    sc.appendChild(h("small", null, " / " + g.total));
  }
  card.appendChild(sc);
  card.appendChild(h("div", "small mut", g.pct + "% correct · " + fmt(g.used) + " used" + (g.mode === "full" ? " · JAMB scales each subject to 100" : "")));
  var subs = Object.keys(g.per);
  subs.forEach(function (s) {
    var p = g.per[s];
    var scaled = Math.round(100 * p.c / p.t);
    var bar = h("div", "sbar");
    var lbl = h("div", "lbl");
    lbl.appendChild(h("span", null, s));
    lbl.appendChild(h("span", "mut", p.c + "/" + p.t + (g.mode === "full" ? " · " + scaled + "/100" : "")));
    bar.appendChild(lbl);
    var tr = h("div", "tr"); var i = h("i", scaled >= 70 ? "band-hi" : scaled >= 50 ? "band-mid" : "band-lo");
    i.style.width = scaled + "%"; tr.appendChild(i); bar.appendChild(tr);
    card.appendChild(bar);
  });
  var acts = h("div", "row"); acts.style.marginTop = "8px";
  var last = null;
  try { last = JSON.parse(sGet(KEY_L) || "null"); } catch (e) {}
  if (last) acts.appendChild(btn("btn main", "Retake with fresh questions", function () { startAttempt(last.mode, last.subs); }));
  acts.appendChild(btn("btn gold", "Print / save as PDF", function () { window.print(); }));
  acts.appendChild(btn("btn ghost", "Home", goHome));
  card.appendChild(acts);
  wrap.appendChild(card);

  /* review */
  var rc = h("div", "card");
  rc.appendChild(h("div", "h2", "Review — every question, explained"));
  var filters = h("div", "row"); filters.style.marginBottom = "14px";
  var fDefs = [["all", "All"], ["wrong", "I got wrong"], ["skipped", "I skipped"], ["flag", "I flagged"]];
  var list = h("div");
  function draw(f) {
    list.textContent = "";
    var n = 0;
    g.qs.forEach(function (e, i) {
      var q = curQ(e);
      var wrong = e.sel && e.sel !== q[5];
      var skipped = !e.sel;
      if (f === "wrong" && !wrong) return;
      if (f === "skipped" && !skipped) return;
      if (f === "flag" && !e.flag) return;
      n++;
      var it = h("div", "rv-item");
      var hd = h("div", "qhead");
      hd.appendChild(h("div", "qnum", "Q" + (i + 1)));
      hd.appendChild(h("span", "tag", short(e.s)));
      it.appendChild(hd);
      if (q[7] != null && PN.passages[String(q[7])]) {
        var ps = h("div", "passage", PN.passages[String(q[7])]);
        ps.style.maxHeight = "120px";
        it.appendChild(ps);
      }
      it.appendChild(h("div", "rv-q", q[0]));
      ["A", "B", "C", "D"].forEach(function (k) {
        var mine = e.sel === k, right = q[5] === k;
        var cls = "rv-opt" + (right ? " ok" : mine ? " bad" : " mute");
        var o = h("div", cls);
        o.appendChild(h("span", "k", k));
        o.appendChild(h("span", null, q[{ A: 1, B: 2, C: 3, D: 4 }[k]]));
        if (right) o.appendChild(h("span", "small", "correct answer"));
        else if (mine) o.appendChild(h("span", "small", "your answer"));
        it.appendChild(o);
      });
      if (!e.sel) it.appendChild(h("div", "small mut", "You did not answer this one."));
      var ex = h("div", "expl");
      ex.appendChild(h("b", null, "Why: "));
      ex.appendChild(document.createTextNode(q[6] || "The correct option is " + q[5] + "."));
      it.appendChild(ex);
      list.appendChild(it);
    });
    if (!n) list.appendChild(h("p", "small mut", "Nothing in this filter."));
  }
  fDefs.forEach(function (fd, ix) {
    var b = btn("fchip" + (ix === 0 ? " on" : ""), fd[1], function () {
      Array.prototype.forEach.call(filters.children, function (c) { c.className = "fchip"; });
      b.className = "fchip on";
      draw(fd[0]);
    });
    filters.appendChild(b);
  });
  rc.appendChild(filters); rc.appendChild(list);
  wrap.appendChild(rc);
  wrap.appendChild(watermark());
  appEl.appendChild(wrap);
  draw("all");
}

/* ---------- keyboard ---------- */
document.addEventListener("keydown", function (ev) {
  if (!inExam || !state || calcOpen) return;
  if (ev.target && /INPUT|TEXTAREA/.test(ev.target.tagName)) return;
  var k = ev.key.toLowerCase();
  if (k === "a" || k === "b" || k === "c" || k === "d") { select(k.toUpperCase()); }
  else if (ev.key === "ArrowRight") { jump(state.idx + 1); }
  else if (ev.key === "ArrowLeft") { jump(state.idx - 1); }
  else if (k === "f") { var e = cur(); e.flag = !e.flag; saveState(); renderQ(); renderPalette(); }
  else if (k === "x") { openCalc(); }
});

renderHome();
})();
</script>
</body>
</html>
"""
