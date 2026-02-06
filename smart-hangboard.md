---
layout: default
title: IoT Smart Climbing Trainer
---

<style>
  /* Contenedor flexible para cada sección: pone texto e imagen lado a lado */
  .tech-section {
    display: flex;
    flex-wrap: wrap; /* En móvil se pone uno debajo de otro */
    gap: 40px;
    align-items: center; /* Centra verticalmente */
    margin-bottom: 60px;
  }

  /* La columna del texto */
  .tech-text {
    flex: 1 1 400px; /* Crece para ocupar espacio, mínimo 400px */
  }

  /* La columna de la imagen */
  .tech-visual {
    flex: 1 1 300px; /* Ocupa espacio pero no se estira demasiado */
    text-align: center;
  }

  /* Estilo para que las imágenes se vean contenidas y bonitas */
  .tech-visual img {
    max-width: 100%;
    max-height: 400px; /* Limita la altura para que no sean gigantes */
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    border: 1px solid #eee;
  }

  /* Caso especial para la galería de Fase 1 */
  .mini-gallery {
    display: flex;
    justify-content: center;
    gap: 15px;
  }
</style>

# 🧗 Smart Climbing Sensor (IoT)

<div align="center" style="margin-bottom: 40px;">
  <img src="/assets/images/climbing_sensor_main.jpg" style="max-width: 80%; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
</div>

> **"Digitalizando la fuerza de agarre."**
> Un dispositivo de medición portátil desarrollado desde cero. Integra diseño mecánico (CNC/3D), electrónica embebida (ESP32) y desarrollo de software móvil.

---

<div class="tech-section">
  <div class="tech-text">
    <h3>📱 Fase 1: Prototipado y Software</h3>
    <p>El proyecto nació con el reto de crear un ecosistema propio. Antes de perfeccionar la mecánica, era vital validar la electrónica y el software.</p>
    <ul>
      <li><strong>Software (V1/V2):</strong> Desarrollé una App en Android (MIT App Inventor) capaz de graficar la fuerza en tiempo real y exportar datos CSV.</li>
      <li><strong>Hardware V1:</strong> Una prueba de concepto básica (ver foto derecha) para testear la comunicación Bluetooth.</li>
    </ul>
  </div>
  
  <div class="tech-visual">
    <div class="mini-gallery">
      <img src="/assets/images/app_dev_v2.jpg" style="height: 300px; width: auto;" alt="App Interface">
      <img src="/assets/images/v1_prototype.jpg" style="height: 300px; width: auto; object-fit: cover;" alt="Prototipo V1">
    </div>
    <p style="font-size: 0.8em; color: #888; margin-top: 10px;">Interfaz V2 y Prototipo inicial</p>
  </div>
</div>

<div class="tech-section" style="flex-direction: row-reverse;"> <div class="tech-text">
    <h3>⚙️ Fase 2: Ingeniería Inversa y CNC</h3>
    <p>Para la versión V2, intenté fabricar mi propio transductor de fuerza mecanizado en aluminio.</p>
    <p><strong>El Aprendizaje Clave:</strong><br>
    Los cálculos de deformación para la pieza CNC no contemplaron correctamente la histéresis del material. Esto provocó que las lecturas no fueran consistentes al descargar peso.</p>
    <p>Este "fallo" fue fundamental para entender que, para obtener precisión de laboratorio, es más eficiente integrar sensores industriales calibrados que fabricarlos desde cero.</p>
  </div>
  
  <div class="tech-visual">
    <img src="/assets/images/v2_internal_cnc.jpg" alt="Interior CNC V2">
    <p style="font-size: 0.8em; color: #888; margin-top: 10px;">Interior V2: Carcasa 3D + Núcleo Aluminio</p>
  </div>
</div>

<div class="tech-section">
  <div class="tech-text">
    <h3>📡 Fase 3: Estandarización (Versión Final)</h3>
    <p>La versión actual (V3) es el producto maduro que soluciona los problemas anteriores.</p>
    <ul>
      <li><strong>Hardware Robusto:</strong> Integración de celda de carga de grado industrial (Puente de Wheatstone completo).</li>
      <li><strong>Firmware Avanzado:</strong> Migración a <strong>ESP32</strong> emulando el protocolo BLE de sensores profesionales (Tindeq).</li>
      <li><strong>Resultado:</strong> Un dispositivo casero con precisión profesional compatible con apps de entrenamiento de terceros.</li>
    </ul>
  </div>
  
  <div class="tech-visual">
    <img src="/assets/images/climbing_sensor_main.jpg" alt="Sensor V3 Final">
  </div>
</div>

<div class="tech-section" style="flex-direction: row-reverse;">
  <div class="tech-text">
    <h3>🧱 Innovación: Sistema Modular Fijo</h3>
    <p>Paralelamente, desarrollé una estación fija para rocódromos con una ventaja competitiva: <strong>Insertos Intercambiables</strong>.</p>
    <p>En lugar de comprar múltiples sensores para distintas profundidades de regleta, diseñé un sistema de acople rápido impreso en 3D. Esto permite cambiar entre regletas de 10mm, 20mm o romos en segundos, usando un único núcleo sensor.</p>
  </div>
  
  <div class="tech-visual">
    <img src="/assets/images/fixed_system_3d.jpg" alt="Sistema Fijo 3D">
  </div>
</div>

---

### 🚀 Ficha Técnica

| Dominio | Tecnologías Aplicadas |
| :--- | :--- |
| **Microcontrolador** | ESP32 (C++ / Arduino IDE) |
| **Sensores** | Celdas de Carga + Amplificador HX711 |
| **Conectividad** | Bluetooth Low Energy (BLE) |
| **Fabricación** | Impresión 3D (PETG) + Mecanizado CNC |
| **Software** | MIT App Inventor + Protocol Emulation |

---
[🔙 Volver al Portafolio](/proyectos/)
