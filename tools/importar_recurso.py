"""Importa un artículo que ya es una página HTML completa (calculadora, guía interactiva) al blog.

Uso:  python tools/importar_recurso.py archivo.html "Categoría" [--leer 8]

Toma del propio HTML el slug (canonical /blog/<slug>), el título, la descripción, la fecha y los minutos de lectura.
Agrega el ícono y Analytics si faltan, guarda la página en tools/recursos/ y crea tools/articulos/<slug>.json.
Después hay que correr `python tools/gen.py blog` (o dejar que lo haga la automatización de GitHub al hacer push).
"""
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def importar(ruta, categoria, minutos=None):
    s = pathlib.Path(ruta).read_text(encoding='utf-8')

    def buscar(patron, obligatorio=True):
        m = re.search(patron, s, re.S)
        if not m and obligatorio:
            raise SystemExit(f'No encuentro {patron!r} en {ruta}')
        return m.group(1) if m else None

    slug = buscar(r'rel="canonical" href="https://lezacconsultoria\.com/blog/([a-z0-9-]+)"')
    title = re.sub(r'\s+', ' ', buscar(r'<title>(.*?)</title>')).strip()
    desc = buscar(r'<meta name="description" content="([^"]*)"')
    h1 = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', buscar(r'<h1[^>]*>(.*?)</h1>', False) or title.split('|')[0])).strip()
    fecha = buscar(r'article:published_time" content="(\d{4}-\d{2}-\d{2})')
    if minutos is None:
        m = re.search(r'(\d+) ?min(?:utos)? de lectura', s)
        minutos = int(m.group(1)) if m else 8

    if 'rel="icon"' not in s:
        s = s.replace('</head>', '    <link rel="icon" type="image/png" href="/logo-lezac-mini.png">\n</head>', 1)
    if 'analytics.js' not in s:
        s = s.replace('</head>', '    <script src="/analytics.js"></script>\n</head>', 1)

    (RAIZ / 'tools' / 'recursos').mkdir(exist_ok=True)
    (RAIZ / 'tools' / 'recursos' / f'{slug}.html').write_text(s, encoding='utf-8', newline='\n')
    art = {'slug': slug, 'h1': h1, 'title': title, 'description': desc, 'category': categoria, 'date': fecha,
           'status': 'publicado', 'read_minutes': minutos, 'html_file': f'tools/recursos/{slug}.html'}
    (RAIZ / 'tools' / 'articulos' / f'{slug}.json').write_text(json.dumps(art, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(f'{slug} | {h1} | {fecha} | {minutos} min | {categoria}')


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 2:
        raise SystemExit(__doc__)
    minutos = int(a[a.index('--leer') + 1]) if '--leer' in a else None
    importar(a[0], a[1], minutos)
