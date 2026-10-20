"""Consultoría de inteligencia comercial (Brújula) y +Clientes Activos. Copy literal de SEO/*.md"""
from lib import *

STRIP = '10+ años de experiencia · 100+ empresas asesoradas · 4 países de LATAM'


def brujula():
    name, path = 'Consultoría de inteligencia comercial', '/consultoria-inteligencia-comercial'
    title = 'Consultoría de inteligencia comercial online | Brújula Comercial'
    desc = ('Consultoría de inteligencia comercial online para pymes, distribuidoras y mayoristas de Argentina, '
            'Paraguay, Bolivia y Uruguay. Más ventas y mejor rentabilidad.')
    faqs = [
        ('¿Qué es la consultoría de inteligencia comercial?',
         'Es un servicio donde un consultor analiza los datos de venta de tu empresa (clientes, productos, vendedores) y te acompaña a decidir mejor: a quién visitar, qué ofrecer y dónde ganás o perdés plata.'),
        ('¿Qué es Brújula Comercial? ¿Es un software?',
         'Brújula Comercial es el método de trabajo de Lezac Consultoría. Combina consultoría uno a uno con una plataforma propia de inteligencia comercial. Es una consultoría: un tablero solo te muestra números, nosotros te explicamos qué significan y qué hacer.'),
        ('¿Qué datos necesito y qué pasa si están desordenados o ya tengo un sistema?',
         'Tu historial de ventas, tu base de clientes y tu listado de productos, en Excel o desde tu sistema (Odoo, SAP Business One u otro). Si están desordenados, ordenarlos es parte del trabajo.'),
        ('¿Qué reportes y reuniones incluye?',
         'Datos actualizados a diario, un reporte cada lunes con cómo viene la semana, un reporte al cierre de cada mes con puntos de mejora y una reunión cada 15 días, con llamadas cuando lo necesites.'),
        ('¿Ayudan a definir objetivos y pago variable para los vendedores?',
         'Sí. Te ayudamos a armar los objetivos de venta y un esquema de pago variable, con buenas prácticas de empresas grandes adaptadas a tu negocio.'),
        ('¿Cuánto cuesta y cuánto tiempo tengo que comprometerme?',
         'Es un abono mensual que adaptamos al tamaño, la necesidad y el presupuesto de tu empresa. Es mes a mes, sin permanencia obligatoria. En la primera charla te contamos el alcance y la inversión.'),
        ('¿Trabajan con empresas de otras ciudades o países?',
         'Sí. Trabajamos online con tus datos, por eso acompañamos a empresas de distintas provincias de Argentina y de Paraguay, Bolivia y Uruguay con la misma calidad, sin necesidad de que un consultor viaje a tu negocio.'),
        ('¿Qué garantía tienen?',
         'En los primeros 15 a 20 días hábiles identificamos, sobre tus últimos 12 meses de ventas, al menos 5 mejoras concretas y las ponemos en marcha. Si no las encontramos, podés dejar de trabajar con nosotros sin compromiso. Para eso necesitamos contar con la información que el análisis requiere.'),
    ]
    service = {
        "@type": "Service", "@id": SITE + path + "#service",
        "name": "Consultoría de inteligencia comercial (método Brújula Comercial)",
        "serviceType": "Consultoría de inteligencia comercial",
        "description": "Consultoría online uno a uno que analiza los datos de venta de pymes, distribuidoras, mayoristas y fábricas con una plataforma propia, para aumentar ventas, ampliar la cobertura de clientes y optimizar la rentabilidad.",
        "provider": org_min(), "areaServed": ["AR", "PY", "BO", "UY"],
        "audience": {"@type": "BusinessAudience", "audienceType": "Pymes, distribuidoras, mayoristas y fábricas"},
        "url": SITE + path}
    ld = jsonld(org_min(), service, faq_ld(faqs), breadcrumb_ld(name, path))

    wa_msg = wa('Hola, quiero consultar por la consultoría de inteligencia comercial.')
    c = hero(name, 'Consultoría de inteligencia comercial online · Método Brújula Comercial',
             'Consultoría de inteligencia comercial, uno a uno,', 'sobre tus propios datos de venta.',
             subtitle='Con nuestro método Brújula Comercial, sabés qué clientes, productos y vendedores te hacen ganar (o perder) plata.',
             paragraph='Brújula Comercial es el método de Lezac Consultoría para aplicar inteligencia comercial en pymes, distribuidoras, mayoristas y fábricas. Un consultor trabaja uno a uno con tu empresa, de forma online y sobre una plataforma propia de datos, para aumentar tus ventas, ampliar tu cobertura de clientes y optimizar tu rentabilidad.',
             focus=['aumentar tus ventas', 'ampliar tu cobertura de clientes', 'optimizar tu rentabilidad'],
             bl=['Online, estés donde estés', 'Auditoría inicial de tus últimos 12 meses', 'Mes a mes, sin permanencia obligatoria'],
             buttons=[btn('Agendar una charla', CAL, 'primary', 'calendar_today'), btn('Ver cómo aplica a mi empresa', wa_msg, 'secondary')],
             micro='Sin contrato inicial. Alcance y abono a tu medida.',
             vid=video('Web VSL I Brújula Comercial.mp4', 'Brújula Comercial: presentación del método'))

    c += prueba('Empresas que confían en Lezac', STRIP)

    c += section(h2('¿Te pasa alguna de estas cosas?') + item_cards([
        ('Clientes que dejaron de comprar y nadie te avisó.', 'Los notás meses después, cuando ya es tarde para recuperarlos.'),
        ('No tenés claridad de cómo trabaja cada vendedor.', 'Sabés cuánto vende cada uno, pero no cómo, ni a quién.'),
        ('Dependés de uno o dos vendedores.', 'Si se van, se llevan la base de clientes.'),
        ('Tus vendedores no tienen objetivos claros ni un pago variable que los empuje.', 'Cada uno trabaja a su manera.'),
        ('Vendés mucho, pero no sabés qué te deja margen.', 'La facturación sube y la ganancia no acompaña.'),
        ('Decidís por intuición.', 'Con planillas que nadie actualiza o reportes que llegan tarde.'),
        ('Tenés datos, pero empezás cada semana sin saber qué priorizar.', None),
    ]) + '<div class="mt-8 text-center">' + btn('Ver cómo aplica a mi empresa', wa_msg, 'primary') + '</div>', bg='dim')

    c += section(h2('Consultoría de inteligencia comercial, no una consultora más') +
                 '<p class="text-on-surface-variant leading-relaxed">Trabajamos uno a uno con tu empresa: nos adaptamos a tu información, tu equipo y tu forma de vender. A diferencia de una consultoría tradicional, sumamos una <strong class="text-white">plataforma propia de inteligencia comercial</strong> y una <strong class="text-white">metodología de trabajo</strong> validada en distintas empresas, con buenas prácticas de compañías grandes adaptadas a tu realidad. Nuestro foco es lo comercial y, cuando hace falta, también la logística, porque venta y logística van de la mano.</p>'
                 '<blockquote class="mt-8 border-l-2 pl-6 py-1 italic text-lg text-white/80 leading-relaxed" style="border-color:var(--color-accent)">"El tablero te muestra números. Brújula Comercial te dice qué hacer con ellos esta semana."</blockquote>')

    c += section(h2('Consultoría online: la distancia no es un límite') +
                 p('Como trabajamos con tus datos, el servicio se hace de forma online. Por eso acompañamos con la misma calidad a empresas de distintas provincias de Argentina y de Paraguay, Bolivia y Uruguay, sin que un consultor tenga que viajar a tu negocio. Reuniones por videollamada, soporte por WhatsApp y una plataforma disponible todos los días, estés donde estés.'), bg='dim')

    def group(title, items):
        return ('<div class="liquid-glass rounded-2xl p-6"><h3 class="text-lg font-black text-white mb-4">' + E(title) + '</h3><ul class="space-y-2.5">' +
                ''.join(check_li(i).replace('items-center', 'items-start', 1) for i in items) + '</ul></div>')
    shots = ''
    for n, (f, alt, w, h) in enumerate([
            ('captura1.png', 'Visión general: ventas, clientes y evolución mensual', 2484, 1265),
            ('captura2.png', 'Vendedores: rubros, marcas y clientes que más aportan', 2474, 1255),
            ('captura3.png', 'Objetivos por vendedor: cumplimiento de ventas, clientes y productos', 2469, 1253)]):
        shots += (f'<div class="rs-slide" data-i="{n}"><img src="/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy" '
                  f'class="w-full h-auto float-shot" data-f="{n}" style="border:1px solid rgba(255,255,255,0.1);" /></div>')
    c += section(h2('Qué incluye') +
                 '<div class="grid grid-cols-1 md:grid-cols-3 gap-5">' +
                 group('Información', ['Plataforma propia de inteligencia comercial, adaptada a tu empresa', 'Datos actualizados todos los días', 'Un reporte cada lunes: cómo viene la semana y qué priorizar', 'Un reporte al cierre de cada mes, con puntos de mejora para el mes siguiente']) +
                 group('Acompañamiento', ['Un consultor que trabaja con vos, uno a uno', 'Reunión cada 15 días, y llamada cuando la necesites', 'Soporte directo por WhatsApp']) +
                 group('Tu equipo de ventas', ['Accesos para gerencia y para vendedores', 'Objetivos de venta por vendedor', 'Esquema de pago variable, con buenas prácticas adaptadas a tu negocio']) +
                 '</div>'
                 f'<div id="rs-carousel" class="rs-wrap flex flex-col gap-6 mt-14" aria-roledescription="carrusel">{shots}</div>'
                 '<p class="mt-8 text-center text-sm text-white/80">Visión general · Vendedores · Objetivos por vendedor</p>'
                 '<p class="text-center text-xs text-on-surface-variant italic mt-1">Imágenes ilustrativas con datos de ejemplo.</p>'
                 '<div class="mt-8 text-center">' + btn('Agendar una charla', CAL, 'primary', 'calendar_today') + '</div>', width='max-w-6xl')

    c += section(h2('Cómo empezamos') + steps([
        ('Una charla.', 'Escuchamos tu caso y vemos si encaja con tu empresa. Solo necesitás tu historial de ventas, tu base de clientes y tu listado de productos.'),
        ('Una auditoría de tus últimos 12 meses.', Raw('Analizamos cómo venís hoy y, en los primeros 15 a 20 días hábiles, identificamos y ponemos en marcha al menos 5 mejoras concretas. <strong class="text-white">Esa es nuestra garantía:</strong> si no las encontramos, podés dejar de trabajar con nosotros sin compromiso. Para eso necesitamos contar con la información que el análisis requiere.')),
        ('Acompañamiento mes a mes.', 'Ponemos en marcha tu plataforma y trabajamos con vos para convertir lo que ves en resultados.'),
    ]), bg='dim', width='max-w-4xl')

    c += section(h2('No es una consultora tradicional ni un BI más') + table(
        ['Una consultora tradicional o un BI', 'Brújula Comercial'],
        [['Informes o herramientas sueltas', 'Plataforma propia, metodología y un consultor'],
         ['Recomendaciones genéricas', 'Todo sale de tus datos reales'],
         ['Entregan y se van', 'Te acompañan cada semana y cada mes'],
         ['Requieren estar en tu negocio', 'Trabajamos online con tus datos, estés donde estés']]), width='max-w-4xl')

    c += section(h2('Para pymes, distribuidoras, mayoristas y fábricas') +
                 '<p class="text-on-surface-variant leading-relaxed mb-10">Para dueños, CEOs y gerentes comerciales de empresas con equipo de ventas propio que quieren decidir con datos y no por intuición, en cualquier punto de Argentina, Paraguay, Bolivia y Uruguay. <em>No es para emprendimientos que recién empiezan ni para empresas que venden servicios profesionales.</em></p>' +
                 h2('Un abono a tu medida') +
                 p('No hay un paquete único. Nos adaptamos al tamaño, la necesidad y el presupuesto de cada empresa, sobre una metodología ya probada en distintos tipos de negocio. Funciona con un abono mensual, mes a mes y sin permanencia obligatoria, y podés empezar solo con la auditoría para decidir después cómo seguir.') +
                 '<div class="mt-8">' + btn('Contanos tu caso', CAL, 'primary') + '</div>', bg='dim')

    c += section(h2('Así se ve en una empresa real') + '<div class="grid grid-cols-1 md:grid-cols-2 gap-5">' +
                 '<div class="liquid-glass rounded-2xl p-7"><h3 class="text-lg font-black text-white mb-3">Distribuidora del sur del país, más de 1.500 productos.</h3><p class="text-sm text-on-surface-variant leading-relaxed">Descubrió qué productos sostenían su rentabilidad por zona y por vendedor, y qué clientes había dejado de atender.</p></div>'
                 '<div class="liquid-glass rounded-2xl p-7"><h3 class="text-lg font-black text-white mb-3">Empresa de materiales de construcción, Entre Ríos.</h3><p class="text-sm text-on-surface-variant leading-relaxed">Anticipó faltantes en los productos clave y detectó sobrestock antes de que afectara su caja.</p></div></div>')

    c += faq_section(faqs)
    c += cta_final('Mirá cómo se vería Brújula Comercial con los datos de tu empresa',
                   'En una charla online escuchamos cómo trabaja hoy tu equipo comercial y te contamos si encaja y qué alcance tendría. Sin contrato inicial.',
                   [btn('Agendar una charla', CAL, 'primary', 'calendar_today'), btn('Escribinos por WhatsApp', wa_msg, 'secondary', 'chat')],
                   PHONE)
    write('consultoria-inteligencia-comercial.html', shell('brujula', title, desc, path, ld, c, extra_css=CAROUSEL_CSS, extra_js=CAROUSEL_JS))


def clientes():
    name, path = '+Clientes Activos', '/mas-clientes-activos'
    title = 'Geolocalización, censo y ruteo comercial | +Clientes Activos'
    desc = ('Recuperamos clientes dormidos y sumamos puntos de venta sin atender. Geolocalización, censo y ruteo '
            'comercial para distribuidoras y mayoristas. 100% online.')
    faqs = [
        ('¿Qué es +Clientes Activos?',
         '+Clientes Activos es el método de Lezac Consultoría para que distribuidoras, mayoristas y fábricas vendan más ampliando la cantidad de clientes que realmente compran. Geolocalizamos tu base, censamos los puntos de venta de tu zona de influencia y rediseñamos las rutas de tu equipo. Se trabaja uno a uno y 100% online.'),
        ('¿Cuánto tarda en dar resultados?',
         'El proyecto dura alrededor de 2 meses. Nuestra proyección es de entre +15% y +30% de clientes activos en ese plazo, en las empresas donde aplicamos el método. La meta de tu proyecto la definimos juntos, a partir de la base real de tu empresa.'),
        ('¿Qué diferencia hay con un software de rutas?',
         'Un software de rutas ordena las visitas que ya hacés. +Clientes Activos encuentra los clientes que no estás visitando: recupera los que dejaron de comprar y suma puntos de venta sin atender. Además, lo implementa un consultor con vos, en lugar de dejarte la configuración a tu cargo.'),
        ('¿Cómo se cobra?',
         'Cobramos por punto de venta censado, con un pago único que se ajusta al rubro de tu empresa, a su actividad y a la amplitud de zona que quieras desarrollar. Escribinos y lo vemos en una conversación.'),
        ('¿Funciona para fábricas y mayoristas, o solo para distribuidoras?',
         'Funciona para distribuidoras, mayoristas y fábricas que venden a través de una red de vendedores o de reparto. Lo que cambia es el foco: en algunas empresas pesa más reactivar clientes inactivos y en otras, ampliar la cobertura en zonas nuevas.'),
        ('¿Necesito cambiar mi sistema de gestión?',
         'No. Trabajamos con los datos de venta que ya tenés, sea cual sea el sistema que uses. Si hace falta una herramienta a medida, ya sea administrativa, logística o comercial, también podemos desarrollarla.'),
        ('¿Se puede hacer 100% online?',
         'Sí. La mayoría de nuestros clientes trabaja con nosotros de forma online: reuniones por videollamada, seguimiento por WhatsApp y un panel con los avances. La distancia no es una limitación en Argentina, Paraguay, Bolivia ni Uruguay.'),
        ('¿Qué pasa si mi base tiene menos de 300 clientes?',
         'Lo ideal es contar con una base de unos 300 clientes o más para que el análisis tenga volumen. Si tenés menos, escribinos y vemos si el proyecto se adapta a tu caso.'),
        ('¿Cuánto tiempo me demanda a mí y a mi equipo?',
         'Poco. Tenés una reunión cada 15 días con tu consultor y seguimiento por WhatsApp. Lo único que necesitamos de tu parte es la información de tu base de clientes; el análisis, el mapa, el censo y las rutas los hacemos nosotros.'),
        ('¿Qué compromiso tienen con los plazos?',
         'Acordamos los plazos desde el inicio. Si no cumplimos con el censo inicial, esa etapa no se cobra. Para eso necesitamos contar con la información de tu base de clientes en tiempo y forma.'),
    ]
    service = {
        "@type": "Service", "@id": SITE + path + "#service",
        "name": "+Clientes Activos: geolocalización, censo y ruteo comercial",
        "serviceType": "Consultoría de cobertura de clientes, geolocalización y ruteo comercial",
        "description": "Servicio online uno a uno para distribuidoras, mayoristas y fábricas que geolocaliza la base de clientes, censa los puntos de venta de la zona de influencia y rediseña las rutas comerciales para aumentar la cantidad de clientes activos.",
        "provider": org_min(), "areaServed": ["AR", "PY", "BO", "UY"],
        "audience": {"@type": "BusinessAudience", "audienceType": "Distribuidoras, mayoristas y fábricas"},
        "url": SITE + path}
    ld = jsonld(org_min(), service, faq_ld(faqs), breadcrumb_ld(name, path))
    wa_pv = wa('Hola, quiero consultar por +Clientes Activos. Mi empresa tiene aproximadamente ___ puntos de venta.')
    ask = 'Contanos cuántos puntos de venta tiene tu empresa'

    c = hero(name, 'Consultoría comercial · Cobertura de clientes · Método +Clientes Activos',
             'Más clientes activos para tu empresa,', 'con geolocalización, censo y ruteo comercial.',
             paragraph='Recuperamos a los clientes que dejaron de comprarte, sumamos puntos de venta que hoy nadie atiende y rediseñamos las rutas de tu equipo. +Clientes Activos es el método de Lezac Consultoría para distribuidoras, mayoristas y fábricas: en 2 meses, con un consultor trabajando uno a uno con tu empresa y sin quitarte tiempo. Proyección: entre +15% y +30% de clientes activos en 60 días.',
             eslogan='Más clientes, más ventas.',
             bl=['100% online', 'Trabajo uno a uno', 'Sin contrato inicial', 'Pago único según la cantidad de puntos de venta'],
             buttons=[btn(ask, wa_pv, 'primary', 'chat'), btn('Ver cómo funciona', '#como-funciona', 'secondary')],
             vid=video('Web VSL I Mas Clientes Activos.mp4', '+Clientes Activos: presentación del método'))
    c += prueba('Más de 100 empresas asesoradas en 4 países', '10+ años · 100+ empresas asesoradas · Argentina, Paraguay, Bolivia y Uruguay')

    c += section(h2('¿Te suena alguna de estas situaciones?') + item_cards([
        ('Clientes que compraban y dejaron de comprar.', 'Nadie los llamó, nadie los visitó. Pasaron meses y ya se los dieron por perdidos.'),
        ('Salís a buscar clientes nuevos mientras los tuyos están dormidos.', 'Es más caro y más lento que reactivar a los que ya te conocen.'),
        ('Tus vendedores visitan por costumbre, no por estrategia.', 'Recorren los mismos lugares que hace años, sin saber qué zonas tienen potencial.'),
        ('Tomar pedidos no es vender.', 'Tu equipo atiende al que llama y descuida al que podría comprar más.'),
        ('No sabés cuántos puntos de venta hay en tu zona.', 'Ni cuántos te compran y cuántos le compran a la competencia.'),
        ('Se va un vendedor y se cae la venta de su zona.', 'Los clientes eran de él, no de la empresa.'),
        ('Las ventas se estancaron y cada visita cuesta más.', 'Más combustible, más horas, mismos resultados.'),
    ]) + '<div class="mt-8 rounded-2xl p-6 text-center max-w-3xl mx-auto" style="background:color-mix(in srgb,var(--color-accent) 8%,transparent);border:1px solid color-mix(in srgb,var(--color-accent) 25%,transparent)"><p class="text-white leading-relaxed">En la mayoría de las empresas con las que trabajamos, entre el 30% y el 60% de la base de clientes está inactiva.</p></div>' +
                 closing('Si te pasa algo de esto, no tenés un problema de vendedores. Tenés un problema de cobertura.').replace('mt-8 ','mt-8 text-center ',1), bg='dim')

    c += section(h2('Un método en 3 pasos para sumar clientes que realmente te compran') + steps([
        ('Geolocalizamos tu base.', 'Ubicamos en el mapa a todos tus clientes y vemos quién compra, quién bajó y quién dejó de comprar.'),
        ('Censamos tu zona.', 'Identificamos los puntos de venta que hoy no atendés dentro de tu zona de influencia.'),
        ('Rediseñamos tus rutas.', 'Reordenamos las visitas de tu equipo para llegar a más clientes con el mismo esfuerzo.'),
    ]) + '<p class="mt-6 text-sm text-on-surface-variant">Compromiso de entrega: acordamos los plazos desde el inicio y, si no cumplimos con el censo inicial, esa etapa no se cobra.</p>',
        sid='como-funciona', width='max-w-4xl')

    c += section(h2('Lo que buscamos lograr') +
                 p('Nuestra proyección es de entre +15% y +30% de clientes activos en 60 días, en las empresas donde aplicamos el método. El objetivo de tu proyecto lo definimos juntos, a partir de la base real de tu empresa.') +
                 '<div class="grid grid-cols-1 md:grid-cols-2 gap-5 mt-8">'
                 '<div class="liquid-glass rounded-2xl p-7"><h3 class="text-lg font-black text-white mb-3">Distribuidora de la provincia de Buenos Aires</h3><p class="text-sm text-on-surface-variant leading-relaxed mb-3">Necesitaba más clientes. Al analizar su base de ventas, solo el 35% de sus clientes había comprado en el último año. Enfocamos el trabajo en reactivar a los clientes inactivos.</p><p class="text-sm text-white leading-relaxed"><strong>Resultado:</strong> más de 15% de clientes activos. Después, el equipo continuó con la metodología por su cuenta.</p></div>'
                 '<div class="liquid-glass rounded-2xl p-7"><h3 class="text-lg font-black text-white mb-3">Empresa de la provincia de Santa Fe</h3><p class="text-sm text-on-surface-variant leading-relaxed mb-3">Además de reactivar clientes, buscamos nuevos clientes potenciales en su zona de influencia.</p><p class="text-sm text-white leading-relaxed"><strong>Resultado:</strong> +25% de cobertura de clientes con compra, mejor capilaridad, una fuerza de venta más productiva y menor costo de entrega en la logística.</p></div></div>', bg='dim')

    c += section(h2('Qué incluye +Clientes Activos') + '<ul class="grid grid-cols-1 md:grid-cols-2 gap-3 md:[&>li:last-child:nth-child(odd)]:col-span-2 md:[&>li:last-child:nth-child(odd)]:w-[calc(50%-0.375rem)] md:[&>li:last-child:nth-child(odd)]:justify-self-center">' + ''.join(
        f'<li class="liquid-glass rounded-xl p-4 flex items-center gap-3 text-sm text-white/90"><span class="material-symbols-outlined accent" style="font-size:20px">{ic}</span>{E(t)}</li>' for ic, t in [
            ('map', 'Mapa geolocalizado de tus clientes'), ('fact_check', 'Censo digital de los puntos de venta de tu zona de influencia'),
            ('route', 'Rutas rediseñadas para tu equipo'), ('monitoring', 'Panel de seguimiento semanal'),
            ('groups', 'Reunión cada 15 días con tu consultor'), ('summarize', 'Informe de cierre en la semana 8'),
            ('menu_book', 'Manual de la metodología para que tu equipo continúe solo')]) + '</ul>')

    c += section(h2('Un servicio concreto, que no te ocupa tiempo') +
                 '<p class="text-on-surface-variant mb-8">Vos seguís vendiendo. Nosotros hacemos el trabajo pesado.</p>' + item_cards([
        ('Tu tiempo, cuidado.', 'Una reunión cada 15 días y seguimiento por WhatsApp. El análisis, el mapa, el censo y el rediseño de rutas los hacemos nosotros.'),
        ('Un servicio concreto.', 'Entregables definidos: mapa, censo, rutas, panel semanal, informe de cierre y manual. Sabés qué recibís y cuándo.'),
        ('Un consultor a tu lado.', 'Un consultor trabaja uno a uno con tu empresa de principio a fin.'),
        ('Experiencia en empresas como la tuya.', 'Más de 10 años y 100+ empresas asesoradas, de distintos rubros y tamaños, en Argentina, Paraguay, Bolivia y Uruguay.'),
        ('Sin cambiar tu forma de trabajar.', 'Usamos los datos que ya tenés, sin cambiar de sistema.'),
        ('Tu equipo queda preparado.', 'Te dejamos el manual de la metodología para que puedan continuar solos.'),
        ('Se adapta a tu presupuesto.', 'Pago único según la cantidad de puntos de venta y sin contrato inicial.'),
    ], cols='md:grid-cols-2'), bg='dim')

    c += section(h2('¿Por qué no alcanza con un software de rutas?') + table(
        ['Software de rutas', '+Clientes Activos'],
        [['Ordena las visitas que ya hacés', 'Encuentra los clientes que no estás visitando'],
         ['Optimiza lo que tenés', 'Amplía lo que tenés'],
         ['Lo configurás vos', 'Lo implementa un consultor con vos'],
         ['Tu equipo sigue decidiendo a ciegas', 'Decisiones con datos reales de tu zona']]), width='max-w-4xl')

    c += section('<div class="grid grid-cols-1 md:grid-cols-2 gap-5">' +
                 '<div class="liquid-glass rounded-2xl p-7 md:p-8 relative overflow-hidden" style="box-shadow:0 8px 32px rgba(0,0,0,0.35),0 0 60px -30px var(--color-accent-glow)"><div class="absolute -top-16 -right-16 w-48 h-48 rounded-full pointer-events-none" style="background:radial-gradient(circle,var(--color-accent-glow) 0%,transparent 70%);opacity:.5"></div><div class="relative"><span class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:color-mix(in srgb,var(--color-accent) 15%,transparent)"><span class="material-symbols-outlined accent" style="font-size:26px">groups</span></span>' + h2('Para quién es') + p('Distribuidoras, mayoristas y fábricas con red de vendedores y una base de clientes de unos 300 o más. Se trabaja 100% online, en Argentina, Paraguay, Bolivia y Uruguay.') + '</div></div>' +
                 '<div class="liquid-glass rounded-2xl p-7 md:p-8 relative overflow-hidden" style="box-shadow:0 8px 32px rgba(0,0,0,0.35),0 0 60px -30px var(--color-accent-glow)"><div class="absolute -top-16 -right-16 w-48 h-48 rounded-full pointer-events-none" style="background:radial-gradient(circle,var(--color-accent-glow) 0%,transparent 70%);opacity:.5"></div><div class="relative"><span class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:color-mix(in srgb,var(--color-accent) 15%,transparent)"><span class="material-symbols-outlined accent" style="font-size:26px">tune</span></span>' + h2('A tu medida, también en presupuesto') + p('Cobramos por punto de venta censado, con un pago único que se adapta al rubro de tu empresa, a su actividad y a la amplitud de zona que quieras desarrollar. Sin contrato inicial. Escribinos y lo vemos en una conversación.') + '</div></div>' +
                 '</div><p class="mt-8 text-center text-sm text-on-surface-variant">¿Primero querés entender tus datos de venta? Conocé nuestra <a href="/consultoria-inteligencia-comercial" class="underline accent hover:text-white">consultoría de inteligencia comercial</a>.</p>', bg='dim')

    c += faq_section(faqs)
    c += cta_final('¿Cuántos clientes más podría tener tu empresa?',
                   'Más clientes, más ventas. Contanos cuántos puntos de venta tiene tu empresa y te mostramos por dónde empezar.',
                   [btn(ask, wa_pv, 'primary', 'chat')], PHONE + ' · 100% online · Sin contrato inicial')
    write('mas-clientes-activos.html', shell('clientes', title, desc, path, ld, c))
