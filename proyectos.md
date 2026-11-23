---
layout: default
title: Proyectos
permalink: /proyectos/
alt: /en/projects/
description: "Proyectos de Fabio Campos: TFG para el experimento DUNE, servidor casero y domótica, bot de trading, simulador de conducción, sensor de fuerza para escalada y cinta transportadora paramétrica."
---

<div class="cabecera" style="margin: 0 auto 34px; text-align: center;">
  <h1>Proyectos</h1>
  <p class="entradilla">La universidad, el trabajo y lo que hago por mi cuenta. Elige uno para ver cómo lo hice.</p>
</div>

<div class="tarjetas">
{% include tarjeta.html url="/tfg-dune" titulo="Criostato modular para DUNE" img="/assets/images/tarjetas/tfg.jpg" texto="Mi TFG: el módulo que protege los sensores de luz de un detector de neutrinos y el bastidor que sostiene 145 de ellos." tipo="TFG · SolidWorks · 2026" %}
{% include tarjeta.html url="/servidor-casero" titulo="Un servidor en casa" img="/assets/images/tarjetas/servidor.jpg" texto="Un mini PC que lleva la domótica del piso, mis aplicaciones y el bot. Con un modelo térmico de la casa sacado de sus sensores." tipo="Linux · Docker · Home Assistant" %}
{% include tarjeta.html url="/trading-bot" titulo="Bot de trading" img="/assets/images/tarjetas/trading-bot.jpg" texto="Operó con dinero real unos meses y no gana. Averiguar por qué fue lo más útil del proyecto." tipo="Python · datos · validación" %}
{% include tarjeta.html url="/simulador-racing" titulo="Simulador de conducción" img="/assets/images/tarjetas/simulador.jpg" texto="Volante con force feedback de 15 Nm sobre el motor de un patinete, pedales con célula de carga y cambio secuencial." tipo="Mecatrónica · impresión 3D" %}
{% include tarjeta.html url="/smart-hangboard" titulo="Sensor de fuerza para escalada" img="/assets/images/tarjetas/hangboard.jpg" texto="Tres versiones hasta medir bien la fuerza de dedos. La segunda, mecanizada en aluminio, no servía." tipo="ESP32 · Bluetooth · CNC" %}
{% include tarjeta.html url="/cinta-modular" titulo="Cinta transportadora paramétrica" img="/assets/images/tarjetas/cinta.jpg" texto="El proyecto final del título propio de SolidWorks: una cinta que cambia de longitud cambiando un parámetro." tipo="SolidWorks" %}
</div>
