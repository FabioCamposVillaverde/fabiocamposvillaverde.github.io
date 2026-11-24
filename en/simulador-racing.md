---
layout: default
title: Sim racing rig
permalink: /en/simulador-racing/
alt: /simulador-racing
image: /assets/images/tarjetas/simulador.jpg
description: "A home-built sim racing rig: 15 Nm direct-drive wheel on an e-scooter motor with FFBeast, load-cell pedals, sequential shifter, handbrake, LED button box and bass shakers."
---

<p class="ruta"><a href="/en/projects/">Projects</a> / Sim racing rig</p>

<div class="cabecera">
  <h1>Direct-drive sim racing rig</h1>
  <p class="entradilla">A driving simulator with 15 Nm of force feedback built on an electric scooter motor, pedals that measure force, a sequential shifter, a handbrake and shakers under the seat. Put together piece by piece in my garage at home.</p>
  <div class="datos">
    <div><b>Tools</b>CAD, PETG 3D printing, Arduino, FFBeast, SimHub</div>
  </div>
</div>

<figure class="portada" style="max-width: 640px;"><img src="/assets/images/simulador/rig-completo.jpg" alt="The complete rig: seat, desk with wheel, shifter, handbrake and pedals"></figure>

<div class="habilidades">
  <div class="hab"><h3>Mechanical</h3><p>Printed parts that take load, springs and elastomers, mounts and the rig structure.</p></div>
  <div class="hab"><h3>Electronics</h3><p>Load cells with HX711 amplifiers, Arduino as a USB controller and contactless Hall sensors.</p></div>
  <div class="hab"><h3>Integration</h3><p>The open-source FFBeast firmware for the motor and SimHub for the LEDs and shakers.</p></div>
</div>

<div class="texto" markdown="1">

## Why

A commercial direct-drive base, where the wheel is mounted straight onto the motor shaft, costs hundreds of euros. I read that you could build one with the hub motor of an electric scooter and the open-source FFBeast project, and I wanted to see how far I could get doing it myself.

## The wheel base

</div>

<div class="fila">
<div markdown="1">

FFBeast drives the motor and compensates for *cogging*, the small magnetic notches you feel when turning a permanent-magnet motor, so the wheel feels smooth. I designed its housing with forced ventilation and the mount to the desk. It peaks at 15 Nm.

On top sits an LED matrix showing gear and revs, and behind the wheel there are shift paddles.

</div>
{% include fig.html src="/assets/images/simulador/base-motor.jpg" pie="The base: scooter motor inside a ventilated printed housing, with the LED matrix on top." %}
</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/simulador/volante.jpg" pie="The wheel." %}
{% include fig.html src="/assets/images/simulador/levas.jpg" pie="Shift paddle behind the wheel." %}
</div>

<div class="texto" markdown="1">

## Pedals

I designed the pedals combining PETG printed parts with plates. The brake doesn't measure how far the pedal travels but how hard you press, with a 100 kg load cell, like a real car. The feel is tuned with elastomers of different hardness. The throttle uses a contactless Hall sensor so it doesn't wear.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/simulador/pedales.jpg" pie="Load-cell brake with elastomers, and throttle." %}
{% include fig.html src="/assets/images/simulador/pedales-34.jpg" pie="The pedals with their electronics box." %}
</div>

<div class="texto" markdown="1">

## Sequential shifter and handbrake

The sequential shifter uses a spring-loaded cam that gives each gear its click. The handbrake has a 20 kg load cell, so it is also modulated by force, which is what you need to drift with control.

</div>

<div class="galeria">
{% include fig.html src="/assets/images/simulador/cambio-y-freno.jpg" pie="Shifter and handbrake mounted on the side." %}
{% include fig.html src="/assets/images/simulador/cambio-secuencial.jpg" pie="Sequential shifter." %}
{% include fig.html src="/assets/images/simulador/freno-de-mano.jpg" pie="Load-cell handbrake." %}
</div>

<div class="texto" markdown="1">

## Button box, LEDs and vibration

The button box has switches and buttons for the car's menus. Through SimHub the LEDs show gear, revs and race flags.

Under the seat and the pedals there are two old speakers used as bass shakers. Force feedback tells you what the front wheels are doing; the shakers tell you the rest: bumps, the engine at idle or a locking wheel.

</div>

<div class="galeria">
{% include fig.html src="/assets/images/simulador/botonera.jpg" pie="Button box and LED matrix." %}
{% include fig.html src="/assets/images/simulador/electronica.jpg" pie="Power supply, boards and wiring." %}
{% include fig.html src="/assets/images/simulador/vista-superior.jpg" pie="The rig from above." %}
</div>

<div class="texto" markdown="1">

| Part | How it works | Electronics and software |
|---|---|---|
| Base | E-scooter hub motor, 15 Nm peak | FFBeast |
| Pedals | 100 kg load cell on the brake, Hall sensor on the throttle | Arduino as a USB controller |
| Handbrake | 20 kg load cell | Arduino Pro Micro + HX711 |
| LEDs | Matrix and RGB strip | SimHub |
| Vibration | Recycled speakers as shakers | SimHub |

## What went wrong

The Arduino side caused the most trouble. The pedals, the handbrake and the other controls run on several boards plugged into the PC over USB, and with so many at once they started failing: they couldn't capture all the information from every side.

## What I learned

- That connecting things is harder than building them. Each part worked on its own; the problems appeared when they all had to work together.

</div>

<div class="volver"><a href="/en/trading-bot/">← Previous: trading bot</a><a href="/en/smart-hangboard/">Next: force sensor →</a></div>
