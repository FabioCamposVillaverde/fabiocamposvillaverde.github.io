# CLAUDE.md

Guía para Claude Code (claude.ai/code) al trabajar en este repositorio.

## Qué es esto

Portafolio personal de Fabio Campos, publicado como sitio **Jekyll en GitHub Pages** (`fabiocamposvillaverde.github.io`, cuenta FabioCamposVillaverde). No hay build propio: GitHub Pages compila en cada push a `main`. La idea de partida es la web de Caleb Waldman (calebwaldman.site): cada proyecto contado en primera persona, con por qué, cómo, qué salió mal y qué aprendí.

## Tono (importante)

- Primera persona, frases cortas, datos concretos. Contar lo que falló.
- Nada de tono de anuncio: sin «apasionado», sin «del CAD al prototipo», sin llamadas a la acción en cada sección, sin emojis, sin contadores animados.
- No afirmar nada que no sea verdad (p. ej. el TFG NO tiene FEM del módulo: está fuera de alcance; el bot NO opera en real desde el 01/10/2026).

## Previsualizar

No hay `Gemfile`. Para compilar en local sin instalar Ruby, copiar el repo a otra carpeta, quitar la línea `theme:` de `_config.yml` y usar Docker:

```bash
docker run --rm -v "$PWD":/srv/jekyll -v /tmp/sitio:/srv/sitio jekyll/jekyll:4.2.2 jekyll build -d /srv/sitio
```

Las páginas ES de proyecto se sirven sin extensión (`/tfg-dune`): un servidor estático de pruebas tiene que probar `ruta + .html`.

## Arquitectura

- **`README.md` es la portada** (front matter `permalink: /`). Editar la home = editar `README.md`.
- **`_layouts/default.html`** es el único layout: `<head>`, cabecera con el menú y el selector ES/EN, pie, todo el CSS (variables `--fondo`, `--papel`, `--tinta`, `--linea`…) y el visor de imágenes. Tema claro, fuente IBM Plex Sans.
- **`_includes/fig.html`**: figura ampliable. `{% include fig.html src="..." pie="..." clase="ancha|media|estrecha|portada" %}`.
- **`_includes/tarjeta.html`**: tarjeta de proyecto para las rejillas de portada y de `proyectos.md`.
- Clases de las páginas de proyecto: `.ruta`, `.cabecera` + `.entradilla` + `.datos`, `.habilidades` (tres `.hab`), `.texto` (columna de lectura, con `markdown="1"`), `.fila`, `.galeria` (`dos`, `tres`), `.volver`.
- `_config.yml` mantiene `theme: jekyll-theme-minimal` por compatibilidad; el layout propio lo sustituye entero. Excluye `CLAUDE.md` del sitio.

### Páginas de proyecto

`tfg-dune.md`, `servidor-casero.md`, `trading-bot.md`, `simulador-racing.md`, `smart-hangboard.md`, `cinta-modular.md`. Las ES no llevan `permalink` (se sirven en `/nombre`, sin barra final); las EN sí (`/en/nombre/`, el servidor es `/en/home-server/`). Proyecto nuevo = página ES + página EN con `alt:` cruzados, tarjeta en `README.md`, `en/index.md`, `proyectos.md` y `en/proyectos.md`, y enlaces anterior/siguiente en `.volver`.

### Bilingüe

Español en la raíz, inglés en `/en/`, todo traducido. El selector usa `alt:` del front matter. Ojo: el `alt` de una página EN apunta a `/nombre` (sin barra), o da 404.

### Imágenes

- `assets/images/<proyecto>/` y `assets/images/tarjetas/` (miniaturas 800×600 para las tarjetas).
- **Antes de subir una foto: máx. 1600 px de lado y sin EXIF** (las del móvil llevan GPS; el historial se limpió el 23/11/2026 con git-filter-repo).
- Fotos del simulador: recortadas con rembg (BiRefNet) en fabiopc (`C:\PortfolioFotos`) y montadas sobre fondo de estudio; el objeto no se retoca.
- Las gráficas (`servidor/inercia-termica.png`, `trading-bot/backtest-vs-replay.png`) salen de datos reales: estadísticas horarias de Home Assistant y `scripts/replay_1m.py` del repo del bot.
- `assets/pdfs/`: currículums ES y EN.
