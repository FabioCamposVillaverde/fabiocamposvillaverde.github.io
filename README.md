---
layout: default
title: Home
permalink: /
order: 1
alt: /en/
description: "Portafolio de ingeniería mecánica de Fabio Campos: diseño paramétrico en SolidWorks, mecatrónica y fabricación. Del CAD al prototipo funcional."
---

<style>
  .home-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 26px; margin-top: 30px; }
  .home-card { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform .25s, box-shadow .25s, border-color .25s; }
  .home-card:hover { transform: translateY(-6px); box-shadow: 0 22px 44px rgba(0,0,0,.5); border-color: rgba(61,220,151,.5); }
  .home-card .thumb { height: 190px; overflow: hidden; background: #0e141c; }
  .home-card .thumb img { width: 100%; height: 100%; object-fit: cover; transition: transform .5s; }
  .home-card:hover .thumb img { transform: scale(1.05); }
  .home-card .body { padding: 22px; flex-grow: 1; display: flex; flex-direction: column; }
  .home-card .tag { font-size: .72rem; text-transform: uppercase; letter-spacing: 1px; color: var(--accent-2); font-weight: 700; margin-bottom: 8px; }
  .home-card h4 { margin: 0 0 8px; font-size: 1.1rem; color: var(--text); }
  .home-card p { margin: 0; font-size: .92rem; color: var(--muted); line-height: 1.6; }
  .skill-card { flex: 1 1 280px; padding: 30px; background: var(--panel); border: 1px solid var(--line); border-radius: 14px; transition: transform .2s, border-color .2s; }
  .skill-card:hover { transform: translateY(-4px); border-color: rgba(61,220,151,.4); }
  .home-cta-band { background: linear-gradient(135deg, #10212a, #131c12); border: 1px solid var(--line); border-radius: 16px; padding: 44px 28px; text-align: center; margin: 10px 0 50px; }
  .hero-btn-primary { background: var(--accent); color: #07120c; padding: 12px 28px; text-decoration: none; border-radius: 8px; font-weight: 700; font-size: 1.05rem; display: inline-block; }
  .hero-btn-ghost { background: transparent; color: var(--text); border: 1px solid var(--line); padding: 11px 24px; text-decoration: none; border-radius: 8px; font-weight: 600; font-size: 1.05rem; display: inline-block; }
</style>

<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 50px; margin-bottom: 60px;">

  <div style="flex: 1; min-width: 280px;">
    <img src="/assets/images/mifoto.jpg" alt="Fabio Campos" style="border-radius: 16px; width: 100%; max-width: 350px; box-shadow: 0 20px 50px rgba(0,0,0,.5); object-fit: cover;">
  </div>

  <div style="flex: 2; min-width: 300px;">
    <span style="background: rgba(61,220,151,.12); color: var(--accent-2); padding: 5px 12px; border-radius: 30px; font-size: .8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">Ingeniería Mecánica</span>
    <h1 style="margin-top: 16px; margin-bottom: 10px; font-size: 2.9rem; line-height: 1.1; color: var(--text);">Hola, soy<br>Fabio Campos.</h1>
    <h3 style="color: var(--muted); font-weight: normal; margin-top: 0; font-size: 1.25rem;">Ingeniería Mecánica · Universidad de Vigo · Graduación 2026</h3>

    <p style="font-size: 1.15em; line-height: 1.7; color: #b9c2cf; margin-top: 20px;">
      Mención en <strong style="color: var(--text);">Diseño y Fabricación</strong>. Me gusta coger un proyecto y llevarlo de principio a fin: del modelo CAD al prototipo que funciona.
      Combino la mecánica clásica con electrónica e IoT y, lo que aún no domino, lo aprendo construyéndolo.
    </p>
    <p style="font-size: 1em; color: #cdd6e0; background: var(--panel); padding: 12px 16px; border-left: 4px solid var(--accent); border-radius: 0 8px 8px 0;">
      🎓 Actualmente desarrollando mi TFG: el diseño termo-estructural de un módulo óptico para el experimento internacional de neutrinos DUNE.
    </p>

    <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 24px;">
      <a href="./proyectos/" class="hero-btn-primary">Ver Proyectos</a>
      <a href="./resume/" class="hero-btn-ghost">📄 Ver Currículum</a>
    </div>
  </div>

</div>

<hr style="border: 0; border-top: 1px solid var(--line); margin: 60px 0;">

<div style="text-align: center; margin-bottom: 40px;">
  <h2 style="margin-bottom: 10px; font-size: 2rem; color: var(--text);">Competencias Técnicas</h2>
  <p style="color: var(--muted); font-size: 1.1em;">Un perfil híbrido entre la mecánica tradicional y la tecnología digital, con muchas horas de taller y de código detrás.</p>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 26px; text-align: left;">

  <div class="skill-card">
    <h4 style="color: var(--accent); margin-top: 0; font-size: 1.3rem;">📐 Ingeniería & CAD</h4>
    <p style="font-size: 1em; color: #b9c2cf; line-height: 1.7;">
      Diseño paramétrico y de chapa metálica en <strong style="color:var(--text);">SolidWorks</strong> y Fusion 360. Experiencia en simulación FEA (ANSYS / SW Simulation) y cálculo de estructuras aplicada a mis proyectos.
    </p>
  </div>

  <div class="skill-card">
    <h4 style="color: #ff6b9d; margin-top: 0; font-size: 1.3rem;">⚡ Electrónica & IoT</h4>
    <p style="font-size: 1em; color: #b9c2cf; line-height: 1.7;">
      Integro microcontroladores (<strong style="color:var(--text);">ESP32/Arduino</strong>) con sensores industriales (células de carga, encoders) y programo en C++ y Python. Electrónica que he aprendido por mi cuenta para dar vida a mis diseños.
    </p>
  </div>

  <div class="skill-card">
    <h4 style="color: #4aa8ff; margin-top: 0; font-size: 1.3rem;">🏭 Fabricación Real</h4>
    <p style="font-size: 1em; color: #b9c2cf; line-height: 1.7;">
      Del ordenador al taller. Diseño de piezas funcionales para <strong style="color:var(--text);">impresión 3D</strong>, mecanizado CNC básico y montaje estructural en obra. Disfruto cuando una idea acaba siendo una pieza real.
    </p>
  </div>

</div>

<br><br>

<div style="text-align: center; margin-bottom: 6px;">
  <h2 style="font-size: 2rem; margin-bottom: 8px; color: var(--text);">Proyectos destacados</h2>
  <p style="color: var(--muted);">Una muestra de en qué he estado trabajando. <a href="./proyectos/" style="font-weight: 600;">Ver todos ➔</a></p>
</div>

<div class="home-cards">

  <a href="./tfg-dune" class="home-card">
    <div class="thumb"><img src="/assets/images/tfg/hero_render.png" alt="TFG · Soportes para sensores del experimento DUNE ND-GAr" loading="lazy"></div>
    <div class="body">
      <span class="tag">TFG · Diseño termo-estructural</span>
      <h4>Soportes para sensores · DUNE</h4>
      <p>Módulo óptico criogénico para un experimento internacional de neutrinos. SolidWorks y validación FEM.</p>
    </div>
  </a>

  <a href="./trading-bot" class="home-card">
    <div class="thumb"><img src="/assets/images/trading-bot/02_market_data.png" alt="Bot de Trading Algorítmico para Bitcoin" loading="lazy" onerror="this.onerror=null;this.src='data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22600%22%20height=%22400%22%3E%3Crect%20width=%22600%22%20height=%22400%22%20fill=%22%23121821%22/%3E%3Ctext%20x=%22300%22%20y=%22205%22%20fill=%22%233ddc97%22%20font-family=%22Segoe%20UI,Arial%22%20font-size=%2226%22%20text-anchor=%22middle%22%3ETrading%20Bot%3C/text%3E%3C/svg%3E'"></div>
    <div class="body">
      <span class="tag">Python · Datos · DevOps</span>
      <h4>Bot de Trading Algorítmico</h4>
      <p>Sistema autónomo en Python que opera Bitcoin 24/7, con dashboard en vivo y gestión de riesgo.</p>
    </div>
  </a>

  <a href="./simulador-racing" class="home-card">
    <div class="thumb"><img src="/assets/images/01_full_rig.jpg" alt="Simulador Direct Drive de 15 Nm" loading="lazy"></div>
    <div class="body">
      <span class="tag">Mecatrónica</span>
      <h4>Simulador Direct Drive 15 Nm</h4>
      <p>Volante Force Feedback construido por ingeniería inversa, con pedales de célula de carga y telemetría propia.</p>
    </div>
  </a>

</div>

<hr style="border: 0; border-top: 1px solid var(--line); margin: 60px 0;">

<div id="sobre-mi" style="max-width: 760px;">
  <h2 style="font-size: 1.9rem; margin-bottom: 14px; color: var(--text);">Sobre mí</h2>
  <p style="font-size: 1.1em; color: #b9c2cf; line-height: 1.8;">
    Soy un ingeniero al que le gusta ensuciarse las manos. Aprendí electrónica, programación e impresión 3D por mi cuenta, a base de prototipos que fallaban hasta que funcionaban. Vengo de la escalada y la cultura maker, y de ahí me llevo la constancia para resolver un problema hasta el final. No lo sé todo, pero con tiempo y trabajo aprendo lo que haga falta para sacar un proyecto adelante.
  </p>
</div>

<div class="home-cta-band">
  <h2 style="font-size: 1.7rem; margin: 0 0 10px; color: var(--text);">¿Tienes un proyecto o una oportunidad en mente?</h2>
  <p style="color: var(--muted); margin: 0 0 24px;">Busco mi primera oportunidad como ingeniero mecánico junior.</p>
  <a href="./contact/" class="hero-btn-primary">Hablemos ➔</a>
</div>
