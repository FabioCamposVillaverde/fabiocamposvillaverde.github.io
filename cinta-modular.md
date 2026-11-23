---
layout: default
title: Cinta transportadora paramétrica
alt: /en/cinta-modular/
image: /assets/images/tarjetas/cinta.jpg
description: "Cinta transportadora de áridos diseñada en SolidWorks con un módulo tipo parametrizado por ecuaciones y tablas de diseño: cambia de longitud sin rediseñar piezas. Proyecto del título propio de CAD de la Universidad de Vigo."
---

<p class="ruta"><a href="/proyectos/">Proyectos</a> / Cinta transportadora paramétrica</p>

<div class="cabecera">
  <h1>Cinta transportadora paramétrica</h1>
  <p class="entradilla">El proyecto final del título propio de diseño asistido por ordenador de la Universidad de Vigo: una cinta para áridos que se alarga o se acorta cambiando un número, sin rediseñar ninguna pieza.</p>
  <div class="datos">
    <div><b>Dónde</b>Título propio de SolidWorks avanzado, Universidad de Vigo</div>
    <div><b>Herramientas</b>SolidWorks, Toolbox, SolidWorks Visualize</div>
  </div>
</div>

<figure class="portada"><img src="/assets/images/cinta_full_render.jpg" alt="Render de la cinta transportadora completa"></figure>

<div class="habilidades">
  <div class="hab"><h3>Modelado</h3><p>Piezas, chapa metálica y ensamblajes diseñados de arriba abajo.</p></div>
  <div class="hab"><h3>Parametrización</h3><p>Ecuaciones globales y tablas de diseño que controlan longitud, rodillos y tornillería.</p></div>
  <div class="hab"><h3>Presentación</h3><p>Renders en SolidWorks Visualize con materiales y texturas realistas.</p></div>
</div>

<div class="texto" markdown="1">

## El objetivo

El encargo no era solo dibujar una máquina, sino que el modelo aguantara cambios. Una cinta de áridos se pide con la longitud que necesita cada obra, y rehacer el chasis cada vez no tiene sentido.

## Un módulo que se repite

En vez de un chasis de 20 metros diseñé un módulo tipo de 3 metros y lo repetí. La longitud total es una variable: al cambiarla, el modelo recalcula cuántos módulos hacen falta y, con ellos, cuántos rodillos, soportes y tornillos lleva. Las relaciones de posición y los patrones lineales se apoyan en esas ecuaciones, así que nada se rompe al añadir o quitar tramos.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/Rende_sin_cinta.jpg" pie="El chasis sin la banda: los módulos repetidos se ven bien." %}
{% include fig.html src="/assets/images/modulo_centro.jpg" pie="El módulo central, la pieza que se repite para cambiar la longitud." %}
</div>

<div class="texto" markdown="1">

## Cabezal motriz y tensor

En el cabezal se juntan las piezas de chapa propias y los componentes comerciales. La tornillería sale de Toolbox y las partes móviles llevan protecciones según la normativa básica de seguridad en máquinas. En la cola, un tensor desliza el eje del tambor por unos raíles para tensar la banda.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/modulo_motor.jpg" pie="Cabezal motriz." %}
{% include fig.html src="/assets/images/modulo_tensor.jpg" pie="Módulo de cola con el tensor de la banda." %}
</div>

<div class="volver"><a href="/smart-hangboard">← Anterior: sensor de fuerza</a><a href="/proyectos/">Todos los proyectos →</a></div>
