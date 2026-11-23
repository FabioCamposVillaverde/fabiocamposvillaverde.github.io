---
layout: default
title: Criostato modular para DUNE ND-GAr
alt: /en/tfg-dune/
image: /assets/images/tarjetas/tfg.jpg
description: "TFG de Fabio Campos: diseño mecánico de un criostato modular para los sensores de luz del detector ND-GAr del experimento DUNE. Módulo, bastidor de 145 módulos, plataforma de mantenimiento y 16 planos."
---

<p class="ruta"><a href="/proyectos/">Proyectos</a> / TFG</p>

<div class="cabecera">
  <h1>Criostato modular para los sensores de DUNE ND-GAr</h1>
  <p class="entradilla">Mi Trabajo Fin de Grado: el diseño mecánico de la caja que protege los sensores de luz de un detector de neutrinos, del bastidor que sostiene 145 de esas cajas y de la plataforma para mantenerlas.</p>
  <div class="datos">
    <div><b>Dónde</b>Escuela de Ingeniería Industrial, Universidad de Vigo</div>
    <div><b>Tutor</b>Jacobo González Baldonedo</div>
    <div><b>Estado</b>Terminando memoria y planos</div>
    <div><b>Herramientas</b>SolidWorks, Python, Excel</div>
  </div>
</div>

{% include fig.html src="/assets/images/tfg/portada.jpg" pie="El mosaico de 145 módulos sobre su bastidor y, a la derecha, un módulo." clase="portada" %}

<div class="habilidades">
  <div class="hab"><h3>Diseño mecánico</h3><p>Piezas mecanizadas y soldadas, ensamblajes grandes, uniones atornilladas y 16 planos de fabricación con el cajetín de la escuela.</p></div>
  <div class="hab"><h3>Diseño para el frío</h3><p>Materiales que encogen distinto a −47 °C, juntas que tienen que seguir sellando y piezas que deben poder deslizar sin romperse.</p></div>
  <div class="hab"><h3>Cálculo</h3><p>Uniones con los conos de presión de Rötscher, un modelo de barras propio para el bastidor y la plataforma, presupuesto y pliego.</p></div>
</div>

<div class="texto" markdown="1">

## Qué es DUNE y qué me tocaba

DUNE es un experimento internacional de neutrinos con el detector cercano en Fermilab (Estados Unidos). Una parte de ese detector, ND-GAr, es una cámara de argón rodeada de sensores de luz (SiPM). Los sensores van en módulos de 400 × 400 mm que se colocan uno al lado del otro hasta cubrir un círculo de unos 5 metros.

Mi parte era el diseño mecánico de ese módulo y de todo lo que lo sostiene. Lo elegí porque era un problema real y con requisitos que no sabía resolver al empezar: temperaturas bajo cero, materiales que se contraen de forma distinta y piezas que se tienen que poder sacar para mantenimiento sin desmontar todo lo demás.

## Requisitos

- Cada módulo mide 400 × 400 mm y tiene que encajar con sus vecinos: 145 módulos en filas de 7 a 13.
- Los sensores trabajan en argón a −25 °C y el montaje se hace a 22 °C: un salto de **−47 °C**.
- La cara frontal tiene que dejar pasar la luz y sellar.
- La electrónica de cada módulo disipa unos 45 W, que se llevan a un intercambiador por la parte de atrás.
- El mantenimiento se hace por detrás, sin tocar la cara frontal ni a los vecinos.

</div>

{% include fig.html src="/assets/images/tfg/teselado.png" pie="Así se reparte el círculo de unos 5 m en módulos de 400 mm." clase="media" %}

<div class="texto" markdown="1">

## El módulo

La carcasa es una caja de aluminio soldada con cuatro paredes de dos tipos. Al soldar se deforma, así que el orden de fabricación es soldar, aliviar tensiones y **fresar después** las caras donde apoyan las juntas, para que queden planas.

Delante va una ventana de dos láminas de PMMA con un recubrimiento de ITO entre ellas. Sella con una junta de Viton que va en un canal mecanizado en el aluminio, nunca en el PMMA, que es frágil y es la pieza óptica.

Detrás, una tapa de aluminio con una placa de G-10 pegada como aislante. La electrónica cuelga de la tapa sobre torres de PEEK, así que todo sale junto, como un cartucho de 16 kg, tirando de las asas.

</div>

<div class="galeria tres">
{% include fig.html src="/assets/images/tfg/modulo-iso.jpg" pie="El módulo: 400 × 400 × 231 mm y 32,5 kg." %}
{% include fig.html src="/assets/images/tfg/modulo-trasera.jpg" pie="La tapa trasera, con las asas, los racores de purga y el conector." %}
{% include fig.html src="/assets/images/tfg/modulo-seccion-iso.jpg" pie="Sección: ventana delante, electrónica sobre las torres de PEEK y tapa con el aislante." %}
</div>

<div class="texto" markdown="1">

## El problema del frío

El PMMA se contrae unas tres veces más que el aluminio. En 400 mm y con −47 °C, la ventana encoge 1,44 mm y la carcasa 0,44 mm: casi un milímetro de diferencia que tiene que poder deslizar sin romper la ventana y sin que la junta deje de apretar.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/tfg/contraccion-componentes.png" pie="Cuánto encoge cada pieza del módulo a −47 °C." %}
{% include fig.html src="/assets/images/tfg/contraccion-diferencial.png" pie="La diferencia entre la ventana y la carcasa, exagerada ×80 para que se vea." %}
</div>

<div class="texto" markdown="1">

La solución fue dejar que la ventana se mueva donde tiene que moverse. Los 48 tornillos que la sujetan pasan por agujeros más grandes que el tornillo, calculados según la distancia de cada uno al centro de contracción. Debajo de cada cabeza hay arandelas Belleville, que son muelles de disco: cuando todo encoge, siguen apretando la junta con una fuerza casi constante. La unión la dimensioné con los conos de presión de Rötscher.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/tfg/esquema-cinematico.png" pie="Esquema de la unión: cuánto se mueve cada tornillo y cuánta holgura necesita su agujero." %}
{% include fig.html src="/assets/images/tfg/conos-rotscher.png" pie="Conos de presión de Rötscher entre dos tornillos de la ventana." %}
</div>

<div class="texto" markdown="1">

## El bastidor

145 módulos pesan unas 4,7 toneladas. Las carcasas se atornillan entre sí y forman un panel que se sostiene solo y apoya en la parte de abajo de un marco de aluminio 6063-T6. Al enfriarse, el mosaico encoge 5,8 mm en sus 5,2 m de ancho, así que solo hay **un punto fijo**, en el módulo central de abajo. El resto se une al marco con 90 guías deslizantes que lo sujetan hacia delante y hacia atrás pero lo dejan moverse en su plano.

El análisis FEM del módulo quedó fuera del alcance del TFG: lo hará el equipo que diseña la electrónica. Para el bastidor escribí un modelo de barras en Python, con cada pared de carcasa como una barra. Con el peso propio, el módulo más cargado soporta 12,5 kN con una tensión de 6,3 MPa, y con una aceleración lateral de 0,1 g el mosaico se desplaza 2,5 mm fuera de su plano. Contrastarlo con SolidWorks Simulation queda como trabajo futuro.

</div>

<div class="galeria">
{% include fig.html src="/assets/images/tfg/bastidor.jpg" pie="El bastidor sin módulos: marco perimetral, patas y contrafuertes." %}
{% include fig.html src="/assets/images/tfg/union-deslizante.png" pie="Una de las 90 guías: deja deslizar el módulo en el plano y lo retiene fuera de él." %}
{% include fig.html src="/assets/images/tfg/carga-por-modulo.png" pie="Carga vertical que atraviesa cada módulo (kN). Todo baja hacia la cuna." %}
{% include fig.html src="/assets/images/tfg/desplazamiento.png" pie="Desplazamiento fuera del plano con 0,1 g lateral: 2,5 mm como máximo." %}
</div>

<div class="texto" markdown="1">

## La plataforma de mantenimiento

Para sacar el cartucho de un módulo de la fila de arriba hay que trabajar a más de 3 m de altura. Diseñé una plataforma de aluminio con tres niveles, a 1,2, 2,4 y 3,6 m, para que cada fila quede entre los nudillos y los hombros de quien trabaja.

La norma de accesos (EN ISO 14122-2) pide 2,1 m de altura libre, y con niveles cada 1,2 m no cabe. Por eso los tableros son abatibles: para trabajar en un nivel se levantan los del nivel de arriba. La plataforma es independiente del bastidor y no lo toca en ningún punto. La dimensiona la flecha y no la resistencia: el perfil más cargado trabaja al 11 % de su capacidad, pero la punta del tablero de arriba baja 4,2 mm de los 5,8 mm permitidos.

</div>

<div class="galeria">
{% include fig.html src="/assets/images/tfg/conjunto-plataforma.jpg" pie="Vista trasera con la plataforma montada detrás del bastidor." %}
{% include fig.html src="/assets/images/tfg/plataforma-niveles.png" pie="Niveles de trabajo y tableros abatidos, en un corte lateral." %}
{% include fig.html src="/assets/images/tfg/plataforma-calculo.png" pie="Deformada y aprovechamiento de cada grupo de perfiles (Eurocódigo 9)." %}
</div>

<div class="texto" markdown="1">

## Los planos

Hice 16 planos A3: conjunto, bastidor, plataforma y todas las piezas que no son comerciales, con tolerancias y listas de materiales. El CAD cambiaba a menudo, así que los generé con scripts de Python que manejan SolidWorks por su API (escritos con ayuda de Claude Code, una herramienta de IA) y que comprueban cada cota contra el valor esperado antes de guardar.

</div>

{% include fig.html src="/assets/images/tfg/plano-seccion-montaje.png" pie="Plano 05: sección de montaje del módulo y lista de materiales." clase="ancha" %}

<div class="texto" markdown="1">

## Qué aprendí

- Que el frío es un problema de geometría tanto como de materiales. Casi todo se resolvió decidiendo qué se puede mover y qué no: un punto fijo, guías deslizantes y agujeros con la holgura justa.
- A pensar en quien monta y mantiene. El cartucho trasero y los tableros abatibles salieron de preguntarme cómo se cambia un módulo de la fila de arriba.
- Que un plano obliga a decidir lo que en el 3D se queda en el aire. Al acotar para fabricar aparecieron incoherencias entre la memoria y el modelo, como taladros de Ø8 en un sitio y Ø9 en el otro, o roscas M4 donde iban M6.

</div>

<div class="volver"><a href="/proyectos/">← Todos los proyectos</a><a href="/servidor-casero">Siguiente: un servidor en casa →</a></div>
