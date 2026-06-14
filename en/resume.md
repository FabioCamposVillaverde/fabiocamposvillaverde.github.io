---
layout: default
title: Resume
permalink: /en/resume/
lang: en
description: "Resume of Fabio Campos Villaverde — Mechanical Engineer specialized in design, manufacturing, SolidWorks and simulation."
---

<style>
  .cv-header {
    text-align: center;
    margin-bottom: 40px;
    padding-top: 20px;
  }

  .btn-download {
    display: inline-block;
    background-color: #24292e; /* Professional dark GitHub-style */
    color: white !important;
    padding: 12px 30px;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }

  .btn-download:hover {
    background-color: #0366d6; /* Blue on hover */
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
  }

  .pdf-container {
    width: 100%;
    height: 900px;
    border: 1px solid #e1e4e8;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    overflow: hidden;
    background-color: #f6f8fa;
  }

  /* Mobile tweak */
  @media (max-width: 768px) {
    .pdf-container {
      height: 500px;
    }
  }
</style>

<div class="cv-header">
  <h1>My Resume</h1>
  <p style="color: #666; max-width: 600px; margin: 0 auto 20px auto;">
    Detailed experience in mechanical engineering, parametric design and mechatronics.
  </p>

  <a href="/assets/pdfs/curriculum-fabio-eng.pdf" download class="btn-download">
    📥 Download Full PDF
  </a>
</div>

<div class="pdf-container">
  <iframe src="/assets/pdfs/curriculum-fabio-eng.pdf" width="100%" height="100%" style="border: none;">
    <div style="text-align: center; padding: 50px;">
      <p>Your browser cannot display the PDF directly.</p>
      <a href="/assets/pdfs/curriculum-fabio-eng.pdf" class="btn-download">Click here to download it</a>
    </div>
  </iframe>
</div>
