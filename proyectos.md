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
  }

  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    border-color: transparent;
  }

  .card-image-container {
    width: 100%;
    height: 200px;
    background-color: #f4f4f4;
    overflow: hidden;
    position: relative;
  }

  .card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
  }

  .project-card:hover .card-image {
    transform: scale(1.05); /* Zoom suave en la foto al pasar el ratón */
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
    Una colección de mis trabajos más destacados en ingeniería mecánica, diseño CAD y mecatrónica. Desde el concepto inicial hasta la fabricación.
  </p>
</div>

<div class="projects-grid">

  <a href="/simulador-racing" class="project-card">
    <div class="card-image-container">
      <img src="/assets/images/simulador-volante.jpg" alt="Simulador Direct Drive" class="card-image">
    </div>
    <div class="card-content">
      <span class="project-tag">Mecatrónica</span>
      <h3 class="project-title">Simulador Direct Drive</h3>
      <p class="project-desc">Diseño y construcción de un volante de simulación Force Feedback reutilizando un motor industrial. Incluye pedales con celdas de carga.</p>
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

  </div>
