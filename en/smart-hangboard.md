---
layout: default
title: IoT Smart Climbing Trainer
permalink: /en/smart-hangboard/
lang: en
description: "Portable grip-strength meter for climbing: mechanical design (CNC/3D), embedded electronics with ESP32 and BLE, and a custom mobile app."
---

<div class="pj" markdown="0">

  <!-- HERO -->
  <section class="pj-hero pj-reveal">
    <button class="pj-shot pj-frame ar-16x9" data-cap="Final climbing sensor (V3)">
      <img src="/assets/images/climbing_sensor_main.jpg" alt="Smart climbing sensor" loading="lazy">
    </button>
    <div class="pj-hero-body">
      <span class="pj-kicker">Personal project · IoT &amp; Mechatronics</span>
      <h1>Smart Climbing Sensor (IoT)</h1>
      <p class="pj-sub">Digitalizing grip strength: a portable device built from scratch, combining mechanical design, embedded electronics and mobile software.</p>
      <div class="pj-chips">
        <span class="chip">ESP32</span>
        <span class="chip">Bluetooth LE</span>
        <span class="chip">HX711</span>
        <span class="chip">Load cell</span>
        <span class="chip">3D Printing</span>
        <span class="chip">CNC</span>
        <span class="chip">MIT App Inventor</span>
      </div>
    </div>
  </section>

  <!-- INTRO -->
  <section class="pj-block pj-reveal">
    <p class="pj-lead">The project started with the challenge of building my own ecosystem to measure finger strength. I developed it over several versions, learning (sometimes the hard way) until I reached a homemade device with professional-grade precision.</p>
  </section>

  <!-- PHASE 1 -->
  <section class="pj-block pj-reveal">
    <h2>Phase 1 · Prototyping &amp; software</h2>
    <p class="pj-lead">Before perfecting the mechanics, it was vital to validate the electronics and software.</p>
    <div class="pj-gallery" style="margin-top:24px;">
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="Android app (V2): real-time force and CSV export">
          <img src="/assets/images/app_dev_v2.jpg" alt="Mobile app interface" loading="lazy">
        </button>
        <figcaption><strong>Software (V1/V2):</strong> an Android app (MIT App Inventor) that plots force in real time and exports CSV data.</figcaption>
      </figure>
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="V1 prototype: proof of concept and Bluetooth communication">
          <img src="/assets/images/v1_prototype.jpg" alt="V1 prototype of the sensor" loading="lazy">
        </button>
        <figcaption><strong>Hardware V1:</strong> a proof of concept to test Bluetooth communication.</figcaption>
      </figure>
    </div>
  </section>

  <!-- PHASE 2 -->
  <section class="pj-block pj-reveal">
    <h2>Phase 2 · Reverse engineering &amp; CNC</h2>
    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="V2 internals: 3D housing + machined aluminium core">
        <img src="/assets/images/v2_internal_cnc.jpg" alt="V2 internals with aluminium core" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">The key lesson</p>
        <p>For the V2 I tried to build my own force transducer machined in aluminium. The strain calculations <strong>didn't properly account for the material's hysteresis</strong>, so readings were inconsistent when unloading weight.</p>
        <p>That "failure" was key: for lab-grade precision it's more efficient to integrate calibrated industrial sensors than to build them from scratch.</p>
      </div>
    </div>
  </section>

  <!-- PHASE 3 -->
  <section class="pj-block pj-reveal">
    <h2>Phase 3 · Final version (V3)</h2>
    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-4x3" data-cap="V3 sensor: industrial load cell and ESP32 firmware">
        <img src="/assets/images/climbing_sensor_main.jpg" alt="V3 climbing sensor" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Mature product</p>
        <p>V3 solves the previous issues and is the final product.</p>
        <ul>
          <li><strong>Robust hardware:</strong> industrial-grade load cell (full Wheatstone bridge).</li>
          <li><strong>Advanced firmware:</strong> migration to <strong>ESP32</strong>, emulating the BLE protocol of professional sensors (Tindeq).</li>
          <li><strong>Result:</strong> professional precision, compatible with third-party training apps.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- FIXED SYSTEM -->
  <section class="pj-block pj-reveal">
    <h2>Innovation · Fixed modular system</h2>
    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Fixed station with interchangeable 3D-printed inserts">
        <img src="/assets/images/fixed_system_3d.jpg" alt="Fixed modular system for climbing gyms" loading="lazy">
      </button>
      <div class="pj-txt">
        <p>In parallel I developed a fixed station for climbing gyms with a competitive edge: <strong>interchangeable inserts</strong>.</p>
        <p>Instead of buying several sensors for different edge depths, a 3D-printed quick-coupling system lets you switch between 10 mm, 20 mm or rounded edges in seconds, using a single sensor core.</p>
      </div>
    </div>
  </section>

  <!-- SPEC SHEET -->
  <section class="pj-block pj-reveal">
    <h2>Tech sheet</h2>
    <table>
      <thead><tr><th>Domain</th><th>Technologies</th></tr></thead>
      <tbody>
        <tr><td><strong>Microcontroller</strong></td><td>ESP32 (C++ / Arduino IDE)</td></tr>
        <tr><td><strong>Sensors</strong></td><td>Load cells + HX711 amplifier</td></tr>
        <tr><td><strong>Connectivity</strong></td><td>Bluetooth Low Energy (BLE)</td></tr>
        <tr><td><strong>Manufacturing</strong></td><td>3D printing (PETG) + CNC machining</td></tr>
        <tr><td><strong>Software</strong></td><td>MIT App Inventor + protocol emulation</td></tr>
      </tbody>
    </table>
  </section>

  <div style="text-align:center; margin-top:50px;">
    <a href="/en/projects/" style="text-decoration:none; font-weight:bold; color:#0366d6; font-size:1.05em; border:1px solid #0366d6; padding:10px 22px; border-radius:30px;">⬅️ Back to my projects</a>
  </div>

</div>
