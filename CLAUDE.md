# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es esto

Portafolio personal de ingeniería mecánica de Fabio Campos, publicado como sitio **Jekyll en GitHub Pages** (`fabiocamposvillaverde.github.io`). No hay JavaScript de aplicación ni build propio: GitHub Pages compila el sitio automáticamente en cada push a `main`.

## Desarrollo y previsualización

No hay scripts npm ni tests. Para servir el sitio localmente se necesita Ruby + Jekyll:

```bash
bundle exec jekyll serve   # http://localhost:4000
```

No existe `Gemfile` en el repo; el tema y los plugins se resuelven vía el entorno de GitHub Pages (`_config.yml`). El flujo habitual es editar el Markdown y hacer push — el despliegue es automático.

## Arquitectura

- **`README.md` es la página de inicio**, no documentación. Lleva front matter Jekyll (`layout: default`, `permalink: /`) y GitHub Pages lo usa como `index`. Editar la home = editar `README.md`.
- **Todas las páginas son `.md` con HTML+CSS inline** dentro del front matter. El estilo vive directamente en cada archivo (atributos `style=`, bloques `<style>`), no en hojas externas. Tema oscuro: los colores son variables CSS del layout (`--bg`, `--panel`, `--line`, `--text`, `--muted`, `--accent` verde `#3ddc97`); las páginas de proyecto usan las clases `.pj-*` definidas en `_layouts/default.html`. Copia de una página existente.
- **`_layouts/default.html`** es el único layout: define `<head>`, la barra de navegación sticky y el footer. La barra de navegación está **hardcodeada** ahí (Home / Proyectos / CV / Contacto) — añadir una sección al menú se hace editando este archivo.
- **`_config.yml`** fija `theme: jekyll-theme-minimal` (sobreescrito en la práctica por el layout propio) más overrides de ancho/colores.
- **Enrutado por `permalink`**: cada página declara su URL en el front matter (`permalink: /proyectos/`, `/resume/`, etc.). Los enlaces internos usan esas rutas, no nombres de archivo.

### Páginas de proyecto

Cada proyecto es un `.md` independiente en la raíz (`simulador-racing.md`, `cinta-modular.md`, `smart-hangboard.md`, `tfg-dune.md`, `trading-bot.md`). Las páginas ES de proyecto NO llevan `permalink` (se sirven en `/nombre`, sin barra final): el `alt:` de su gemela EN debe apuntar a `/nombre`, no a `/nombre/` (da 404). El índice `proyectos.md` los enlaza mediante tarjetas (`.project-card`) con imagen, etiqueta y descripción. Al añadir un proyecto: crear el `.md` con su `permalink` y agregar su tarjeta en `proyectos.md`.

### Bilingüe (ES / EN)

- El español vive en la raíz; el inglés en **`/en/`**, con todas las páginas traducidas.
- El selector ES/EN está en la cabecera del layout y usa el campo `alt:` del front matter de cada página (la URL de su gemela en el otro idioma). Página nueva = crear las dos y poner `alt:` en ambas.

### Assets

- `assets/images/` — fotos/renders de proyectos (referenciados con rutas absolutas `/assets/images/...`). **Antes de subir una foto: máx. 1600 px de lado y sin EXIF** (las del móvil llevan GPS). Las capturas de pantalla, máx. 1680 px de ancho.
- `assets/pdfs/` — currículums (`curriculum-fabio-esp.pdf`, `curriculum-fabio-eng.pdf`).
