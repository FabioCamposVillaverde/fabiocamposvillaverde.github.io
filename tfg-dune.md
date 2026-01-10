---
layout: default
title: Diseño Estructural DUNE (TFG)
---

<div style="background-color: #fff8c5; border: 1px solid #d4a72c; color: #5a3e08; padding: 15px; border-radius: 8px; margin-bottom: 30px; display: flex; align-items: center; gap: 15px;">
    <span style="font-size: 24px;">🚧</span>
    <div>
        <strong>Proyecto en Desarrollo (Work in Progress)</strong>
        <p style="margin: 0; font-size: 0.9em;">Este es mi actual Trabajo de Fin de Grado. El diseño está en fase de iteración y validación mediante simulación.</p>
    </div>
</div>

# ⚛️ Soporte Criogénico para DUNE (TFG)

<img src="/assets/images/dune-cad-v1.jpg" width="100%" style="border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">

> **Colaboración Internacional**
> Diseño mecánico de un sistema de soporte para los sensores de fotones (Arapuca) del experimento **DUNE** (Deep Underground Neutrino Experiment - FD3), en colaboración con la Universidad de Campinas (Brasil).

---

## 🎯 El Desafío de Ingeniería

El objetivo es diseñar una estructura ("cubo dentro de otro cubo") que aloje detectores de fotones y PCBs en un entorno extremadamente hostil.

* **Entorno:** Argón líquido a **-184°C (87 K)**.
* [cite_start]**Restricciones:** * Dimensiones exteriores estrictas: **90x90x180 mm**.
    * [cite_start]Materiales compatibles con alto campo eléctrico (Teflón, Acrílico, Acero Inoxidable)[cite: 46].
    * [cite_start]Necesidad de **centrado preciso** del cubo interior respecto al exterior[cite: 169].

---

## 🛠️ Proceso de Diseño

### 1. Conceptualización y Bocetos
El primer paso fue traducir los requerimientos de los físicos en soluciones mecánicas. Se plantearon sistemas de fijación que minimizaran el uso de tornillería metálica para no interferir con los sensores.

<img src="/assets/images/dune-sketches.jpg" width="100%" style="border-radius: 8px; margin: 20px 0;">
*Bocetos iniciales explorando sistemas de anclaje y centrado.*

### 2. Primera Iteración CAD (SolidWorks)
Actualmente estoy trabajando en la validación del primer modelo 3D.
* [cite_start]**Estructura Externa:** Marco de Acero Inoxidable (AISI 304L) para soportar las cargas térmicas[cite: 128].
* [cite_start]**Componentes Internos:** Elementos en Teflón/Acrílico para aislamiento eléctrico y soporte de las láminas reflectoras[cite: 166].

**Retos actuales:**
[cite_start]Estoy optimizando el diseño para mejorar la rigidez vertical (actualmente dependiente de la fricción) y simplificar el ensamblaje reduciendo el número de tornillos M6[cite: 115, 126].

---

## 💻 Siguientes Pasos: Simulación (FEA)

El diseño no sirve de nada si falla al enfriarse. La siguiente fase del TFG consiste en realizar simulaciones térmicas y estáticas (usando **ANSYS** o SolidWorks Simulation) para responder a:

1.  ¿Cómo afecta la **contracción térmica diferencial** (el acero encoge menos que el teflón) a la integridad del sensor?
2.  ¿Soportará la estructura las vibraciones durante el transporte e instalación a 1.5km de profundidad?

---

<br>
<a href="/proyectos/" style="text-decoration: none; font-weight: bold; color: #0366d6;">⬅️ Volver a mis Proyectos</a>
