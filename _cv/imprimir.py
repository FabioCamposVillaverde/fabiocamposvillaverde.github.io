"""Imprime cv-es.html y cv-en.html a PDF con Chromium (lo llama generar.sh dentro de Docker)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

aqui = Path(__file__).resolve().parent
salida = aqui.parent / "assets" / "pdfs"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for fuente, pdf in [("cv-es.html", "curriculum-fabio-esp.pdf"), ("cv-en.html", "curriculum-fabio-eng.pdf")]:
        pg.goto((aqui / fuente).as_uri(), wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(salida / pdf), format="A4", print_background=True, prefer_css_page_size=True)
        print(pdf, "ok")
    b.close()
