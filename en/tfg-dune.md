---
layout: default
title: BSc Thesis · Sensor supports for DUNE ND-GAr
permalink: /en/tfg-dune/
lang: en
alt: /tfg-dune/
description: "Thermo-structural design of an optical module for the international DUNE neutrino experiment (ND-GAr): SolidWorks, structural & thermal FEM, cryogenic design."
---

<div class="pj" markdown="0">

  <!-- 1. HERO -->
  <section class="pj-hero pj-reveal">
    <button class="pj-shot pj-frame ar-16x9" data-cap="Render of the light readout module for DUNE ND-GAr">
      <img src="/assets/images/tfg/hero_render.png" alt="Render of the light readout module for DUNE ND-GAr" onerror="pjPH(this)">
    </button>
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
      <button class="pj-shot pj-frame ar-16x9" data-cap="Context of the DUNE ND-GAr experiment">
        <img src="/assets/images/tfg/diagrama_dune.png" alt="Context of the DUNE ND-GAr experiment" onerror="pjPH(this)">
      </button>
    </div>
  </section>

  <!-- 3. THE SOLUTION -->
  <section class="pj-block pj-reveal">
    <h2>The solution</h2>

    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Exploded view of the module">
        <img src="/assets/images/tfg/explosionada.png" alt="Exploded view of the module" onerror="pjPH(this)">
      </button>
      <div class="pj-txt">
        <p class="why">Structure · manufacturability</p>
        <h3>Welded aluminium housing (Al 6061-T6)</h3>
        <p>A welded box — light and stiff — designed around <strong>real manufacturing</strong>: geometry ready to be welded and machined without extra cost. Design for Manufacturing from the very first sketch.</p>
      </div>
    </div>

    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-16x10" data-cap="Section view of the optical seal">
        <img src="/assets/images/tfg/seccion_sellado.png" alt="Section view of the optical seal" onerror="pjPH(this)">
      </button>
      <div class="pj-txt">
        <p class="why">Optics · sealing</p>
        <h3>Dual PMMA + ITO optical window and Viton seal</h3>
        <p>Two PMMA sheets with an intermediate <strong>ITO</strong> coating: they let light through to the sensors while helping to <strong>dissipate heat</strong>. The closure uses a <strong>Viton seal</strong>, compatible with zero differential pressure. One solution covering optics, thermal and sealing.</p>
      </div>
    </div>

    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-1x1" data-cap="Detail of the Belleville washers">
        <img src="/assets/images/tfg/detalle_belleville.png" alt="Detail of the Belleville washers" onerror="pjPH(this)">
      </button>
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
        <button class="pj-shot pj-frame ar-4x3" data-cap="Structural stress analysis (von Mises)">
          <img src="/assets/images/tfg/fem_tensiones.png" alt="Structural stress analysis (von Mises)" onerror="pjPH(this)">
        </button>
        <p class="pj-cap"><strong>Structural analysis (von Mises).</strong> The assembly withstands the stresses caused by thermal contraction without exceeding the material limit.</p>
      </div>
      <div>
        <button class="pj-shot pj-frame ar-4x3" data-cap="Thermal analysis of the module">
          <img src="/assets/images/tfg/analisis_termico.png" alt="Thermal analysis of the module" onerror="pjPH(this)">
        </button>
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
    <a href="/en/projects/" style="text-decoration: none; font-weight: bold; color: var(--accent); font-size: 1.05em; border: 1px solid var(--accent); padding: 10px 22px; border-radius: 30px;">⬅️ Back to my projects</a>
  </div>

</div>
