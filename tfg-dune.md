---
layout: default
title: Diseño Estructural DUNE (TFG)
---

<div style="background-color: #fff8c5; border: 1px solid #d4a72c; color: #5a3e08; padding: 20px; border-radius: 8px; margin-bottom: 40px; display: flex; align-items: center; gap: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
    <span style="font-size: 30px;">🚧</span>
    <div>
        <strong style="font-size: 1.1em;">Proyecto en Desarrollo (Work in Progress)</strong>
        <p style="margin: 5px 0 0 0; font-size: 0.95em;">Este es mi actual Trabajo de Fin de Grado. El diseño se encuentra en fase de iteración y validación mediante simulación térmica.</p>
    </div>
</div>

# ⚛️ Soporte Criogénico para DUNE (TFG)

<div align="center">
  <img src="/assets/images/dune-cad-v1.jpg" width="100%" style="border-radius: 8px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
</div>

> **Colaboración Internacional**
> Diseño mecánico de un sistema de soporte para los sensores de fotones (módulos Arapuca) del experimento **DUNE** (Deep Underground Neutrino Experiment - FD3), en colaboración con la Universidad de Campinas (Brasil).

---

## 🎯 El Desafío de Ingeniería

El objetivo principal es diseñar una estructura de soporte ("un cubo dentro de otro cubo") capaz de alojar detectores de fotones y placas PCB en un entorno extremadamente hostil.

* **Entorno Criogénico:** Operación sumergida en **Argón líquido a -184°C (87 K)**.
* **Restricciones Geométricas:** Dimensiones exteriores estrictas de **90x90x180 mm** para encajar en los módulos del detector.
* **Compatibilidad de Materiales:** Uso exclusivo de materiales dieléctricos y compatibles con altos campos eléctricos (Teflón, Acrílico) y acero inoxidable para partes estructurales.
* **Precisión:** Necesidad crítica de un centrado perfecto del cubo interior respecto al marco exterior para evitar sombras en la detección.

---

## 🛠️ Proceso de Diseño

### 1. Conceptualización y Bocetos
El primer paso fue traducir los requerimientos físicos teóricos en soluciones mecánicas tangibles. Se plantearon sistemas de fijación por "clip" o deslizamiento para minimizar el uso de tornillería metálica, la cual podría interferir con las señales de los sensores.

<div align="center">
  <img src="/assets/images/dune-sketches.jpg" width="90%" style="border-radius: 8px; margin: 30px 0; border: 1px solid #eee;">
  <p style="font-size: 0.9em; color: #666; margin-top: -15px; margin-bottom: 30px;"><i>Bocetos iniciales explorando sistemas de anclaje y tolerancia térmica.</i></p>
</div>

### 2. Primera Iteración CAD (SolidWorks)
Actualmente estoy trabajando en la validación del primer modelo 3D detallado.

* **Estructura Externa:** Marco de **Acero Inoxidable (AISI 304L)** para soportar las cargas térmicas y proteger el módulo durante la instalación.
* **Componentes Internos:** Elementos en Teflón y Acrílico que cumplen una doble función: aislamiento eléctrico y soporte estructural de las láminas reflectoras.

**Retos actuales de diseño:**
Estoy optimizando la geometría para mejorar la rigidez vertical del conjunto, que actualmente depende excesivamente de la fricción. El objetivo es simplificar el ensamblaje reduciendo el número de tornillos M6 necesarios.

---

## 💻 Siguientes Pasos: Simulación (FEA)

Un diseño mecánico no es válido hasta que se prueba. Dado que no podemos replicar fácilmente -184°C en el taller, la validación será digital. La fase final del TFG consistirá en simulaciones térmicas y estáticas (usando **ANSYS** o SolidWorks Simulation) para responder a dos preguntas críticas:

1.  **Contracción Diferencial:** ¿Cómo afectará el hecho de que el acero inoxidable se contrae menos que el teflón al enfriarse? ¿Se romperá el acrílico por compresión?
2.  **Integridad Estructural:** ¿Soportará la estructura las vibraciones y g-forces durante el transporte e instalación a 1.5km de profundidad bajo tierra?

---

<br>
<div style="text-align: center; margin-top: 40px;">
    <a href="/proyectos/" style="text-decoration: none; font-weight: bold; color: #0366d6; font-size: 1.1em; border: 1px solid #0366d6; padding: 10px 20px; border-radius: 30px; transition: all 0.3s;">⬅️ Volver a mis Proyectos</a>
</div>
