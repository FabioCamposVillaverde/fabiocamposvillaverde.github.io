---
layout: default
title: Currículum
permalink: /resume/
alt: /en/resume/
---

<style>
  .cv-header { text-align: center; margin-bottom: 40px; padding-top: 20px; }
  .btn-download {
    display: inline-block; background-color: var(--accent); color: #07120c !important;
    padding: 12px 30px; text-decoration: none; border-radius: 8px; font-weight: 700;
    transition: all .3s ease; box-shadow: 0 8px 20px rgba(61,220,151,.25);
  }
  .btn-download:hover { transform: translateY(-2px); box-shadow: 0 12px 26px rgba(61,220,151,.35); text-decoration: none; }
  .pdf-container {
    width: 100%; height: 900px; border: 1px solid var(--line); border-radius: 12px;
    box-shadow: 0 18px 44px rgba(0,0,0,.5); overflow: hidden; background-color: var(--panel);
  }
  @media (max-width: 768px) { .pdf-container { height: 520px; } }
</style>

<div class="cv-header">
  <h1 style="color: var(--text);">Mi Currículum</h1>
  <p style="color: var(--muted); max-width: 600px; margin: 0 auto 22px auto;">
    Experiencia detallada en ingeniería mecánica, diseño paramétrico y mecatrónica.
  </p>

  <a href="/assets/pdfs/curriculum-fabio-esp.pdf" download class="btn-download">
    📥 Descargar PDF Completo
  </a>
</div>

<div class="pdf-container">
  <iframe src="/assets/pdfs/curriculum-fabio-esp.pdf" width="100%" height="100%" style="border: none;">
    <div style="text-align: center; padding: 50px;">
      <p>Tu navegador no puede visualizar el PDF directamente.</p>
      <a href="/assets/pdfs/curriculum-fabio-esp.pdf" class="btn-download">Haz clic aquí para descargarlo</a>
    </div>
  </iframe>
</div>
