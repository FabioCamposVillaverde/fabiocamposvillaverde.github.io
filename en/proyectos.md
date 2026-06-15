---
layout: default
title: Projects
permalink: /en/projects/
lang: en
alt: /proyectos/
---

<style>
  .projects-header { text-align: center; margin-bottom: 50px; padding: 20px; }
  .projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; padding-bottom: 50px; }
  .project-card { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; text-decoration: none; color: inherit; transition: all .3s ease; display: flex; flex-direction: column; height: 100%; position: relative; }
  .project-card:hover { transform: translateY(-6px); box-shadow: 0 22px 44px rgba(0,0,0,.5); border-color: rgba(61,220,151,.5); }
  .card-image-container { width: 100%; height: 220px; background-color: #0e141c; overflow: hidden; position: relative; border-bottom: 1px solid var(--line); }
  .card-image { width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform .5s; }
  .project-card:hover .card-image { transform: scale(1.05); }
  .wip-badge { position: absolute; top: 10px; right: 10px; background: var(--accent); color: #07120c; font-size: .75rem; font-weight: bold; padding: 4px 10px; border-radius: 20px; box-shadow: 0 2px 8px rgba(0,0,0,.4); z-index: 10; }
  .card-content { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; }
  .project-tag { font-size: .8rem; text-transform: uppercase; letter-spacing: 1px; color: var(--accent-2); font-weight: 600; margin-bottom: 10px; }
  .project-title { margin: 0 0 10px 0; font-size: 1.25rem; color: var(--text); }
  .project-desc { font-size: .95rem; color: var(--muted); line-height: 1.6; margin-bottom: 20px; }
  .card-link { margin-top: auto; font-weight: 600; color: var(--accent); font-size: .9rem; }
</style>

<div class="projects-header">
  <h1>My Projects</h1>
  <p style="color: var(--muted); max-width: 600px; margin: 0 auto;">
    Projects I've taken from start to finish, combining mechanical design, electronics and plenty of workshop hours.
  </p>
</div>

<div class="projects-grid">

  <a href="/en/tfg-dune" class="project-card">
    <span class="wip-badge">🚧 WORK IN PROGRESS</span>
    <div class="card-image-container">
      <img src="/assets/images/tfg/hero_render.png" alt="DUNE Structure BSc Thesis" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Thermo-structural design</span>
      <h3 class="project-title">Sensor supports · DUNE ND-GAr (BSc Thesis)</h3>
      <p class="project-desc">Cryogenic optical module (ΔT −47 °C) for the international DUNE neutrino experiment. SolidWorks design with structural and thermal FEM validation.</p>
      <span class="card-link">View progress ➔</span>
    </div>
  </a>

  <a href="/en/trading-bot/" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/trading-bot/02_market_data.png" alt="Algorithmic Trading Bot" class="card-image" loading="lazy" onerror="this.onerror=null;this.src='data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22600%22%20height=%22400%22%3E%3Crect%20width=%22600%22%20height=%22400%22%20fill=%22%23121821%22/%3E%3Ctext%20x=%22300%22%20y=%22205%22%20fill=%22%233ddc97%22%20font-family=%22Segoe%20UI,Arial%22%20font-size=%2226%22%20text-anchor=%22middle%22%3ETrading%20Bot%3C/text%3E%3C/svg%3E'">
    </div>
    <div class="card-content">
      <span class="project-tag">Python · Data · DevOps</span>
      <h3 class="project-title">Algorithmic Trading Bot</h3>
      <p class="project-desc">Autonomous Python system trading Bitcoin 24/7: data pipeline, cloud deployment, live dashboard, backtesting and risk management.</p>
      <span class="card-link">View details ➔</span>
    </div>
  </a>

  <a href="/en/simulador-racing" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/04_pedals_profile.jpg" alt="Direct Drive Sim Rig" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Mechatronics</span>
      <h3 class="project-title">Direct Drive Sim Rig</h3>
      <p class="project-desc">Design and construction of a 15 Nm Force Feedback wheel by repurposing an industrial motor. Reverse engineering and additive manufacturing.</p>
      <span class="card-link">View details ➔</span>
    </div>
  </a>

  <a href="/en/cinta-modular" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/cinta_full_render.jpg" alt="Modular Conveyor Render" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Mechanical Design</span>
      <h3 class="project-title">Modular Conveyor Belt</h3>
      <p class="project-desc">Scalable aggregate transport system. Parametric design in SolidWorks allowing length adaptation without component redesign.</p>
      <span class="card-link">View details ➔</span>
    </div>
  </a>

  <a href="/en/smart-hangboard" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/fixed_system_3d.jpg" alt="Smart Climbing Trainer" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">IoT & App Development</span>
      <h3 class="project-title">IoT Smart Climbing Trainer</h3>
      <p class="project-desc">Connected device to measure finger strength. Load cells, ESP32 and a mobile app for real-time visualization.</p>
      <span class="card-link">View details ➔</span>
    </div>
  </a>

</div>
