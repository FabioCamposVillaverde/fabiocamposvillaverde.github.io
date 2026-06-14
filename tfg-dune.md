---
layout: default
title: TFG · Soportes para sensores DUNE ND-GAr
description: "Diseño termo-estructural de un módulo óptico para el experimento internacional de neutrinos DUNE (ND-GAr): SolidWorks, FEM estructural y térmico, diseño criogénico."
---

<style>
  /* ===== Sección de proyecto reutilizable (plantilla TFG) ===== */
  .pj { --accent: #0366d6; --ink: #24292e; --muted: #6b7480; }
  .pj h1 { font-size: 2.4rem; line-height: 1.15; margin: 0 0 12px; color: var(--ink); }
  .pj h2 { font-size: 1.6rem; color: var(--ink); border-left: 5px solid var(--accent); padding-left: 14px; margin: 0 0 26px; }
  .pj h3 { font-size: 1.25rem; color: var(--ink); margin: 0 0 8px; }
  .pj p  { color: #444; line-height: 1.7; }

  /* Marcos de imagen con relación de aspecto fija (evita saltos de maquetación) */
  .pj-frame { width: 100%; border-radius: 12px; overflow: hidden; background: #eef1f4;
              box-shadow: 0 12px 30px rgba(0,0,0,.12); }
  .pj-frame img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .pj-frame img.is-ph { object-fit: cover; }
  .ar-16x9 { aspect-ratio: 16 / 9; }
  .ar-16x10 { aspect-ratio: 16 / 10; }
  .ar-4x3 { aspect-ratio: 4 / 3; }
  .ar-1x1 { aspect-ratio: 1 / 1; }

  /* Hero */
  .pj-hero { margin-bottom: 60px; }
  .pj-hero-body { margin-top: 28px; }
  .pj-kicker { display: inline-block; background: #e1f5fe; color: #0277bd; padding: 5px 12px;
               border-radius: 4px; font-size: .8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
  .pj-sub { font-size: 1.2rem; color: #555; max-width: 760px; margin: 6px 0 22px; }
  .pj-chips { display: flex; flex-wrap: wrap; gap: 10px; }
  .chip { background: #f1f3f6; border: 1px solid #e2e6ea; color: #3a424c; border-radius: 30px;
          padding: 6px 14px; font-size: .85rem; font-weight: 600; }

  /* Bloques */
  .pj-block { margin: 70px 0; }
  .pj-two { display: flex; flex-wrap: wrap; gap: 40px; align-items: center; }
  .pj-two > * { flex: 1 1 360px; }

  /* Galería de soluciones (alterna imagen / texto) */
  .pj-sol { display: flex; flex-wrap: wrap; gap: 40px; align-items: center; margin-bottom: 48px; }
  .pj-sol > .pj-frame, .pj-sol > .pj-txt { flex: 1 1 360px; }
  .pj-sol.alt { flex-direction: row-reverse; }
  .pj-txt .why { color: var(--muted); font-size: .85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; margin-bottom: 6px; }

  /* Validación */
  .pj-grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
  .pj-cap { font-size: .92rem; color: #555; margin-top: 12px; }

  /* Resultados */
  .pj-results { background: #f6f8fa; border: 1px solid #e9edf1; border-radius: 12px; padding: 30px 34px; }
  .pj-results ul { margin: 0; padding-left: 20px; }
  .pj-results li { margin-bottom: 10px; color: #3a424c; }
  .pj-btn { display: inline-block; margin-top: 8px; background: var(--ink); color: #fff !important;
            padding: 12px 26px; border-radius: 30px; font-weight: 600; text-decoration: none; }
  .pj-btn.disabled { background: #c7ccd1; cursor: not-allowed; }
  .pj-note { font-size: .82rem; color: #8a93a0; margin-top: 8px; }

  /* Animación de aparición al hacer scroll (solo si hay JS) */
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
      <img class="pj-img" src="/assets/images/tfg/hero_render.png" alt="Render del módulo de lectura de luz para DUNE ND-GAr" onerror="pjPH(this)">
    </div>
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
      <div class="pj-frame ar-16x9">
        <img class="pj-img" src="/assets/images/tfg/diagrama_dune.png" alt="Contexto del experimento DUNE ND-GAr" onerror="pjPH(this)">
      </div>
    </div>
  </section>

  <!-- 3. LA SOLUCIÓN -->
  <section class="pj-block pj-reveal">
    <h2>La solución</h2>

    <div class="pj-sol">
      <div class="pj-frame ar-4x3">
        <img class="pj-img" src="/assets/images/tfg/explosionada.png" alt="Vista explosionada del módulo" onerror="pjPH(this)">
      </div>
      <div class="pj-txt">
        <p class="why">Estructura · fabricabilidad</p>
        <h3>Carcasa de aluminio soldada (Al 6061-T6)</h3>
        <p>Una caja soldada, ligera y rígida, diseñada pensando en su <strong>fabricación real</strong>: geometría preparada para soldar y mecanizar sin sobrecostes. Diseño para fabricación desde el primer boceto.</p>
      </div>
    </div>

    <div class="pj-sol alt">
      <div class="pj-frame ar-16x10">
        <img class="pj-img" src="/assets/images/tfg/seccion_sellado.png" alt="Sección del sellado óptico" onerror="pjPH(this)">
      </div>
      <div class="pj-txt">
        <p class="why">Óptica · sellado</p>
        <h3>Ventana óptica de doble PMMA + ITO y junta Viton</h3>
        <p>Dos láminas de PMMA con un recubrimiento intermedio de <strong>ITO</strong>: dejan pasar la luz a los sensores y, a la vez, ayudan a <strong>disipar el calor</strong>. El cierre se resuelve con una <strong>junta de Viton</strong>, compatible con presión diferencial nula. Una sola solución para óptica, térmica y estanqueidad.</p>
      </div>
    </div>

    <div class="pj-sol">
      <div class="pj-frame ar-1x1">
        <img class="pj-img" src="/assets/images/tfg/detalle_belleville.png" alt="Detalle de las arandelas Belleville" onerror="pjPH(this)">
      </div>
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
        <div class="pj-frame ar-4x3">
          <img class="pj-img" src="/assets/images/tfg/fem_tensiones.png" alt="Análisis estructural de tensiones (von Mises)" onerror="pjPH(this)">
        </div>
        <p class="pj-cap"><strong>Análisis estructural (von Mises).</strong> El conjunto soporta las tensiones generadas por la contracción térmica sin superar el límite del material.</p>
      </div>
      <div>
        <div class="pj-frame ar-4x3">
          <img class="pj-img" src="/assets/images/tfg/analisis_termico.png" alt="Análisis térmico del módulo" onerror="pjPH(this)">
        </div>
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
    <a href="/proyectos/" style="text-decoration: none; font-weight: bold; color: #0366d6; font-size: 1.05em; border: 1px solid #0366d6; padding: 10px 22px; border-radius: 30px;">⬅️ Volver a mis proyectos</a>
  </div>

</div>

<script>
  // Sustituye una imagen que aún no existe por un panel "en preparación" (evita el icono de imagen rota)
  function pjPH(el){
    el.onerror = null;
    el.classList.add('is-ph');
    el.src = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='800' height='600'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%23262b33'/><stop offset='1' stop-color='%233b424d'/></linearGradient></defs><rect width='800' height='600' fill='url(%23g)'/><g fill='none' stroke='%236f7a8a' stroke-width='6'><rect x='300' y='235' width='200' height='150' rx='10'/><path d='M300 235 L350 195 L550 195 L500 235 M500 385 L550 345 L550 195'/></g><text x='400' y='450' fill='%238a93a0' font-family='Segoe UI,Arial,sans-serif' font-size='30' text-anchor='middle'>Render en preparación</text></svg>";
  }

  // Aparición suave al hacer scroll
  (function(){
    var els = document.querySelectorAll('.pj-reveal');
    if (!('IntersectionObserver' in window)) { els.forEach(function(e){ e.classList.add('is-visible'); }); return; }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting){ en.target.classList.add('is-visible'); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    els.forEach(function(e){ io.observe(e); });
  })();
</script>
