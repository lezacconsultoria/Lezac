"""Blog: /blog (listado) y /blog/<slug> (artículos). Cada artículo es un JSON en articulos/ (los que empiezan con _ se ignoran)."""
import datetime
import glob
import json
import re
import unicodedata
from lib import *

ART_DIR = pathlib.Path(__file__).parent / 'articulos'
MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
AUTHOR = 'Lic. Leandro Zacaria'
ROLE = 'Fundador · Lezac Consultoría'
SVC_COLOR = {'Inteligencia comercial': '#25F5A4', '+Clientes Activos': '#38BDF8', 'IA a Medida': '#8C52FF'}
# La última tarjeta suelta de una grilla de 2 columnas queda centrada
ODD = ('md:[&>*:last-child:nth-child(odd)]:col-span-2 md:[&>*:last-child:nth-child(odd)]:w-[calc(50%-0.5rem)] '
       'md:[&>*:last-child:nth-child(odd)]:justify-self-center')
GLOW = 'box-shadow:0 8px 32px rgba(0,0,0,0.35),0 0 60px -34px var(--color-accent-glow)'


def normalize(a):
    """Completa los datos opcionales de un artículo (los creados desde Control Maestro traen solo lo básico)."""
    a = dict(a)
    a.setdefault('status', 'publicado')
    a.setdefault('category', 'Inteligencia comercial')
    a.setdefault('subtitle', '')
    a.setdefault('title', f"{a['h1']} | Lezac")
    a.setdefault('date', datetime.date.today().isoformat())
    if 'blocks' not in a and 'html_file' not in a:
        a['blocks'] = [{'t': 'md', 'text': a.get('body', ''), 'toc': bool(a.get('toc', False))}]
    if 'read_minutes' not in a:
        n = len(re.findall(r'\w+', re.sub(r'<[^>]+>', ' ', json.dumps(a['blocks'], ensure_ascii=False))))
        a['read_minutes'] = max(1, round(n / 200))
    a.setdefault('wa_text', f"Hola Leandro, leí el artículo {a['h1']} y quiero charlar.")
    return a


def load(todos=False):
    """Artículos publicados (con todos=True, también los borradores), del más nuevo al más viejo."""
    arts = []
    for f in sorted(glob.glob(str(ART_DIR / '*.json'))):
        if pathlib.Path(f).name.startswith('_'):
            continue
        a = normalize(json.load(open(f, encoding='utf-8')))
        if todos or a['status'] == 'publicado':
            arts.append(a)
    return sorted(arts, key=lambda a: a['date'], reverse=True)


def pages():
    return ['blog.html'] + ['blog/' + a['slug'] + '.html' for a in load()]


def fdate(iso):
    d = datetime.date.fromisoformat(iso)
    return f'{d.day} de {MESES[d.month - 1]} de {d.year}'


def crumbs(items):
    out = '<nav aria-label="Breadcrumb" class="text-xs text-on-surface-variant"><ol class="flex flex-wrap items-center gap-2">'
    for i, (name, href) in enumerate(items):
        if i == len(items) - 1:
            out += f'<li aria-current="page" class="text-white/80">{E(name)}</li>'
        else:
            out += f'<li><a href="{href}" class="hover:text-white transition-colors">{E(name)}</a></li><li aria-hidden="true">›</li>'
    return out + '</ol></nav>'


def byline(a):
    return ('<div class="flex flex-wrap items-center gap-x-4 gap-y-2 text-sm text-on-surface-variant">'
            '<img src="/perfil-leandro.jpg" alt="Lic. Leandro Zacaria" width="44" height="44" class="w-11 h-11 rounded-full object-cover" style="border:1px solid rgba(255,255,255,0.12)">'
            f'<span><span class="text-white font-semibold">{AUTHOR}</span><br>{ROLE}</span>'
            f'<span aria-hidden="true">·</span><time datetime="{a["date"]}">{fdate(a["date"])}</time>'
            f'<span aria-hidden="true">·</span><span>{a["read_minutes"]} min de lectura</span></div>')


def chip(text, color='var(--color-accent)'):
    return (f'<span class="inline-block text-[11px] font-semibold tracking-wide px-2.5 py-1 rounded-full" '
            f'style="color:{color};background:color-mix(in srgb,{color} 12%,transparent)">{E(text)}</span>')


def check(text, sub=None):
    s = f'<span class="block text-sm text-on-surface-variant mt-1">{E(sub)}</span>' if sub else ''
    return ('<li class="flex items-start gap-3 text-white/90 leading-relaxed"><span class="w-5 h-5 mt-0.5 rounded-full flex-shrink-0 flex items-center justify-center" '
            'style="background:color-mix(in srgb,var(--color-accent) 15%,transparent);color:var(--color-accent)">'
            '<span class="material-symbols-outlined" style="font-size:13px">check</span></span>'
            f'<span>{E(text)}{s}</span></li>')


def clave(b):
    por = b['por'].replace('<strong>', '<strong class="text-white">')
    x = f'<article id="clave-{b["n"]}" class="scroll-mt-28 liquid-glass rounded-2xl p-6 md:p-9 mb-6" style="{GLOW}">'
    x += f'<p class="text-xs font-semibold tracking-widest uppercase accent mb-3">Clave {b["n"]:02d} de 10</p>'
    x += f'<h3 class="text-xl md:text-2xl font-black text-white leading-snug mb-6">{E(b["h2"])}</h3>'
    x += f'<h4 class="text-sm font-bold uppercase tracking-wider text-white mb-2">Qué es</h4><p class="text-on-surface-variant leading-relaxed mb-6">{E(b["que"])}</p>'
    x += f'<h4 class="text-sm font-bold uppercase tracking-wider text-white mb-2">Por qué importa</h4><p class="text-on-surface-variant leading-relaxed mb-4">{por}</p>'
    if b.get('pct'):
        x += ('<div class="flex items-center gap-3 mb-6" aria-hidden="true"><div class="flex-1 h-2 rounded-full overflow-hidden" style="background:rgba(255,255,255,0.07)">'
              f'<div class="h-full rounded-full" style="width:{b["pct"]}%;background:var(--color-accent)"></div></div>'
              f'<span class="text-sm font-black accent tabular-nums">{b["pct"]}%</span></div>')
    else:
        x += '<div class="mb-6"></div>'
    x += '<h4 class="text-sm font-bold uppercase tracking-wider text-white mb-3">Qué implementar</h4><ul class="space-y-3">'
    x += ''.join(check(it['t'], it.get('sub')) for it in b['items'])
    return x + '</ul></article>'

SAFE_URL = re.compile(r'^(https?://|/|#|mailto:)')


def slugify(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-') or 'seccion'


def inline(t):
    """Markdown en línea (negrita, cursiva, código, links). Todo lo demás se escapa."""
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code class="px-1.5 py-0.5 rounded bg-white/10 text-white text-[0.9em]">\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong class="text-white">\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])', r'<em>\1</em>', t)

    def link(m):
        url = m.group(2).replace('&amp;', '&')
        if not SAFE_URL.match(url):
            return m.group(0)
        ext = url.startswith('http') and 'lezacconsultoria.com' not in url
        rel = ' target="_blank" rel="noopener"' if ext else ''
        return f'<a href="{html.escape(url)}" class="underline accent hover:text-white"{rel}>{m.group(1)}</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, t)


BUL = re.compile(r'^[-*•]\s+')
NUM = re.compile(r'^\d+[.)]\s+')
IMG = re.compile(r'^!\[([^\]]*)\]\((\S+)\)$')


def md_to_html(text, toc=False):
    lines = text.replace('\r\n', '\n').split('\n')
    out, h2s, para, i = [], [], [], 0

    def flush():
        if para:
            out.append(f'<p class="text-base md:text-lg text-on-surface-variant leading-relaxed mb-5">{inline(" ".join(para))}</p>')
            para.clear()
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            flush()
            i += 1
            continue
        m = re.match(r'^(#{1,3})\s+(.+)$', s)
        if m:
            flush()
            level, txt = len(m.group(1)), m.group(2).strip()
            if level <= 2:
                sid = slugify(txt)
                n = sum(1 for x in h2s if x[0] == sid or re.fullmatch(re.escape(sid) + r'-\d+', x[0]))
                sid = sid if not n else f'{sid}-{n + 1}'
                h2s.append((sid, txt))
                out.append(f'<h2 id="{sid}" class="scroll-mt-28 text-2xl md:text-3xl font-black text-white leading-tight tracking-tight mt-14 mb-5">{inline(txt)}</h2>')
            else:
                out.append(f'<h3 class="text-xl md:text-2xl font-bold text-white leading-snug mt-9 mb-3">{inline(txt)}</h3>')
            i += 1
        elif BUL.match(s):
            flush()
            items = []
            while i < len(lines) and BUL.match(lines[i].strip()):
                items.append(BUL.sub('', lines[i].strip()))
                i += 1
            out.append('<ul class="space-y-3 my-5">' + ''.join(
                '<li class="flex items-start gap-3 text-white/90 leading-relaxed"><span class="w-1.5 h-1.5 rounded-full mt-2.5 flex-shrink-0" style="background:var(--color-accent)"></span>'
                f'<span>{inline(x)}</span></li>' for x in items) + '</ul>')
        elif NUM.match(s):
            flush()
            items = []
            while i < len(lines) and NUM.match(lines[i].strip()):
                items.append(NUM.sub('', lines[i].strip()))
                i += 1
            out.append('<ol class="space-y-3 my-5">' + ''.join(
                f'<li class="flex items-start gap-3 text-white/90 leading-relaxed"><span class="accent font-bold tabular-nums w-6 flex-shrink-0">{n}.</span><span>{inline(x)}</span></li>'
                for n, x in enumerate(items, 1)) + '</ol>')
        elif s.startswith('>'):
            flush()
            q = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                q.append(lines[i].strip().lstrip('>').strip())
                i += 1
            out.append('<blockquote class="my-6 pl-5 py-1 text-lg text-white/90 leading-relaxed" style="border-left:3px solid var(--color-accent)">'
                       f'{inline(" ".join(q))}</blockquote>')
        elif re.match(r'^(-{3,}|\*{3,})$', s):
            flush()
            out.append('<hr class="my-10 border-white/10">')
            i += 1
        elif IMG.match(s):
            flush()
            alt, url = IMG.match(s).groups()
            if SAFE_URL.match(url) and not url.startswith(('#', 'mailto:')):
                cap = f'<figcaption class="text-xs text-on-surface-variant text-center mt-2">{html.escape(alt, quote=False)}</figcaption>' if alt else ''
                out.append(f'<figure class="my-8"><img src="{html.escape(url)}" alt="{html.escape(alt)}" loading="lazy" class="w-full h-auto rounded-2xl" '
                           f'style="border:1px solid rgba(255,255,255,0.08)">{cap}</figure>')
            i += 1
        else:
            para.append(s)
            i += 1
    flush()
    body = ''.join(out)
    if toc and len(h2s) >= 3:
        nav = ('<nav aria-label="Índice" class="liquid-glass rounded-2xl p-6 md:p-7 my-8"><p class="text-xs font-semibold tracking-widest uppercase text-on-surface-variant mb-4">Índice</p>'
               '<ol class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-2.5">' + ''.join(
                   f'<li><a href="#{sid}" class="flex items-baseline gap-3 text-sm text-white/85 hover:text-white transition-colors"><span class="accent font-bold tabular-nums">{n:02d}</span><span>{html.escape(t, quote=False)}</span></a></li>'
                   for n, (sid, t) in enumerate(h2s, 1)) + '</ol></nav>')
        body = nav + body
    return body


def render(b):
    t = b['t']
    if t == 'h2':
        return f'<h2 id="{b["id"]}" class="scroll-mt-28 text-2xl md:text-3xl font-black text-white leading-tight tracking-tight mt-14 mb-5">{E(b["text"])}</h2>'
    if t == 'p':
        x = f'<p class="text-base md:text-lg text-on-surface-variant leading-relaxed mb-5">{b["html"]}</p>'
        if b.get('link'):
            x += btn(b['link'][0], b['link'][1], 'secondary') + '<div class="mb-5"></div>'
        return x
    if t == 'stats':
        out = '<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-6">'
        for s in b['items']:
            out += (f'<div class="liquid-glass rounded-2xl p-6"><p class="text-5xl font-black accent leading-none mb-3">{E(s["v"])}</p>'
                    f'<p class="text-white/90 leading-snug mb-2">{E(s["d"])}</p><p class="text-xs text-on-surface-variant">{E(s["src"])}</p></div>')
        return out + '</div>'
    if t == 'toc':
        out = (f'<nav aria-label="{E(b["title"])}" class="liquid-glass rounded-2xl p-6 md:p-7 my-8"><p class="text-xs font-semibold tracking-widest uppercase text-on-surface-variant mb-4">'
               f'{E(b["title"])}</p><ol class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-2.5">')
        for i, it in enumerate(b['items'], 1):
            out += (f'<li><a href="#clave-{i}" class="flex items-baseline gap-3 text-sm text-white/85 hover:text-white transition-colors">'
                    f'<span class="accent font-bold tabular-nums">{i:02d}</span><span>{E(it)}</span></a></li>')
        return out + '</ol></nav>'
    if t == 'cards':
        out = f'<ul class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 {ODD}">'
        for n, (ti, de, tag, href) in enumerate(b['items'], 1):
            out += ('<li class="liquid-glass rounded-xl p-5 flex flex-col gap-2 transition-transform duration-300 hover:-translate-y-1">'
                    f'<div class="flex items-center justify-between"><span class="text-xs font-bold tabular-nums text-on-surface-variant">{n:02d}</span>'
                    f'<a href="{href}">{chip(tag, SVC_COLOR.get(tag, "#8C52FF"))}</a></div>'
                    f'<p class="text-white font-bold">{E(ti)}</p><p class="text-sm text-on-surface-variant leading-relaxed">{E(de)}</p></li>')
        return out + '</ul>'
    if t == 'md':
        return md_to_html(b['text'], b.get('toc', False))
    if t == 'clave':
        return clave(b)
    if t == 'services':
        out = '<ul class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">'
        for ti, de, href, col in b['items']:
            out += (f'<li><a href="{href}" class="liquid-glass rounded-xl p-5 flex flex-col gap-2 h-full transition-transform duration-300 hover:-translate-y-1" '
                    f'style="box-shadow:0 8px 32px rgba(0,0,0,0.35),0 0 50px -30px {col}">'
                    f'<span class="w-2 h-2 rounded-full" style="background:{col}"></span><span class="text-white font-bold">{E(ti)}</span>'
                    f'<span class="text-sm text-on-surface-variant leading-relaxed">{E(de)}</span></a></li>')
        return out + '</ul>'
    raise ValueError(t)


def article_page(a):
    path = f'/blog/{a["slug"]}'
    url = SITE + path
    author = {"@type": "Person", "name": "Leandro Zacaria", "jobTitle": "Fundador de Lezac Consultoría",
              "worksFor": {"@id": SITE + "/#organization"}, "url": SITE + "/"}
    post = {"@type": "BlogPosting", "@id": url + "#article", "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "headline": a['h1'], "description": a['description'], "datePublished": a['date'],
            "dateModified": a.get('updated', a['date']), "inLanguage": "es-AR", "articleSection": a['category'],
            "image": OG_IMAGE, "author": author, "publisher": {"@id": SITE + "/#organization"}, "isPartOf": {"@id": SITE + "/#website"}}
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog"},
        {"@type": "ListItem", "position": 3, "name": a['h1'], "item": url}]}
    ld = jsonld(org_min(), website_min(), post, bc)
    share = 'https://www.linkedin.com/sharing/share-offsite/?url=' + urllib.parse.quote(url, safe='')
    hero_x = ('<section class="relative px-6 md:px-12 pt-28 md:pt-32 pb-10 overflow-hidden grid-bg">'
              '<div class="glow-blob w-[600px] h-[600px] opacity-[0.07] top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2" style="background:var(--color-accent)"></div>'
              '<div class="max-w-3xl mx-auto relative z-10 space-y-6">'
              + crumbs([('Inicio', '/'), ('Blog', '/blog'), (a['h1'], path)])
              + f'<div>{chip(a["category"])}</div>'
              + h1(a['h1'], None, 'text-4xl md:text-5xl')
              + (f'<p class="text-lg md:text-xl text-white/90 font-medium leading-relaxed">{E(a["subtitle"])}</p>' if a['subtitle'] else '')
              + byline(a)
              + '<div class="flex flex-col sm:flex-row gap-3 pt-2">'
              + (btn('Ver como presentación', a['deck'], 'secondary') if a.get('deck') else '')
              + f'<a href="{share}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-full text-sm font-semibold text-white/80 hover:text-white transition-colors">Compartir en LinkedIn</a>'
              + '</div>'
              + (f'<img src="{html.escape(a["cover"])}" alt="{html.escape(a["h1"])}" class="w-full h-auto rounded-2xl" style="border:1px solid rgba(255,255,255,0.08)">' if a.get('cover') else '')
              + '</div></section>')
    body_x = section('<div class="max-w-3xl mx-auto">' + ''.join(render(b) for b in a['blocks']) + '</div>', reveal=False)
    author_x = ('<section class="px-6 md:px-12 pb-12"><div class="max-w-3xl mx-auto liquid-glass rounded-2xl p-6 flex items-center gap-5">'
                '<img src="/perfil-leandro.jpg" alt="Lic. Leandro Zacaria" width="72" height="72" loading="lazy" class="w-[72px] h-[72px] rounded-full object-cover flex-shrink-0" style="border:1px solid rgba(255,255,255,0.12)">'
                f'<div><p class="text-white font-bold">{AUTHOR}</p><p class="text-sm text-on-surface-variant">{ROLE}</p>'
                '<a href="/" class="text-sm underline accent hover:text-white">Conocé más sobre nosotros</a></div></div></section>')
    cta = cta_final('¿Charlamos?', 'Si querés lo charlamos: escribime desde el botón de WhatsApp.',
                    [btn('Escribir por WhatsApp', wa(a['wa_text']), 'primary'), btn('Agendar una charla', CAL, 'secondary', 'calendar_today')],
                    'Sin contrato inicial. Alcance y presupuesto a tu medida.')
    out = shell('blog', a['title'], a['description'], path, ld, hero_x + body_x + author_x + cta)
    out = out.replace('property="og:type" content="website"', 'property="og:type" content="article"')
    if a.get('cover'):
        out = out.replace(OG_IMAGE, SITE + a['cover'])
    return out


def index_page(arts):
    path = '/blog'
    title = 'Blog de inteligencia comercial | Lezac Consultoría'
    desc = 'Ideas prácticas de inteligencia comercial para pymes, distribuidoras y mayoristas: gestión del equipo, clientes y datos de venta.'
    ld = jsonld(org_min(), website_min(),
                {"@type": "Blog", "@id": SITE + "/blog#blog", "url": SITE + "/blog", "name": "Blog de Lezac Consultoría", "description": desc,
                 "inLanguage": "es-AR", "publisher": {"@id": SITE + "/#organization"},
                 "blogPost": [{"@type": "BlogPosting", "headline": a['h1'], "url": f'{SITE}/blog/{a["slug"]}', "datePublished": a['date'],
                               "author": {"@type": "Person", "name": "Leandro Zacaria"}} for a in arts]},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog"}]})
    hero_x = ('<section class="relative px-6 md:px-12 pt-28 md:pt-32 pb-12 overflow-hidden grid-bg">'
              '<div class="glow-blob w-[600px] h-[600px] opacity-[0.07] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" style="background:var(--color-accent)"></div>'
              '<div class="max-w-5xl mx-auto text-center space-y-6 relative z-10">'
              '<div class="flex justify-center">' + crumbs([('Inicio', '/'), ('Blog', path)]) + '</div>'
              '<span class="pill-badge"><span class="pill-dot"></span>Blog · Lezac Consultoría</span>'
              + h1('Blog de', 'inteligencia comercial', 'text-4xl md:text-5xl')
              + '<p class="text-base md:text-lg text-on-surface-variant font-light max-w-2xl mx-auto leading-relaxed">Ideas prácticas para gestionar mejor tu equipo, tus clientes y tus datos de venta.</p>'
              '</div></section>')
    cards = f'<ul class="grid grid-cols-1 md:grid-cols-2 gap-5 {ODD}">'
    for a in arts:
        cards += (f'<li><a href="/blog/{a["slug"]}" class="liquid-glass rounded-2xl p-7 flex flex-col gap-4 h-full transition-transform duration-300 hover:-translate-y-1" style="{GLOW}">'
                  f'<div class="flex items-center justify-between gap-3">{chip(a["category"])}<span class="text-xs text-on-surface-variant">{a["read_minutes"]} min de lectura</span></div>'
                  f'<h2 class="text-xl md:text-2xl font-black text-white leading-snug">{E(a["h1"])}</h2>'
                  f'<p class="text-sm text-on-surface-variant leading-relaxed">{E(a["description"])}</p>'
                  f'<div class="mt-auto flex items-center justify-between text-sm"><time datetime="{a["date"]}" class="text-on-surface-variant">{fdate(a["date"])}</time>'
                  '<span class="font-semibold accent">Leer artículo →</span></div></a></li>')
    cards += '</ul>'
    cta = cta_final('¿Querés aplicarlo en tu empresa?', 'Contanos cómo trabajan hoy y vemos por dónde conviene empezar.',
                    [btn('Agendar una charla', CAL, 'primary', 'calendar_today'), btn('Ver servicios', '/', 'secondary')],
                    'Sin contrato inicial. Alcance y presupuesto a tu medida.')
    return shell('blog', title, desc, path, ld, hero_x + section(cards, reveal=False) + cta)


def update_sitemap(arts):
    p = ROOT / 'sitemap.xml'
    s = p.read_text(encoding='utf-8')
    s = re.sub(r'\s*<url>\s*<loc>' + re.escape(SITE) + r'/blog[^<]*</loc>.*?</url>', '', s, flags=re.S)
    last = max(a.get('updated', a['date']) for a in arts)
    new = f'  <url>\n    <loc>{SITE}/blog</loc>\n    <lastmod>{last}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n'
    for a in arts:
        new += (f'  <url>\n    <loc>{SITE}/blog/{a["slug"]}</loc>\n    <lastmod>{a.get("updated", a["date"])}</lastmod>\n'
                '    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n')
    p.write_text(s.replace('</urlset>', new + '</urlset>'), encoding='utf-8', newline='\n')


def update_llms(arts):
    p = ROOT / 'llms.txt'
    s = p.read_text(encoding='utf-8')
    s = re.sub(r'\n## Blog\n(?:- .*\n?)*', '\n', s).rstrip('\n') + '\n'
    s += '\n## Blog\n' + f'- [Blog de inteligencia comercial]({SITE}/blog)\n'
    s += ''.join(f'- [{a["h1"]}]({SITE}/blog/{a["slug"]}): {a["description"]}\n' for a in arts)
    p.write_text(s, encoding='utf-8', newline='\n')


def generate():
    arts = load()
    (ROOT / 'blog').mkdir(exist_ok=True)
    write('blog.html', index_page(arts))
    for a in arts:
        if a.get('html_file'):
            # Página propia y funcional (calculadora, guía interactiva): se publica tal cual
            fuente = (ROOT / a['html_file']).read_text(encoding='utf-8')
            (ROOT / 'blog' / f'{a["slug"]}.html').write_text(fuente, encoding='utf-8', newline='\n')
            print('copiado', a['slug'])
        else:
            write(f'blog/{a["slug"]}.html', article_page(a))
    vivos = {a['slug'] for a in arts}
    for f in (ROOT / 'blog').glob('*.html'):
        if f.stem not in vivos:
            f.unlink()
            print('eliminado', f.name)
    update_sitemap(arts)
    update_llms(arts)
