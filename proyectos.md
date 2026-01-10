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
    position: relative; /* Para poder posicionar etiquetas si hiciera falta */
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
    Una colección de mis trabajos más destacados en ingeniería mecánica, diseño CAD y mecatrónica.
  </p>
</div>

<div class="projects-grid">

  <a href="/tfg-dune" class="project-card">
    <span class="wip-badge">🚧 EN DESARROLLO</span>
    
    <div class="card-image-container">
      <img src="/assets/images/dune-cad-v1.jpg" alt="Estructura DUNE TFG" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Investigación & Estructuras</span>
      <h3 class="project-title">Soporte Sensor DUNE (TFG)</h3>
      <p class="project-desc">Diseño de una estructura criogénica (-186°C) para soportar sensores de fotones en el experimento internacional DUNE.</p>
      <span class="card-link">Ver progreso ➔</span>
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
      <img src="/assets/images/cinta-render.jpg" alt="Cinta Modular" class="card-image">
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
      <img src="/assets/images/smart-hangboard.jpg" alt="Entrenador Inteligente" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">IoT & Desarrollo App</span>
      <h3 class="project-title">Entrenador de Escalada IoT</h3>
      <p class="project-desc">Dispositivo conectado para medir fuerza de dedos. Sensores de carga, ESP32 y App móvil para visualización en tiempo real.</p>
      <span class="card-link">Ver detalles ➔</span>
    </div>
  </a>

</div>
