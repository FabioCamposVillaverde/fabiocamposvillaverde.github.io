---
layout: default
title: Algorithmic Trading Bot
permalink: /en/trading-bot/
lang: en
alt: /trading-bot/
description: "Algorithmic Bitcoin trading bot built in Python: data pipeline, 24/7 deployment, real-time dashboard, backtesting and risk management."
---

<style>
  .tb { --bg: #0b0f14; --panel: #121821; --panel-2: #161d27; --line: #232c38;
        --text: #e6edf3; --muted: #93a1b1; --mint: #3ddc97; --mint-2: #2ee6a6; --mint-soft: rgba(61,220,151,.12);
        margin: -40px calc(50% - 50vw) -40px; background: var(--bg); color: var(--text);
        overflow-x: clip; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; }
  .tb-inner { max-width: 1040px; margin: 0 auto; padding: 70px 22px; }
  .tb a { color: var(--mint); text-decoration: none; }
  .tb a:hover { text-decoration: underline; }
  .tb h1, .tb h2, .tb h3 { color: var(--text); line-height: 1.15; margin: 0; }
  .tb p { color: var(--muted); line-height: 1.75; }
  .tb section { margin-top: 90px; }
  .tb-eyebrow { color: var(--mint); font-weight: 700; font-size: .8rem; letter-spacing: 2px; text-transform: uppercase; display: block; margin-bottom: 14px; }
  .tb h2 { font-size: 1.9rem; margin-bottom: 10px; }
  .tb-lead { font-size: 1.05rem; max-width: 720px; }
  .tb-chips { display: flex; flex-wrap: wrap; gap: 10px; }
  .tb-chip { background: var(--mint-soft); color: var(--mint-2); border: 1px solid rgba(61,220,151,.28); border-radius: 30px; padding: 6px 14px; font-size: .82rem; font-weight: 600; }
  .tb-badge { background: var(--panel-2); color: #c9d4e0; border: 1px solid var(--line); border-radius: 8px; padding: 8px 14px; font-size: .85rem; font-weight: 600; }
  .tb-btn { display: inline-flex; align-items: center; gap: 8px; background: var(--mint); color: #07120c !important; font-weight: 700; padding: 12px 24px; border-radius: 10px; text-decoration: none !important; transition: transform .2s, box-shadow .2s; }
  .tb-btn:hover { transform: translateY(-2px); box-shadow: 0 10px 26px rgba(61,220,151,.3); }
  .tb-btn.ghost { background: transparent; color: var(--mint) !important; border: 1px solid rgba(61,220,151,.4); }
  .tb-frame { border-radius: 14px; overflow: hidden; background: var(--panel); border: 1px solid var(--line); box-shadow: 0 24px 60px rgba(0,0,0,.5); }
  .tb-frame img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .tb-hero { display: grid; grid-template-columns: 1fr 1.15fr; gap: 48px; align-items: center; margin-top: 10px; }
  .tb-hero h1 { font-size: 2.7rem; margin-bottom: 14px; }
  .tb-hero .tag { font-size: 1.2rem; color: #c9d4e0; margin: 0 0 24px; }
  .tb-hero-cta { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 26px; }
  .tb-hero-media { aspect-ratio: 16 / 10; }
  .tb-hero-media img { transition: transform .1s linear; }
  .tb-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }
  .tb-stat { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 26px 18px; text-align: center; }
  .tb-stat-num { font-size: 2.3rem; font-weight: 800; color: var(--mint); line-height: 1; }
  .tb-stat-lbl { color: var(--muted); font-size: .85rem; margin-top: 8px; }
  .tb-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }
  .tb-card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 26px; transition: transform .25s, border-color .25s, box-shadow .25s; }
  .tb-card:hover { transform: translateY(-6px); border-color: rgba(61,220,151,.5); box-shadow: 0 18px 40px rgba(0,0,0,.45); }
  .tb-card .ico { font-size: 1.8rem; display: inline-block; margin-bottom: 12px; }
  .tb-card h3 { font-size: 1.12rem; margin-bottom: 8px; }
  .tb-card p { font-size: .92rem; margin: 0; }
  .tb-arch { text-align: center; }
  .tb-arch .tb-frame { display: inline-block; padding: 18px; background: var(--panel-2); }
  .tb-arch img { max-width: 100%; border-radius: 6px; }
  .tb-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 22px; }
  .tb-fig { margin: 0; }
  .tb-shot { display: block; width: 100%; padding: 0; border: 0; background: none; cursor: zoom-in; border-radius: 14px; }
  .tb-shot .tb-frame { aspect-ratio: 16 / 10; }
  .tb-shot:focus-visible { outline: 3px solid var(--mint); outline-offset: 3px; }
  .tb-shot img { transition: transform .4s; }
  .tb-shot:hover img { transform: scale(1.04); }
  .tb-fig figcaption { color: var(--muted); font-size: .88rem; margin-top: 12px; line-height: 1.55; }
  .tb-lb { position: fixed; inset: 0; z-index: 4000; background: rgba(5,8,11,.92); display: none; align-items: center; justify-content: center; flex-direction: column; padding: 30px; }
  .tb-lb.open { display: flex; }
  .tb-lb img { max-width: 92vw; max-height: 78vh; border-radius: 10px; box-shadow: 0 30px 80px rgba(0,0,0,.7); }
  .tb-lb-cap { color: #c9d4e0; margin-top: 18px; max-width: 760px; text-align: center; font-size: .95rem; }
  .tb-lb-close { position: absolute; top: 20px; right: 24px; background: var(--panel); color: var(--text); border: 1px solid var(--line); width: 44px; height: 44px; border-radius: 50%; font-size: 1.4rem; cursor: pointer; }
  .tb-cta { background: linear-gradient(135deg, #0f1722, #131c12); border: 1px solid var(--line); border-radius: 18px; padding: 50px 36px; text-align: center; }
  .tb-cta h2 { margin-bottom: 14px; }
  .tb-cta .row { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; margin-top: 24px; }
  .tb-reveal { transition: opacity .7s ease, transform .7s ease; }
  html.js .tb-reveal { opacity: 0; transform: translateY(26px); }
  html.js .tb-reveal.is-visible { opacity: 1; transform: none; }
  @media (prefers-reduced-motion: reduce) { html.js .tb-reveal { opacity: 1; transform: none; } .tb-hero-media img { transform: none !important; } }
  @media (max-width: 820px) {
    .tb-hero { grid-template-columns: 1fr; }
    .tb-hero h1 { font-size: 2.1rem; }
    .tb-stats { grid-template-columns: repeat(2, 1fr); }
  }
</style>

<div class="tb" markdown="0">
  <div class="tb-inner">

    <!-- 1. HERO -->
    <section class="tb-hero tb-reveal" style="margin-top: 0;">
      <div>
        <span class="tb-eyebrow">Python · Data Engineering · DevOps</span>
        <h1>Algorithmic Bitcoin Trading Bot</h1>
        <p class="tag">An autonomous system that trades, monitors and validates itself — live 24/7.</p>
        <div class="tb-chips">
          <span class="tb-chip">Python</span>
          <span class="tb-chip">DuckDB</span>
          <span class="tb-chip">Streamlit</span>
        </div>
        <div class="tb-hero-cta">
          <a class="tb-btn" href="/en/contact/">Let's talk about it</a>
        </div>
        <p style="font-size: .82rem; color: var(--muted); margin-top: 14px;">Personal project · private code, available on request.</p>
      </div>
      <div class="tb-hero-media tb-frame">
        <img src="/assets/images/trading-bot/02_market_data.png" loading="lazy" decoding="async"
             alt="Market data pipeline: aggregated order flow across 150+ markets" onerror="tbPH(this)">
      </div>
    </section>

    <!-- Stats -->
    <section class="tb-stats tb-reveal" style="margin-top: 64px;">
      <div class="tb-stat"><div class="tb-stat-num"><span class="tb-count" data-to="150">0</span>+</div><div class="tb-stat-lbl">aggregated markets</div></div>
      <div class="tb-stat"><div class="tb-stat-num">24/7</div><div class="tb-stat-lbl">live in production</div></div>
      <div class="tb-stat"><div class="tb-stat-num"><span class="tb-count" data-to="100">0</span>%</div><div class="tb-stat-lbl">Python, from scratch</div></div>
      <div class="tb-stat"><div class="tb-stat-num"><span class="tb-count" data-to="0">0</span></div><div class="tb-stat-lbl">manual intervention</div></div>
    </section>

    <!-- 2. OVERVIEW -->
    <section class="tb-reveal">
      <span class="tb-eyebrow">Overview</span>
      <h2>What it is</h2>
      <p class="tb-lead">A fully Python-built automated trading system for Bitcoin. It collects real-time market data from multiple sources, processes it and decides when to trade following programmed strategies, all while managing risk automatically. It runs unattended 24/7 on a cloud server and is monitored through a live web dashboard. Every strategy is first validated against years of historical data using rigorous statistical methods.</p>
    </section>

    <!-- 3. HIGHLIGHTS -->
    <section class="tb-reveal">
      <span class="tb-eyebrow">What it shows</span>
      <h2>Key skills</h2>
      <div class="tb-grid" style="margin-top: 30px;">
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🐍</span><h3>Python Backend</h3><p>Asynchronous, modular system built from scratch.</p></div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🔗</span><h3>Data Engineering</h3><p>A pipeline that ingests and normalizes data from multiple market APIs.</p></div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🚀</span><h3>24/7 Deployment</h3><p>Runs on a Linux cloud server as a managed service with auto-recovery.</p></div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">📊</span><h3>Real-time Dashboard</h3><p>A web panel to monitor the bot, markets and performance.</p></div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🧪</span><h3>Rigorous Validation</h3><p>Walk-forward and Monte Carlo backtesting to prove (or discard) each strategy.</p></div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🛡️</span><h3>Risk Management</h3><p>A kill switch halts trading on abnormal losses or errors.</p></div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">✅</span><h3>Best Practices</h3><p>Git/GitHub, automated tests and strict typing.</p></div>
      </div>
    </section>

    <!-- 4. ARCHITECTURE -->
    <section class="tb-reveal tb-arch">
      <span class="tb-eyebrow">How it fits together</span>
      <h2>System Architecture</h2>
      <div class="tb-frame" style="margin-top: 30px;">
        <img loading="lazy" decoding="async" src="/assets/images/trading-bot/architecture-en.svg" alt="Trading bot architecture diagram" onerror="tbPH(this)">
      </div>
    </section>

    <!-- 5. GALLERY -->
    <section class="tb-reveal">
      <span class="tb-eyebrow">In action</span>
      <h2>Inside the system</h2>
      <div class="tb-gallery" style="margin-top: 30px;">

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/images/trading-bot/02_market_data.png" data-cap="Multi-source data pipeline: aggregated order flow across 150+ markets (CVD, open interest, liquidations).">
            <span class="tb-frame"><img src="/assets/images/trading-bot/02_market_data.png" loading="lazy" decoding="async" alt="Multi-source data pipeline with aggregated order flow" onerror="tbPH(this)"></span>
          </button>
          <figcaption>Multi-source data pipeline: aggregated order flow across 150+ markets (CVD, open interest, liquidations).</figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/images/trading-bot/04_backtests.png" data-cap="Backtesting &amp; validation engine: strategy comparison with robustness metrics.">
            <span class="tb-frame"><img src="/assets/images/trading-bot/04_backtests.png" loading="lazy" decoding="async" alt="Backtesting engine with strategy comparison and equity curve" onerror="tbPH(this)"></span>
          </button>
          <figcaption>Backtesting &amp; validation engine: strategy comparison with robustness metrics.</figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/images/trading-bot/05_risk_engine.png" data-cap="Risk engine: kill-switch state machine, halt triggers and order validation.">
            <span class="tb-frame"><img src="/assets/images/trading-bot/05_risk_engine.png" loading="lazy" decoding="async" alt="Risk engine with kill-switch state machine" onerror="tbPH(this)"></span>
          </button>
          <figcaption>Risk engine: kill-switch state machine, halt triggers and order validation.</figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/images/trading-bot/03_signal_lab.png" data-cap="Signal lab: custom detectors (NPOC, divergences, liquidations) with a live stream.">
            <span class="tb-frame"><img src="/assets/images/trading-bot/03_signal_lab.png" loading="lazy" decoding="async" alt="Signal lab with custom detectors and a live stream" onerror="tbPH(this)"></span>
          </button>
          <figcaption>Signal lab: custom detectors (NPOC, divergences, liquidations) with a live stream.</figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/images/trading-bot/01_cockpit.png" data-cap="Live control panel: bot status, kill-switch, equity and strategy parameters.">
            <span class="tb-frame"><img src="/assets/images/trading-bot/01_cockpit.png" loading="lazy" decoding="async" alt="Live control panel with bot status and equity" onerror="tbPH(this)"></span>
          </button>
          <figcaption>Live control panel: bot status, kill-switch, equity and strategy parameters.</figcaption>
        </figure>

      </div>
    </section>

    <!-- 6. STACK -->
    <section class="tb-reveal">
      <span class="tb-eyebrow">Tooling</span>
      <h2>Tech Stack</h2>
      <div class="tb-chips" style="margin-top: 26px;">
        <span class="tb-badge">Python</span><span class="tb-badge">asyncio</span><span class="tb-badge">DuckDB</span>
        <span class="tb-badge">Polars</span><span class="tb-badge">Pydantic</span><span class="tb-badge">Streamlit</span>
        <span class="tb-badge">REST APIs</span><span class="tb-badge">Git/GitHub</span><span class="tb-badge">Linux</span>
        <span class="tb-badge">systemd</span><span class="tb-badge">VPS (Cloud)</span><span class="tb-badge">pytest</span>
      </div>
    </section>

    <!-- 7. CTA -->
    <section class="tb-reveal">
      <div class="tb-cta">
        <h2>Let's talk engineering</h2>
        <p style="max-width: 560px; margin: 0 auto;">Get in touch if you'd like to know more about the system or see the code.</p>
        <div class="row">
          <a class="tb-btn" href="/en/contact/">Contact</a>
        </div>
        <p style="font-size: .82rem; color: var(--muted); margin-top: 16px;">Private code · available on request.</p>
      </div>

      <div style="text-align: center; margin-top: 40px;">
        <a href="/en/projects/">⬅️ Back to my projects</a>
      </div>
    </section>

  </div>

  <!-- Lightbox -->
  <div class="tb-lb" id="tb-lb" role="dialog" aria-modal="true" aria-label="Enlarged view">
    <button type="button" class="tb-lb-close" id="tb-lb-close" aria-label="Close">&times;</button>
    <img id="tb-lb-img" src="" alt="">
    <p class="tb-lb-cap" id="tb-lb-cap"></p>
  </div>
</div>

<script>
(function(){
  var tb = document.querySelector('.tb');
  if (!tb) return;

  window.tbPH = function(el){
    el.onerror = null;
    el.src = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='500'><rect width='800' height='500' fill='%23121821'/><rect x='1' y='1' width='798' height='498' fill='none' stroke='%23232c38' stroke-width='2'/><g fill='none' stroke='%233ddc97' stroke-width='5' opacity='.8'><rect x='320' y='190' width='160' height='120' rx='10'/><circle cx='365' cy='230' r='14'/><path d='M325 305 L390 255 L430 285 L475 240 L475 305 Z' fill='%233ddc97' fill-opacity='.18'/></g><text x='400' y='360' fill='%2393a1b1' font-family='Segoe UI,Arial' font-size='24' text-anchor='middle'>preview · screenshot coming soon</text></svg>";
  };

  var lb = document.getElementById('tb-lb'), lbImg = document.getElementById('tb-lb-img'),
      lbCap = document.getElementById('tb-lb-cap'), lbClose = document.getElementById('tb-lb-close'), lastFocus = null;
  function openLB(btn){ lastFocus = btn; lbImg.setAttribute('src', btn.getAttribute('data-full')); var cap = btn.getAttribute('data-cap') || ''; lbImg.setAttribute('alt', cap); lbCap.textContent = cap; lb.classList.add('open'); lbClose.focus(); }
  function closeLB(){ lb.classList.remove('open'); if (lastFocus) lastFocus.focus(); }
  tb.querySelectorAll('.tb-shot').forEach(function(btn){ btn.addEventListener('click', function(){ openLB(btn); }); });
  lbClose.addEventListener('click', closeLB);
  lb.addEventListener('click', function(e){ if (e.target === lb) closeLB(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && lb.classList.contains('open')) closeLB(); });

  function countUp(el){ var to = parseInt(el.getAttribute('data-to'), 10) || 0, start = null, dur = 1100;
    function step(ts){ if (!start) start = ts; var p = Math.min((ts - start) / dur, 1); el.textContent = Math.floor(p * to).toString(); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step); }
  var reveals = tb.querySelectorAll('.tb-reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting){ en.target.classList.add('is-visible'); en.target.querySelectorAll && en.target.querySelectorAll('.tb-count').forEach(countUp); io.unobserve(en.target); } });
    }, { threshold: 0.14 });
    reveals.forEach(function(el){ io.observe(el); });
  } else { reveals.forEach(function(el){ el.classList.add('is-visible'); }); tb.querySelectorAll('.tb-count').forEach(countUp); }

  var heroImg = tb.querySelector('.tb-hero-media img');
  if (heroImg && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    window.addEventListener('scroll', function(){ var y = Math.min(window.scrollY || 0, 500); heroImg.style.transform = 'scale(' + (1 + y * 0.00016) + ')'; }, { passive: true });
  }
})();
</script>
