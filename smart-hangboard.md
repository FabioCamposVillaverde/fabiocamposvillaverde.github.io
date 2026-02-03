---
layout: default
title: IoT Smart Climbing Trainer
---

# 🧗 Smart Climbing Sensor (IoT)

<div align="center">
  <img src="/assets/images/climbing_sensor_main.jpg" width="100%" style="border-radius: 8px; margin-bottom: 20px;">
</div>

> **"Digitalizando la fuerza de agarre."**
> Un dispositivo de medición portátil desarrollado desde cero. Integra diseño mecánico (CNC/3D), electrónica embebida (ESP32) y desarrollo de software móvil.

---

### 📱 Fase 1: Prototipado y Desarrollo de App

El proyecto nació de la necesidad de una alternativa accesible a los sensores comerciales. El reto principal fue crear un ecosistema de software propio antes de perfeccionar el hardware.

* **Software (V1/V2):** Se desarrolló una App Android (MIT App Inventor) con gráficos en tiempo real y exportación CSV.
* **Hardware Inicial:** La V1 (derecha) fue una prueba de concepto con una celda de carga genérica. Aunque funcional, sirvió para validar la comunicación Bluetooth antes de invertir en mecanizado.

<div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px; flex-wrap: wrap;">
  <div style="text-align: center; width: 45%;">
    <img src="/assets/images/app_dev_v2.jpg" style="height: 400px; object-fit: contain; border-radius: 6px; border: 1px solid #ddd;">
    <p style="font-size: 0.8rem; color: #666;">Interfaz App V2</p>
  </div>
  <div style="text-align: center; width: 45%;">
    <img src="/assets/images/v1_prototype.jpg" style="height: 400px; object-fit: cover; border-radius: 6px;">
    <p style="font-size: 0.8rem; color: #666;">Prototipo V1 (Prueba de concepto)</p>
  </div>
</div>

<br>

### ⚙️ Fase 2: El Reto del Mecanizado CNC

Para la versión V2, se buscó profesionalizar el hardware diseñando una celda de carga personalizada en **Aluminio**.

* **El Error Instructivo:** Los cálculos de deformación para la pieza CNC no fueron correctos para el tipo de aleación usada, resultando en una histéresis alta (la pieza no recuperaba su forma original perfectamente).
* **Aprendizaje:** Este fallo permitió comprender la complejidad de diseñar transductores de fuerza, redirigiendo el proyecto en la V3 hacia la integración de sensores industriales calibrados.

<div align="center" style="margin-top: 15px;">
  <img src="/assets/images/v2_internal_cnc.jpg" width="80%" style="border-radius: 6px;">
  <p style="font-size: 0.8rem; color: #666; margin-top: 5px;">Interior de la V2: Integración de amplificador HX711 en carcasa 3D</p>
</div>

<br>

### 📡 Fase 3: Estandarización (Versión Final)

La versión actual (V3) soluciona los problemas mecánicos y mejora la conectividad, logrando un producto final fiable.

* **Hardware Robusto:** Se integró una celda de carga comercial de grado industrial (Puente de Wheatstone completo).
* **Protocolo Open Source:** Se migró a **ESP32** para emular el protocolo de comunicación de sensores profesionales (Tindeq). Esto permite usar mi hardware casero con software de entrenamiento avanzado existente en el mercado.

<div align="center" style="margin-top: 15px;">
  <img src="/assets/images/climbing_sensor_main.jpg" width="80%" style="border-radius: 6px;">
</div>

<br>

### 🧱 Innovación: Sistema Fijo Intercambiable

Paralelamente, se desarrolló una estación de medición fija para rocódromos con una ventaja clave sobre las tablas comerciales: la **modularidad**.

Mediante impresión 3D rápida, se pueden fabricar insertos con distintas profundidades (10mm, 20mm, romos) que se acoplan al sensor base, permitiendo testear diferentes agarres con un solo sensor.

<div align="center" style="margin-top: 15px;">
  <img src="/assets/images/fixed_system_3d.jpg" width="60%" style="border-radius: 6px;">
</div>

<br>

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
