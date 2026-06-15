---
layout: default
title: Proyectos
permalink: /proyectos/
---

<style>
  .projects-header {
    text-align: center;
    margin-bottom: 50px;
    padding: 20px;
  }
  
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
    padding-bottom: 50px;
  }

  /* Tarjeta del Proyecto */
  .project-card {
    background: white;
    border: 1px solid #eaeaea;
    border-radius: 8px;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
  }

  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    border-color: transparent;
  }

  .card-image-container {
    width: 100%;
    height: 220px; 
    background-color: #f4f4f4;
    overflow: hidden;
    position: relative;
    border-bottom: 1px solid #eaeaea;
  }

  .card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition: transform 0.5s;
  }

  .project-card:hover .card-image {
    transform: scale(1.05);
  }

  /* Etiqueta para proyectos en curso */
  .wip-badge {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #ffd700;
    color: #333;
    font-size: 0.75rem;
    font-weight: bold;
    padding: 4px 8px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    z-index: 10;
  }

  .card-content {
    padding: 25px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }

  .project-tag {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #888;
    font-weight: 600;
    margin-bottom: 10px;
  }

  .project-title {
    margin: 0 0 10px 0;
    font-size: 1.25rem;
    color: #222;
  }

  .project-desc {
    font-size: 0.95rem;
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
  }

  .card-link {
    margin-top: auto;
    font-weight: 600;
    color: #0366d6;
    font-size: 0.9rem;
  }
</style>

<div class="projects-header">
  <h1>Mis Proyectos</h1>
  <p style="color: #666; max-width: 600px; margin: 0 auto;">
    Proyectos que he sacado adelante de principio a fin, combinando diseño mecánico, electrónica y muchas horas de taller.
  </p>
</div>

<div class="projects-grid">

  <a href="/tfg-dune" class="project-card">
    <span class="wip-badge">🚧 EN DESARROLLO</span>
    <div class="card-image-container">
      <img src="/assets/images/dune-cad-v1.jpg" alt="Estructura DUNE TFG" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Diseño termo-estructural</span>
      <h3 class="project-title">Soportes para sensores · DUNE ND-GAr (TFG)</h3>
      <p class="project-desc">Módulo óptico criogénico (ΔT −47 °C) para el experimento internacional de neutrinos DUNE. Diseño en SolidWorks y validación FEM estructural y térmica.</p>
      <span class="card-link">Ver progreso ➔</span>
    </div>
  </a>

  <a href="/trading-bot" class="project-card">
    <div class="card-image-container">
      <img src="/assets/trading-bot/market-data.png" alt="Bot de Trading Algorítmico" class="card-image" loading="lazy" onerror="this.onerror=null;this.src='data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22600%22%20height=%22400%22%3E%3Crect%20width=%22600%22%20height=%22400%22%20fill=%22%23121821%22/%3E%3Ctext%20x=%22300%22%20y=%22205%22%20fill=%22%233ddc97%22%20font-family=%22Segoe%20UI,Arial%22%20font-size=%2226%22%20text-anchor=%22middle%22%3ETrading%20Bot%3C/text%3E%3C/svg%3E'">
    </div>
    <div class="card-content">
      <span class="project-tag">Python · Datos · DevOps</span>
      <h3 class="project-title">Bot de Trading Algorítmico</h3>
      <p class="project-desc">Sistema autónomo en Python que opera Bitcoin 24/7: pipeline de datos, despliegue en la nube, dashboard en vivo, backtesting y gestión de riesgo.</p>
      <span class="card-link">Ver detalles ➔</span>
    </div>
  </a>

  <a href="/simulador-racing" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/04_pedals_profile.jpg" alt="Simulador Direct Drive" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Mecatrónica</span>
      <h3 class="project-title">Simulador Direct Drive</h3>
      <p class="project-desc">Diseño y construcción de un volante Force Feedback de 15Nm reutilizando un motor industrial. Ingeniería inversa y fabricación aditiva.</p>
      <span class="card-link">Ver detalles ➔</span>
    </div>
  </a>

  <a href="/cinta-modular" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/cinta_full_render.jpg" alt="Cinta Modular Render" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Diseño Mecánico</span>
      <h3 class="project-title">Cinta Transportadora Modular</h3>
      <p class="project-desc">Sistema de transporte de áridos escalable. Diseño paramétrico en SolidWorks que permite adaptar la longitud sin rediseño.</p>
      <span class="card-link">Ver detalles ➔</span>
    </div>
  </a>

  <a href="/smart-hangboard" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/fixed_system_3d.jpg" alt="Entrenador Inteligente" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">IoT & Desarrollo App</span>
      <h3 class="project-title">Entrenador de Escalada IoT</h3>
      <p class="project-desc">Dispositivo conectado para medir fuerza de dedos. Sensores de carga, ESP32 y App móvil para visualización en tiempo real.</p>
      <span class="card-link">Ver detalles ➔</span>
    </div>
  </a>

</div>
