"""Genera las 6 páginas y reparte el nav/footer estáticos (fuente única: shared.js).
Uso:  python tools/gen.py            (genera todo)
      python tools/gen.py sync       (solo vuelve a copiar nav/footer de shared.js a las páginas)
      python tools/gen.py blog       (solo el blog: listado, artículos, sitemap y llms.txt; lo usa la automatización de GitHub)
"""
import json
import re
import subprocess
import sys

sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from lib import ROOT, icons_to_attr
import pages_a
import pages_b
import pages_c
import blog

PAGES = ['index.html', 'consultoria-inteligencia-comercial.html', 'mas-clientes-activos.html',
         'ia-a-medida.html', 'wa-ventas.html', 'partner.html']


def layout():
    js = ("const fs=require('fs');const src=fs.readFileSync('shared.js','utf8');const m={};"
          "new Function('m',src.split('// ─── BOOTSTRAP')[0]+';m.nav=getLezacNav();m.footer=getLezacFooter();')(m);"
          "process.stdout.write(JSON.stringify(m))")
    r = subprocess.run(['node', '-e', js], cwd=ROOT, capture_output=True, encoding='utf-8')
    if r.returncode != 0:
        raise SystemExit('node falló: ' + r.stderr)
    return json.loads(r.stdout)


def sync(only_blog=False):
    m = layout()
    m = {k: icons_to_attr(v) for k, v in m.items()}
    for f in (blog.pages() if only_blog else PAGES + blog.pages()):
        s = (ROOT / f).read_text(encoding='utf-8')
        s, n1 = re.subn(r'<!--lz:nav-->.*?<!--/lz:nav-->', lambda _: '<!--lz:nav-->' + m['nav'].strip() + '<!--/lz:nav-->', s, flags=re.S)
        s, n2 = re.subn(r'<!--lz:footer-->.*?<!--/lz:footer-->', lambda _: '<!--lz:footer-->' + m['footer'].strip() + '<!--/lz:footer-->', s, flags=re.S)
        (ROOT / f).write_text(s, encoding='utf-8', newline='\n')
        print('nav/footer', f, n1, n2)


if __name__ == '__main__':
    if 'blog' in sys.argv:
        blog.generate()
        sync(only_blog=True)
        raise SystemExit
    if 'sync' not in sys.argv:
        pages_a.brujula()
        pages_a.clientes()
        pages_b.ia()
        pages_b.wa_ventas()
        pages_b.partner()
        pages_c.home()
        blog.generate()
    sync()
