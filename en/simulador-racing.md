---
layout: default
title: DIY Direct Drive Sim Rig
permalink: /en/simulador-racing/
lang: en
description: "A 15 Nm Direct Drive sim rig designed and built part by part: FFBeast, load-cell pedals, LED telemetry and bass shakers."
---

<div class="pj" markdown="0">

  <!-- HERO -->
  <section class="pj-hero pj-reveal">
    <button class="pj-shot pj-frame ar-16x9" data-cap="The complete Direct Drive sim rig">
      <img src="/assets/images/01_full_rig.jpg" alt="Complete Direct Drive sim rig" loading="lazy">
    </button>
    <div class="pj-hero-body">
      <span class="pj-kicker">Personal project · Mechatronics</span>
      <h1>Direct Drive Sim Rig · DIY</h1>
      <p class="pj-sub">A full motorsport simulation setup, designed and built from scratch to replicate the forces of a real car.</p>
      <div class="pj-chips">
        <span class="chip">FFBeast</span>
        <span class="chip">Force Feedback 15 Nm</span>
        <span class="chip">Arduino</span>
        <span class="chip">SimHub</span>
        <span class="chip">3D Printing</span>
        <span class="chip">Load cells</span>
        <span class="chip">Reverse engineering</span>
      </div>
    </div>
  </section>

  <!-- INTRO -->
  <section class="pj-block pj-reveal">
    <p class="pj-lead">Instead of buying a closed commercial base, I built a complete system by combining an open-source Force Feedback project, 3D printing and custom-programmed electronics. Every peripheral was designed in CAD and fine-tuned by hand.</p>
  </section>

  <!-- BLOCKS -->
  <section class="pj-block pj-reveal">
    <h2>The heart: FFBeast project</h2>
    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Motor base with 3D-printed housing and forced-air cooling">
        <img src="/assets/images/03_motor_base.jpg" alt="Sim rig motor base" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Force Feedback</p>
        <p>The Force Feedback is based on the open-source <strong>FFBeast</strong> project, able to handle high torque with great fidelity.</p>
        <ul>
          <li><strong>Motor:</strong> repurposed from an electric scooter, with peaks of <strong>15 Nm</strong>.</li>
          <li><strong>Smoothness:</strong> the software removes the motor's <em>cogging</em>, achieving a feel comparable to high-end Direct Drive bases.</li>
          <li><strong>Cooling:</strong> 3D-printed housing with forced airflow.</li>
        </ul>
      </div>
    </div>

    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Pedals with PETG bodies and a load cell">
        <img src="/assets/images/04_pedals_profile.jpg" alt="Sim rig pedals profile" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Pedals</p>
        <h3>Braking by pressure, not by travel</h3>
        <p>Pedals inspired by <em>Heusinkveld</em> engineering, with steel plates and PETG bodies at 100% infill.</p>
        <ul>
          <li><strong>Brake:</strong> measures pressure with a <strong>100 kg load cell</strong>.</li>
          <li><strong>Adjustable feel:</strong> elastomers of different hardness, from a road car to an F1.</li>
          <li><strong>Throttle:</strong> contactless magnetic Hall sensor, full durability.</li>
        </ul>
      </div>
    </div>

    <div class="pj-sol">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Wheel with LED matrix and button box, driven by SimHub">
        <img src="/assets/images/02_cockpit_layout.jpg" alt="Wheel with LED telemetry" loading="lazy">
      </button>
      <div class="pj-txt">
        <p class="why">Visual telemetry</p>
        <h3>On-wheel information with SimHub</h3>
        <ul>
          <li><strong>Central LED matrix:</strong> shows the engaged gear.</li>
          <li><strong>RPM bar:</strong> an RGB strip marks the shift point.</li>
          <li><strong>Flags &amp; spotter:</strong> side LEDs warn about track flags and blind spots.</li>
          <li><strong>Button box:</strong> button matrix + joystick for the car menus.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- RALLY & DRIFT -->
  <section class="pj-block pj-reveal">
    <h2>Control for rally and drift</h2>
    <p class="pj-lead">For more aggressive disciplines I built two dedicated peripherals in metal and 3D print.</p>
    <div class="pj-gallery" style="margin-top:24px;">
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="Sequential shifter with an internal cam mechanism">
          <img src="/assets/images/05_shifter_detail.jpg" alt="Sequential shifter detail" loading="lazy">
        </button>
        <figcaption><strong>Sequential shifter:</strong> internal cam mechanism with high-tension springs and a real metallic "clack".</figcaption>
      </figure>
      <figure class="pj-fig">
        <button class="pj-shot pj-frame ar-4x3" data-cap="Handbrake with a 20 kg load cell for drift">
          <img src="/assets/images/06_handbrake_detail.jpg" alt="Handbrake detail" loading="lazy">
        </button>
        <figcaption><strong>Handbrake:</strong> uses a <strong>20 kg load cell</strong> to modulate rear braking with precision while drifting.</figcaption>
      </figure>
    </div>
  </section>

  <!-- BASS SHAKERS -->
  <section class="pj-block pj-reveal">
    <h2>Haptic immersion: bass shakers</h2>
    <div class="pj-sol alt">
      <button class="pj-shot pj-frame ar-4x3" data-cap="Bass shaker built from recycled speakers">
        <img src="/assets/images/08_bass_shaker.jpg" alt="Bass shaker under the seat" loading="lazy">
      </button>
      <div class="pj-txt">
        <p>Force Feedback tells you what the front wheels are doing; the <strong>bass shakers</strong> convey the rest of the chassis. I built them from recycled speakers turned into vibration pistons, anchored under the seat and pedals.</p>
        <p>You feel bumps, gear changes, idle vibration and wheel lock-up: the difference between playing and driving.</p>
      </div>
    </div>
  </section>

  <!-- SPECS -->
  <section class="pj-block pj-reveal">
    <h2>Specs summary</h2>
    <table>
      <thead><tr><th>Component</th><th>Technology</th><th>Software / Driver</th></tr></thead>
      <tbody>
        <tr><td><strong>Base</strong></td><td>Modded scooter motor (15 Nm)</td><td><strong>FFBeast</strong> project</td></tr>
        <tr><td><strong>Pedals</strong></td><td>100 kg load cell</td><td>Arduino Joystick Lib</td></tr>
        <tr><td><strong>Handbrake</strong></td><td>20 kg load cell</td><td>HX711 amplifier</td></tr>
        <tr><td><strong>Dashboard</strong></td><td>LED matrix + WS2812b</td><td><strong>SimHub</strong></td></tr>
        <tr><td><strong>Structure</strong></td><td>Reinforced wood + steel</td><td>Custom CAD design</td></tr>
      </tbody>
    </table>
  </section>

  <div style="text-align:center; margin-top:50px;">
    <a href="/en/projects/" style="text-decoration:none; font-weight:bold; color:#0366d6; font-size:1.05em; border:1px solid #0366d6; padding:10px 22px; border-radius:30px;">⬅️ Back to my projects</a>
  </div>

</div>
