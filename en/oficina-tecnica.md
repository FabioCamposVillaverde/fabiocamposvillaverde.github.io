---
layout: default
title: My job at EINGAL
permalink: /en/design-office/
alt: /oficina-tecnica
image: /assets/images/tarjetas/trabajo-en.jpg
description: "Fabio Campos, mechanical engineer in the design office of EINGAL (Pontevedra, Spain): design in Inventor, FEA with Nastran, design for manufacturing, energy certification and AI-based automation."
---

<p class="ruta"><a href="/en/projects/">Projects</a> / Work</p>

<div class="cabecera">
  <h1>Mechanical engineer in a design office</h1>
  <p class="entradilla">Since July 2026 I've worked at EINGAL, an engineering studio in Pontevedra, Spain. I design in Inventor, run finite element analyses, prepare the drawings that go to the workshops and produce building energy certificates. The models belong to clients, so there are no screenshots here: I describe the work in words and with generic diagrams drawn for this page.</p>
  <div class="datos">
    <div><b>Where</b>EINGAL, Estudio de Ingeniería de Galicia (Pontevedra)</div>
    <div><b>Since</b>July 2026</div>
    <div><b>Tools</b>Inventor, Inventor Nastran, CYPE, CE3X, Python, Claude Code</div>
  </div>
</div>

<div class="habilidades">
  <div class="hab"><h3>Design for manufacturing</h3><p>Large parametric models, parts designed for the shop that will make them, and drawings that follow the model when it changes.</p></div>
  <div class="hab"><h3>Analysis</h3><p>Linear and non-linear FEA in Inventor Nastran, quick handling and wind calculations, and bolts checked to VDI 2230.</p></div>
  <div class="hab"><h3>Automation</h3><p>An AI assistant I set up for the office: drawings, FEA models and reports, and quotations, always reviewed by me before they go out.</p></div>
</div>

<div class="texto" markdown="1">

## A stage that travels on a truck

The biggest project I work on is a touring stage for live shows. A truck trailer unfolds into a platform, and on top of it sits a sphere several metres across: aluminium segments with a fibreglass skin covered in mirrors, a motorised door and, inside, a platform for the performer. External workshops build it; I own the full 3D model, the drawings and the assembly plan.

Almost everything comes from one question: how does it travel? The sphere's pieces are just the right size to stand upright in the truck, they ride on welded trolleys with wheels and levelling feet, and the top pieces are identical to the bottom ones so there are fewer different parts to make. The joints between pieces come apart with pins, and the joining plates follow the arc of the profile.

The truck's folding platform (walls, roofs and ends that open on hinges) is driven by a single master sketch with zero degrees of freedom. Each phase (closed for the road, half open and open) is a model state, and none of them has interferences. For closing the roof I calculated masses, centres of gravity, overturning moments and the forces in cables and pulleys, compared catalogues and sent technical requests for quotation to manufacturers. The answer was a telescopic mast with two winches.

The sphere's door moves on a four-bar linkage. I calculated the torque needed against the wind, both to move it and to hold it, and chose a worm gear motor coaxial with the arm, with a drive and torque limiting. I tried another motor position and dropped it: near the dead point, the required torque went up elevenfold.

</div>

{% include fig.html src="/assets/images/trabajo/cuadrilatero-en.png" pie="Generic sketch of a four-bar linkage, not the actual design. Depending on which link the motor drives, the torque it needs shoots up near the dead point." clase="media" %}

<div class="texto" markdown="1">

On top of that: thousands of mirrors laid out over the sphere with sealed joints and only two moulds for all the fibreglass pieces, a performer platform that folds 180° face to face on a double-axis hinge, more than 25 fabrication drawings, and an 83-task assembly plan with crews of 2 to 8 people and a Gantt chart.

## Finite element analysis

At university I had done FEA in ANSYS and SolidWorks Simulation. At work I do it in Inventor Nastran and a client receives the result. Two examples:

- **A thin-walled plastic drone wing.** I repaired the client's CAD and built a mid-surface (shell) model for Nastran with every surface connected, across three successive design versions of several hundred surfaces each. The output was a structural report with load cases, mesh, stresses and safety factors, with every screenshot on the same scale so they can be compared.
- **A large-diameter flanged joint with preloaded bolts.** One sector of the assembly using cyclic symmetry, and a non-linear analysis in four chained steps: tightening, heating (from a steady-state thermal analysis), service with pressure, and unloading, with plasticity in the flanges and contact that is allowed to separate. I compared four ways of modelling the preload on computing cost, complexity and realism. I got it to converge by tuning the criteria, increments, adaptive stepping, the connector material and the bearing area; to test it I edited the solver file, ran it from the command line and asked the software vendor's support. The bolts were checked to VDI 2230.

## A part the shop couldn't make

An aluminium part for a consumer product came back twice from the machine shop: it couldn't be made as drawn. I redesigned it without touching the seats that make the part work: no undercuts, no V-notches and no steps of a few tenths of a millimetre. The feature that mattered most was an inclined face that required 5-axis machining and multiplied the cost of each part by 3.5.

## The rest

- **Building energy certificates with CE3X:** envelope, building services, rating, improvement measures and the paperwork for the regional register. I automated part of the workflow with Python.
- **An aeroplane-shaped bench for events**, 2.5 m long, for two or three people. Over six versions it went from a steel frame to CNC-cut board with ribs and half-lap joints, and I checked it with FEA because people sit on it.
- **Product development:** a telescopic exercise bar with folding arms, analysed in CYPE, and a phased proposal for a folding product for camper vans.
- **Illuminated stage pieces:** the make-or-buy study, and the design of the LED lighting and the acrylic diffuser.
- **An archaeological figure rebuilt in 3D** for printing, using generative image AI, image-to-3D AI and clean-up in Blender, with no licence costs.
- **Engineering quotations** split into phases, with hours estimated from past jobs.

## Automating the design office

Part of a design office's work is repetitive: the twentieth drawing in the company format, a mid-surface model, or a report with dozens of screenshots. For that I set up an AI assistant with Claude Code that works at my desk on Inventor, Nastran and Office, with confidentiality rules, a memory for each project and procedures built on custom scripts.

</div>

{% include fig.html src="/assets/images/trabajo/flujo-ia-en.svg" pie="How it works. I decide what gets automated and to what standard, and nothing leaves the office without my review." clase="ancha" %}

<div class="texto" markdown="1">

It produces drawings with views, scale, parts list, balloons, dimensions and title block, and audits the dimensions before saving. It prepares mid-surface models and checks there are no free edges, and builds FEA reports in Word and PDF by reading the solver's results, with screenshots on a consistent scale and tables of displacements and safety factors. Inventor is driven through its COM API; Nastran has no API, so the analysis is set up through the interface and the solver is run from the command line. I also wrote a ten-chapter internal FEA guide for newcomers.

## What I learned

- To design with the maker and the transport in mind: as few different parts as possible, a drawing for every part that isn't off the shelf, and a design that suits how the shop works.
- An order for FEA: model, contacts, mesh, constraints and masses; a gravity check and a modal analysis; and only then the loads. And to tell a singularity from a real stress before showing anything to a client.
- To do the quick calculation before choosing an off-the-shelf component, and to send requests for quotation with the technical requirements in writing.
- Method: cumulative meeting minutes, a to-do list, versioned models and an interference check after every change.

</div>

<div class="volver"><a href="/en/projects/">← All projects</a><a href="/en/tfg-dune/">Next: my final-year project →</a></div>
