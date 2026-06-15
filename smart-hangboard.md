---
layout: default
title: IoT Smart Climbing Trainer
description: "Medidor portátil de fuerza de agarre para escalada: diseño mecánico (CNC/3D), electrónica embebida con ESP32 y BLE, y app móvil propia."
---

<div class="pj" markdown="0">

  <!-- HERO -->
  <section class="pj-hero pj-reveal">
    <button class="pj-shot pj-frame ar-16x9" data-cap="Sensor de escalada final (V3)">
      <img src="/assets/images/climbing_sensor_main.jpg" alt="Sensor inteligente de escalada" loading="lazy">
    </button>
    <div class="pj-hero-body">
      <span class="pj-kicker">Proyecto personal · IoT &amp; Mecatrónica</span>
      <h1>Smart Climbing Sensor (IoT)</h1>
      <p class="pj-sub">Digitalizar la fuerza de agarre: un dispositivo portátil desarrollado desde cero, uniendo diseño mecánico, electrónica embebida y software móvil.</p>
      <div class="pj-chips">
        <span class="chip">ESP32</span>
        <span class="chip">Bluetooth LE</span>
        <span class="chip">HX711</span>
        <span class="chip">Célula de carga</span>
        <span class="chip">Impresión 3D</span>
        <span class="chip">CNC</span>
        <span class="chip">MIT App Inventor</span>
      </div>
    </div>
  </section>

  <!-- INTRO -->
  <section class="pj-block pj-reveal">
    <p class="pj-lead">El proyecto nació del reto de crear un ecosistema propio para medir la fuerza de los dedos. Lo desarrollé en varias versiones, aprendiendo (a veces a base de errores) hasta llegar a un dispositivo casero con precisión profesional.</p>
  </section>

  <!-- FASE 1 -->
  <section class="pj-block pj-reveal">
    <h2>Fase 1 · Prototipado y software</h2>
    <p class="pj-lead">Antes de perfeccionar la mecánica, era vital validar la electrónica y el software.</p>
    <div class="pj-gallery" style="margin-top:24px;">
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="App Android (V2): fuerza en tiempo real y exportación CSV">
          <img src="/assets/images/app_dev_v2.jpg" alt="Interfaz de la app móvil" loading="lazy">
        </button>
        <figcaption><strong>Software (V1/V2):</strong> app Android (MIT App Inventor) que grafica la fuerza en tiempo real y exporta datos CSV.</figcaption>
      </figure>
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="Prototipo V1: prueba de concepto y comunicación Bluetooth">
          <img src="/assets/images/v1_prototype.jpg" alt="Prototipo V1 del sensor" loading="lazy">
        </button>
        <figcaption><strong>Hardware V1:</strong> prueba de concepto para testear la comunicación Bluetooth.</figcaption>
      </figure>
    </div>
  </section>

  <!-- FASE 2 -->
  <section class="pj-block pj-reveal">
    <h2>Fase 2 · Ingeniería inversa y CNC</h2>
    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Interior V2: carcasa 3D + núcleo de aluminio mecanizado">
        <img src="/assets/images/v2_internal_cnc.jpg" alt="Interior de la versión V2 con núcleo de aluminio" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">El aprendizaje clave</p>
        <p>Para la V2 intenté fabricar mi propio transductor de fuerza mecanizado en aluminio. Los cálculos de deformación <strong>no contemplaron bien la histéresis del material</strong>, así que las lecturas no eran consistentes al descargar peso.</p>
        <p>Ese «fallo» fue clave: para precisión de laboratorio es más eficiente integrar sensores industriales calibrados que fabricarlos desde cero.</p>
      </div>
    </div>
  </section>

  <!-- FASE 3 -->
  <section class="pj-block pj-reveal">
    <h2>Fase 3 · Versión final (V3)</h2>
    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Sensor V3: célula de carga industrial y firmware ESP32">
        <img src="/assets/images/climbing_sensor_main.jpg" alt="Sensor de escalada V3" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Producto maduro</p>
        <p>La V3 resuelve los problemas anteriores y es el producto final.</p>
        <ul>
          <li><strong>Hardware robusto:</strong> célula de carga de grado industrial (puente de Wheatstone completo).</li>
          <li><strong>Firmware avanzado:</strong> migración a <strong>ESP32</strong> emulando el protocolo BLE de sensores profesionales (Tindeq).</li>
          <li><strong>Resultado:</strong> precisión profesional, compatible con apps de entrenamiento de terceros.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SISTEMA FIJO -->
  <section class="pj-block pj-reveal">
    <h2>Innovación · Sistema modular fijo</h2>
    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Estación fija con insertos intercambiables impresos en 3D">
        <img src="/assets/images/fixed_system_3d.jpg" alt="Sistema fijo modular para rocódromo" loading="lazy">
      </button>
      <div class="pj-txt">
        <p>En paralelo desarrollé una estación fija para rocódromos con una ventaja competitiva: <strong>insertos intercambiables</strong>.</p>
        <p>En lugar de comprar varios sensores para distintas profundidades de regleta, un sistema de acople rápido impreso en 3D permite cambiar entre regletas de 10 mm, 20 mm o romos en segundos, usando un único núcleo sensor.</p>
      </div>
    </div>
  </section>

  <!-- FICHA -->
  <section class="pj-block pj-reveal">
    <h2>Ficha técnica</h2>
    <table>
      <thead><tr><th>Dominio</th><th>Tecnologías</th></tr></thead>
      <tbody>
        <tr><td><strong>Microcontrolador</strong></td><td>ESP32 (C++ / Arduino IDE)</td></tr>
        <tr><td><strong>Sensores</strong></td><td>Células de carga + amplificador HX711</td></tr>
        <tr><td><strong>Conectividad</strong></td><td>Bluetooth Low Energy (BLE)</td></tr>
        <tr><td><strong>Fabricación</strong></td><td>Impresión 3D (PETG) + mecanizado CNC</td></tr>
        <tr><td><strong>Software</strong></td><td>MIT App Inventor + emulación de protocolo</td></tr>
      </tbody>
    </table>
  </section>

  <div style="text-align:center; margin-top:50px;">
    <a href="/proyectos/" style="text-decoration:none; font-weight:bold; color:#0366d6; font-size:1.05em; border:1px solid #0366d6; padding:10px 22px; border-radius:30px;">⬅️ Volver a mis proyectos</a>
  </div>

</div>
