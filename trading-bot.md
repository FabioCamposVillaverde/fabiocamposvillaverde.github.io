---
layout: default
title: Bot de trading
alt: /en/trading-bot/
image: /assets/images/tarjetas/trading-bot.jpg
description: "Bot de trading para Bitcoin en Python: operó con dinero real, no ganaba, y averiguar por qué llevó a rehacer la validación con datos de 1 minuto, pruebas placebo y criterios escritos antes de mirar."
---

<p class="ruta"><a href="/proyectos/">Proyectos</a> / Bot de trading</p>

<div class="cabecera">
  <h1>Bot de trading para Bitcoin</h1>
  <p class="entradilla">Un programa en Python que operó con dinero real durante unos meses. No gana dinero, y averiguar por qué fue lo más útil de todo el proyecto.</p>
  <div class="datos">
    <div><b>Cuándo</b>2026; en real de junio a septiembre</div>
    <div><b>Estado</b>Estrategia original apagada; otra en simulación</div>
    <div><b>Herramientas</b>Python, DuckDB, Polars, asyncio, Streamlit, systemd</div>
  </div>
</div>

{% include fig.html src="/assets/images/trading-bot/backtest-vs-replay.png" pie="La misma estrategia con las mismas entradas y comisiones. Lo único que cambia es cómo se simula el camino del precio dentro de cada hora." clase="portada" %}

<div class="habilidades">
  <div class="hab"><h3>Software</h3><p>Un servicio que corre solo, recupera su estado al reiniciar, se para si pierde demasiado y avisa por Telegram. Con tests.</p></div>
  <div class="hab"><h3>Datos</h3><p>Velas de 1 minuto desde 2018, interés abierto, liquidaciones y funding de varias fuentes, guardados en DuckDB.</p></div>
  <div class="hab"><h3>Validación</h3><p>Backtests, simulación minuto a minuto, pruebas placebo, corrección por búsqueda múltiple y criterios escritos antes de mirar.</p></div>
</div>

<div class="texto" markdown="1">

## Por qué

Seguía un curso de trading que enseñaba a marcar zonas del gráfico a las que el precio «tenía que volver». Quise automatizarlo. Si el método funcionaba, un programa lo aplicaría sin cansarse; si no, quería saberlo con datos y no con opiniones.

## Qué construí

Un bot en Python que lee el mercado del exchange (KuCoin) y datos de derivados de otras fuentes, calcula las señales y manda las órdenes. Primero corría en un servidor alquilado y ahora en [mi servidor de casa](/servidor-casero), como un servicio más. Tiene un interruptor de emergencia que lo para si las pérdidas pasan de un límite, compara su estado con el del exchange cada vez que arranca y me escribe por Telegram cuando pasa algo raro.

</div>

<div class="fila tercio">
{% include fig.html src="/assets/images/trading-bot/panel-inicial.jpg" pie="El primer panel de control, en modo simulación. Lo más vistoso del proyecto y lo que menos me enseñó." %}
<div markdown="1">

La estrategia principal era un grid: órdenes de compra escalonadas por debajo del precio y una venta un poco por encima de cada compra. En el backtest con velas de 1 hora ganaba un 20 % en dos años, con siete de siete periodos de prueba en positivo. Con esos números puse una cuenta pequeña en real.

</div>
</div>

<div class="texto" markdown="1">

## Perdía poco, pero perdía

Lo primero que encontré fueron fallos míos:

- Posiciones que se quedaban huérfanas al reiniciar el bot y que había que cerrar a mercado. Fueron casi toda la pérdida de los dos primeros meses.
- Un grid que solo sabía recolocarse hacia abajo. Si el precio se escapaba por arriba, se quedaba parado horas con el dinero bloqueado.
- Ocho días en los que las señales se emitían pero no llegaban a convertirse en órdenes, porque un control de tamaño mínimo las descartaba en silencio. El panel decía que todo iba bien.

Los arreglé todos y el bot seguía sin ganar.

## El fallo de verdad estaba en el backtest

De una vela de 1 hora solo conoces la apertura, el cierre, el máximo y el mínimo, no en qué orden pasaron. Mi backtest daba por hecho que dentro de la misma hora el precio bajaba hasta mi compra y luego subía hasta mi venta. En una vela bajista pasa al revés: primero el máximo y después el mínimo, y esa operación es imposible.

Al recorrer el mismo grid con velas de 1 minuto, el +20 % se convierte en −13 % (la gráfica de arriba). La simulación de 1 minuto no es pesimista sin más: dice que el 61 % de las operaciones se cierran dentro de su misma hora, y en las operaciones reales del bot fueron el 59 %.

Después probé 28 000 combinaciones de parámetros con esa simulación. Corrigiendo por haber buscado tanto (el Reality Check de White), ninguna tenía ventaja real (p = 0,71). Y el bot en real lo confirmó: en 44 ciclos su resultado medio fue casi idéntico al que predecía la simulación de 1 minuto.

## Lo que vino después

Volví a medir todas las estrategias del curso con la simulación de 1 minuto y sin mirar datos del futuro, que era otro error que tenía la primera revisión. Ninguna gana más de lo que paga en comisiones.

Luego organicé una semana de investigación con reglas escritas antes de empezar: hipótesis registradas de antemano, un periodo de datos reservado que no se toca, pruebas placebo contra entradas al azar y varios modelos de IA haciendo de críticos de cada propuesta. De cinco hipótesis no pasó ninguna.

Lo único que aguanta es seguir la tendencia diaria: comprar cuando el precio lleva semanas subiendo y salir cuando deja de hacerlo. No es un truco, es una prima de riesgo conocida, con años malos incluidos. El grid está apagado desde el 1 de octubre y la estrategia de tendencia corre en simulación antes de decidir si merece dinero real.

## Qué aprendí

- A simular a la misma resolución a la que se opera. Un backtest bonito hecho con datos gruesos no demuestra nada.
- A escribir el criterio de éxito antes de mirar los resultados, y a comparar siempre contra el azar.
- Que los fallos silenciosos cuestan más que una mala estrategia. Casi todo lo que perdí fue por errores de programación, no por el mercado.
- Que con una cuenta pequeña el servidor alquilado costaba más de lo que la estrategia podía ganar en el mejor caso.
- Que el código que escribo con un asistente de IA (Claude Code) hay que revisarlo con la misma desconfianza que el backtest.

</div>

<div class="volver"><a href="/servidor-casero">← Anterior: servidor casero</a><a href="/simulador-racing">Siguiente: simulador de conducción →</a></div>
