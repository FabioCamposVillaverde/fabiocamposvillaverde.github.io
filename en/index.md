---
layout: default
title: Home
permalink: /en/
alt: /
description: "Fabio Campos, mechanical engineer in the design office of EINGAL (Pontevedra, Spain). Projects in mechanical design, analysis, fabrication, electronics and software."
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
  <img src="/assets/images/mifoto.jpg" alt="Fabio Campos climbing">
  <div>
    <h1>Hi, I'm Fabio.</h1>
    <p>I study Mechanical Engineering at the University of Vigo (Spain), specialising in Design and Manufacturing, and all I have left is my final-year project: the design of a modular cryostat for the light sensors of the DUNE neutrino experiment.</p>
    <p>I work as a mechanical engineer at <a href="/en/design-office/">EINGAL</a>, a design office in Pontevedra: I design in Inventor, run analyses in Nastran and produce building energy certificates with CE3X. Outside work I build things: a sim racing rig driven by an e-scooter motor, a home server that runs my flat, and a trading bot that taught me more by failing than by winning.</p>
    <p>For each project I explain how I built it, what went wrong and what I learned.</p>
    <div class="botones">
      <a class="boton lleno" href="/en/projects/">See projects</a>
      <a class="boton" href="/en/resume/">Resume</a>
    </div>
  </div>
</section>

<h2 class="seccion-titulo">Projects</h2>
<p class="seccion-sub">Pick one to see the details.</p>

<div class="tarjetas">
{% include tarjeta.html url="/en/design-office/" titulo="My job at EINGAL" img="/assets/images/tarjetas/trabajo-en.jpg" texto="A truck-mounted stage with a demountable sphere, FEA for clients and an AI assistant that produces drawings and reports." tipo="Inventor · Nastran · CE3X" %}
{% include tarjeta.html url="/en/tfg-dune/" titulo="Modular cryostat for DUNE" img="/assets/images/tarjetas/tfg.jpg" texto="My final-year project: the module that protects the light sensors of a neutrino detector, and the frame that holds 145 of them." tipo="Thesis · SolidWorks · 2026" %}
{% include tarjeta.html url="/en/home-server/" titulo="A server at home" img="/assets/images/tarjetas/servidor.jpg" texto="A mini PC that runs my flat's home automation, my own apps and the bot. Includes a thermal model of the flat built from its sensors." tipo="Linux · Docker · Home Assistant" %}
{% include tarjeta.html url="/en/trading-bot/" titulo="Trading bot" img="/assets/images/tarjetas/trading-bot.jpg" texto="It traded real money for a few months and doesn't make any. Finding out why was the most useful part." tipo="Python · data · validation" %}
{% include tarjeta.html url="/en/simulador-racing/" titulo="Sim racing rig" img="/assets/images/tarjetas/simulador.jpg" texto="A 15 Nm force-feedback wheel built on an e-scooter motor, load-cell pedals and a sequential shifter." tipo="Mechatronics · 3D printing" %}
{% include tarjeta.html url="/en/smart-hangboard/" titulo="Climbing force sensor" img="/assets/images/tarjetas/hangboard.jpg" texto="Three versions to measure finger strength properly. The second one, machined from aluminium, didn't work." tipo="ESP32 · Bluetooth · CNC" %}
{% include tarjeta.html url="/en/cinta-modular/" titulo="Parametric conveyor belt" img="/assets/images/tarjetas/cinta.jpg" texto="Final project of my SolidWorks course: a conveyor that changes length by changing one parameter." tipo="SolidWorks" %}
</div>

<section class="sobre" id="about">
  <div>
    <h2>About me</h2>
    <p>I like to understand things by building them. Whatever I don't know I learn along the way, usually by getting it wrong first: the force sensor I machined in aluminium didn't measure properly, my bot's backtest showed impossible profits and the thermometer outside my flat was sitting in the sun. Each of those mistakes changed how I work.</p>
    <p>I started climbing in 2020 and, from September 2024 to July 2026, volunteered as coach of the competition team at Grupo de Montaña Alud. That's where the finger-strength sensor came from.</p>
    <p>From 2018 to 2025 I spent every summer working as a construction labourer: mixing mortar, moving materials and helping the foreman.</p>
  </div>
  <div class="herramientas">
    <h3>What I work with</h3>
    <dl>
      <dt>Design</dt><dd>Autodesk Inventor, SolidWorks, Fusion 360, AutoCAD. Manufacturing drawings.</dd>
      <dt>Analysis</dt><dd>Linear and non-linear FEA in Inventor Nastran; also ANSYS, SolidWorks Simulation and CYPE. Bolted joints (VDI 2230, Rötscher) and beam models in Python.</dd>
      <dt>Energy</dt><dd>Building energy certification with CE3X.</dd>
      <dt>Fabrication</dt><dd>Design for manufacturing (CNC, welding, sheet metal, fibreglass), 3D printing, mechanical assembly.</dd>
      <dt>Electronics</dt><dd>Arduino and ESP32, load cells, Bluetooth LE.</dd>
      <dt>Software</dt><dd>Python, PowerShell, Linux, Docker, Home Assistant, Git. Claude Code to automate CAD and analysis work.</dd>
      <dt>Languages</dt><dd>Spanish and Galician (native), English (B1 certified, used daily), German (beginner).</dd>
    </dl>
  </div>
</section>

<section class="contacto">
  <h2>Contact</h2>
  <p>If you'd like to ask about a project or talk about work, email me at {% include correo.html %} or reach me on <a href="https://linkedin.com/in/fabiocamposvillaverde" target="_blank" rel="noopener">LinkedIn</a>.</p>
  <a class="boton" href="/en/contact/">Contact form</a>
</section>
