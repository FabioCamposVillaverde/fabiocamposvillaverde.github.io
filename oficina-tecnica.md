---
layout: default
title: Mi trabajo en EINGAL
alt: /en/design-office/
image: /assets/images/tarjetas/trabajo.jpg
description: "Fabio Campos, ingeniero mecánico en la oficina técnica de EINGAL (Pontevedra): diseño en Inventor, cálculo FEM con Nastran, diseño para fabricación, certificación energética y automatización con IA."
---

<p class="ruta"><a href="/proyectos/">Proyectos</a> / Trabajo</p>

<div class="cabecera">
  <h1>Ingeniero mecánico en una oficina técnica</h1>
  <p class="entradilla">Desde julio de 2026 trabajo en EINGAL, un estudio de ingeniería de Pontevedra. Diseño en Inventor, calculo por elementos finitos, preparo los planos que van a los talleres y hago certificados energéticos. Los modelos son de clientes, así que aquí no hay capturas: lo cuento con palabras y con esquemas genéricos hechos a propósito.</p>
  <div class="datos">
    <div><b>Dónde</b>EINGAL, Estudio de Ingeniería de Galicia (Pontevedra)</div>
    <div><b>Desde</b>Julio de 2026</div>
    <div><b>Herramientas</b>Inventor, Inventor Nastran, CYPE, CE3X, Python, Claude Code</div>
  </div>
</div>

<div class="habilidades">
  <div class="hab"><h3>Diseño para fabricar</h3><p>Modelos paramétricos grandes, piezas pensadas para el taller que las va a hacer y planos que siguen al modelo cuando cambia.</p></div>
  <div class="hab"><h3>Cálculo</h3><p>FEM lineal y no lineal con Inventor Nastran, cálculos rápidos de maniobra y viento, y tornillos comprobados con VDI 2230.</p></div>
  <div class="hab"><h3>Automatización</h3><p>Un asistente de IA que monté para la oficina: planos, modelos e informes FEM y ofertas, siempre revisados por mí antes de salir.</p></div>
</div>

<div class="texto" markdown="1">

## Un escenario que viaja en un camión

El proyecto más grande en el que trabajo es un escenario itinerante para espectáculos. El remolque de un camión se despliega en una plataforma y encima se monta una esfera de varios metros de diámetro: gajos de aluminio con una piel de fibra de vidrio cubierta de espejos, una puerta motorizada y, dentro, una plataforma para el artista. La fabrican talleres externos; yo llevo el modelo 3D completo, los planos y la planificación del montaje.

Casi todo sale de una pregunta: cómo se transporta. Las piezas de la esfera tienen el tamaño justo para ir de pie en el camión, viajan en carritos soldados con ruedas y nivelación, y las de arriba son iguales que las de abajo para fabricar menos referencias distintas. Las uniones entre piezas se desmontan con pasadores, y las chapas de unión siguen el arco del perfil.

La plataforma plegable del camión (paredes, techos y puntas que se abren sobre bisagras) la controla un único croquis maestro sin grados de libertad. Cada fase (cerrado para circular, semiabierto y abierto) es un estado del modelo, y en ninguna hay interferencias. Para el cierre del techo calculé masas, centros de gravedad, momentos de vuelco y las fuerzas en cables y poleas, comparé catálogos y pedí ofertas técnicas a fabricantes. La solución fue un mástil telescópico con dos cabrestantes.

La puerta de la esfera se mueve con un cuadrilátero articulado. Calculé el par necesario contra el viento, tanto para moverla como para retenerla, y elegí un motorreductor de sinfín coaxial al brazo, con variador y límite de par. Probé otra posición del motor y la descarté: cerca del punto muerto, el par necesario se multiplicaba por 11.

</div>

{% include fig.html src="/assets/images/trabajo/cuadrilatero.png" pie="Esquema genérico de un cuadrilátero articulado, no el diseño real. Según en qué barra se ponga el motor, cerca del punto muerto el par necesario se dispara." clase="media" %}

<div class="texto" markdown="1">

Además: miles de espejos repartidos sobre la esfera con juntas estancas y solo dos moldes para todas las piezas de fibra, una plataforma del artista que se pliega 180° cara contra cara con una bisagra de doble eje, más de 25 planos de fabricación y un plan de montaje de 83 tareas con cuadrillas de 2 a 8 personas y diagrama de Gantt.

## Cálculo por elementos finitos

En la carrera había hecho FEM con ANSYS y SolidWorks Simulation. En el trabajo lo hago con Inventor Nastran y el resultado lo recibe un cliente. Dos ejemplos:

- **Un ala de dron de plástico de pared fina.** Reparé el CAD del cliente y construí un modelo de superficies medias (shell) para Nastran, con todas las superficies conectadas, en tres versiones sucesivas del diseño de varios cientos de superficies cada una. De ahí salió un informe estructural con casos de carga, malla, tensiones y factores de seguridad, con todas las capturas a la misma escala para poder compararlas.
- **Una unión embridada de gran diámetro con tornillos pretensados.** Un sector del conjunto con simetría cíclica y un análisis no lineal en cuatro pasos encadenados: apriete, calentamiento (a partir de un análisis térmico estacionario), servicio con presión y descarga, con plasticidad en las bridas y un contacto que puede separarse. Comparé cuatro formas de modelar la precarga por coste de cálculo, complejidad y realismo. La convergencia la saqué ajustando criterios, incrementos, paso adaptativo, el material del conector y la zona de apoyo; para probarlo edité el archivo del solver, lo lancé por línea de comandos y consulté al soporte del fabricante del programa. Los tornillos los comprobé con VDI 2230.

## Una pieza que el taller no podía hacer

Una pieza de aluminio de un producto de consumo volvió dos veces del taller de mecanizado: así no se podía fabricar. La rediseñé sin tocar los alojamientos que hacen funcionar la pieza: fuera contrasalidas, muescas en V y escalones de décimas. El detalle que más pesaba era una cara inclinada que obligaba a mecanizar en 5 ejes y multiplicaba por 3,5 el coste de cada pieza.

## Lo demás

- **Certificados energéticos de edificios con CE3X:** envolvente, instalaciones, calificación, medidas de mejora y documentación para el registro. Parte del flujo lo automaticé con Python.
- **Un banco con forma de avión para eventos**, de 2,5 m y para dos o tres personas. En seis versiones pasó de estructura metálica a tablero cortado por CNC, con costillas y uniones a media madera, y lo comprobé con FEM porque se sienta gente encima.
- **Desarrollo de producto:** una barra de ejercicio telescópica con brazos plegables, calculada en CYPE, y la oferta por fases de un producto plegable para furgonetas camperizadas.
- **Elementos escenográficos iluminados:** el estudio de hacerlos en la empresa o subcontratarlos, y el diseño de la iluminación LED y del difusor de metacrilato.
- **Una figura arqueológica reconstruida en 3D** para imprimirla, con IA generativa de imagen y de imagen a 3D y retoque en Blender, sin pagar licencias.
- **Ofertas de ingeniería** por fases, con las horas estimadas a partir de trabajos anteriores.

## Automatizar la oficina técnica

Parte del trabajo de una oficina técnica es repetitivo: sacar el vigésimo plano con el formato de la empresa, preparar un modelo de superficies medias o montar un informe con decenas de capturas. Para eso monté un asistente de IA con Claude Code que trabaja en mi puesto sobre Inventor, Nastran y Office, con reglas de confidencialidad, memoria de cada proyecto y procedimientos con scripts hechos a medida.

</div>

{% include fig.html src="/assets/images/trabajo/flujo-ia.svg" pie="Cómo funciona. Yo decido qué se automatiza y con qué criterio, y nada sale de la oficina sin pasar por mi revisión." clase="ancha" %}

<div class="texto" markdown="1">

Saca planos con vistas, escala, lista de piezas, globos, cotas y cajetín, y audita las cotas antes de guardar. Prepara modelos de superficies medias comprobando que no queden bordes libres, y monta los informes FEM en Word y PDF leyendo los resultados del solver, con capturas a escala homogénea y tablas de desplazamientos y factores de seguridad. Inventor se maneja por su API COM; Nastran no tiene API, así que el análisis se monta por la interfaz y el solver se lanza por línea de comandos. Aparte, escribí una guía interna de cálculo FEM de diez capítulos para quien empieza.

## Qué aprendí

- A diseñar pensando en quién lo fabrica y cómo se transporta: el mínimo de piezas distintas, un plano para cada pieza que no sea comercial y el diseño adaptado a cómo trabaja el taller.
- Un orden para el FEM: modelo, contactos, malla, restricciones y masas; chequeo con gravedad y análisis modal; y solo entonces las cargas. Y a separar una singularidad de una tensión real antes de enseñarle nada a un cliente.
- A hacer la cuenta rápida antes de elegir un componente comercial, y a pedir ofertas con los requisitos técnicos por escrito.
- Método: actas de reunión acumulativas, lista de pendientes, versiones de los modelos y comprobar interferencias en cada cambio.

</div>

<div class="volver"><a href="/proyectos/">← Todos los proyectos</a><a href="/tfg-dune">Siguiente: mi TFG →</a></div>
