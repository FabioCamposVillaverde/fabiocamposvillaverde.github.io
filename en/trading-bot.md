---
layout: default
title: Trading bot
permalink: /en/trading-bot/
alt: /trading-bot
image: /assets/images/tarjetas/trading-bot.jpg
description: "A Bitcoin trading bot in Python: it traded real money, didn't make any, and finding out why meant rebuilding the validation with 1-minute data, placebo tests and criteria written before looking."
---

<p class="ruta"><a href="/en/projects/">Projects</a> / Trading bot</p>

<div class="cabecera">
  <h1>A Bitcoin trading bot</h1>
  <p class="entradilla">A Python program that traded real money for a few months. It doesn't make money, and finding out why was the most useful part of the whole project.</p>
  <div class="datos">
    <div><b>When</b>2026; live from June to September</div>
    <div><b>Status</b>Original strategy switched off; another one in simulation</div>
    <div><b>Tools</b>Python, DuckDB, Polars, asyncio, Streamlit, systemd</div>
  </div>
</div>

{% include fig.html src="/assets/images/trading-bot/backtest-vs-replay.png" pie="The same strategy, same entries, same fees. The only difference is how the price path inside each hour is simulated (labels in Spanish: orange is the 1-hour backtest, blue the 1-minute replay)." clase="portada" %}

<div class="habilidades">
  <div class="hab"><h3>Software</h3><p>A service that runs on its own, recovers its state after restarts, stops itself if it loses too much and reports on Telegram. With tests.</p></div>
  <div class="hab"><h3>Data</h3><p>1-minute candles since 2018, open interest, liquidations and funding from several sources, stored in DuckDB.</p></div>
  <div class="hab"><h3>Validation</h3><p>Backtests, minute-by-minute replay, placebo tests, multiple-testing correction and criteria written before looking.</p></div>
</div>

<div class="texto" markdown="1">

## Why

I was following a trading course that taught you to mark zones on the chart the price "had to come back to". I wanted to automate it. If the method worked, a program would apply it without getting tired; if it didn't, I wanted to know from data rather than opinions.

## What I built

A Python bot that reads the exchange's market (KuCoin) plus derivatives data from other sources, computes the signals and sends the orders. It first ran on a rented server and now runs on [my home server](/en/home-server/) as just another service. It has an emergency switch that stops it if losses pass a limit, reconciles its state with the exchange every time it starts, and messages me on Telegram when something odd happens.

</div>

<div class="fila tercio">
{% include fig.html src="/assets/images/trading-bot/panel-inicial.jpg" pie="The first control panel, in simulation mode. The flashiest part of the project and the one that taught me least." %}
<div markdown="1">

The main strategy was a grid: buy orders stepped below the price and a sell slightly above each buy. In the backtest on 1-hour candles it made 20 % over two years, with seven out of seven test periods positive. With those numbers I put a small account live.

</div>
</div>

<div class="texto" markdown="1">

## It lost a little, but it lost

The first things I found were my own bugs:

- Positions left orphaned when the bot restarted, which had to be closed at market. They were almost all of the loss in the first two months.
- A grid that could only re-centre downwards. If the price escaped upwards, it sat idle for hours with the money locked up.
- Eight days in which signals were emitted but never became orders, because a minimum-size check silently discarded them. The dashboard said everything was fine.

I fixed them all and the bot still didn't make money.

## The real bug was in the backtest

A 1-hour candle tells you the open, close, high and low, but not the order in which the high and low happened. My backtest assumed that within the same hour the price first dropped to my buy and then rose to my sell. In a falling candle it's the other way round: high first, then low, and that trade is impossible.

Replaying the same grid on 1-minute candles turns +20 % into −13 % (chart above). The 1-minute replay isn't just pessimistic: it says 61 % of the trades close within their own hour, and in the bot's real trades it was 59 %.

I then tried 28,000 parameter combinations with that replay. Correcting for having searched that much (White's Reality Check), none had a real edge (p = 0.71). The live bot confirmed it: over 44 cycles its average result was almost identical to what the 1-minute replay predicted.

## What came next

I re-tested every strategy from the course with the 1-minute replay and no look-ahead, another mistake the first review had. None makes more than it pays in fees.

Then I ran a research week with rules written before starting: pre-registered hypotheses, a held-out period of data that nobody touches, placebo tests against random entries, and several AI models acting as critics of each proposal. Out of five hypotheses, none passed.

The only thing that holds up is following the daily trend: buying when the price has been rising for weeks and getting out when it stops. It isn't a trick, it's a known risk premium, bad years included. The grid has been off since 1 October and the trend strategy is running in simulation before I decide whether it deserves real money.

## What I learned

- To simulate at the same resolution you trade at. A pretty backtest built on coarse data proves nothing.
- To write down the success criterion before looking at the results, and to always compare against chance.
- That silent failures cost more than a bad strategy. Almost everything I lost was due to programming errors, not the market.
- That with a small account, the rented server cost more than the strategy could make in the best case.
- That the code I write with an AI assistant (Claude Code) needs the same distrust as the backtest.

</div>

<div class="volver"><a href="/en/home-server/">← Previous: home server</a><a href="/en/simulador-racing/">Next: sim racing rig →</a></div>
