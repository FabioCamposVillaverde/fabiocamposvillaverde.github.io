---
layout: default
title: DIY Direct Drive Sim Rig
permalink: /en/simulador-racing/
lang: en
description: "15 Nm Direct Drive sim rig built through reverse engineering: repurposed motor, FFBeast, load-cell pedals and custom visual telemetry."
---

# 🏎️ OpenSource DIY Direct Drive Sim Rig

<img src="/assets/images/01_full_rig.jpg" width="100%">

<br>

> **"Motorsport engineering within the maker's reach."**
> A complete simulation ecosystem, designed from scratch to replicate the forces of a real car using the **FFBeast** project, advanced 3D printing and visual telemetry.

---

### ⚡ The Heart: FFBeast Project
<img src="/assets/images/03_motor_base.jpg" align="right" width="350" style="margin-left: 20px; margin-bottom: 10px;">

For the Force Feedback, I stayed away from closed commercial solutions. The system is based on the Open Source **FFBeast** project, known for its ability to handle extreme torque with incredible fidelity.

* **Motor:** Repurposed from electric mobility (a scooter), capable of peaks of **15Nm**.
* **Driver:** Modified high-power controller.
* **Feel:** Thanks to the FFBeast software, the motor's "cogging" (notchiness) is eliminated, achieving smoothness comparable to Direct Drive bases worth +1500€.
* **Cooling:** 3D-printed housing with a forced-airflow design.

<br clear="all">
<br>

### 🦶 Hydraulic Pedals (Simulated)
<img src="/assets/images/04_pedals_profile.jpg" align="left" width="350" style="margin-right: 20px; margin-bottom: 10px;">

Consistency under braking is everything. I designed pedals inspired by the engineering of *Heusinkveld*, built with steel plates and structural bodies in PETG at 100% infill.

* **Brake:** It does not work by travel, but by pressure, using a **100kg Load Cell**.
* **Customization:** The feel is fully adjustable using elastomers (rubbers) of different hardness, to simulate anything from a road car to an F1.
* **Throttle:** Contactless magnetic Hall sensor for infinite durability and total smoothness.

<br clear="all">
<br>

### 🚥 Visual Telemetry: LED Matrix
<img src="/assets/images/02_cockpit_layout.jpg" align="right" width="350" style="margin-left: 20px; margin-bottom: 10px;">

To keep my eyes on the road, I integrated a visual information system right on top of the wheel base, managed through **SimHub**.

* **Central LED Matrix:** Shows the engaged gear large and clear.
* **RPM Bar:** An RGB LED strip indicates the exact shift point.
* **Spotter & Flags:** The side LEDs blink yellow/blue/red according to track flags or if there is a car in my blind spot.
* **Button Box:** A matrix of physical buttons + joystick to navigate the car menus without using the mouse.

<br clear="all">
<br>

### 🕹️ Vehicle Control: Rally & Drift

For disciplines that demand aggression, the wheel is not enough. I built two dedicated peripherals in metal and 3D print.

<div align="center">
  <img src="/assets/images/05_shifter_detail.jpg" height="250" style="margin-right: 10px;">
  <img src="/assets/images/06_handbrake_detail.jpg" height="250" style="margin-left: 10px;">
</div>

* **Sequential Shifter (Purple):** Internal cam mechanism with high-tension springs. The metallic "clack" when shifting gives a real mechanical satisfaction.
* **Handbrake (Red):** Designed for drift. It uses a **20kg Load Cell** instead of a simple button. This lets me modulate the rear braking to place the car with millimetric precision in the corners.

<br>

### 🔊 Haptic Immersion (Bass Shakers)
<img src="/assets/images/08_bass_shaker.jpg" align="left" width="350" style="margin-right: 20px; margin-bottom: 10px;">

Force Feedback tells you what the front wheels are doing, but... what about the rest of the chassis?

I built a **Bass Shaker** system using recycled speakers modified to act as vibration pistons. They are strategically anchored under the seat and the pedals.

* **What do you feel?** Road bumps, engine gear changes, idle engine vibration and wheel lock-up. It's the difference between playing a video game and driving a car.

<br clear="all">

---

### 🚀 Specs Summary

| Component | Technology | Software/Driver |
| :--- | :--- | :--- |
| **Base** | Modded scooter motor (15Nm) | **FFBeast** project |
| **Pedals** | 100kg Load Cell | Arduino Joystick Lib |
| **Handbrake** | 20kg Load Cell | HX711 Amplifier |
| **Dashboard** | LED Matrix + WS2812b | **SimHub** |
| **Structure** | Reinforced wood + Steel | Custom CAD design |

---
[🔙 Back to Portfolio](/en/projects/)
