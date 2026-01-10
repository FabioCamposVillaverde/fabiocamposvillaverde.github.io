---
layout: default
title: Smart Hangboard IoT
---

# 🧗 Entrenador de Escalada IoT

<img src="/assets/images/smart-hangboard.jpg" width="100%" style="border-radius: 8px; margin-bottom: 20px;">

> **"Entrena inteligente, no solo fuerte."**
> Dispositivo conectado para medir la fuerza de dedos en tiempo real, visualizar gráficas en el móvil y registrar el progreso del escalador.

## 📋 Sobre el Proyecto

En el entrenamiento de escalada, medir el progreso es difícil. Este dispositivo convierte una tabla multipresa (hangboard) en una herramienta de precisión. Utilizando sensores de galgas extensiométricas, el sistema envía los datos de fuerza vía Bluetooth a una aplicación móvil desarrollada a medida.

---

### 🛠️ Hardware y Electrónica

<img src="/assets/images/smart-hangboard.jpg" align="left" width="350" style="margin-right: 20px; margin-bottom: 10px;">

El núcleo del sistema es un microcontrolador **ESP32**, elegido por su conectividad Bluetooth/WiFi nativa.

* **Sensores:** Células de carga integradas en una base de madera donde se acoplan las regletas intercambiables.
* **Amplificación:** Conversor **HX711** de 24 bits para leer las variaciones milimétricas de las galgas.
* **Diseño Modular:** Las regletas (agarres) se pueden cambiar para entrenar distintos tipos de agarre (regleta, bidedo, romo) sin cambiar la electrónica.

<br clear="all">

### 📱 Software y Aplicación Móvil

La aplicación recibe los datos en tiempo real (50Hz) y permite:
1. **Gráfica en vivo:** Ver el pico de fuerza instantáneo.
2. **Cronómetro:** Rutinas de suspensión/descanso programables.
3. **Histórico:** Guardar los récords personales para ver la evolución.

---

### 💻 Ficha Técnica

| Componente | Descripción |
| :--- | :--- |
| **Microcontrolador** | ESP32 (WROOM) |
| **Sensor** | Célula de carga tipo viga (Strain Gauge) |
| **Protocolo** | Bluetooth Serial (Classic & BLE) |
| **App Frontend** | [Tecnología usada, ej: MIT App Inventor / Flutter / Android Studio] |
| **Fabricación** | Impresión 3D (Carcasa) + Madera CNC |

<br>
<a href="/proyectos/" style="text-decoration: none;">⬅️ Volver a Proyectos</a>
