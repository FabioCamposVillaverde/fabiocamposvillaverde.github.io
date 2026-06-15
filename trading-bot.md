---
layout: default
title: Bot de Trading Algorítmico · Algorithmic Trading Bot
description: "Bot de trading algorítmico para Bitcoin construido en Python: pipeline de datos, despliegue 24/7, dashboard en tiempo real, backtesting y gestión de riesgo."
---

<style>
  /* ===================== Trading Bot · tema oscuro ===================== */
  .tb {
    --bg: #0b0f14; --panel: #121821; --panel-2: #161d27; --line: #232c38;
    --text: #e6edf3; --muted: #93a1b1; --mint: #3ddc97; --mint-2: #2ee6a6;
    --mint-soft: rgba(61,220,151,.12);
    /* full-bleed: ocupa todo el ancho aunque el layout sea estrecho */
    margin: -40px calc(50% - 50vw) -40px;
    background: var(--bg);
    color: var(--text);
    overflow-x: clip;
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
  }
  .tb-inner { max-width: 1040px; margin: 0 auto; padding: 70px 22px; }
  .tb a { color: var(--mint); text-decoration: none; }
  .tb a:hover { text-decoration: underline; }
  .tb h1, .tb h2, .tb h3 { color: var(--text); line-height: 1.15; margin: 0; }
  .tb p { color: var(--muted); line-height: 1.75; }
  .tb section { margin-top: 90px; }
  .tb-eyebrow { color: var(--mint); font-weight: 700; font-size: .8rem; letter-spacing: 2px;
                text-transform: uppercase; display: block; margin-bottom: 14px; }
  .tb h2 { font-size: 1.9rem; margin-bottom: 10px; }
  .tb-lead { font-size: 1.05rem; max-width: 720px; }

  /* Conmutador de idioma */
  .tb-lang { position: sticky; top: 78px; z-index: 20; display: flex; justify-content: flex-end; }
  .tb-lang .group { display: inline-flex; background: var(--panel); border: 1px solid var(--line);
                    border-radius: 30px; padding: 4px; box-shadow: 0 6px 20px rgba(0,0,0,.35); }
  .tb-lang button { background: transparent; border: 0; color: var(--muted); font-weight: 700;
                    padding: 7px 16px; border-radius: 30px; cursor: pointer; font-size: .85rem; transition: all .2s; }
  .tb-lang button[aria-pressed="true"] { background: var(--mint); color: #07120c; }

  /* Solo se muestra el idioma activo */
  .tb[data-lang="es"] [data-l="en"] { display: none !important; }
  .tb[data-lang="en"] [data-l="es"] { display: none !important; }

  /* Chips / badges */
  .tb-chips { display: flex; flex-wrap: wrap; gap: 10px; }
  .tb-chip { background: var(--mint-soft); color: var(--mint-2); border: 1px solid rgba(61,220,151,.28);
             border-radius: 30px; padding: 6px 14px; font-size: .82rem; font-weight: 600; }
  .tb-badge { background: var(--panel-2); color: #c9d4e0; border: 1px solid var(--line);
              border-radius: 8px; padding: 8px 14px; font-size: .85rem; font-weight: 600; }

  /* Botones */
  .tb-btn { display: inline-flex; align-items: center; gap: 8px; background: var(--mint); color: #07120c !important;
            font-weight: 700; padding: 12px 24px; border-radius: 10px; text-decoration: none !important; transition: transform .2s, box-shadow .2s; }
  .tb-btn:hover { transform: translateY(-2px); box-shadow: 0 10px 26px rgba(61,220,151,.3); }
  .tb-btn.ghost { background: transparent; color: var(--mint) !important; border: 1px solid rgba(61,220,151,.4); }

  /* Marco de imagen */
  .tb-frame { border-radius: 14px; overflow: hidden; background: var(--panel);
              border: 1px solid var(--line); box-shadow: 0 24px 60px rgba(0,0,0,.5); }
  .tb-frame img { width: 100%; height: 100%; object-fit: cover; display: block; }

  /* HERO */
  .tb-hero { display: grid; grid-template-columns: 1fr 1.15fr; gap: 48px; align-items: center; margin-top: 30px; }
  .tb-hero h1 { font-size: 2.7rem; margin-bottom: 14px; }
  .tb-hero .tag { font-size: 1.2rem; color: #c9d4e0; margin: 0 0 24px; }
  .tb-hero-cta { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 26px; }
  .tb-hero-media { aspect-ratio: 16 / 10; }
  .tb-hero-media img { transition: transform .1s linear; }

  /* Stats / contadores */
  .tb-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }
  .tb-stat { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 26px 18px; text-align: center; }
  .tb-stat-num { font-size: 2.3rem; font-weight: 800; color: var(--mint); line-height: 1; }
  .tb-stat-lbl { color: var(--muted); font-size: .85rem; margin-top: 8px; }

  /* Highlights grid */
  .tb-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }
  .tb-card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 26px;
             transition: transform .25s, border-color .25s, box-shadow .25s; }
  .tb-card:hover { transform: translateY(-6px); border-color: rgba(61,220,151,.5); box-shadow: 0 18px 40px rgba(0,0,0,.45); }
  .tb-card .ico { font-size: 1.8rem; display: inline-block; margin-bottom: 12px; }
  .tb-card h3 { font-size: 1.12rem; margin-bottom: 8px; }
  .tb-card p { font-size: .92rem; margin: 0; }

  /* Arquitectura */
  .tb-arch { text-align: center; }
  .tb-arch .tb-frame { display: inline-block; padding: 18px; background: var(--panel-2); }
  .tb-arch img { max-width: 100%; border-radius: 6px; }

  /* Galería */
  .tb-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 22px; }
  .tb-fig { margin: 0; }
  .tb-shot { display: block; width: 100%; padding: 0; border: 0; background: none; cursor: zoom-in; border-radius: 14px; }
  .tb-shot .tb-frame { aspect-ratio: 16 / 10; }
  .tb-shot:focus-visible { outline: 3px solid var(--mint); outline-offset: 3px; }
  .tb-shot img { transition: transform .4s; }
  .tb-shot:hover img { transform: scale(1.04); }
  .tb-fig figcaption { color: var(--muted); font-size: .88rem; margin-top: 12px; line-height: 1.55; }

  /* Lightbox */
  .tb-lb { position: fixed; inset: 0; z-index: 4000; background: rgba(5,8,11,.92);
           display: none; align-items: center; justify-content: center; flex-direction: column; padding: 30px; }
  .tb-lb.open { display: flex; }
  .tb-lb img { max-width: 92vw; max-height: 78vh; border-radius: 10px; box-shadow: 0 30px 80px rgba(0,0,0,.7); }
  .tb-lb-cap { color: #c9d4e0; margin-top: 18px; max-width: 760px; text-align: center; font-size: .95rem; }
  .tb-lb-close { position: absolute; top: 20px; right: 24px; background: var(--panel); color: var(--text);
                 border: 1px solid var(--line); width: 44px; height: 44px; border-radius: 50%; font-size: 1.4rem; cursor: pointer; }

  /* CTA final */
  .tb-cta { background: linear-gradient(135deg, #0f1722, #131c12); border: 1px solid var(--line);
            border-radius: 18px; padding: 50px 36px; text-align: center; }
  .tb-cta h2 { margin-bottom: 14px; }
  .tb-cta .row { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; margin-top: 24px; }

  /* Reveal al hacer scroll */
  .tb-reveal { transition: opacity .7s ease, transform .7s ease; }
  html.js .tb-reveal { opacity: 0; transform: translateY(26px); }
  html.js .tb-reveal.is-visible { opacity: 1; transform: none; }
  @media (prefers-reduced-motion: reduce) { html.js .tb-reveal { opacity: 1; transform: none; } .tb-hero-media img { transform: none !important; } }

  @media (max-width: 820px) {
    .tb-hero { grid-template-columns: 1fr; }
    .tb-hero h1 { font-size: 2.1rem; }
    .tb-stats { grid-template-columns: repeat(2, 1fr); }
    .tb-lang { top: 72px; }
  }
</style>

<script>document.documentElement.classList.add('js');</script>

<div class="tb" data-lang="es" markdown="0">
  <script>
    /* Idioma inicial sin parpadeo: localStorage > #en > es */
    (function(){
      var w = document.currentScript.parentElement;
      var l = localStorage.getItem('tb-lang') || (location.hash === '#en' ? 'en' : 'es');
      w.setAttribute('data-lang', l);
    })();
  </script>

  <div class="tb-inner">

    <!-- Conmutador de idioma -->
    <div class="tb-lang">
      <div class="group" role="group" aria-label="Idioma / Language">
        <button type="button" data-set-lang="es" aria-pressed="true">ES</button>
        <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>

    <!-- 1. HERO -->
    <section class="tb-hero tb-reveal" style="margin-top: 24px;">
      <div>
        <span class="tb-eyebrow">Python · Data Engineering · DevOps</span>
        <h1>
          <span data-l="es">Bot de Trading Algorítmico para Bitcoin</span>
          <span data-l="en">Algorithmic Bitcoin Trading Bot</span>
        </h1>
        <p class="tag">
          <span data-l="es">Un sistema autónomo que opera, se vigila y se valida solo — en producción 24/7.</span>
          <span data-l="en">An autonomous system that trades, monitors and validates itself — live 24/7.</span>
        </p>
        <div class="tb-chips">
          <span class="tb-chip">Python</span>
          <span class="tb-chip">DuckDB</span>
          <span class="tb-chip">Streamlit</span>
        </div>
        <div class="tb-hero-cta">
          <a class="tb-btn" data-l="es" href="/contact/">Hablemos del proyecto</a>
          <a class="tb-btn" data-l="en" href="/en/contact/">Let's talk about it</a>
        </div>
        <p style="font-size: .82rem; color: var(--muted); margin-top: 14px;">
          <span data-l="es">Proyecto personal · código privado, disponible bajo petición.</span>
          <span data-l="en">Personal project · private code, available on request.</span>
        </p>
        <!-- ¿Tienes repo público? Sustituye el botón de arriba por:
          <a class="tb-btn" href="URL_DEL_REPO" target="_blank" rel="noopener">
            <span data-l="es">Ver en GitHub</span><span data-l="en">View on GitHub</span></a> -->
      </div>
      <div class="tb-hero-media tb-frame">
        <img src="/assets/trading-bot/market-data.png" loading="lazy" decoding="async"
             data-alt-es="Pipeline de datos de mercado: order flow agregado de más de 150 mercados"
             data-alt-en="Market data pipeline: aggregated order flow across 150+ markets"
             alt="Pipeline de datos de mercado: order flow agregado de más de 150 mercados"
             onerror="tbPH(this)">
      </div>
    </section>

    <!-- Stats -->
    <section class="tb-stats tb-reveal" style="margin-top: 64px;">
      <div class="tb-stat">
        <div class="tb-stat-num"><span class="tb-count" data-to="150">0</span>+</div>
        <div class="tb-stat-lbl"><span data-l="es">mercados agregados</span><span data-l="en">aggregated markets</span></div>
      </div>
      <div class="tb-stat">
        <div class="tb-stat-num">24/7</div>
        <div class="tb-stat-lbl"><span data-l="es">en producción</span><span data-l="en">live in production</span></div>
      </div>
      <div class="tb-stat">
        <div class="tb-stat-num"><span class="tb-count" data-to="100">0</span>%</div>
        <div class="tb-stat-lbl"><span data-l="es">Python, desde cero</span><span data-l="en">Python, from scratch</span></div>
      </div>
      <div class="tb-stat">
        <div class="tb-stat-num"><span class="tb-count" data-to="0">0</span></div>
        <div class="tb-stat-lbl"><span data-l="es">intervención manual</span><span data-l="en">manual intervention</span></div>
      </div>
    </section>

    <!-- 2. RESUMEN -->
    <section class="tb-reveal">
      <span class="tb-eyebrow"><span data-l="es">Resumen</span><span data-l="en">Overview</span></span>
      <h2><span data-l="es">Qué es</span><span data-l="en">What it is</span></h2>
      <p class="tb-lead" data-l="es">Sistema de trading automático para Bitcoin construido íntegramente en Python. Recoge datos de mercado en tiempo real desde varias fuentes, los procesa y decide cuándo operar siguiendo estrategias programadas, mientras gestiona el riesgo de forma automática. Funciona sin intervención 24/7 en un servidor en la nube y se supervisa desde un panel de control web en directo. Cada estrategia se valida antes contra años de datos históricos con métodos estadísticos rigurosos.</p>
      <p class="tb-lead" data-l="en">A fully Python-built automated trading system for Bitcoin. It collects real-time market data from multiple sources, processes it and decides when to trade following programmed strategies, all while managing risk automatically. It runs unattended 24/7 on a cloud server and is monitored through a live web dashboard. Every strategy is first validated against years of historical data using rigorous statistical methods.</p>
    </section>

    <!-- 3. HIGHLIGHTS -->
    <section class="tb-reveal">
      <span class="tb-eyebrow"><span data-l="es">Lo que demuestra</span><span data-l="en">What it shows</span></span>
      <h2><span data-l="es">Competencias clave</span><span data-l="en">Key skills</span></h2>
      <div class="tb-grid" style="margin-top: 30px;">
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🐍</span>
          <h3><span data-l="es">Backend en Python</span><span data-l="en">Python Backend</span></h3>
          <p data-l="es">Sistema asíncrono y modular construido desde cero.</p>
          <p data-l="en">Asynchronous, modular system built from scratch.</p>
        </div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🔗</span>
          <h3><span data-l="es">Ingeniería de datos</span><span data-l="en">Data Engineering</span></h3>
          <p data-l="es">Pipeline que ingiere y normaliza datos de varias APIs de mercado.</p>
          <p data-l="en">A pipeline that ingests and normalizes data from multiple market APIs.</p>
        </div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🚀</span>
          <h3><span data-l="es">Despliegue 24/7</span><span data-l="en">24/7 Deployment</span></h3>
          <p data-l="es">Corre en un servidor Linux en la nube como servicio gestionado, con auto-recuperación.</p>
          <p data-l="en">Runs on a Linux cloud server as a managed service with auto-recovery.</p>
        </div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">📊</span>
          <h3><span data-l="es">Dashboard en tiempo real</span><span data-l="en">Real-time Dashboard</span></h3>
          <p data-l="es">Panel web para monitorizar el bot, los mercados y el rendimiento.</p>
          <p data-l="en">A web panel to monitor the bot, markets and performance.</p>
        </div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🧪</span>
          <h3><span data-l="es">Validación rigurosa</span><span data-l="en">Rigorous Validation</span></h3>
          <p data-l="es">Backtesting walk-forward y Monte Carlo para probar (o descartar) cada estrategia.</p>
          <p data-l="en">Walk-forward and Monte Carlo backtesting to prove (or discard) each strategy.</p>
        </div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">🛡️</span>
          <h3><span data-l="es">Gestión de riesgo</span><span data-l="en">Risk Management</span></h3>
          <p data-l="es">Un «kill switch» detiene la operativa ante pérdidas o errores anómalos.</p>
          <p data-l="en">A kill switch halts trading on abnormal losses or errors.</p>
        </div>
        <div class="tb-card tb-reveal"><span class="ico" aria-hidden="true">✅</span>
          <h3><span data-l="es">Buenas prácticas</span><span data-l="en">Best Practices</span></h3>
          <p data-l="es">Git/GitHub, tests automatizados y tipado estricto.</p>
          <p data-l="en">Git/GitHub, automated tests and strict typing.</p>
        </div>
      </div>
    </section>

    <!-- 4. ARQUITECTURA -->
    <section class="tb-reveal tb-arch">
      <span class="tb-eyebrow"><span data-l="es">Cómo encaja todo</span><span data-l="en">How it fits together</span></span>
      <h2><span data-l="es">Arquitectura del sistema</span><span data-l="en">System Architecture</span></h2>
      <div class="tb-frame" style="margin-top: 30px;">
        <img id="tb-arch-img" loading="lazy" decoding="async"
             data-src-es="/assets/trading-bot/architecture-es.svg"
             data-src-en="/assets/trading-bot/architecture-en.svg"
             src="/assets/trading-bot/architecture-es.svg"
             data-alt-es="Diagrama de arquitectura del bot de trading"
             data-alt-en="Trading bot architecture diagram"
             alt="Diagrama de arquitectura del bot de trading"
             onerror="tbPH(this)">
      </div>
    </section>

    <!-- 5. GALERÍA -->
    <section class="tb-reveal">
      <span class="tb-eyebrow"><span data-l="es">En acción</span><span data-l="en">In action</span></span>
      <h2><span data-l="es">El sistema por dentro</span><span data-l="en">Inside the system</span></h2>
      <div class="tb-gallery" style="margin-top: 30px;">

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/trading-bot/market-data.png"
                  data-cap-es="Pipeline de datos multi-fuente: order flow agregado de +150 mercados (CVD, interés abierto, liquidaciones)."
                  data-cap-en="Multi-source data pipeline: aggregated order flow across 150+ markets (CVD, open interest, liquidations).">
            <span class="tb-frame"><img src="/assets/trading-bot/market-data.png" loading="lazy" decoding="async" alt="Pipeline de datos multi-fuente con order flow agregado" onerror="tbPH(this)"></span>
          </button>
          <figcaption>
            <span data-l="es">Pipeline de datos multi-fuente: order flow agregado de +150 mercados (CVD, interés abierto, liquidaciones).</span>
            <span data-l="en">Multi-source data pipeline: aggregated order flow across 150+ markets (CVD, open interest, liquidations).</span>
          </figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/trading-bot/backtesting.png"
                  data-cap-es="Motor de backtesting y validación: comparativa de estrategias con métricas de robustez."
                  data-cap-en="Backtesting & validation engine: strategy comparison with robustness metrics.">
            <span class="tb-frame"><img src="/assets/trading-bot/backtesting.png" loading="lazy" decoding="async" alt="Motor de backtesting con comparativa de estrategias y curva de equity" onerror="tbPH(this)"></span>
          </button>
          <figcaption>
            <span data-l="es">Motor de backtesting y validación: comparativa de estrategias con métricas de robustez.</span>
            <span data-l="en">Backtesting &amp; validation engine: strategy comparison with robustness metrics.</span>
          </figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/trading-bot/risk-engine.png"
                  data-cap-es="Motor de riesgo: máquina de estados del kill-switch, disparadores de parada y validación de órdenes."
                  data-cap-en="Risk engine: kill-switch state machine, halt triggers and order validation.">
            <span class="tb-frame"><img src="/assets/trading-bot/risk-engine.png" loading="lazy" decoding="async" alt="Motor de riesgo con máquina de estados del kill-switch" onerror="tbPH(this)"></span>
          </button>
          <figcaption>
            <span data-l="es">Motor de riesgo: máquina de estados del kill-switch, disparadores de parada y validación de órdenes.</span>
            <span data-l="en">Risk engine: kill-switch state machine, halt triggers and order validation.</span>
          </figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/trading-bot/signal-lab.png"
                  data-cap-es="Laboratorio de señales: detectores propios (NPOC, divergencias, liquidaciones) con stream en vivo."
                  data-cap-en="Signal lab: custom detectors (NPOC, divergences, liquidations) with a live stream.">
            <span class="tb-frame"><img src="/assets/trading-bot/signal-lab.png" loading="lazy" decoding="async" alt="Laboratorio de señales con detectores propios y stream en vivo" onerror="tbPH(this)"></span>
          </button>
          <figcaption>
            <span data-l="es">Laboratorio de señales: detectores propios (NPOC, divergencias, liquidaciones) con stream en vivo.</span>
            <span data-l="en">Signal lab: custom detectors (NPOC, divergences, liquidations) with a live stream.</span>
          </figcaption>
        </figure>

        <figure class="tb-fig tb-reveal">
          <button type="button" class="tb-shot" data-full="/assets/trading-bot/cockpit.png"
                  data-cap-es="Panel de control en vivo: estado del bot, kill-switch, equity y parámetros de la estrategia."
                  data-cap-en="Live control panel: bot status, kill-switch, equity and strategy parameters.">
            <span class="tb-frame"><img src="/assets/trading-bot/cockpit.png" loading="lazy" decoding="async" alt="Panel de control en vivo con estado del bot y equity" onerror="tbPH(this)"></span>
          </button>
          <figcaption>
            <span data-l="es">Panel de control en vivo: estado del bot, kill-switch, equity y parámetros de la estrategia.</span>
            <span data-l="en">Live control panel: bot status, kill-switch, equity and strategy parameters.</span>
          </figcaption>
        </figure>

      </div>
    </section>

    <!-- 6. STACK -->
    <section class="tb-reveal">
      <span class="tb-eyebrow"><span data-l="es">Herramientas</span><span data-l="en">Tooling</span></span>
      <h2><span data-l="es">Stack técnico</span><span data-l="en">Tech Stack</span></h2>
      <div class="tb-chips" style="margin-top: 26px;">
        <span class="tb-badge">Python</span>
        <span class="tb-badge">asyncio</span>
        <span class="tb-badge">DuckDB</span>
        <span class="tb-badge">Polars</span>
        <span class="tb-badge">Pydantic</span>
        <span class="tb-badge">Streamlit</span>
        <span class="tb-badge">APIs REST</span>
        <span class="tb-badge">Git/GitHub</span>
        <span class="tb-badge">Linux</span>
        <span class="tb-badge">systemd</span>
        <span class="tb-badge">VPS (Cloud)</span>
        <span class="tb-badge">pytest</span>
      </div>
    </section>

    <!-- 7. CTA -->
    <section class="tb-reveal">
      <div class="tb-cta">
        <h2><span data-l="es">¿Hablamos de ingeniería?</span><span data-l="en">Let's talk engineering</span></h2>
        <p style="max-width: 560px; margin: 0 auto;">
          <span data-l="es">Escríbeme si quieres conocer más detalles del sistema o ver el código.</span>
          <span data-l="en">Get in touch if you'd like to know more about the system or see the code.</span>
        </p>
        <div class="row">
          <a class="tb-btn" data-l="es" href="/contact/">Contacto</a>
          <a class="tb-btn" data-l="en" href="/en/contact/">Contact</a>
        </div>
        <p style="font-size: .82rem; color: var(--muted); margin-top: 16px;">
          <span data-l="es">Código privado · disponible bajo petición.</span>
          <span data-l="en">Private code · available on request.</span>
        </p>
        <!-- ¿Tienes repo público? Añade dentro de .row:
          <a class="tb-btn ghost" href="URL_DEL_REPO" target="_blank" rel="noopener">
            <span data-l="es">Ver repositorio</span><span data-l="en">View repository</span></a> -->
      </div>

      <div style="text-align: center; margin-top: 40px;">
        <a data-l="es" href="/proyectos/">⬅️ Volver a mis proyectos</a>
        <a data-l="en" href="/en/projects/">⬅️ Back to my projects</a>
      </div>
    </section>

  </div>

  <!-- Lightbox -->
  <div class="tb-lb" id="tb-lb" role="dialog" aria-modal="true" aria-label="Vista ampliada / Enlarged view">
    <button type="button" class="tb-lb-close" id="tb-lb-close" aria-label="Cerrar / Close">&times;</button>
    <img id="tb-lb-img" src="" alt="">
    <p class="tb-lb-cap" id="tb-lb-cap"></p>
  </div>
</div>

<script>
(function(){
  var tb = document.querySelector('.tb');
  if (!tb) return;

  /* ---- Placeholder oscuro para imágenes aún no subidas ---- */
  window.tbPH = function(el){
    el.onerror = null;
    el.src = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='500'><rect width='800' height='500' fill='%23121821'/><rect x='1' y='1' width='798' height='498' fill='none' stroke='%23232c38' stroke-width='2'/><g fill='none' stroke='%233ddc97' stroke-width='5' opacity='.8'><rect x='320' y='190' width='160' height='120' rx='10'/><circle cx='365' cy='230' r='14'/><path d='M325 305 L390 255 L430 285 L475 240 L475 305 Z' fill='%233ddc97' fill-opacity='.18'/></g><text x='400' y='360' fill='%2393a1b1' font-family='Segoe UI,Arial' font-size='24' text-anchor='middle'>preview · captura en preparación</text></svg>";
  };

  /* ---- Cambio de idioma ---- */
  function applyAlts(lang){
    tb.querySelectorAll('[data-alt-'+lang+']').forEach(function(img){
      img.setAttribute('alt', img.getAttribute('data-alt-'+lang));
    });
  }
  function setLang(lang){
    tb.setAttribute('data-lang', lang);
    try { localStorage.setItem('tb-lang', lang); } catch(e){}
    tb.querySelectorAll('[data-set-lang]').forEach(function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-set-lang') === lang ? 'true' : 'false');
    });
    var arch = document.getElementById('tb-arch-img');
    if (arch) { arch.onerror = window.tbPH.bind(null, arch); arch.src = arch.getAttribute('data-src-'+lang); }
    applyAlts(lang);
    document.documentElement.lang = lang;
  }
  tb.querySelectorAll('[data-set-lang]').forEach(function(b){
    b.addEventListener('click', function(){ setLang(b.getAttribute('data-set-lang')); });
  });
  setLang(tb.getAttribute('data-lang') || 'es');

  /* ---- Lightbox ---- */
  var lb = document.getElementById('tb-lb'),
      lbImg = document.getElementById('tb-lb-img'),
      lbCap = document.getElementById('tb-lb-cap'),
      lbClose = document.getElementById('tb-lb-close'),
      lastFocus = null;
  function openLB(btn){
    var lang = tb.getAttribute('data-lang');
    lastFocus = btn;
    lbImg.setAttribute('src', btn.getAttribute('data-full'));
    lbImg.setAttribute('alt', btn.getAttribute('data-cap-'+lang) || '');
    lbCap.textContent = btn.getAttribute('data-cap-'+lang) || '';
    lb.classList.add('open');
    lbClose.focus();
  }
  function closeLB(){ lb.classList.remove('open'); if (lastFocus) lastFocus.focus(); }
  tb.querySelectorAll('.tb-shot').forEach(function(btn){
    btn.addEventListener('click', function(){ openLB(btn); });
  });
  lbClose.addEventListener('click', closeLB);
  lb.addEventListener('click', function(e){ if (e.target === lb) closeLB(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && lb.classList.contains('open')) closeLB(); });

  /* ---- Reveal + contadores al entrar en viewport ---- */
  function countUp(el){
    var to = parseInt(el.getAttribute('data-to'), 10) || 0, start = null, dur = 1100;
    function step(ts){
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      el.textContent = Math.floor(p * to).toString();
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var reveals = tb.querySelectorAll('.tb-reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting){
          en.target.classList.add('is-visible');
          en.target.querySelectorAll && en.target.querySelectorAll('.tb-count').forEach(countUp);
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.14 });
    reveals.forEach(function(el){ io.observe(el); });
  } else {
    reveals.forEach(function(el){ el.classList.add('is-visible'); });
    tb.querySelectorAll('.tb-count').forEach(countUp);
  }

  /* ---- Zoom sutil en la imagen del hero al hacer scroll (sin huecos) ---- */
  var heroImg = tb.querySelector('.tb-hero-media img');
  if (heroImg && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    window.addEventListener('scroll', function(){
      var y = Math.min(window.scrollY || 0, 500);
      heroImg.style.transform = 'scale(' + (1 + y * 0.00016) + ')';
    }, { passive: true });
  }
})();
</script>
