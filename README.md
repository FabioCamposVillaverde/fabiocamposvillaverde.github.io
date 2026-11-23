---
layout: default
title: Inicio
permalink: /
alt: /en/
description: "Fabio Campos, estudiante de último curso de Ingeniería Mecánica en la Universidad de Vigo. Proyectos de diseño mecánico, fabricación, electrónica y software."
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
    <p>En el trabajo uso Autodesk Inventor y hago certificados de eficiencia energética con CE3X. Fuera de él construyo cosas: un simulador de conducción con el motor de un patinete, un servidor que lleva la domótica de mi casa o un bot de trading que me enseñó más por lo que falló que por lo que ganó.</p>
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
    <p>Escalo desde hace años y entreno como voluntario a escaladores de competición en el Grupo de Montaña Alud. De ahí salió, por ejemplo, el sensor de fuerza de dedos.</p>
    <p>Antes de la carrera trabajé varios veranos en construcción y mantenimiento, montando estructuras en obra.</p>
  </div>
  <div class="herramientas">
    <h3>Con qué trabajo</h3>
    <dl>
      <dt>Diseño</dt><dd>SolidWorks, Autodesk Inventor, Fusion 360, AutoCAD. Planos de fabricación.</dd>
      <dt>Cálculo</dt><dd>Uniones atornilladas y estructuras a mano y con modelos de barras en Python. Nociones de FEA (ANSYS, SolidWorks Simulation).</dd>
      <dt>Energía</dt><dd>Certificación energética de edificios con CE3X.</dd>
      <dt>Fabricación</dt><dd>Impresión 3D, montaje mecánico, mecanizado CNC básico.</dd>
      <dt>Electrónica</dt><dd>Arduino y ESP32, células de carga, Bluetooth LE.</dd>
      <dt>Software</dt><dd>Python, Linux, Docker, Home Assistant, Git.</dd>
      <dt>Idiomas</dt><dd>Español y gallego (nativos), inglés (B1 certificado, lo uso a diario), alemán (empezando).</dd>
    </dl>
  </div>
</section>

<section class="contacto">
  <h2>Contacto</h2>
  <p>Si quieres preguntarme por algún proyecto o hablar de trabajo, escríbeme a <a href="mailto:fabio11fcv@gmail.com">fabio11fcv@gmail.com</a> o por <a href="https://linkedin.com/in/fabio-campos-villaverde-23543b352" target="_blank" rel="noopener">LinkedIn</a>.</p>
  <a class="boton" href="/contact/">Formulario de contacto</a>
</section>
