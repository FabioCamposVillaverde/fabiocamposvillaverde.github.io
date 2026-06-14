---
layout: default
title: BSc Thesis · Sensor supports for DUNE ND-GAr
permalink: /en/tfg-dune/
lang: en
description: "Thermo-structural design of an optical module for the international DUNE neutrino experiment (ND-GAr): SolidWorks, structural & thermal FEM, cryogenic design."
---

<style>
  /* ===== Reusable project section (BSc Thesis template) ===== */
  .pj { --accent: #0366d6; --ink: #24292e; --muted: #6b7480; }
  .pj h1 { font-size: 2.4rem; line-height: 1.15; margin: 0 0 12px; color: var(--ink); }
  .pj h2 { font-size: 1.6rem; color: var(--ink); border-left: 5px solid var(--accent); padding-left: 14px; margin: 0 0 26px; }
  .pj h3 { font-size: 1.25rem; color: var(--ink); margin: 0 0 8px; }
  .pj p  { color: #444; line-height: 1.7; }

  .pj-frame { width: 100%; border-radius: 12px; overflow: hidden; background: #eef1f4;
              box-shadow: 0 12px 30px rgba(0,0,0,.12); }
  .pj-frame img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .pj-frame img.is-ph { object-fit: cover; }
  .ar-16x9 { aspect-ratio: 16 / 9; }
  .ar-16x10 { aspect-ratio: 16 / 10; }
  .ar-4x3 { aspect-ratio: 4 / 3; }
  .ar-1x1 { aspect-ratio: 1 / 1; }

  .pj-hero { margin-bottom: 60px; }
  .pj-hero-body { margin-top: 28px; }
  .pj-kicker { display: inline-block; background: #e1f5fe; color: #0277bd; padding: 5px 12px;
               border-radius: 4px; font-size: .8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
  .pj-sub { font-size: 1.2rem; color: #555; max-width: 760px; margin: 6px 0 22px; }
  .pj-chips { display: flex; flex-wrap: wrap; gap: 10px; }
  .chip { background: #f1f3f6; border: 1px solid #e2e6ea; color: #3a424c; border-radius: 30px;
          padding: 6px 14px; font-size: .85rem; font-weight: 600; }

  .pj-block { margin: 70px 0; }
  .pj-two { display: flex; flex-wrap: wrap; gap: 40px; align-items: center; }
  .pj-two > * { flex: 1 1 360px; }

  .pj-sol { display: flex; flex-wrap: wrap; gap: 40px; align-items: center; margin-bottom: 48px; }
  .pj-sol > .pj-frame, .pj-sol > .pj-txt { flex: 1 1 360px; }
  .pj-sol.alt { flex-direction: row-reverse; }
  .pj-txt .why { color: var(--muted); font-size: .85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 6px; }

  .pj-grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
  .pj-cap { font-size: .92rem; color: #555; margin-top: 12px; }

  .pj-results { background: #f6f8fa; border: 1px solid #e9edf1; border-radius: 12px; padding: 30px 34px; }
  .pj-results ul { margin: 0; padding-left: 20px; }
  .pj-results li { margin-bottom: 10px; color: #3a424c; }
  .pj-btn { display: inline-block; margin-top: 8px; background: var(--ink); color: #fff !important;
            padding: 12px 26px; border-radius: 30px; font-weight: 600; text-decoration: none; }
  .pj-btn.disabled { background: #c7ccd1; cursor: not-allowed; }
  .pj-note { font-size: .82rem; color: #8a93a0; margin-top: 8px; }

  .pj-reveal { transition: opacity .7s ease, transform .7s ease; }
  html.js .pj-reveal { opacity: 0; transform: translateY(24px); }
  html.js .pj-reveal.is-visible { opacity: 1; transform: none; }
  @media (prefers-reduced-motion: reduce) { html.js .pj-reveal { opacity: 1; transform: none; } }

  @media (max-width: 768px) {
    .pj h1 { font-size: 1.9rem; }
    .pj-sol.alt { flex-direction: column; }
  }
</style>

<script>document.documentElement.classList.add('js');</script>

<div class="pj" markdown="0">

  <!-- 1. HERO -->
  <section class="pj-hero pj-reveal">
    <div class="pj-frame ar-16x9">
      <img class="pj-img" src="/assets/images/tfg/hero_render.png" alt="Render of the light readout module for DUNE ND-GAr" onerror="pjPH(this)">
    </div>
    <div class="pj-hero-body">
      <span class="pj-kicker">BSc Thesis · University of Vigo</span>
      <h1>Mechanical supports for sensors of the DUNE ND-GAr experiment</h1>
      <p class="pj-sub">Thermo-structural design of an optical module for an international neutrino physics experiment.</p>
      <div class="pj-chips">
        <span class="chip">SolidWorks</span>
        <span class="chip">FEM Simulation</span>
        <span class="chip">Thermal analysis</span>
        <span class="chip">Cryogenic design</span>
        <span class="chip">Al 6061-T6</span>
        <span class="chip">Bolted joints</span>
        <span class="chip">Design for Manufacturing</span>
      </div>
    </div>
  </section>

  <!-- 2. THE CHALLENGE -->
  <section class="pj-block pj-reveal">
    <h2>The challenge</h2>
    <div class="pj-two">
      <div>
        <p>The module operates submerged in argon at <strong>−25 °C</strong>: a thermal swing of <strong>−47 °C</strong> from workshop assembly. As it cools, each material contracts differently.</p>
        <p>That means solving three problems at once: keeping the <strong>optical seal tight</strong>, holding a <strong>constant contact pressure</strong>, and avoiding <strong>stresses</strong> that could damage the sensors. A structural, thermal and sealing problem, all at the same time.</p>
      </div>
      <div class="pj-frame ar-16x9">
        <img class="pj-img" src="/assets/images/tfg/diagrama_dune.png" alt="Context of the DUNE ND-GAr experiment" onerror="pjPH(this)">
      </div>
    </div>
  </section>

  <!-- 3. THE SOLUTION -->
  <section class="pj-block pj-reveal">
    <h2>The solution</h2>

    <div class="pj-sol">
      <div class="pj-frame ar-4x3">
        <img class="pj-img" src="/assets/images/tfg/explosionada.png" alt="Exploded view of the module" onerror="pjPH(this)">
      </div>
      <div class="pj-txt">
        <p class="why">Structure · manufacturability</p>
        <h3>Welded aluminium housing (Al 6061-T6)</h3>
        <p>A welded box — light and stiff — designed around <strong>real manufacturing</strong>: geometry ready to be welded and machined without extra cost. Design for Manufacturing from the very first sketch.</p>
      </div>
    </div>

    <div class="pj-sol alt">
      <div class="pj-frame ar-16x10">
        <img class="pj-img" src="/assets/images/tfg/seccion_sellado.png" alt="Section view of the optical seal" onerror="pjPH(this)">
      </div>
      <div class="pj-txt">
        <p class="why">Optics · sealing</p>
        <h3>Dual PMMA + ITO optical window and Viton seal</h3>
        <p>Two PMMA sheets with an intermediate <strong>ITO</strong> coating: they let light through to the sensors while helping to <strong>dissipate heat</strong>. The closure uses a <strong>Viton seal</strong>, compatible with zero differential pressure. One solution covering optics, thermal and sealing.</p>
      </div>
    </div>

    <div class="pj-sol">
      <div class="pj-frame ar-1x1">
        <img class="pj-img" src="/assets/images/tfg/detalle_belleville.png" alt="Detail of the Belleville washers" onerror="pjPH(this)">
      </div>
      <div class="pj-txt">
        <p class="why">Thermal compensation</p>
        <h3>Belleville washers for cold contraction</h3>
        <p>As the assembly cools, parts shrink and the joint would lose preload. The <strong>Belleville washers</strong> absorb that contraction and <strong>keep the sealing contact pressure constant</strong>, without overloading the bolts.</p>
      </div>
    </div>
  </section>

  <!-- 4. VALIDATION -->
  <section class="pj-block pj-reveal">
    <h2>Validation by simulation (FEM)</h2>
    <div class="pj-grid2">
      <div>
        <div class="pj-frame ar-4x3">
          <img class="pj-img" src="/assets/images/tfg/fem_tensiones.png" alt="Structural stress analysis (von Mises)" onerror="pjPH(this)">
        </div>
        <p class="pj-cap"><strong>Structural analysis (von Mises).</strong> The assembly withstands the stresses caused by thermal contraction without exceeding the material limit.</p>
      </div>
      <div>
        <div class="pj-frame ar-4x3">
          <img class="pj-img" src="/assets/images/tfg/analisis_termico.png" alt="Thermal analysis of the module" onerror="pjPH(this)">
        </div>
        <p class="pj-cap"><strong>Thermal analysis.</strong> The design manages the temperature gradient and keeps the sensors within their operating range.</p>
      </div>
    </div>
  </section>

  <!-- 5. RESULTS -->
  <section class="pj-block pj-reveal">
    <h2>Results</h2>
    <div class="pj-results">
      <ul>
        <li>Complete, <strong>manufacturable</strong> CAD model of a light readout module for DUNE ND-GAr.</li>
        <li>Thermo-structural solution <strong>validated by FEM</strong> (von Mises + thermal) for a −47 °C swing.</li>
        <li>Optical sealing with a Viton gasket and <strong>stable preload</strong> via Belleville washers.</li>
        <li>Dual-sheet PMMA + ITO optical window with combined optical and thermal function.</li>
        <li>Supporting analytical calculations: thermal contractions, bolted joints and heat spreader.</li>
      </ul>
      <p style="margin: 22px 0 0;">
        <span class="pj-btn disabled" aria-disabled="true">📄 Full report (PDF)</span>
      </p>
      <p class="pj-note">Coming soon. <!-- To enable it, replace the span with:
        <a class="pj-btn" href="/assets/pdfs/memoria-tfg-fabio.pdf" target="_blank" rel="noopener">📄 Full report (PDF)</a> --></p>
    </div>
  </section>

  <div style="text-align: center; margin-top: 50px;">
    <a href="/en/projects/" style="text-decoration: none; font-weight: bold; color: #0366d6; font-size: 1.05em; border: 1px solid #0366d6; padding: 10px 22px; border-radius: 30px;">⬅️ Back to my projects</a>
  </div>

</div>

<script>
  function pjPH(el){
    el.onerror = null;
    el.classList.add('is-ph');
    el.src = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='600'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%23262b33'/><stop offset='1' stop-color='%233b424d'/></linearGradient></defs><rect width='800' height='600' fill='url(%23g)'/><g fill='none' stroke='%236f7a8a' stroke-width='6'><rect x='300' y='235' width='200' height='150' rx='10'/><path d='M300 235 L350 195 L550 195 L500 235 M500 385 L550 345 L550 195'/></g><text x='400' y='450' fill='%238a93a0' font-family='Segoe UI,Arial,sans-serif' font-size='30' text-anchor='middle'>Render coming soon</text></svg>";
  }

  (function(){
    var els = document.querySelectorAll('.pj-reveal');
    if (!('IntersectionObserver' in window)) { els.forEach(function(e){ e.classList.add('is-visible'); }); return; }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting){ en.target.classList.add('is-visible'); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    els.forEach(function(e){ io.observe(e); });
  })();
</script>
