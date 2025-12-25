---
layout: page
title: Proyectos
permalink: /proyectos/
order: 2
---

<style>
  /* Estilo para las Tarjetas tipo Caleb */
  .project-card {
    border: 1px solid #eee;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s;
    background: white;
    text-decoration: none;
    color: inherit;
    display: block;
  }
  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  }
  .card-image {
    width: 100%;
    height: 200px;
    background-color: #eee; /* Gris mientras no haya foto */
    object-fit: cover;
  }
  .card-content {
    padding: 20px;
  }
</style>

<div style="text-align: center; margin-bottom: 40px;">
  <h1>Portafolio de Ingeniería</h1>
  <p>Selección de trabajos académicos y personales.</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px;">

  <a href="../simulador-racing" class="project-card">
    <img src="../assets/images/simulador-volante.jpg" alt="Simulador" class="card-image">
    <div class="card-content">
      <h3 style="margin-top: 0;">🏎️ Simulador Direct Drive</h3>
      <p style="font-size: 0.9em; color: #666;">Mecatrónica / Prototipado</p>
      <p>Sistema de Force Feedback de alto par usando motores reciclados.</p>
    </div>
  </a>

  <a href="../cinta-modular" class="project-card">
    <img src="../assets/images/cinta-render.jpg" alt="Cinta Transportadora" class="card-image">
    <div class="card-content">
      <h3 style="margin-top: 0;">🏭 Cinta Modular</h3>
      <p style="font-size: 0.9em; color: #666;">Diseño Mecánico / SolidWorks</p>
      <p>Diseño paramétrico de transporte de áridos adaptable.</p>
    </div>
  </a>

  </div>
