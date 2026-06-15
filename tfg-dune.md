---
layout: default
title: TFG · Soportes para sensores DUNE ND-GAr
alt: /en/tfg-dune/
description: "Diseño termo-estructural de un módulo óptico para el experimento internacional de neutrinos DUNE (ND-GAr): SolidWorks, FEM estructural y térmico, diseño criogénico."
---

<div class="pj" markdown="0">

  <!-- 1. HERO -->
  <section class="pj-hero pj-reveal">
    <button class="pj-shot pj-frame ar-16x9" data-cap="Render del módulo de lectura de luz para DUNE ND-GAr">
      <img src="/assets/images/tfg/hero_render.png" alt="Render del módulo de lectura de luz para DUNE ND-GAr" onerror="pjPH(this)">
    </button>
    <div class="pj-hero-body">
      <span class="pj-kicker">Trabajo Fin de Grado · Universidad de Vigo</span>
      <h1>Soportes mecánicos para sensores del experimento DUNE ND-GAr</h1>
      <p class="pj-sub">Diseño termo-estructural de un módulo óptico para un experimento internacional de física de neutrinos.</p>
      <div class="pj-chips">
        <span class="chip">SolidWorks</span>
        <span class="chip">Simulación FEM</span>
        <span class="chip">Análisis térmico</span>
        <span class="chip">Diseño criogénico</span>
        <span class="chip">Al 6061-T6</span>
        <span class="chip">Uniones atornilladas</span>
        <span class="chip">Diseño para fabricación</span>
      </div>
    </div>
  </section>

  <!-- 2. EL RETO -->
  <section class="pj-block pj-reveal">
    <h2>El reto</h2>
    <div class="pj-two">
      <div>
        <p>El módulo trabaja sumergido en argón a <strong>−25 °C</strong>: un salto térmico de <strong>−47 °C</strong> respecto al montaje en taller. Al enfriarse, cada material se contrae de forma distinta.</p>
        <p>Eso obliga a resolver tres problemas a la vez: mantener el <strong>sellado óptico estanco</strong>, conservar una <strong>presión de contacto constante</strong> y evitar <strong>tensiones</strong> que dañen los sensores. Un problema estructural, térmico y de sellado, simultáneo.</p>
      </div>
      <button class="pj-shot pj-frame ar-16x9" data-cap="Contexto del experimento DUNE ND-GAr">
        <img src="/assets/images/tfg/diagrama_dune.png" alt="Contexto del experimento DUNE ND-GAr" onerror="pjPH(this)">
      </button>
    </div>
  </section>

  <!-- 3. LA SOLUCIÓN -->
  <section class="pj-block pj-reveal">
    <h2>La solución</h2>

    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Vista explosionada del módulo">
        <img src="/assets/images/tfg/explosionada.png" alt="Vista explosionada del módulo" onerror="pjPH(this)">
      </button>
      <div class="pj-txt">
        <p class="why">Estructura · fabricabilidad</p>
        <h3>Carcasa de aluminio soldada (Al 6061-T6)</h3>
        <p>Una caja soldada, ligera y rígida, diseñada pensando en su <strong>fabricación real</strong>: geometría preparada para soldar y mecanizar sin sobrecostes. Diseño para fabricación desde el primer boceto.</p>
      </div>
    </div>

    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-16x10" data-cap="Sección del sellado óptico">
        <img src="/assets/images/tfg/seccion_sellado.png" alt="Sección del sellado óptico" onerror="pjPH(this)">
      </button>
      <div class="pj-txt">
        <p class="why">Óptica · sellado</p>
        <h3>Ventana óptica de doble PMMA + ITO y junta Viton</h3>
        <p>Dos láminas de PMMA con un recubrimiento intermedio de <strong>ITO</strong>: dejan pasar la luz a los sensores y, a la vez, ayudan a <strong>disipar el calor</strong>. El cierre se resuelve con una <strong>junta de Viton</strong>, compatible con presión diferencial nula. Una sola solución para óptica, térmica y estanqueidad.</p>
      </div>
    </div>

    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-1x1" data-cap="Detalle de las arandelas Belleville">
        <img src="/assets/images/tfg/detalle_belleville.png" alt="Detalle de las arandelas Belleville" onerror="pjPH(this)">
      </button>
      <div class="pj-txt">
        <p class="why">Compensación térmica</p>
        <h3>Arandelas Belleville para la contracción en frío</h3>
        <p>Al enfriarse el conjunto, las piezas encogen y la unión perdería apriete. Las <strong>arandelas Belleville</strong> absorben esa contracción y <strong>mantienen constante la presión de contacto del sellado</strong>, sin sobrecargar los tornillos.</p>
      </div>
    </div>
  </section>

  <!-- 4. VALIDACIÓN -->
  <section class="pj-block pj-reveal">
    <h2>Validación por simulación (FEM)</h2>
    <div class="pj-grid2">
      <div>
        <button class="pj-shot pj-frame ar-4x3" data-cap="Análisis estructural de tensiones (von Mises)">
          <img src="/assets/images/tfg/fem_tensiones.png" alt="Análisis estructural de tensiones (von Mises)" onerror="pjPH(this)">
        </button>
        <p class="pj-cap"><strong>Análisis estructural (von Mises).</strong> El conjunto soporta las tensiones generadas por la contracción térmica sin superar el límite del material.</p>
      </div>
      <div>
        <button class="pj-shot pj-frame ar-4x3" data-cap="Análisis térmico del módulo">
          <img src="/assets/images/tfg/analisis_termico.png" alt="Análisis térmico del módulo" onerror="pjPH(this)">
        </button>
        <p class="pj-cap"><strong>Análisis térmico.</strong> El diseño gestiona el gradiente de temperatura y mantiene los sensores dentro de su rango de trabajo.</p>
      </div>
    </div>
  </section>

  <!-- 5. RESULTADOS -->
  <section class="pj-block pj-reveal">
    <h2>Resultados</h2>
    <div class="pj-results">
      <ul>
        <li>Modelo CAD completo y <strong>fabricable</strong> de un módulo de lectura de luz para DUNE ND-GAr.</li>
        <li>Solución termo-estructural <strong>validada por FEM</strong> (von Mises + térmico) para un salto de −47 °C.</li>
        <li>Sellado óptico con junta Viton y <strong>precarga estable</strong> mediante arandelas Belleville.</li>
        <li>Ventana óptica de doble lámina PMMA + ITO con doble función óptica y térmica.</li>
        <li>Cálculos analíticos de apoyo: contracciones térmicas, uniones atornilladas y heat spreader.</li>
      </ul>
      <p style="margin: 22px 0 0;">
        <span class="pj-btn disabled" aria-disabled="true">📄 Memoria completa (PDF)</span>
      </p>
      <p class="pj-note">Disponible próximamente. <!-- Para activarlo, sustituye el span por:
        <a class="pj-btn" href="/assets/pdfs/memoria-tfg-fabio.pdf" target="_blank" rel="noopener">📄 Memoria completa (PDF)</a> --></p>
    </div>
  </section>

  <div style="text-align: center; margin-top: 50px;">
    <a href="/proyectos/" style="text-decoration: none; font-weight: bold; color: var(--accent); font-size: 1.05em; border: 1px solid var(--accent); padding: 10px 22px; border-radius: 30px;">⬅️ Volver a mis proyectos</a>
  </div>

</div>
