---
layout: default
title: Contacto
permalink: /contact/
alt: /en/contact/
description: "Cómo contactar con Fabio Campos."
---

<style>
  .contacto-rejilla { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 30px; }
  .formulario { background: var(--papel); border: 1px solid var(--linea); border-radius: 14px; padding: 26px; }
  .formulario label { display: block; font-weight: 500; font-size: .95rem; margin-bottom: 6px; }
  .formulario input, .formulario textarea { width: 100%; padding: 10px 12px; margin-bottom: 16px; border: 1px solid var(--linea); border-radius: 8px; font: inherit; background: #fbfbf9; }
  .formulario button { font: inherit; cursor: pointer; }
  @media (max-width: 760px) { .contacto-rejilla { grid-template-columns: 1fr; } }
</style>

<div class="cabecera">
  <h1>Contacto</h1>
  <p class="entradilla">Si quieres preguntarme por algún proyecto o hablar de trabajo, escríbeme.</p>
</div>

<div class="contacto-rejilla">
  <div>
    <p><b>Correo</b><br>{% include correo.html %}</p>
    <p><b>LinkedIn</b><br><a href="https://linkedin.com/in/fabio-campos-villaverde-23543b352" target="_blank" rel="noopener">Fabio Campos Villaverde</a></p>
    <p><b>Dónde</b><br>Vigo, Galicia</p>
  </div>
  <form class="formulario" action="https://formspree.io/f/xpqebqzo" method="POST">
    <label for="nombre">Nombre</label>
    <input id="nombre" type="text" name="name" required>
    <label for="correo">Correo</label>
    <input id="correo" type="email" name="email" required>
    <label for="mensaje">Mensaje</label>
    <textarea id="mensaje" name="message" rows="6" required></textarea>
    <button type="submit" class="boton lleno">Enviar</button>
  </form>
</div>
