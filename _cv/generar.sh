#!/bin/sh
# Regenera assets/pdfs/curriculum-fabio-{esp,eng}.pdf a partir de cv-es.html y cv-en.html.
# Necesita Docker y red (la fuente IBM Plex Sans viene de Google Fonts).
cd "$(dirname "$0")/.." || exit 1
docker run --rm --network host -v "$PWD":/repo -u "$(id -u):$(id -g)" -e HOME=/tmp \
  mcr.microsoft.com/playwright/python:v1.55.0-noble \
  sh -c 'pip install -q --user playwright==1.55.0 >/dev/null 2>&1 && python3 /repo/_cv/imprimir.py'
