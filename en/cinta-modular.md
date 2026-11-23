---
layout: default
title: Parametric conveyor belt
permalink: /en/cinta-modular/
alt: /cinta-modular
image: /assets/images/tarjetas/cinta.jpg
description: "An aggregate conveyor designed in SolidWorks around a standard module driven by equations and design tables: it changes length without redesigning parts. Final project of the University of Vigo CAD course."
---

<p class="ruta"><a href="/en/projects/">Projects</a> / Parametric conveyor belt</p>

<div class="cabecera">
  <h1>Parametric conveyor belt</h1>
  <p class="entradilla">The final project of the University of Vigo's computer-aided design course: an aggregate conveyor that gets longer or shorter by changing one number, without redesigning a single part.</p>
  <div class="datos">
    <div><b>Where</b>Advanced SolidWorks course, University of Vigo</div>
    <div><b>Tools</b>SolidWorks, Toolbox, SolidWorks Visualize</div>
  </div>
</div>

<figure class="portada"><img src="/assets/images/cinta_full_render.jpg" alt="Render of the complete conveyor belt"></figure>

<div class="habilidades">
  <div class="hab"><h3>Modelling</h3><p>Parts, sheet metal and top-down assemblies.</p></div>
  <div class="hab"><h3>Parametrisation</h3><p>Global equations and design tables controlling length, rollers and fasteners.</p></div>
  <div class="hab"><h3>Presentation</h3><p>Renders in SolidWorks Visualize with realistic materials and textures.</p></div>
</div>

<div class="texto" markdown="1">

## The goal

The brief wasn't just to draw a machine, but for the model to survive changes. An aggregate conveyor is ordered at whatever length each site needs, and redrawing the chassis every time makes no sense.

## A module that repeats

Instead of a 20-metre chassis I designed a 3-metre standard module and repeated it. Total length is a variable: change it and the model works out how many modules are needed and, from that, how many rollers, supports and bolts it takes. Mates and linear patterns are driven by those equations, so nothing breaks when sections are added or removed.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/Rende_sin_cinta.jpg" pie="The chassis without the belt: the repeated modules are easy to see." %}
{% include fig.html src="/assets/images/modulo_centro.jpg" pie="The middle module, the piece that repeats to change the length." %}
</div>

<div class="texto" markdown="1">

## Drive head and tensioner

The drive head is where my own sheet-metal parts meet the off-the-shelf components. Fasteners come from Toolbox and the moving parts have guards following basic machinery safety rules. At the tail, a tensioner slides the drum shaft along rails to tension the belt.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/modulo_motor.jpg" pie="Drive head." %}
{% include fig.html src="/assets/images/modulo_tensor.jpg" pie="Tail module with the belt tensioner." %}
</div>

<div class="volver"><a href="/en/smart-hangboard/">← Previous: force sensor</a><a href="/en/projects/">All projects →</a></div>
