---
layout: default
title: Simulador Direct Drive DIY
description: "Simulador de conducción Direct Drive (15 Nm) diseñado y fabricado pieza a pieza: FFBeast, pedales con célula de carga, telemetría LED y bass shakers."
---

<div class="pj" markdown="0">

  <!-- HERO -->
  <section class="pj-hero pj-reveal">
    <button class="pj-shot pj-frame ar-16x9" data-cap="Conjunto completo del simulador Direct Drive">
      <img src="/assets/images/01_full_rig.jpg" alt="Simulador de conducción Direct Drive completo" loading="lazy">
    </button>
    <div class="pj-hero-body">
      <span class="pj-kicker">Proyecto personal · Mecatrónica</span>
      <h1>Simulador Direct Drive · DIY</h1>
      <p class="pj-sub">Un ecosistema de simulación de competición diseñado y fabricado desde cero para replicar las fuerzas de un coche real.</p>
      <div class="pj-chips">
        <span class="chip">FFBeast</span>
        <span class="chip">Force Feedback 15 Nm</span>
        <span class="chip">Arduino</span>
        <span class="chip">SimHub</span>
        <span class="chip">Impresión 3D</span>
        <span class="chip">Células de carga</span>
        <span class="chip">Ingeniería inversa</span>
      </div>
    </div>
  </section>

  <!-- INTRO -->
  <section class="pj-block pj-reveal">
    <p class="pj-lead">En vez de comprar una base comercial cerrada, monté un sistema completo combinando un proyecto open-source de Force Feedback, impresión 3D y electrónica programada a medida. Cada periférico está pensado, diseñado en CAD y ajustado a mano.</p>
  </section>

  <!-- BLOQUES -->
  <section class="pj-block pj-reveal">
    <h2>El corazón: proyecto FFBeast</h2>
    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Base del motor con carcasa impresa en 3D y refrigeración forzada">
        <img src="/assets/images/03_motor_base.jpg" alt="Base del motor del simulador" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Force Feedback</p>
        <p>El Force Feedback se basa en el proyecto open-source <strong>FFBeast</strong>, capaz de gestionar pares de fuerza altos con gran fidelidad.</p>
        <ul>
          <li><strong>Motor:</strong> recuperado de un patinete eléctrico, con picos de <strong>15 Nm</strong>.</li>
          <li><strong>Suavidad:</strong> el software elimina el <em>cogging</em> del motor, logrando un tacto comparable al de bases Direct Drive de gama alta.</li>
          <li><strong>Refrigeración:</strong> carcasa impresa en 3D con flujo de aire forzado.</li>
        </ul>
      </div>
    </div>

    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Pedales con cuerpo en PETG y célula de carga">
        <img src="/assets/images/04_pedals_profile.jpg" alt="Perfil de los pedales del simulador" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Pedales</p>
        <h3>Frenada por presión, no por recorrido</h3>
        <p>Pedales inspirados en la ingeniería de <em>Heusinkveld</em>, con placas de acero y cuerpos en PETG al 100 % de relleno.</p>
        <ul>
          <li><strong>Freno:</strong> mide presión con una <strong>célula de carga de 100 kg</strong>.</li>
          <li><strong>Tacto ajustable:</strong> elastómeros de distinta dureza para simular desde un coche de calle hasta un F1.</li>
          <li><strong>Acelerador:</strong> sensor Hall magnético sin contacto, durabilidad total.</li>
        </ul>
      </div>
    </div>

    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Volante con matriz LED y botonera, gestionado por SimHub">
        <img src="/assets/images/02_cockpit_layout.jpg" alt="Volante con telemetría LED" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Telemetría visual</p>
        <h3>Información en el volante con SimHub</h3>
        <ul>
          <li><strong>Matriz LED central:</strong> muestra la marcha engranada.</li>
          <li><strong>Barra de revoluciones:</strong> una tira RGB marca el punto de cambio.</li>
          <li><strong>Banderas y spotter:</strong> los LED laterales avisan de banderas de pista y ángulo muerto.</li>
          <li><strong>Botonera:</strong> matriz de botones + joystick para los menús del coche.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- RALLY & DRIFT -->
  <section class="pj-block pj-reveal">
    <h2>Control para rally y drift</h2>
    <p class="pj-lead">Para disciplinas más agresivas fabriqué dos periféricos dedicados en metal e impresión 3D.</p>
    <div class="pj-gallery" style="margin-top:24px;">
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="Cambio secuencial con mecanismo de leva interna">
          <img src="/assets/images/05_shifter_detail.jpg" alt="Detalle del cambio secuencial" loading="lazy">
        </button>
        <figcaption><strong>Cambio secuencial:</strong> mecanismo de leva interna con muelles de alta tensión y un «clack» metálico real.</figcaption>
      </figure>
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="Freno de mano con célula de carga de 20 kg para drift">
          <img src="/assets/images/06_handbrake_detail.jpg" alt="Detalle del freno de mano" loading="lazy">
        </button>
        <figcaption><strong>Freno de mano:</strong> usa una <strong>célula de carga de 20 kg</strong> para modular la frenada trasera con precisión en el drift.</figcaption>
      </figure>
    </div>
  </section>

  <!-- BASS SHAKERS -->
  <section class="pj-block pj-reveal">
    <h2>Inmersión háptica: bass shakers</h2>
    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Bass shaker fabricado con altavoces reciclados">
        <img src="/assets/images/08_bass_shaker.jpg" alt="Bass shaker bajo el asiento" loading="lazy">
      </button>
      <div class="pj-txt">
        <p>El Force Feedback te dice lo que hacen las ruedas delanteras; los <strong>bass shakers</strong> transmiten el resto del chasis. Los construí con altavoces reciclados convertidos en pistones de vibración, anclados bajo el asiento y los pedales.</p>
        <p>Se sienten los baches, los cambios de marcha, la vibración al ralentí y el bloqueo de ruedas: la diferencia entre jugar y conducir.</p>
      </div>
    </div>
  </section>

  <!-- ESPECIFICACIONES -->
  <section class="pj-block pj-reveal">
    <h2>Resumen de especificaciones</h2>
    <table>
      <thead><tr><th>Componente</th><th>Tecnología</th><th>Software / Driver</th></tr></thead>
      <tbody>
        <tr><td><strong>Base</strong></td><td>Motor de patinete modificado (15 Nm)</td><td>Proyecto <strong>FFBeast</strong></td></tr>
        <tr><td><strong>Pedales</strong></td><td>Célula de carga 100 kg</td><td>Arduino Joystick Lib</td></tr>
        <tr><td><strong>Freno de mano</strong></td><td>Célula de carga 20 kg</td><td>Amplificador HX711</td></tr>
        <tr><td><strong>Dashboard</strong></td><td>Matriz LED + WS2812b</td><td><strong>SimHub</strong></td></tr>
        <tr><td><strong>Estructura</strong></td><td>Madera reforzada + acero</td><td>Diseño propio CAD</td></tr>
      </tbody>
    </table>
  </section>

  <div style="text-align:center; margin-top:50px;">
    <a href="/proyectos/" style="text-decoration:none; font-weight:bold; color:#0366d6; font-size:1.05em; border:1px solid #0366d6; padding:10px 22px; border-radius:30px;">⬅️ Volver a mis proyectos</a>
  </div>

</div>
