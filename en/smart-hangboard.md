---
layout: default
title: IoT Smart Climbing Trainer
permalink: /en/smart-hangboard/
lang: en
description: "Portable finger-strength measurement device: mechanical design (CNC/3D), embedded electronics (ESP32) and a custom mobile app with BLE."
---

<style>
  /* Flexible container for each section: text and image side by side */
  .tech-section {
    display: flex;
    flex-wrap: wrap; /* On mobile they stack */
    gap: 40px;
    align-items: center; /* Vertically centered */
    margin-bottom: 60px;
  }

  /* Text column */
  .tech-text {
    flex: 1 1 400px; /* Grows to fill space, min 400px */
  }

  /* Image column */
  .tech-visual {
    flex: 1 1 300px; /* Fills space but doesn't stretch too much */
    text-align: center;
  }

  /* Keep images contained and tidy */
  .tech-visual img {
    max-width: 100%;
    max-height: 400px; /* Limit height so they aren't huge */
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    border: 1px solid #eee;
  }

  /* Special case for the Phase 1 gallery */
  .mini-gallery {
    display: flex;
    justify-content: center;
    gap: 15px;
  }
</style>

# 🧗 Smart Climbing Sensor (IoT)

<div align="center" style="margin-bottom: 40px;">
  <img src="/assets/images/climbing_sensor_main.jpg" style="max-width: 80%; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
</div>

> **"Digitalizing grip strength."**
> A portable measurement device developed from scratch. It combines mechanical design (CNC/3D), embedded electronics (ESP32) and mobile software development.

---

<div class="tech-section">
  <div class="tech-text">
    <h3>📱 Phase 1: Prototyping & Software</h3>
    <p>The project started with the challenge of building my own ecosystem. Before perfecting the mechanics, it was vital to validate the electronics and the software.</p>
    <ul>
      <li><strong>Software (V1/V2):</strong> I developed an Android app (MIT App Inventor) able to plot force in real time and export CSV data.</li>
      <li><strong>Hardware V1:</strong> A basic proof of concept (see photo on the right) to test Bluetooth communication.</li>
    </ul>
  </div>

  <div class="tech-visual">
    <div class="mini-gallery">
      <img src="/assets/images/app_dev_v2.jpg" style="height: 300px; width: auto;" alt="App Interface">
      <img src="/assets/images/v1_prototype.jpg" style="height: 300px; width: auto; object-fit: cover;" alt="Prototype V1">
    </div>
    <p style="font-size: 0.8em; color: #888; margin-top: 10px;">V2 interface and initial prototype</p>
  </div>
</div>

<div class="tech-section" style="flex-direction: row-reverse;"> <div class="tech-text">
    <h3>⚙️ Phase 2: Reverse Engineering & CNC</h3>
    <p>For the V2 version, I tried to manufacture my own force transducer machined in aluminium.</p>
    <p><strong>The Key Lesson:</strong><br>
    The strain calculations for the CNC part did not correctly account for the material's hysteresis. This caused the readings to be inconsistent when unloading weight.</p>
    <p>This "failure" was fundamental to understand that, to achieve lab-grade precision, it is more efficient to integrate calibrated industrial sensors than to build them from scratch.</p>
  </div>

  <div class="tech-visual">
    <img src="/assets/images/v2_internal_cnc.jpg" alt="CNC V2 internals">
    <p style="font-size: 0.8em; color: #888; margin-top: 10px;">V2 internals: 3D housing + aluminium core</p>
  </div>
</div>

<div class="tech-section">
  <div class="tech-text">
    <h3>📡 Phase 3: Standardization (Final Version)</h3>
    <p>The current version (V3) is the mature product that solves the previous issues.</p>
    <ul>
      <li><strong>Robust Hardware:</strong> Integration of an industrial-grade load cell (full Wheatstone bridge).</li>
      <li><strong>Advanced Firmware:</strong> Migration to <strong>ESP32</strong>, emulating the BLE protocol of professional sensors (Tindeq).</li>
      <li><strong>Result:</strong> A homemade device with professional precision, compatible with third-party training apps.</li>
    </ul>
  </div>

  <div class="tech-visual">
    <img src="/assets/images/climbing_sensor_main.jpg" alt="Final V3 Sensor">
  </div>
</div>

<div class="tech-section" style="flex-direction: row-reverse;">
  <div class="tech-text">
    <h3>🧱 Innovation: Fixed Modular System</h3>
    <p>In parallel, I developed a fixed station for climbing gyms with a competitive edge: <strong>Interchangeable Inserts</strong>.</p>
    <p>Instead of buying multiple sensors for different edge depths, I designed a 3D-printed quick-coupling system. This makes it possible to swap between 10mm, 20mm or rounded edges in seconds, using a single sensor core.</p>
  </div>

  <div class="tech-visual">
    <img src="/assets/images/fixed_system_3d.jpg" alt="Fixed 3D System">
  </div>
</div>

---

### 🚀 Tech Sheet

| Domain | Applied Technologies |
| :--- | :--- |
| **Microcontroller** | ESP32 (C++ / Arduino IDE) |
| **Sensors** | Load Cells + HX711 Amplifier |
| **Connectivity** | Bluetooth Low Energy (BLE) |
| **Manufacturing** | 3D Printing (PETG) + CNC Machining |
| **Software** | MIT App Inventor + Protocol Emulation |

---
[🔙 Back to Portfolio](/en/projects/)
