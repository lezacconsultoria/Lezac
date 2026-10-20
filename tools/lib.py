"""Utilidades para generar las páginas del sitio (copy literal desde SEO/*.md)."""
import html
import json
import pathlib
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
VER = '20261014'
SITE = 'https://lezacconsultoria.com'
CAL = 'https://calendly.com/lezacconsultoria/consultoria-comercial'
WA = 'https://wa.me/5491154107921'
PHONE = '+54 9 11 5410-7921'
OG_IMAGE = SITE + '/opengrap.jpeg'
LOGO = SITE + '/logo-lezac-completo.png'
LINKEDIN = 'https://www.linkedin.com/company/lezac-consultoria'
INSTAGRAM = 'https://www.instagram.com/lezacconsultoria/'

ACCENTS = {
    'home': ('#8C52FF', '#7131E3', 'rgba(140,82,255,0.3)', '#FFFFFF'),
    'brujula': ('#25F5A4', '#00C87E', 'rgba(37,245,164,0.25)', '#0A0A0B'),
    'clientes': ('#38BDF8', '#0EA5E9', 'rgba(56,189,248,0.25)', '#0A0A0B'),
    'ia': ('#8C52FF', '#7131E3', 'rgba(140,82,255,0.3)', '#FFFFFF'),
    'wa': ('#25D366', '#1FAF55', 'rgba(37,211,102,0.25)', '#0A0A0B'),
    'blog': ('#8C52FF', '#7131E3', 'rgba(140,82,255,0.3)', '#FFFFFF'),
    'partner': ('#F5C842', '#D4A800', 'rgba(245,200,66,0.25)', '#0A0A0B'),
}


class Raw(str):
    """Texto que ya trae HTML (por ejemplo <strong>) y no se escapa."""


def E(s):
    return s if isinstance(s, Raw) else html.escape(s, quote=False)


def wa(text=None):
    return WA if not text else WA + '?text=' + urllib.parse.quote(text)


def ext(href):
    return href.startswith('http')


# ───────────────────────── CSS / JS base ─────────────────────────
BASE_CSS = """
:root{--color-accent:@@A@@;--color-accent-dim:@@B@@;--color-accent-glow:@@G@@;--accent-ink:@@I@@;}
html{font-size:clamp(14px,13px + .23vw,19px);scroll-behavior:smooth;}
body{font-family:'Inter',sans-serif;background:#0A0A0B;color:#E5E2E3;-webkit-font-smoothing:antialiased;overflow-x:hidden;}
h1,h2,h3,h4{font-family:'Montserrat',sans-serif;}
.serif-italic{font-family:'Playfair Display',serif;font-style:italic;}
.material-symbols-outlined{font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 24;}
.material-symbols-outlined[data-i]::before{content:attr(data-i);}
.grid-bg{background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px);background-size:72px 72px;}
.glass{background:rgba(17,17,18,0.6);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.06);}
.liquid-glass{background:rgba(26,26,27,0.45);backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);border:1px solid rgba(255,255,255,0.07);box-shadow:0 8px 32px rgba(0,0,0,0.35),inset 0 1px 0 rgba(255,255,255,0.04);}
.pill-badge{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border-radius:9999px;background:color-mix(in srgb,var(--color-accent) 9%,transparent);border:1px solid color-mix(in srgb,var(--color-accent) 30%,transparent);font-size:11px;font-weight:600;letter-spacing:.05em;color:var(--color-accent);}
.pill-dot{width:7px;height:7px;border-radius:50%;background:var(--color-accent);animation:pulse-dot 2s ease-in-out infinite;flex-shrink:0;}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(.75)}}
.glow-blob{position:absolute;border-radius:50%;filter:blur(120px);pointer-events:none;}
.btn-accent{background:var(--color-accent);color:var(--accent-ink);box-shadow:0 0 40px var(--color-accent-glow);}
.accent{color:var(--color-accent);}
.lezac-reveal{opacity:0;transform:translateY(22px);transition:opacity .65s ease,transform .65s ease;}
.lezac-reveal.revealed{opacity:1;transform:translateY(0);}
.faq-answer{max-height:0;overflow:hidden;transition:max-height .4s ease;}
.faq-answer.open{max-height:700px;}
.faq-chevron{transition:transform .3s ease;}
.faq-chevron.rotated{transform:rotate(180deg);}
.cmp-table th,.cmp-table td{padding:14px 18px;text-align:left;font-size:.9rem;vertical-align:top;}
.cmp-table thead th{font-family:'Montserrat',sans-serif;font-weight:800;color:#fff;background:rgba(255,255,255,0.04);}
.cmp-table thead th:last-child{color:var(--color-accent);}
.cmp-table tbody tr{border-top:1px solid rgba(255,255,255,0.06);}
.cmp-table tbody td{color:#958DA1;}
.cmp-table tbody td:last-child{color:#E5E2E3;font-weight:500;}
"""

CAROUSEL_CSS = """
.float-shot{border-radius:8px;animation:lezac-float 7s ease-in-out infinite;will-change:transform;}
.float-shot[data-f="0"]{animation-duration:7s;animation-delay:-1s;}
.float-shot[data-f="1"]{animation-duration:8.5s;animation-delay:-4s;}
.float-shot[data-f="2"]{animation-duration:7.5s;animation-delay:-2.5s;}
@keyframes lezac-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@media (min-width:768px){
 .rs-wrap{position:relative;display:block;padding-top:22%;}
 .rs-slide{position:absolute;cursor:pointer;transition:left .9s cubic-bezier(.4,0,.2,1),top .9s cubic-bezier(.4,0,.2,1),width .9s cubic-bezier(.4,0,.2,1),filter .9s ease;}
 .rs-slide[data-p="0"]{left:0;top:3.9%;width:32%;z-index:1;filter:brightness(.8);}
 .rs-slide[data-p="1"]{left:29%;top:0;width:42.5%;z-index:10;filter:none;}
 .rs-slide[data-p="2"]{left:65.8%;top:3.9%;width:34%;z-index:1;filter:brightness(.8);}
 .rs-slide[data-p="1"] img{box-shadow:0 30px 80px rgba(0,0,0,.7),0 0 80px -30px var(--color-accent-glow);}
 .rs-slide:not([data-p="1"]) img{box-shadow:0 24px 60px rgba(0,0,0,.55);}
}
"""

BASE_JS = """
document.addEventListener('DOMContentLoaded', () => {
  const revObs = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('revealed'); revObs.unobserve(e.target); } }), { threshold: .08, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.lezac-reveal').forEach(el => revObs.observe(el));

  document.querySelectorAll('.faq-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const ans = btn.closest('h3').nextElementSibling, chev = btn.querySelector('.faq-chevron'), open = ans.classList.contains('open');
      document.querySelectorAll('.faq-answer.open').forEach(a => { a.classList.remove('open'); const b = a.previousElementSibling.querySelector('.faq-btn'); b.setAttribute('aria-expanded', 'false'); b.querySelector('.faq-chevron').classList.remove('rotated'); });
      if (!open) { ans.classList.add('open'); chev.classList.add('rotated'); btn.setAttribute('aria-expanded', 'true'); }
    });
  });
});
"""

CAROUSEL_JS = """
document.addEventListener('DOMContentLoaded', () => {
  const wrap = document.getElementById('rs-carousel');
  if (!wrap) return;
  const slides = [...wrap.querySelectorAll('.rs-slide')];
  let step = 0, timer;
  const layout = () => slides.forEach((el, i) => { el.dataset.p = (i + step) % 3; });
  const next = () => { step = (step + 1) % 3; layout(); };
  layout();
  const start = () => { timer = setInterval(next, 3800); };
  const stop = () => clearInterval(timer);
  wrap.addEventListener('mouseenter', stop);
  wrap.addEventListener('mouseleave', () => { stop(); start(); });
  slides.forEach((el, i) => el.addEventListener('click', () => { step = (1 - i + 3) % 3; layout(); }));
  start();
});
"""

TAILWIND_CFG = """tailwind.config = {
  darkMode:"class",
  theme:{extend:{
    colors:{
      "surface":"#0A0A0B","surface-dim":"#050506","surface-container":"#111112",
      "surface-container-low":"#0D0D0E","surface-container-high":"#1A1A1B",
      "on-surface":"#E5E2E3","on-surface-variant":"#958DA1","outline-variant":"#2A2A2B",
      "primary":"#8C52FF","primary-container":"#7131E3","on-primary":"#FFFFFF",
      "error":"#EC0543","success":"#25F5A4",
      "accent":"var(--color-accent)","accent-dim":"var(--color-accent-dim)",
    },
    borderRadius:{"DEFAULT":"0.75rem","sm":"0.5rem","lg":"1rem","xl":"1.5rem","2xl":"2rem","full":"9999px"},
    fontFamily:{"headline":["Montserrat","sans-serif"],"serif":["Playfair Display","serif"],"body":["Inter","sans-serif"]},
  }},
}"""


# ───────────────────────── JSON-LD ─────────────────────────
def org_min():
    return {"@type": "Organization", "@id": SITE + "/#organization", "name": "Lezac Consultoría",
            "url": SITE + "/", "logo": LOGO}


def website_min():
    return {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Lezac Consultoría",
            "inLanguage": "es-AR", "publisher": {"@id": SITE + "/#organization"}}


def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def breadcrumb_ld(name, path):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}


def jsonld(*nodes):
    g = {"@context": "https://schema.org", "@graph": list(nodes)}
    return '<script type="application/ld+json">\n' + json.dumps(g, ensure_ascii=False, indent=1) + '\n</script>'


# ───────────────────────── head / shell ─────────────────────────
def head(page, title, desc, path, ld, extra_css=''):
    a, b, g, i = ACCENTS[page]
    css = BASE_CSS.replace('@@A@@', a).replace('@@B@@', b).replace('@@G@@', g).replace('@@I@@', i) + extra_css
    url = SITE + path
    t, d = html.escape(title), html.escape(desc)
    return f'''<!DOCTYPE html>
<html class="dark" lang="es-AR" data-page="{page}">
<head>
<meta charset="utf-8"/>
<link rel="icon" type="image/png" href="/logo-lezac-mini.png"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{t}</title>
<meta name="description" content="{d}"/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="{url}"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="es_AR"/>
<meta property="og:site_name" content="Lezac Consultoría"/>
<meta property="og:url" content="{url}"/>
<meta property="og:title" content="{t}"/>
<meta property="og:description" content="{d}"/>
<meta property="og:image" content="{OG_IMAGE}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{t}"/>
<meta name="twitter:description" content="{d}"/>
<meta name="twitter:image" content="{OG_IMAGE}"/>
{ld}
<script src="/analytics.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Playfair+Display:ital,wght@1,400;1,600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script>
{TAILWIND_CFG}
</script>
<style>{css}</style>
</head>
'''


def shell(page, title, desc, path, ld, content, extra_css='', extra_js='', body_attrs=''):
    return (head(page, title, desc, path, ld, extra_css) + f'''<body class="bg-surface selection:bg-primary/30 selection:text-white"{body_attrs}>
<!--lz:nav--><!--/lz:nav-->
<main>
{content}
</main>
<!--lz:footer--><!--/lz:footer-->
<script src="/shared.js?v={VER}"></script>
<script>{BASE_JS}{extra_js}</script>
</body>
</html>
''')


# ───────────────────────── componentes ─────────────────────────
def btn(text, href, kind='primary', icon=None):
    base = 'inline-flex items-center justify-center gap-2 px-8 py-4 rounded-full text-sm transition-all hover:scale-[1.02] '
    if kind == 'primary':
        cls = base + 'font-bold btn-accent hover:brightness-110'
    else:
        cls = base + 'font-semibold text-white/85 hover:text-white hover:bg-white/5'
    style = '' if kind == 'primary' else ' style="border:1px solid rgba(255,255,255,0.15)"'
    tgt = ' target="_blank" rel="noopener"' if ext(href) else ''
    ic = f'<span class="material-symbols-outlined" style="font-size:18px">{icon}</span>' if icon else ''
    return f'<a href="{html.escape(href)}"{tgt} class="{cls}"{style}>{ic}{E(text)}</a>'


def btns(*bs):
    return '<div class="flex flex-col sm:flex-row gap-3 justify-center">' + ''.join(bs) + '</div>'


def check_li(text):
    return ('<li class="flex items-center gap-2 text-sm text-white/80"><span class="w-5 h-5 rounded-full flex-shrink-0 flex '
            'items-center justify-center" style="background:color-mix(in srgb,var(--color-accent) 15%,transparent);'
            'color:var(--color-accent)"><span class="material-symbols-outlined" style="font-size:13px">check</span></span>'
            f'{E(text)}</li>')


def bullets(items, center=True):
    j = 'justify-center ' if center else ''
    return f'<ul class="flex flex-wrap {j}gap-x-6 gap-y-2">' + ''.join(check_li(i) for i in items) + '</ul>'


def breadcrumb(name):
    return ('<nav aria-label="Breadcrumb" class="text-xs text-on-surface-variant"><ol class="flex items-center justify-center gap-2">'
            '<li><a href="/" class="hover:text-white transition-colors">Inicio</a></li><li aria-hidden="true">›</li>'
            f'<li aria-current="page" class="text-white/80">{E(name)}</li></ol></nav>')


def h1(a, b=None, size='text-3xl md:text-5xl'):
    inner = E(a) + (f' <span class="serif-italic font-semibold accent">{E(b)}</span>' if b else '')
    return f'<h1 class="{size} font-black leading-[1.1] tracking-tight text-white">{inner}</h1>'


def h2(text, center=False, extra=''):
    c = ' text-center' if center else ''
    return f'<h2 class="text-3xl md:text-4xl font-black text-white leading-tight tracking-tight mb-6{c} {extra}">{E(text)}</h2>'


def eyebrow(text):
    return f'<span class="text-xs font-semibold tracking-widest uppercase block mb-3 accent">{E(text)}</span>'


def p(text, cls='text-on-surface-variant leading-relaxed'):
    return f'<p class="{cls}">{E(text)}</p>'


def section(inner, bg='surface', sid=None, width='max-w-5xl', reveal=True):
    bgc = 'bg-surface' if bg == 'surface' else ''
    st = '' if bg == 'surface' else ' style="background:#050506"'
    idattr = f' id="{sid}"' if sid else ''
    rv = ' lezac-reveal' if reveal else ''
    return (f'<section class="py-20 md:py-24 px-6 md:px-12 relative overflow-hidden {bgc}"{st}{idattr}>'
            f'<div class="{width} mx-auto{rv}">{inner}</div></section>')


def item_cards(items, cols='md:grid-cols-2'):
    odd = ' md:[&>li:last-child:nth-child(odd)]:col-span-2 md:[&>li:last-child:nth-child(odd)]:w-[calc(50%-0.5rem)] md:[&>li:last-child:nth-child(odd)]:justify-self-center' if cols == 'md:grid-cols-2' else ''
    out = f'<ul class="grid grid-cols-1 {cols} gap-4{odd}">'
    for t, s in items:
        desc = f'<p class="text-sm text-on-surface-variant leading-relaxed">{E(s)}</p>' if s else ''
        out += ('<li class="liquid-glass rounded-xl p-5">'
                f'<p class="text-white font-bold mb-1">{E(t)}</p>{desc}</li>')
    return out + '</ul>'


def steps(items):
    out = '<ol class="space-y-4">'
    for n, (t, s) in enumerate(items, 1):
        out += ('<li class="flex gap-5 items-start liquid-glass rounded-xl p-6">'
                f'<div class="flex-shrink-0 w-11 h-11 rounded-xl flex items-center justify-center font-black accent" style="background:color-mix(in srgb,var(--color-accent) 12%,transparent)">{n}</div>'
                f'<div><p class="text-white font-bold mb-1">{E(t)}</p><p class="text-sm text-on-surface-variant leading-relaxed">{E(s)}</p></div></li>')
    return out + '</ol>'


def table(headers, rows):
    out = '<div class="overflow-x-auto rounded-2xl liquid-glass"><table class="cmp-table w-full min-w-[520px]"><thead><tr>'
    out += ''.join(f'<th scope="col">{E(h)}</th>' for h in headers) + '</tr></thead><tbody>'
    for r in rows:
        out += '<tr>' + ''.join(f'<td>{E(c)}</td>' for c in r) + '</tr>'
    return out + '</tbody></table></div>'


def faq(items):
    out = '<div class="space-y-3">'
    for q, a in items:
        out += ('<div class="glass rounded-xl overflow-hidden"><h3 class="m-0">'
                '<button type="button" class="faq-btn w-full flex items-center justify-between p-6 text-left gap-4" aria-expanded="false">'
                f'<span class="font-bold text-white text-sm md:text-base">{E(q)}</span>'
                '<span class="material-symbols-outlined faq-chevron text-on-surface-variant flex-shrink-0">keyboard_arrow_down</span></button></h3>'
                f'<div class="faq-answer px-6 text-sm text-on-surface-variant leading-relaxed"><p class="pb-5">{E(a)}</p></div></div>')
    return out + '</div>'


def faq_section(items):
    return section(h2('Preguntas frecuentes', center=True) + faq(items), width='max-w-3xl')


def closing(text):
    return f'<p class="mt-8 text-white font-bold text-lg">{E(text)}</p>'


def prueba(h2text, line):
    inner = (f'<div class="text-center">{h2(h2text, center=True)}'
             f'<p class="text-sm font-semibold tracking-wide text-white/80 mb-8">{E(line)}</p></div>'
             '<div data-lezac-marquee></div>')
    return section(inner, bg='dim', width='max-w-6xl')


def cta_final(h2text, text, buttons, line):
    inner = ('<div class="text-center relative z-10">' + h2(h2text, center=True) +
             f'<p class="text-on-surface-variant max-w-xl mx-auto mb-8 leading-relaxed">{E(text)}</p>' + btns(*buttons) +
             f'<p class="mt-6 text-xs text-on-surface-variant">{E(line)}</p></div>')
    return ('<section class="py-24 px-6 md:px-12 relative overflow-hidden" style="background:#050506">'
            '<div class="glow-blob w-[600px] h-[600px] opacity-[0.06] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" style="background:var(--color-accent)"></div>'
            f'<div class="max-w-3xl mx-auto lezac-reveal">{inner}</div></section>')


def video(src, label):
    s = urllib.parse.quote(src)
    return ('<div class="relative mt-8 max-w-4xl mx-auto"><div class="absolute -inset-2 rounded-2xl opacity-40" '
            'style="background:radial-gradient(ellipse at center,var(--color-accent-glow) 0%,transparent 70%);filter:blur(24px);"></div>'
            '<div class="relative aspect-video rounded-2xl overflow-hidden" style="box-shadow:0 0 0 1px color-mix(in srgb,var(--color-accent) 20%,transparent),0 32px 64px rgba(0,0,0,0.5)">'
            f'<video data-vsl controls autoplay muted playsinline preload="auto" aria-label="{html.escape(label)}" class="absolute inset-0 w-full h-full" style="background:#000;">'
            f'<source src="/{s}" type="video/mp4"></video></div></div>')


def hero(page_name, label, h1a, h1b, subtitle=None, paragraph=None, eslogan=None, focus=None, bl=None,
         buttons=(), micro=None, vid=None, h1size='text-3xl md:text-5xl'):
    x = '<section class="relative flex flex-col items-center justify-center px-6 md:px-12 pt-28 md:pt-32 pb-16 overflow-hidden grid-bg">'
    x += ('<div class="glow-blob w-[600px] h-[600px] opacity-[0.07] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" style="background:var(--color-accent)"></div>'
          '<div class="w-full max-w-5xl mx-auto text-center space-y-6 relative z-10">')
    x += breadcrumb(page_name)
    x += f'<span class="pill-badge"><span class="pill-dot"></span>{E(label)}</span>'
    x += h1(h1a, h1b, h1size)
    if subtitle:
        x += f'<p class="text-lg md:text-xl text-white/90 font-medium max-w-3xl mx-auto leading-relaxed">{E(subtitle)}</p>'
    if paragraph:
        x += f'<p class="text-base md:text-lg text-on-surface-variant font-light max-w-3xl mx-auto leading-relaxed">{E(paragraph)}</p>'
    if eslogan:
        x += f'<p class="serif-italic text-2xl md:text-3xl font-semibold accent">{E(eslogan)}</p>'
    if focus:
        x += ('<div><p class="text-xs font-semibold tracking-widest uppercase text-on-surface-variant mb-3">Nos enfocamos en:</p>'
              + bullets(focus) + '</div>')
    if bl:
        x += bullets(bl)
    if buttons:
        x += btns(*buttons)
    if micro:
        x += f'<p class="text-xs text-on-surface-variant">{E(micro)}</p>'
    if vid:
        x += vid
    x += '</div></section>'
    return x


import re as _re
_ICON = _re.compile(r'<span class="([^"]*material-symbols-outlined[^"]*)"([^>]*)>([a-z0-9_]+)</span>')


def icons_to_attr(markup):
    """Pasa los nombres de ícono de texto a atributo (data-i) para que no se indexen como texto de la página."""
    return _ICON.sub(lambda m: f'<span class="{m.group(1)}"{m.group(2)} aria-hidden="true" data-i="{m.group(3)}"></span>', markup)


def write(name, content):
    (ROOT / name).write_text(icons_to_attr(content), encoding='utf-8', newline='\n')
    print('escrito', name, len(content) // 1024, 'KB')


def dual_cards(ic1, h1, t1, ic2, h2t, t2):
    def card(ic, h, t):
        return ('<div class="liquid-glass rounded-2xl p-7 md:p-8 relative overflow-hidden" style="box-shadow:0 8px 32px rgba(0,0,0,0.35),0 0 60px -30px var(--color-accent-glow)">'
                '<div class="absolute -top-16 -right-16 w-48 h-48 rounded-full pointer-events-none" style="background:radial-gradient(circle,var(--color-accent-glow) 0%,transparent 70%);opacity:.5"></div>'
                '<div class="relative"><span class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:color-mix(in srgb,var(--color-accent) 15%,transparent)">'
                f'<span class="material-symbols-outlined accent" style="font-size:26px">{ic}</span></span>' + h2(h) + p(t) + '</div></div>')
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-5">' + card(ic1, h1, t1) + card(ic2, h2t, t2) + '</div>'
