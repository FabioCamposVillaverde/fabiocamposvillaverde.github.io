# Simulador de Conducción Híbrido "Direct Drive"
**Categoría:** Mecatrónica / Prototipado | **Estado:** Funcional

![Foto Principal del Simulador](aqui-va-tu-foto-principal.jpg)
*(Prototipo final ensamblado con estructura personalizada)*

## 1. Resumen del Proyecto
Diseño y fabricación de un ecosistema de simulación de alto rendimiento. El objetivo fue democratizar la tecnología **Direct Drive** (acople directo motor-volante) reutilizando componentes industriales y de movilidad personal, logrando una fidelidad de fuerza (Force Feedback) superior a sistemas comerciales de gama media.

## 2. Subsistemas Técnicos

### A. Sistema de Dirección (Direct Drive)
En lugar de usar engranajes o correas (que introducen holguras), adapté un **motor BLDC de patinete eléctrico** para transmisión directa.
* **Ingeniería Inversa:** Se rediseñó el eje del motor para acoplar un volante de competición estándar.
* **Control:** Implementación de una controladora electrónica programada para interpretar la telemetría del simulador y traducirla en par motor (torque) en tiempo real.

### B. Pedalería y Cambio Secuencial
Diseño mecánico propio para los periféricos de entrada.
* **Freno:** Sistema con celda de carga (Load Cell) para medir presión en lugar de distancia, simulando la dureza hidráulica real de un coche de carreras.
* **Cambio:** Mecanismo secuencial impreso en 3D con accionamiento magnético para feedback táctil.

### C. Sistema Háptico (Bass Shakers)
Implementación de vibración localizada mediante el reciclaje de componentes de audio.
* **Funcionamiento:** Se extrajo la señal de telemetría (baches, pianos, RPM del motor) y se separó por canales.
* **Transductores:** Modificación de altavoces convencionales para actuar como "Bass Shakers", transmitiendo vibración física al chasis en función de la frecuencia de la suspensión virtual.

## 3. Galería de Fabricación
*(Aquí subiremos fotos del cableado, el motor desmontado y las piezas 3D)*

[🔙 Volver al Inicio](./)
