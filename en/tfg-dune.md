---
layout: default
title: Modular cryostat for DUNE ND-GAr
permalink: /en/tfg-dune/
alt: /tfg-dune
image: /assets/images/tarjetas/tfg.jpg
description: "Final-year project by Fabio Campos: mechanical design of a modular cryostat for the light sensors of the DUNE ND-GAr detector. Module, frame for 145 modules, maintenance platform and 16 drawings."
---

<p class="ruta"><a href="/en/projects/">Projects</a> / Final-year project</p>

<div class="cabecera">
  <h1>Modular cryostat for the DUNE ND-GAr sensors</h1>
  <p class="entradilla">My final-year project: the mechanical design of the box that protects the light sensors of a neutrino detector, of the frame that holds 145 of those boxes, and of the platform used to maintain them.</p>
  <div class="datos">
    <div><b>Where</b>School of Industrial Engineering, University of Vigo</div>
    <div><b>Supervisor</b>Jacobo González Baldonedo</div>
    <div><b>Status</b>Finishing the report and drawings</div>
    <div><b>Tools</b>SolidWorks, Python, Excel</div>
  </div>
</div>

{% include fig.html src="/assets/images/tfg/portada.jpg" pie="The 145-module mosaic on its frame and, on the right, a single module." clase="portada" %}

<div class="habilidades">
  <div class="hab"><h3>Mechanical design</h3><p>Machined and welded parts, large assemblies, bolted joints and 16 manufacturing drawings using the school's title block.</p></div>
  <div class="hab"><h3>Designing for the cold</h3><p>Materials that shrink differently at −47 °C, seals that must keep sealing and parts that must slide without breaking.</p></div>
  <div class="hab"><h3>Analysis</h3><p>Bolted joints with Rötscher pressure cones, my own beam model for the frame and platform, budget and specifications.</p></div>
</div>

<div class="texto" markdown="1">

## What DUNE is and what my part was

DUNE is an international neutrino experiment with its near detector at Fermilab (USA). One part of that detector, ND-GAr, is an argon chamber surrounded by light sensors (SiPMs). The sensors sit in 400 × 400 mm modules placed side by side until they cover a circle about 5 metres across.

My part was the mechanical design of that module and of everything that holds it. I chose it because it was a real problem with requirements I didn't know how to meet when I started: sub-zero temperatures, materials that contract differently, and parts that have to come out for maintenance without dismantling everything else.

## Requirements

- Each module is 400 × 400 mm and must fit its neighbours: 145 modules in rows of 7 to 13.
- The sensors work in argon at −25 °C and assembly happens at 22 °C: a **−47 °C** swing.
- The front face has to let light through and seal.
- Each module's electronics dissipate about 45 W, carried away by a heat exchanger at the back.
- Maintenance is done from the back, without touching the front face or the neighbouring modules.

</div>

{% include fig.html src="/assets/images/tfg/teselado.png" pie="How the ~5 m circle is split into 400 mm modules." clase="media" %}

<div class="texto" markdown="1">

## The module

The housing is a welded aluminium box with four walls of two types. Welding distorts it, so the manufacturing sequence is weld, stress-relieve and **then mill** the faces where the seals sit so they end up flat.

At the front there is a window made of two PMMA sheets with an ITO coating between them. It seals with a Viton gasket sitting in a groove machined into the aluminium, never into the PMMA, which is brittle and is the optical part.

At the back, an aluminium cover with a G-10 plate bonded to it as insulation. The electronics hang from the cover on PEEK standoffs, so everything comes out together as a 16 kg cartridge, pulled out by its handles.

</div>

<div class="galeria tres">
{% include fig.html src="/assets/images/tfg/modulo-iso.jpg" pie="The module: 400 × 400 × 231 mm and 32.5 kg." %}
{% include fig.html src="/assets/images/tfg/modulo-trasera.jpg" pie="The back cover, with handles, purge fittings and connector." %}
{% include fig.html src="/assets/images/tfg/modulo-seccion-iso.jpg" pie="Section: window at the front, electronics on the PEEK standoffs and the insulated cover." %}
</div>

<div class="texto" markdown="1">

## The cold problem

PMMA contracts about three times as much as aluminium. Over 400 mm and −47 °C, the window shrinks 1.44 mm and the housing 0.44 mm: almost a millimetre of difference that has to slide without cracking the window or unloading the gasket.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/tfg/contraccion-componentes.png" pie="How much each part of the module shrinks at −47 °C (labels in Spanish)." %}
{% include fig.html src="/assets/images/tfg/contraccion-diferencial.png" pie="The difference between window and housing, exaggerated ×80 so it can be seen." %}
</div>

<div class="texto" markdown="1">

The fix was to let the window move where it needs to. The 48 screws holding it pass through holes larger than the screw, sized according to each one's distance from the centre of contraction. Under each head there are Belleville washers, which are disc springs: when everything shrinks they keep pressing the gasket with almost constant force. I sized the joint using Rötscher pressure cones.

</div>

<div class="galeria dos">
{% include fig.html src="/assets/images/tfg/esquema-cinematico.png" pie="The joint layout: how far each screw moves and how much clearance its hole needs." %}
{% include fig.html src="/assets/images/tfg/conos-rotscher.png" pie="Rötscher pressure cones between two window screws." %}
</div>

<div class="texto" markdown="1">

## The frame

145 modules weigh about 4.7 tonnes. The housings bolt to each other into a self-supporting panel that rests on the bottom of a 6063-T6 aluminium perimeter frame. When it cools, the mosaic shrinks 5.8 mm across its 5.2 m, so there is **only one fixed point**, at the bottom centre module. Everything else is tied to the frame with 90 sliding guides that hold it front-to-back but let it move in its own plane.

FEA of the module was outside the scope of the project: the team designing the electronics will do it. For the frame I wrote a beam model in Python, with each housing wall as a beam. Under self-weight, the most loaded module carries 12.5 kN at a stress of 6.3 MPa, and with a 0.1 g lateral acceleration the mosaic moves 2.5 mm out of plane. Checking it against SolidWorks Simulation is left as future work.

</div>

<div class="galeria">
{% include fig.html src="/assets/images/tfg/bastidor.jpg" pie="The frame without modules: perimeter frame, legs and braces." %}
{% include fig.html src="/assets/images/tfg/union-deslizante.png" pie="One of the 90 guides: the module slides in-plane and is held out of plane." %}
{% include fig.html src="/assets/images/tfg/carga-por-modulo.png" pie="Vertical load through each module (kN). Everything flows down to the cradle." %}
{% include fig.html src="/assets/images/tfg/desplazamiento.png" pie="Out-of-plane displacement under 0.1 g lateral: 2.5 mm at most." %}
</div>

<div class="texto" markdown="1">

## The maintenance platform

Pulling the cartridge out of a top-row module means working more than 3 m up. I designed an aluminium platform with three levels, at 1.2, 2.4 and 3.6 m, so that each row sits between the knuckles and shoulders of whoever is working.

The access standard (EN ISO 14122-2) requires 2.1 m of headroom, which doesn't fit with levels 1.2 m apart. So the decks fold up: to work on one level you lift the decks of the level above. The platform is independent of the frame and doesn't touch it anywhere. Deflection drives the design, not strength: the most loaded member works at 11 % of its capacity, but the tip of the top deck drops 4.2 mm out of the 5.8 mm allowed.

</div>

<div class="galeria">
{% include fig.html src="/assets/images/tfg/conjunto-plataforma.jpg" pie="Rear view with the platform set up behind the frame." %}
{% include fig.html src="/assets/images/tfg/plataforma-niveles.png" pie="Working levels and folded decks, in a side section." %}
{% include fig.html src="/assets/images/tfg/plataforma-calculo.png" pie="Deflected shape and utilisation of each member group (Eurocode 9)." %}
</div>

<div class="texto" markdown="1">

## The drawings

I produced 16 A3 drawings: general assembly, frame, platform and every part that isn't off-the-shelf, with tolerances and bills of materials. The CAD kept changing, so I generated them with Python scripts that drive SolidWorks through its API (which I wrote with Claude Code, an AI assistant) and check every dimension against its expected value before saving.

</div>

{% include fig.html src="/assets/images/tfg/plano-seccion-montaje.png" pie="Drawing 05: module assembly section and bill of materials (in Spanish)." clase="ancha" %}

<div class="texto" markdown="1">

## What I learned

- That cold is as much a geometry problem as a materials one. Almost everything was solved by deciding what is allowed to move and what isn't: one fixed point, sliding guides and holes with just enough clearance.
- To think about whoever assembles and maintains the thing. The rear cartridge and the folding decks came from asking how you replace a top-row module.
- That a drawing forces decisions a 3D model lets you postpone. Dimensioning for manufacture exposed inconsistencies between the report and the model, like Ø8 holes in one place and Ø9 in the other, or M4 threads where M6 belonged.

</div>

<div class="volver"><a href="/en/design-office/">← Previous: my job</a><a href="/en/home-server/">Next: a server at home →</a></div>
