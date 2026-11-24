---
layout: default
title: Inicio
permalink: /
alt: /en/
description: "Fabio Campos, ingeniero mecánico en la oficina técnica de EINGAL (Pontevedra). Proyectos de diseño mecánico, cálculo, fabricación, electrónica y software."
---

<style>
  .hola { display: grid; grid-template-columns: 300px 1fr; gap: 46px; align-items: center; margin-bottom: 70px; }
  .hola img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; border-radius: 14px; border: 1px solid var(--linea); }
  .hola h1 { font-size: 2.6rem; margin: 0 0 18px; }
  .hola p { font-size: 1.1rem; color: #33322e; margin: 0 0 14px; max-width: 640px; }
  .hola .botones { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
  .seccion-titulo { text-align: center; margin: 0 0 8px; font-size: 1.6rem; }
  .seccion-sub { text-align: center; color: var(--gris); margin: 0 0 30px; }
  .sobre { display: grid; grid-template-columns: 1.2fr 1fr; gap: 46px; margin-top: 80px; }
  .sobre h2 { font-size: 1.6rem; margin: 0 0 14px; }
  .sobre p { color: #33322e; }
  .herramientas { background: var(--papel); border: 1px solid var(--linea); border-radius: 14px; padding: 22px 26px; }
  .herramientas h3 { font-size: 1rem; margin: 0 0 12px; }
  .herramientas dl { margin: 0; font-size: .93rem; }
  .herramientas dt { font-weight: 600; margin-top: 10px; }
  .herramientas dd { margin: 2px 0 0; color: var(--tinta-2); }
  .contacto { text-align: center; margin-top: 80px; padding: 40px 20px; background: var(--papel); border: 1px solid var(--linea); border-radius: 14px; }
  .contacto h2 { margin: 0 0 8px; font-size: 1.5rem; }
  .contacto p { color: var(--tinta-2); margin: 0 0 20px; }
  @media (max-width: 760px) { .hola, .sobre { grid-template-columns: 1fr; } .hola img { max-width: 280px; } .hola h1 { font-size: 2rem; } }
</style>

<section class="hola">
  <img src="/assets/images/mifoto.jpg" alt="Fabio Campos escalando">
  <div>
    <h1>Hola, soy Fabio.</h1>
    <p>Estudio Ingeniería Mecánica en la Universidad de Vigo, con la mención en Diseño y Fabricación, y solo me queda el TFG: el diseño de un criostato modular para los sensores de luz del experimento de neutrinos DUNE.</p>
    <p>Trabajo como ingeniero mecánico en <a href="/oficina-tecnica">EINGAL</a>, una oficina técnica de Pontevedra: diseño en Inventor, calculo con Nastran y hago certificados energéticos con CE3X. Fuera del trabajo construyo cosas: un simulador de conducción con el motor de un patinete, un servidor que lleva la domótica de mi casa o un bot de trading que me enseñó más por lo que falló que por lo que ganó.</p>
    <p>En cada proyecto cuento cómo lo hice, qué salió mal y qué aprendí.</p>
    <div class="botones">
      <a class="boton lleno" href="/proyectos/">Ver proyectos</a>
      <a class="boton" href="/resume/">Currículum</a>
    </div>
  </div>
</section>

<h2 class="seccion-titulo">Proyectos</h2>
<p class="seccion-sub">Elige uno para ver los detalles.</p>

<div class="tarjetas">
{% include tarjeta.html url="/oficina-tecnica" titulo="Mi trabajo en EINGAL" img="/assets/images/tarjetas/trabajo.jpg" texto="Un escenario sobre camión con una esfera desmontable, cálculo FEM para clientes y un asistente de IA que saca planos e informes." tipo="Inventor · Nastran · CE3X" %}
{% include tarjeta.html url="/tfg-dune" titulo="Criostato modular para DUNE" img="/assets/images/tarjetas/tfg.jpg" texto="Mi TFG: el módulo que protege los sensores de luz de un detector de neutrinos y el bastidor que sostiene 145 de ellos." tipo="TFG · SolidWorks · 2026" %}
{% include tarjeta.html url="/servidor-casero" titulo="Un servidor en casa" img="/assets/images/tarjetas/servidor.jpg" texto="Un mini PC que lleva la domótica del piso, mis aplicaciones y el bot. Con un modelo térmico de la casa sacado de sus sensores." tipo="Linux · Docker · Home Assistant" %}
{% include tarjeta.html url="/trading-bot" titulo="Bot de trading" img="/assets/images/tarjetas/trading-bot.jpg" texto="Operó con dinero real unos meses y no gana. Averiguar por qué fue lo más útil del proyecto." tipo="Python · datos · validación" %}
{% include tarjeta.html url="/simulador-racing" titulo="Simulador de conducción" img="/assets/images/tarjetas/simulador.jpg" texto="Volante con force feedback de 15 Nm sobre el motor de un patinete, pedales con célula de carga y cambio secuencial." tipo="Mecatrónica · impresión 3D" %}
{% include tarjeta.html url="/smart-hangboard" titulo="Sensor de fuerza para escalada" img="/assets/images/tarjetas/hangboard.jpg" texto="Tres versiones hasta medir bien la fuerza de dedos. La segunda, mecanizada en aluminio, no servía." tipo="ESP32 · Bluetooth · CNC" %}
{% include tarjeta.html url="/cinta-modular" titulo="Cinta transportadora paramétrica" img="/assets/images/tarjetas/cinta.jpg" texto="El proyecto final del título propio de SolidWorks: una cinta que cambia de longitud cambiando un parámetro." tipo="SolidWorks" %}
</div>

<section class="sobre" id="sobre-mi">
  <div>
    <h2>Sobre mí</h2>
    <p>Me gusta entender las cosas construyéndolas. Lo que no sé lo aprendo por el camino, y casi siempre equivocándome primero: el sensor de fuerza que mecanicé en aluminio no medía bien, el backtest de mi bot daba ganancias imposibles y el termómetro de casa estaba al sol. De cada error salió algo que ahora hago de otra manera.</p>
    <p>Empecé a escalar en 2020 y, de septiembre de 2024 a julio de 2026, entrené como voluntario al equipo de competición del Grupo de Montaña Alud. De ahí salió, por ejemplo, el sensor de fuerza de dedos.</p>
    <p>De 2018 a 2025 trabajé todos los veranos de peón de albañil: hacer masa, mover material y ayudar al capataz.</p>
  </div>
  <div class="herramientas">
    <h3>Con qué trabajo</h3>
    <dl>
      <dt>Diseño</dt><dd>Autodesk Inventor, SolidWorks, Fusion 360, AutoCAD. Planos de fabricación.</dd>
      <dt>Cálculo</dt><dd>FEM lineal y no lineal con Inventor Nastran; también ANSYS, SolidWorks Simulation y CYPE. Uniones atornilladas (VDI 2230, Rötscher) y modelos de barras en Python.</dd>
      <dt>Energía</dt><dd>Certificación energética de edificios con CE3X.</dd>
      <dt>Fabricación</dt><dd>Diseño para fabricación (CNC, soldadura, chapa, fibra de vidrio), impresión 3D, montaje mecánico.</dd>
      <dt>Electrónica</dt><dd>Arduino y ESP32, células de carga, Bluetooth LE.</dd>
      <dt>Software</dt><dd>Python, PowerShell, Linux, Docker, Home Assistant, Git. Claude Code para automatizar CAD y cálculo.</dd>
      <dt>Idiomas</dt><dd>Español y gallego (nativos), inglés (B1 certificado, lo uso a diario), alemán (empezando).</dd>
    </dl>
  </div>
</section>

<section class="contacto">
  <h2>Contacto</h2>
  <p>Si quieres preguntarme por algún proyecto o hablar de trabajo, escríbeme a {% include correo.html %} o por <a href="https://linkedin.com/in/fabiocamposvillaverde" target="_blank" rel="noopener">LinkedIn</a>.</p>
  <a class="boton" href="/contact/">Formulario de contacto</a>
</section>
