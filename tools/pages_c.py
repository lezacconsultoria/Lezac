"""Home. Copy literal de SEO/Home_Lezac_Copy_y_Estructura_para_Claude_Code.md (con los overrides del Plan Maestro)"""
from lib import *
from PIL import Image

STRIP = '10+ años de experiencia · 100+ empresas asesoradas · 4 países de LATAM'


def home():
    path = '/'
    title = 'Inteligencia comercial para pymes y distribuidoras | Lezac'
    desc = ('Lezac Consultoría ayuda a pymes, distribuidoras y mayoristas a vender más con sus datos, online y uno a uno. '
            '10+ años, 100+ empresas, 4 países.')
    faqs = [
        ('¿Qué es la inteligencia comercial?',
         'Es usar los datos de venta de tu empresa (clientes, productos, vendedores, rutas) para decidir mejor: a quién visitar, qué ofrecer y dónde ganás o perdés plata.'),
        ('¿Para qué empresas trabaja Lezac?',
         'Para pymes, distribuidoras y mayoristas de Argentina, Paraguay, Bolivia y Uruguay que venden a otros negocios y quieren ordenar y hacer crecer su gestión comercial.'),
        ('¿En qué se diferencia Lezac de una consultoría tradicional?',
         'Trabajamos con una metodología propia, uno a uno y sobre tus datos reales, no con recomendaciones genéricas. Ejecutamos y acompañamos en lugar de entregar un informe, y lo hacemos online, así que no importa dónde esté tu empresa.'),
        ('¿Cuánto cuesta trabajar con Lezac?',
         'Depende del servicio y del tamaño de tu empresa. Adaptamos el alcance y el presupuesto a cada caso, y podés empezar con algo chico, como el diagnóstico o una primera mejora en 15 días. En la primera charla te decimos qué encaja y qué inversión implicaría.'),
        ('¿Por dónde empiezo?',
         'Con una charla. Escuchamos cómo trabaja hoy tu equipo comercial y te recomendamos el servicio que mejor encaja. No hay contrato inicial.'),
        ('¿Desarrollan aplicaciones o herramientas a medida?',
         'Sí. Además de trabajar con las herramientas que ya usás, podemos desarrollar aplicaciones a medida según la necesidad de tu negocio, sean administrativas, logísticas o comerciales.'),
        ('¿En cuánto tiempo se ven resultados?',
         'Depende del servicio. IA a Medida entrega una primera mejora en 15 días, y +Clientes Activos es un proyecto de 2 meses con una proyección de +15% a +30% de clientes activos.'),
        ('¿Trabajan con empresas de otras ciudades o países?',
         'Sí. La mayoría de nuestros clientes trabaja de forma online, porque nuestros servicios se basan en el análisis de información. Acompañamos con la misma calidad a empresas de distintas provincias de Argentina y de Paraguay, Bolivia y Uruguay, sin que nadie tenga que viajar a tu negocio.'),
    ]
    org = {"@type": "Organization", "@id": SITE + "/#organization", "name": "Lezac Consultoría", "url": SITE + "/",
           "logo": LOGO,
           "description": "Consultora de inteligencia comercial para pymes, distribuidoras y mayoristas de Argentina, Paraguay, Bolivia y Uruguay. Trabaja online y uno a uno, con metodología propia.",
           "telephone": "+5491154107921", "areaServed": ["AR", "PY", "BO", "UY"],
           "knowsAbout": ["Consultoría de inteligencia comercial", "Inteligencia comercial", "Análisis de ventas", "Ruteo comercial",
                          "Censo comercial", "Inteligencia artificial aplicada a ventas", "Automatización de ventas por WhatsApp"],
           "sameAs": [LINKEDIN, INSTAGRAM]}
    ld = jsonld(org, website_min(), faq_ld(faqs))
    wa_home = wa('Hola, quiero consultar por los servicios de Lezac.')

    # ───── hero ─────
    focus = ''.join(check_li(t) for t in ['aumentar tus ventas', 'ampliar tu cobertura de clientes', 'mejorar tu rentabilidad', 'optimizar tus recursos'])
    vid_attrs = 'data-speed="1.5" autoplay muted loop playsinline preload="auto" aria-label="Tablero de inteligencia comercial de Lezac"'
    c = f'''<section class="relative min-h-screen flex items-center px-6 md:px-12 lg:px-20 pt-24 pb-12 overflow-hidden grid-bg">
<div class="glow-blob w-[700px] h-[700px] opacity-[0.07] top-1/2 left-1/3 -translate-x-1/2 -translate-y-1/2" style="background:var(--color-accent)"></div>
<div class="glow-blob w-[300px] h-[300px] opacity-10 top-16 right-16" style="background:#38BDF8"></div>
<div class="hidden lg:block absolute z-0" style="top:50%;right:-6rem;width:50%;transform:translateY(-50%);">
<div class="absolute -inset-10 rounded-3xl opacity-25 pointer-events-none" style="background:radial-gradient(ellipse at center,var(--color-accent-glow) 0%,transparent 70%);filter:blur(48px);"></div>
<video {vid_attrs} class="relative w-full h-auto rounded-2xl" style="box-shadow:0 0 100px -20px var(--color-accent-glow),0 40px 80px rgba(0,0,0,0.6);border:1px solid rgba(255,255,255,0.08);-webkit-mask-image:linear-gradient(to right,#000 55%,transparent 100%);mask-image:linear-gradient(to right,#000 55%,transparent 100%);"><source src="/bi-hero.mp4" type="video/mp4"></video>
</div>
<div class="w-full grid grid-cols-12 gap-8 lg:gap-16 items-start relative z-10">
<div class="col-span-12 lg:col-span-6 space-y-6 pb-12 pt-4">
<span class="pill-badge"><span class="pill-dot"></span>Inteligencia Comercial B2B · LATAM</span>
{h1('Consultoría de inteligencia comercial', 'para pymes, distribuidoras y mayoristas.', 'text-4xl md:text-5xl xl:text-[3.5rem]')}
<p class="text-base lg:text-lg text-on-surface-variant font-light max-w-xl leading-relaxed">Lezac Consultoría es una consultora de inteligencia comercial para pymes, distribuidoras y mayoristas. Trabajamos online y uno a uno, con tus propios datos, para corregir los procesos que te hacen perder tiempo o plata.</p>
<div><p class="text-xs font-semibold tracking-widest uppercase text-on-surface-variant mb-3">Nos enfocamos en:</p><ul class="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-2 max-w-xl">{focus}</ul></div>
<ul class="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-2 max-w-xl">{check_li('Online, estés donde estés')}{check_li('10+ años y 100+ empresas asesoradas')}</ul>
<div class="flex flex-col sm:flex-row gap-3 pt-1">{btn('Agendar una charla', CAL, 'primary', 'calendar_today')}{btn('Ver servicios', '#servicios', 'secondary')}</div>
<p class="text-xs text-on-surface-variant">Alcance y presupuesto a tu medida. Sin contrato inicial.</p>
</div>
<div class="block lg:hidden col-span-12 pb-8"><video {vid_attrs} class="w-full h-auto rounded-2xl" style="box-shadow:0 0 60px -10px var(--color-accent-glow);border:1px solid rgba(255,255,255,0.07);"><source src="/bi-hero.mp4" type="video/mp4"></video></div>
</div>
</section>'''

    c += prueba('Empresas que confían en Lezac', STRIP)

    # ───── qué hacemos ─────
    def card(color, icon, name, sub, text, label, href, span):
        e = ' target="_blank" rel="noopener"' if ext(href) else ''
        subh = f'<span class="text-[11px] font-bold uppercase tracking-widest block mb-2" style="color:{color}">{E(sub)}</span>' if sub else ''
        return (f'<a href="{href}"{e} class="service-card liquid-glass rounded-2xl p-8 group flex flex-col justify-between {span}" style="min-height:300px;--card-accent:{color}">'
                f'<div><div class="flex items-start justify-between mb-5"><div>{subh}<h3 class="text-2xl font-black text-white leading-tight">{E(name)}</h3></div>'
                f'<div class="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0" style="background:color-mix(in srgb,{color} 12%,transparent)"><span class="material-symbols-outlined" style="color:{color};font-size:22px">{icon}</span></div></div>'
                f'<p class="text-on-surface-variant text-sm leading-relaxed">{E(text)}</p></div>'
                f'<span class="text-xs font-bold uppercase tracking-widest flex items-center gap-2 mt-6" style="color:{color}">{E(label)} <span class="material-symbols-outlined" style="font-size:16px">arrow_forward</span></span></a>')
    s3, s32 = 'lg:col-span-2', 'md:col-span-1 lg:col-span-3'
    cards = (
        card('#F97316', 'query_stats', 'Diagnóstico Comercial', None, 'El punto de partida. Un análisis online de cómo vende hoy tu empresa y dónde se te escapa plata. Te llevás prioridades claras para actuar.', 'Hacer el diagnóstico', 'https://diagnostico.lezacconsultoria.com/', s3) +
        card('#25F5A4', 'explore', 'Brújula Comercial', 'consultoría de inteligencia comercial · acompañamiento mensual', 'Convertimos tus datos de venta en decisiones sobre clientes, productos, vendedores y rentabilidad. Sabés qué pasa en tu negocio todos los meses, no una vez al año.', 'Conocer Brújula Comercial', '/consultoria-inteligencia-comercial', s3) +
        card('#38BDF8', 'map', '+Clientes Activos', 'proyecto de 2 meses', 'Más clientes, más ventas. Geolocalizamos tu base, censamos puntos de venta y rediseñamos las rutas de tu equipo. Proyección: entre +15% y +30% de clientes activos en 60 días.', 'Conocer +Clientes Activos', '/mas-clientes-activos', s3) +
        card('#8C52FF', 'auto_awesome', 'IA a Medida', 'primera mejora en 15 días', 'Resolvemos lo que tu empresa necesita. Bots de WhatsApp, herramientas internas, automatizaciones y desarrollos a medida, con inteligencia artificial cuando aporta valor. Primera mejora en 15 días.', 'Conocer IA a Medida', '/ia-a-medida', s32) +
        card('#25D366', 'chat_bubble', 'WA Ventas', None, 'Ordenamos y automatizamos pedidos y consultas de clientes por WhatsApp, para que ningún mensaje quede sin respuesta.', 'Conocer WA Ventas', '/wa-ventas', s32 + ' md:col-span-2'))
    c += section(f'<div class="max-w-2xl mb-12">{h2("Qué hacemos")}{p("Cinco servicios para distintos momentos de tu empresa. Elegís uno o los combinás, y todos se adaptan a tu tamaño y presupuesto.")}</div>'
                 f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-6">{cards}</div>'
                 '<p class="mt-6 text-xs text-on-surface-variant">La proyección no es un resultado garantizado.</p>', sid='servicios', width='max-w-7xl')

    # ───── cómo trabajamos ─────
    c += section(h2('Cómo trabajamos: una metodología propia') +
                 p('Trabajamos con una metodología propia, aplicada en más de 100 empresas, y siempre uno a uno: un consultor que conoce tu negocio y analiza tus datos.') +
                 '<div class="mt-6"></div>' + steps([
        ('Escuchamos.', 'Entendemos tu negocio, tu equipo y qué querés lograr.'),
        ('Analizamos tus datos.', 'Revisamos ventas, clientes, productos y rutas para encontrar dónde se pierde tiempo o plata.'),
        ('Proponemos y ejecutamos.', 'Armamos un plan priorizado, a tu medida y a tu presupuesto, y lo implementamos con vos. Si hace falta, desarrollamos la herramienta que tu proceso necesita.'),
        ('Medimos y acompañamos.', 'Definimos indicadores claros y seguimos de cerca hasta que funcione.'),
    ]), bg='dim', width='max-w-4xl')

    # ───── por qué es distinto ─────
    c += section(h2('¿Probaste con una consultoría y no te dio resultados?') +
                 p('Es más común de lo que parece. Estas son las razones habituales y cómo las resolvemos.') +
                 '<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-5">' + ''.join(
                     f'<div class="liquid-glass rounded-2xl p-6"><h3 class="text-lg font-black text-white mb-2">{E(q)}</h3><p class="text-sm text-on-surface-variant leading-relaxed">{E(a)}</p></div>' for q, a in [
                         ('Te entregaron un informe y quedó en un cajón.', 'Nosotros ejecutamos y acompañamos. No entregamos un documento y nos vamos.'),
                         ('Recomendaciones genéricas, pensadas para otra empresa.', 'Todo sale de tus datos reales y se adapta a tu negocio.'),
                         ('Pagaste mucho y no viste el retorno.', 'Adaptamos el alcance y el presupuesto a tu empresa. Empezás con algo chico y crecés a medida que ves resultados.'),
                         ('El consultor desapareció después de la entrega.', 'Trabajamos uno a uno, con seguimiento continuo y soporte directo cuando lo necesites.')]) + '</div>'
                 '<p class="mt-8 text-white font-semibold">Por eso trabajamos con una metodología propia y con tus datos, ya probada en más de 100 empresas.</p>'
                 '<div class="mt-6">' + btn('Contanos tu caso', CAL, 'primary') + '</div>')

    # ───── online ─────
    c += section(h2('Consultoría online: a un clic de distancia') +
                 p('La mayoría de nuestros clientes trabaja con nosotros de forma online. Como nuestros servicios se basan en el análisis de información, la distancia deja de ser un límite: estés en Buenos Aires, en el interior del país, en Asunción, Santa Cruz o Montevideo, recibís el mismo servicio profesional y de alto valor, con reuniones por videollamada uno a uno, soporte por WhatsApp y sin que nadie tenga que viajar a tu negocio.') +
                 '<p class="mt-5 text-white font-semibold leading-relaxed">Si tu empresa necesita una consultoría de calidad y especialidad, no importa dónde estés: estamos a un clic.</p>'
                 '<div class="mt-8">' + btns(btn('Agendar una charla', CAL, 'primary', 'calendar_today'), btn('Escribinos por WhatsApp', wa_home, 'secondary', 'chat')).replace('justify-center', 'justify-start') + '</div>', bg='dim')

    # ───── accesibilidad ─────
    c += section(h2('Trabajamos a tu medida, también en presupuesto') +
                 p('No hay un paquete único. Trabajamos con pymes, distribuidoras y mayoristas de distintos tamaños, y por eso adaptamos el alcance, los tiempos y la inversión a la etapa de cada empresa. Podés empezar con algo chico, como un diagnóstico o una primera mejora en 15 días, y crecer a medida que ves resultados.') +
                 '<div class="mt-8">' + btn('Contanos tu caso', CAL, 'primary') + '</div>')

    # ───── testimonios ─────
    stars = '<div class="flex gap-1 mb-5">' + '<span class="material-symbols-outlined text-yellow-400" style="font-size:16px;font-variation-settings:\'FILL\' 1,\'wght\' 400,\'GRAD\' 0,\'opsz\' 20" aria-hidden="true">star</span>' * 5 + '</div>'

    def testi(q, n, co, ini):
        return (f'<figure class="liquid-glass rounded-2xl p-7 flex flex-col justify-between">{stars}<blockquote class="text-white/85 text-sm leading-relaxed italic mb-6">"{E(q)}"</blockquote>'
                f'<figcaption class="flex items-center gap-3 pt-5 border-t border-white/5"><div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0 accent" style="background:rgba(140,82,255,.2)" aria-hidden="true">{ini}</div>'
                f'<div><p class="text-white text-sm font-bold">{E(n)}</p><p class="text-on-surface-variant text-xs">{E(co)}</p></div></figcaption></figure>')
    c += section(h2('Lo que dicen las empresas con las que trabajamos', center=True) +
                 '<div class="grid grid-cols-1 md:grid-cols-2 gap-5 max-w-3xl mx-auto">' +
                 testi('Lezac transformó nuestra visión comercial. En una sola sesión identificamos oportunidades de rentabilidad que no habíamos visto en años.', 'Mariano', 'Madersa', 'MA') +
                 testi('Teníamos vendedores pisando las mismas zonas sin saberlo. Con el censo y el ruteo de Lezac reorganizamos todo el territorio y empezamos a crecer de verdad.', 'Gabriel', 'Weilen', 'GA') +
                 '</div>', bg='dim')

    # ───── para quién ─────
    c += section(h2('Para quién trabajamos') +
                 p('Pymes, distribuidoras y mayoristas con equipo de ventas propio (preventistas, viajantes o vendedores de ruta) que quieren vender más y gastar mejor, en cualquier punto de Argentina, Paraguay, Bolivia y Uruguay.') +
                 '<ul class="mt-8 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">' + ''.join(
                     f'<li class="liquid-glass rounded-xl p-5"><p class="text-white font-bold mb-1">{E(pais)}</p><p class="text-sm text-on-surface-variant">{E(ciu)}</p></li>' for pais, ciu in [
                         ('Argentina', 'Buenos Aires, Córdoba, Rosario'), ('Paraguay', 'Asunción'), ('Bolivia', 'Santa Cruz'), ('Uruguay', 'Montevideo')]) + '</ul>')

    # ───── herramientas ─────
    tools = [('Odoo', 'odo-300x167.png'), ('SAP Business One', 'sap-300x100.png'), ('Power BI', '1200px-Power_bi_logo_black.svg_-300x300.png'),
             ('Power Automate', 'auto-300x300.png'), ('Shopify', 'shopi-300x169.png'), ('n8n', 'n8n-color.png'),
             ('Contabilium', 'logo_contabilium.png'), ('Meta', 'Meta_logo.png'), ('Hostinger', 'Hostinger_Logo.png')]
    imgs = ''
    for nm, f in tools:
        w, h = Image.open(ROOT / 'logos-trabajo' / f).size
        imgs += (f'<img src="/logos-trabajo/{f}" alt="{nm}" width="{w}" height="{h}" loading="lazy" '
                 'style="height:40px;width:auto;max-width:120px;object-fit:contain;filter:brightness(0) invert(1);opacity:.55;">')
    c += section(h2('Trabajamos sobre las herramientas que ya usás', center=True) +
                 f'<div class="flex flex-wrap items-center justify-center gap-x-12 gap-y-8">{imgs}</div>', width='max-w-5xl')

    c += faq_section(faqs)

    # ───── partners ─────
    c += ('<section class="py-20 px-6 md:px-12 relative overflow-hidden" style="background:#050506"><div class="max-w-3xl mx-auto text-center lezac-reveal">'
          '<p class="text-sm text-on-surface-variant mb-4">¿Conocés una empresa que necesita esto?</p>'
          '<h2 class="text-3xl md:text-4xl font-black text-white mb-6">Conocé el programa de <span style="color:#F5C842">Partners →</span></h2>'
          '<p class="text-on-surface-variant mb-8 max-w-xl mx-auto text-sm leading-relaxed">Recomendás la empresa, nosotros hacemos el trabajo, y vos cobrás una comisión cuando el proyecto se concreta.</p>'
          '<a href="/partner" class="inline-flex items-center gap-2 px-8 py-4 rounded-full font-bold text-sm transition-all hover:brightness-110" style="background:#F5C842;color:#0A0A0B">Conocer el programa</a></div></section>')

    c += cta_final('Contanos cómo trabaja hoy tu equipo comercial',
                   'En una charla online vemos si podemos ayudarte y qué alcance tendría, a tu medida y a tu presupuesto. Sin contrato inicial.',
                   [btn('Agendar una charla', CAL, 'primary', 'calendar_today'), btn('Escribinos por WhatsApp', WA, 'secondary', 'chat')], PHONE)

    css = '.service-card{transition:transform .35s cubic-bezier(.34,1.56,.64,1),box-shadow .35s ease,border-color .35s ease;}.service-card:hover{transform:translateY(-6px);box-shadow:0 18px 48px -12px color-mix(in srgb,var(--card-accent) 45%,transparent);border-color:color-mix(in srgb,var(--card-accent) 60%,transparent)!important;}'
    js = """
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('video[data-speed]').forEach(v => {
    const r = parseFloat(v.dataset.speed) || 1;
    const set = () => { v.playbackRate = r; };
    set(); v.addEventListener('loadedmetadata', set); v.addEventListener('play', set);
  });
});
"""
    write('index.html', shell('home', title, desc, path, ld, c, extra_css=css, extra_js=js))
