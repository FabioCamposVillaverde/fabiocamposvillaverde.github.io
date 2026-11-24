---
layout: default
title: Contact
permalink: /en/contact/
alt: /contact/
description: "How to contact Fabio Campos."
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
  <h1>Contact</h1>
  <p class="entradilla">If you'd like to ask about a project or talk about work, get in touch.</p>
</div>

<div class="contacto-rejilla">
  <div>
    <p><b>Email</b><br>{% include correo.html %}</p>
    <p><b>LinkedIn</b><br><a href="https://linkedin.com/in/fabiocamposvillaverde" target="_blank" rel="noopener">Fabio Campos Villaverde</a></p>
    <p><b>Where</b><br>Vigo, Galicia (Spain)</p>
  </div>
  <form class="formulario" action="https://formspree.io/f/xpqebqzo" method="POST">
    <label for="nombre">Name</label>
    <input id="nombre" type="text" name="name" required>
    <label for="correo">Email</label>
    <input id="correo" type="email" name="email" required>
    <label for="mensaje">Message</label>
    <textarea id="mensaje" name="message" rows="6" required></textarea>
    <button type="submit" class="boton lleno">Send</button>
  </form>
</div>
