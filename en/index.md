---
layout: default
title: Home
permalink: /en/
order: 1
lang: en
description: "Mechanical engineering portfolio of Fabio Campos: parametric design in SolidWorks, mechatronics and manufacturing. From CAD to functional prototype."
---

<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 50px; margin-bottom: 60px;">
  
  <div style="flex: 1; min-width: 280px;">
    <img src="/assets/images/mifoto.jpg" alt="Fabio Campos" style="border-radius: 12px; width: 100%; max-width: 350px; box-shadow: 0 15px 30px rgba(0,0,0,0.15); object-fit: cover;">
  </div>

  <div style="flex: 2; min-width: 300px;">
    <span style="background-color: #e1f5fe; color: #0277bd; padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">Mechanical Engineering</span>
    <h1 style="margin-top: 15px; margin-bottom: 10px; font-size: 2.8rem; line-height: 1.1;">Hi, I'm<br>Fabio Campos.</h1>
    <h3 style="color: #555; font-weight: normal; margin-top: 0; font-size: 1.3rem;">Mechanical Engineering · University of Vigo · Graduating 2026</h3>
    
    <p style="font-size: 1.15em; line-height: 1.6; color: #444; margin-top: 20px;">
      Specialization in <strong>Design &amp; Manufacturing</strong>. I like taking a project end to end: from the CAD model to a working prototype. 
      I blend classic mechanics with electronics and IoT — and whatever I don't master yet, I learn by building it.
    </p>
    <p style="font-size: 1em; color: #0366d6; font-weight: 500; background: #f0f7ff; padding: 10px; border-left: 4px solid #0366d6; border-radius: 4px;">
      🎓 Currently developing my Bachelor Thesis: the thermo-structural design of an optical module for the international DUNE neutrino experiment.
    </p>
    
    <br>
    
    <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 10px;">
      <a href="/en/projects/" style="background-color: #24292e; color: white; padding: 12px 28px; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 1.05rem; transition: background 0.3s;">View Projects</a>
      <a href="/en/resume/" style="background-color: white; color: #24292e; border: 2px solid #24292e; padding: 10px 23px; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 1.05rem; transition: all 0.3s;">📄 View Resume</a>
    </div>
  </div>

</div>

<hr style="border: 0; border-top: 1px solid #eaeaea; margin: 60px 0;">

<div style="text-align: center; margin-bottom: 40px;">
  <h2 style="margin-bottom: 10px; font-size: 2rem;">Technical Skills</h2>
  <p style="color: #666; font-size: 1.1em;">A hybrid profile bridging traditional mechanics and digital technology — with plenty of workshop and coding hours behind it.</p>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; text-align: left;">
  
  <div style="flex: 1; min-width: 280px; padding: 30px; background: #fff; border: 1px solid #eee; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: transform 0.2s;">
    <h4 style="color: #0366d6; margin-top: 0; font-size: 1.3rem;">📐 Engineering & CAD</h4>
    <p style="font-size: 1em; color: #555; line-height: 1.6;">
      Parametric and sheet-metal design in <strong>SolidWorks</strong> and Fusion 360. Experience with FEA simulation (ANSYS / SW Simulation) and structural calculation applied to my own projects.
    </p>
  </div>

  <div style="flex: 1; min-width: 280px; padding: 30px; background: #fff; border: 1px solid #eee; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: transform 0.2s;">
    <h4 style="color: #d63384; margin-top: 0; font-size: 1.3rem;">⚡ Electronics & IoT</h4>
    <p style="font-size: 1em; color: #555; line-height: 1.6;">
      I integrate microcontrollers (<strong>ESP32/Arduino</strong>) with industrial sensors (load cells, encoders) and program in C++ and Python. Electronics I taught myself to bring my designs to life.
    </p>
  </div>

  <div style="flex: 1; min-width: 280px; padding: 30px; background: #fff; border: 1px solid #eee; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: transform 0.2s;">
    <h4 style="color: #2ea44f; margin-top: 0; font-size: 1.3rem;">🏭 Real-World Manufacturing</h4>
    <p style="font-size: 1em; color: #555; line-height: 1.6;">
      From the computer to the workshop. Functional part design for <strong>3D printing</strong>, basic CNC machining and on-site structural assembly. I love it when an idea ends up as a real part.
    </p>
  </div>

</div>

<br><br>

<style>
  .home-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 26px; margin-top: 30px; }
  .home-card { background:#fff; border:1px solid #eaeaea; border-radius:12px; overflow:hidden; text-decoration:none; color:inherit; display:flex; flex-direction:column; transition: transform .25s, box-shadow .25s; }
  .home-card:hover { transform: translateY(-6px); box-shadow: 0 18px 36px rgba(0,0,0,.1); }
  .home-card .thumb { height: 190px; overflow:hidden; background:#f4f4f4; }
  .home-card .thumb img { width:100%; height:100%; object-fit:cover; transition: transform .5s; }
  .home-card:hover .thumb img { transform: scale(1.05); }
  .home-card .body { padding: 22px; flex-grow:1; display:flex; flex-direction:column; }
  .home-card .tag { font-size:.72rem; text-transform:uppercase; letter-spacing:1px; color:#888; font-weight:700; margin-bottom:8px; }
  .home-card h4 { margin:0 0 8px; font-size:1.1rem; color:#222; }
  .home-card p { margin:0; font-size:.92rem; color:#666; line-height:1.6; }
  .home-cta-band { background:#f6f8fa; border:1px solid #e9edf1; border-radius:14px; padding:42px 28px; text-align:center; margin: 10px 0 50px; }
</style>

<div style="text-align:center; margin-bottom:6px;">
  <h2 style="font-size:2rem; margin-bottom:8px;">Featured projects</h2>
  <p style="color:#666;">A glimpse of what I've been working on. <a href="/en/projects/" style="font-weight:600;">View all ➔</a></p>
</div>

<div class="home-cards">

  <a href="/en/tfg-dune" class="home-card">
    <div class="thumb"><img src="/assets/images/tfg/hero_render.png" alt="BSc Thesis · sensor supports for the DUNE ND-GAr experiment" loading="lazy"></div>
    <div class="body">
      <span class="tag">BSc Thesis · Thermo-structural design</span>
      <h4>Sensor supports · DUNE</h4>
      <p>Cryogenic optical module for an international neutrino experiment. SolidWorks and FEM validation.</p>
    </div>
  </a>

  <a href="/trading-bot#en" class="home-card">
    <div class="thumb"><img src="/assets/images/trading-bot/02_market_data.png" alt="Algorithmic Bitcoin trading bot" loading="lazy" onerror="this.onerror=null;this.src='data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22600%22%20height=%22400%22%3E%3Crect%20width=%22600%22%20height=%22400%22%20fill=%22%23121821%22/%3E%3Ctext%20x=%22300%22%20y=%22205%22%20fill=%22%233ddc97%22%20font-family=%22Segoe%20UI,Arial%22%20font-size=%2226%22%20text-anchor=%22middle%22%3ETrading%20Bot%3C/text%3E%3C/svg%3E'"></div>
    <div class="body">
      <span class="tag">Python · Data · DevOps</span>
      <h4>Algorithmic Trading Bot</h4>
      <p>Autonomous Python system trading Bitcoin 24/7, with a live dashboard and risk management.</p>
    </div>
  </a>

  <a href="/en/simulador-racing" class="home-card">
    <div class="thumb"><img src="/assets/images/01_full_rig.jpg" alt="15 Nm Direct Drive sim rig" loading="lazy"></div>
    <div class="body">
      <span class="tag">Mechatronics</span>
      <h4>Direct Drive Sim Rig 15 Nm</h4>
      <p>A Force Feedback wheel built through reverse engineering, with load-cell pedals and custom telemetry.</p>
    </div>
  </a>

</div>

<hr style="border:0; border-top:1px solid #eaeaea; margin:60px 0;">

<div id="about" style="max-width:760px;">
  <h2 style="font-size:1.8rem; margin-bottom:14px;">About me</h2>
  <p style="font-size:1.08em; color:#444; line-height:1.75;">
    I'm an engineer who likes to get his hands dirty. I taught myself electronics, programming and 3D printing through prototypes that failed until they worked. I come from climbing and maker culture, and that's where I get the persistence to solve a problem all the way through. I don't know everything, but give me time and work and I'll learn whatever it takes to ship a project.
  </p>
</div>

<div class="home-cta-band">
  <h2 style="font-size:1.6rem; margin:0 0 10px;">Got a project or an opportunity in mind?</h2>
  <p style="color:#666; margin:0 0 22px;">I'm looking for my first role as a junior mechanical engineer.</p>
  <a href="/en/contact/" style="background:#24292e; color:#fff; padding:12px 30px; border-radius:8px; font-weight:600; text-decoration:none; display:inline-block;">Let's talk ➔</a>
</div>
