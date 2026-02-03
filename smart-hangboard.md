---
layout: default
title: IoT Smart Climbing Trainer
---

# 🧗 Smart Climbing Sensor (IoT)

<img src="/assets/images/climbing_sensor_main.jpg" width="100%" style="border-radius: 8px;">

<br>

> **"Digitalizando la fuerza de agarre."**
> Un dispositivo de medición portátil desarrollado desde cero. Integra diseño mecánico (CNC/3D), electrónica embebida (ESP32) y desarrollo de software móvil para monitorizar el rendimiento en escalada.

---

### 📱 Fase 1: Prototipado y Desarrollo de App
<img src="/assets/images/app_dev_v2.jpg" align="right" width="35%" style="margin-left: 20px; margin-bottom: 10px; border-radius: 6px; border: 1px solid #ddd;">
<img src="/assets/images/v1_prototype.jpg" align="right" width="35%" style="margin-left: 20px; margin-bottom: 10px; border-radius: 6px; margin-top: 10px;">

El proyecto nació de la necesidad de una alternativa accesible a los sensores comerciales (como Tindeq).

* **Software Propio (V1/V2):** Se desarrolló una aplicación Android utilizando *MIT App Inventor*.
    * **Funcionalidades:** Visualización de gráficos en tiempo real, guardado de datos en CSV para post-procesado y temporizadores acústicos para entrenamientos de repeticiones.
* **Hardware Inicial:** La primera versión (V1) fue una prueba de concepto fabricada manualmente. Aunque funcional, la falta de precisión mecánica en la celda de carga casera impulsó la siguiente iteración.

<br clear="all">
<br>

### ⚙️ Fase 2: Mecanizado CNC e Integración
<img src="/assets/images/v2_internal_cnc.jpg" align="left" width="45%" style="margin-right: 20px; margin-bottom: 10px; border-radius: 6px;">

Para la versión V2, se buscó profesionalizar el hardware.

* **Diseño Mecánico:** Se diseñó una celda de carga personalizada y se mandó fabricar en **Aluminio mediante CNC**. Se diseñó una carcasa compacta impresa en 3D para alojar la batería y el amplificador HX711.
* **Lecciones Aprendidas:** Esta fase fue crítica. Los cálculos de deformación para la pieza CNC no fueron correctos, resultando en una histéresis alta y mediciones inconsistentes.
* **Solución:** Este "fallo" ingenieril permitió comprender la complejidad de diseñar transductores de fuerza desde cero, redirigiendo el proyecto hacia la integración de sensores industriales calibrados.

<br clear="all">
<br>

### 📡 Fase 3: Estandarización y Conectividad (V3)
<img src="/assets/images/climbing_sensor_main.jpg" align="right" width="45%" style="margin-left: 20px; margin-bottom: 10px; border-radius: 6px;">

La versión actual (V3) soluciona los problemas mecánicos y mejora la conectividad.

* **Hardware Robusto:** Se integró una celda de carga comercial de grado industrial (Puente de Wheatstone completo) garantizando linealidad y precisión.
* **Firmware ESP32:** Se migró a un microcontrolador ESP32 por su capacidad Bluetooth Low Energy (BLE).
* **Protocolo Open Source:** Se implementó una emulación del protocolo de comunicación de Tindeq (basado en el repositorio *crimpdeq*). Esto permite que mi hardware casero sea compatible con la aplicación oficial profesional, aprovechando lo mejor de ambos mundos: hardware económico propio y software comercial depurado.

<br clear="all">
<br>

### 🧱 Innovación: Sistema Fijo Intercambiable
<img src="/assets/images/fixed_system_3d.jpg" align="left" width="45%" style="margin-right: 20px; margin-bottom: 10px; border-radius: 6px;">

Paralelamente al sensor portátil, se desarrolló una estación de medición fija para rocódromos.

* **Diseño Modular:** A diferencia de las tablas multipresa tradicionales, este sistema cuenta con un **cabezal intercambiable**.
* **Versatilidad:** Mediante impresión 3D rápida, se pueden fabricar insertos con distintas profundidades (10mm, 20mm, romos) que se acoplan al sensor base. Esto permite testear diferentes tipos de agarre sin necesitar múltiples sensores costosos.

<br clear="all">

---

### 🚀 Ficha Técnica del Proyecto

| Dominio | Tecnologías Aplicadas |
| :--- | :--- |
| **Microcontrolador** | ESP32 (C++ / Arduino IDE) |
| **Sensores** | Celdas de Carga + Amplificador HX711 |
| **Conectividad** | Bluetooth Low Energy (BLE) |
| **Fabricación** | Impresión 3D (PETG) + Mecanizado CNC |
| **Software** | MIT App Inventor + Protocol Emulation |

---
[🔙 Volver al Portafolio](/proyectos/)
