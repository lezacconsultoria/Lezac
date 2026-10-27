"""IA a Medida, WA Ventas y Partner. Copy literal de SEO/*.md"""
from lib import *


def ia():
    name, path = 'IA a Medida', '/ia-a-medida'
    title = 'Desarrollo a medida y automatización con IA | IA a Medida'
    desc = ('Bots de WhatsApp, herramientas internas y automatizaciones con IA a medida para pymes, distribuidoras '
            'y mayoristas. Reunión inicial sin costo.')
    faqs = [
        ('¿Qué es IA a Medida?',
         'IA a Medida es el servicio de Lezac Consultoría para resolver un proceso concreto de tu empresa con una solución a medida: bots de WhatsApp, automatizaciones, herramientas internas, aplicaciones, tableros o sitios web inteligentes. Empezamos con una reunión inicial sin costo para conocer tu necesidad y tu flujo de trabajo.'),
        ('¿Qué tipo de herramientas pueden construir?',
         'Desde un bot de WhatsApp que toma pedidos o responde consultas, hasta una herramienta interna para controlar cobranzas, entregas o stock, un formulario que reemplaza una planilla, un tablero de indicadores o una página web con asistente. El alcance se define con vos en la reunión inicial.'),
        ('¿Tiene que ser sí o sí con inteligencia artificial?',
         'No. Usamos inteligencia artificial cuando aporta valor al proceso. Si una automatización simple o una herramienta a medida resuelve el problema, es lo que te proponemos.'),
        ('¿La IA va a reemplazar a mi gente?',
         'No. El objetivo es sacarles las tareas repetitivas para que se dediquen a lo que genera valor en tu empresa.'),
        ('¿Cuánto cuesta?',
         'La reunión inicial y la evaluación no tienen costo. Cada proyecto se cotiza según su alcance y lo que tu empresa necesita: hay soluciones simples y desarrollos más completos. Trabajamos sin contrato inicial.'),
        ('¿Cuánto tarda?',
         'La primera mejora llega en 15 días. Si hace falta un proyecto de mayor alcance, lleva entre 30 y 60 días y se cotiza por separado.'),
        ('¿Necesito un equipo técnico o sistemas modernos?',
         'No. Nos ocupamos de la implementación y partimos de las herramientas y los procesos que tu empresa ya tiene. La forma de trabajo concreta depende de cada proyecto.'),
        ('¿Qué pasa si no sé qué necesito?',
         'Es lo más habitual. En la reunión inicial conocemos tu empresa y tu flujo, detectamos el proceso que más te cuesta y te presentamos una evaluación con tres mejoras concretas.'),
        ('¿Qué tan seguros están mis datos?',
         'Depende de cada proyecto. En la reunión inicial definimos qué información interviene y cómo se resguarda, y tenemos en cuenta desde el comienzo cualquier requisito de seguridad que tenga tu empresa.'),
        ('¿Cuál es la diferencia con comprar una herramienta de IA ya hecha?',
         'Una herramienta genérica te obliga a adaptar tu empresa a ella. Nosotros conocemos primero tu flujo de trabajo y construimos la solución para tu proceso.'),
        ('¿Qué compromiso tienen con los plazos?',
         'Acordamos los plazos desde el inicio. Si no resolvemos el problema más urgente que definimos juntos en la reunión inicial, esa etapa no se cobra. Para eso necesitamos contar con la información del proceso en tiempo y forma.'),
    ]
    service = {
        "@type": "Service", "@id": SITE + path + "#service",
        "name": "IA a Medida: desarrollo a medida y automatización de procesos con inteligencia artificial",
        "serviceType": "Desarrollo a medida y automatización de procesos",
        "description": "Servicio online para pymes, distribuidoras, mayoristas y fábricas que resuelve procesos concretos con bots de WhatsApp, automatizaciones, herramientas internas, aplicaciones, tableros y sitios web inteligentes, con inteligencia artificial cuando aporta valor.",
        "provider": org_min(), "areaServed": ["AR", "PY", "BO", "UY"],
        "audience": {"@type": "BusinessAudience", "audienceType": "Pymes, distribuidoras, mayoristas y fábricas"},
        "url": SITE + path}
    ld = jsonld(org_min(), service, faq_ld(faqs), breadcrumb_ld(name, path))
    meet = 'Agendá tu reunión inicial sin costo'
    wa_ia = wa('Hola, quiero consultar por IA a Medida. Mi necesidad es: ___')

    c = hero(name, 'Desarrollo a medida · Automatización con IA · Método IA a Medida',
             'Desarrollo a medida e inteligencia artificial', 'para resolver los procesos de tu empresa.',
             paragraph='IA a Medida es el servicio de Lezac Consultoría para pymes, distribuidoras, mayoristas y fábricas que necesitan una herramienta o un proceso resuelto a su medida: bots de WhatsApp, automatizaciones, herramientas internas de control, aplicaciones, tableros y sitios web inteligentes, con inteligencia artificial cuando aporta valor. Empezamos con una reunión inicial sin costo para conocer tu empresa y tu forma de trabajar, y la primera mejora llega en 15 días.',
             eslogan='Resolvemos lo que tu empresa necesita.',
             bl=['Reunión inicial sin costo', 'Primera mejora en 15 días', '100% online', 'Sin contrato inicial', 'Presupuesto a tu medida'],
             buttons=[btn(meet, CAL, 'primary', 'calendar_today'), btn('Ver qué podemos construir', '#que-hacemos', 'secondary')],
             vid=video('Web Vsl I IA a medida.mp4', 'IA a Medida: presentación del servicio'))
    c += prueba('Más de 100 empresas asesoradas en 4 países', '10+ años · 100+ empresas asesoradas · Argentina, Paraguay, Bolivia y Uruguay')

    c += section(h2('¿Hay un proceso que hoy te consume horas todas las semanas?') + item_cards([
        ('Los pedidos llegan por WhatsApp y por audios, y alguien los pasa a mano.', 'Cada carga manual es una chance de error.'),
        ('Las cobranzas no tienen un criterio claro de seguimiento.', 'Se llama al que se acuerdan, no al que corresponde.'),
        ('Las entregas se hacen sin avisarle al cliente.', 'Ni a qué hora llegan, ni si ya llegaron.'),
        ('Siempre la misma persona contesta las mismas consultas.', 'Y cuando no está, se frena todo.'),
        ('Hay un Excel que sostiene a la empresa.', 'Depende de una sola persona y nadie más sabe cómo funciona.'),
        ('Los reportes los arma alguien a mano.', 'Llegan tarde y cada uno trae un número distinto.'),
        ('La información está repartida en herramientas que no se hablan entre sí.', 'Para saber algo simple hay que buscar en cuatro lugares.'),
        ('Probaste herramientas genéricas y no encajaron.', 'O querés usar IA y no sabés por dónde empezar.'),
    ]) + closing('No necesitás más tecnología. Necesitás resolver un proceso concreto.'), bg='dim')

    c += section(h2('Una solución hecha para tu proceso, no para el promedio') +
                 p('Construimos la herramienta que tu empresa necesita, en cualquier área: comercial, administrativa o logística. Según el caso, puede ser:') +
                 '<ul class="mt-5 grid grid-cols-1 md:grid-cols-2 gap-3">' + ''.join(
                     f'<li class="liquid-glass rounded-xl p-4 flex items-start gap-3 text-sm text-white/90"><span class="material-symbols-outlined accent" style="font-size:20px">{ic}</span>{E(t)}</li>' for ic, t in [
                         ('forum', 'Un bot o asistente de WhatsApp que atiende consultas y toma pedidos'),
                         ('bolt', 'Una automatización que elimina tareas repetitivas'),
                         ('fact_check', 'Una herramienta interna de control (seguimiento, cobranzas, entregas, stock)'),
                         ('app_registration', 'Una aplicación o formulario a medida'),
                         ('monitoring', 'Un tablero de indicadores para decidir con datos'),
                         ('language', 'Una página web inteligente que atiende y deriva consultas'),
                         ('sync_alt', 'Una integración entre las herramientas que ya usás')]) + '</ul>'
                 '<p class="mt-6 text-white font-semibold leading-relaxed">Usamos inteligencia artificial cuando aporta valor, y no la usamos cuando no hace falta. Desde algo simple hasta un sistema completo, nos adaptamos al tamaño de tu necesidad.</p>',
                 sid='que-hacemos')

    c += section(h2('De conocer tu empresa a tener la solución funcionando') +
                 p('No hay dos empresas iguales. Por eso, antes de proponer nada, conocemos tu necesidad y tu flujo de trabajo.') +
                 '<div class="mt-6"></div>' + steps([
        ('Reunión inicial sin costo.', 'Nos contás qué proceso te frena y cómo trabajan hoy. Sin compromiso.'),
        ('Te presentamos una evaluación con 3 mejoras concretas.', 'Un documento claro con qué haríamos, qué resolvería cada mejora y por cuál conviene empezar.'),
        ('Primera mejora en 15 días.', 'Resolvemos el problema más urgente y lo dejamos funcionando en tu empresa.'),
        ('Si hace falta, vamos por más.', 'Un proyecto de mayor alcance, de 30 a 60 días, cotizado por separado.'),
        ('Tu equipo queda preparado.', 'Capacitación de buenas prácticas y manual de funcionamiento.'),
    ]) + '<p class="mt-6 text-sm text-on-surface-variant">Acordamos los plazos desde el inicio y, si no resolvemos el problema más urgente que definimos juntos en la reunión inicial, esa etapa no se cobra.</p>', bg='dim', width='max-w-4xl')

    def li(t):
        return f'<li class="flex items-start gap-3 text-sm text-white/85 leading-relaxed"><span class="w-1.5 h-1.5 rounded-full mt-2 flex-shrink-0" style="background:var(--color-accent)"></span><span>{E(t)}</span></li>'
    def ico(n, sz=22):
        return (f'<span class="w-11 h-11 rounded-xl flex items-center justify-center flex-shrink-0" style="background:color-mix(in srgb,var(--color-accent) 15%,transparent)">'
                f'<span class="material-symbols-outlined accent" style="font-size:{sz}px">{n}</span></span>')
    def proj(ic, t, d):
        return ('<li class="liquid-glass rounded-xl p-5 flex gap-4 items-start transition-transform duration-300 hover:-translate-y-1" style="box-shadow:0 8px 32px rgba(0,0,0,0.35),0 0 50px -28px var(--color-accent-glow)">'
                + ico(ic) + f'<div><p class="text-white font-bold mb-1">{t}</p><p class="text-sm text-on-surface-variant leading-relaxed">{d}</p></div></li>')
    done = ('<ul class="grid grid-cols-1 md:grid-cols-2 gap-4">'
            + proj('chat', 'Pedidos por WhatsApp con cobro integrado.', 'Una plataforma para una distribuidora: el cliente hace su pedido por WhatsApp y paga en el mismo chat. <a href="/wa-ventas" class="underline accent hover:text-white">WA Ventas</a>')
            + proj('query_stats', 'Indicadores de cobranza.', 'Un sistema que analiza las cuentas corrientes y define en qué etapa de cobro está cada cliente.')
            + proj('local_shipping', 'Registro de entregas con aviso automático.', 'Formularios que registran cada entrega y notifican el día y la hora en que se hizo.')
            + proj('forum', 'Asistente conversacional en una web.', 'Un bot que responde en el momento a quienes consultan por un servicio.')
            + '</ul>')
    def chip(ic, t):
        return ('<li class="liquid-glass rounded-xl p-4 flex gap-3 items-center w-full md:w-[calc(33.333%-0.667rem)] transition-transform duration-300 hover:-translate-y-1">'
                + ico(ic, 20) + f'<span class="text-sm text-white/85 leading-relaxed">{E(t)}</span></li>')
    also = ('<ul class="flex flex-wrap justify-center gap-4 mt-2">' + ''.join(chip(i, t) for i, t in [
        ('description', 'Un formulario que reemplace una planilla compartida y avise automáticamente a quien corresponde'),
        ('dashboard', 'Un tablero simple con lo que hoy armás a mano cada semana'),
        ('inventory_2', 'Una herramienta interna para controlar tareas, pedidos o stock'),
        ('forum', 'Un bot que responda las consultas más frecuentes de tus clientes'),
        ('language', 'Una página web que atienda y clasifique consultas')]) + '</ul>')
    c += section(h2('Proyectos que ya construimos') + done + '<div class="mt-12"></div>' + h2('También podemos construir') + also)

    c += section(h2('Un servicio concreto, que no te ocupa tiempo') +
                 '<p class="text-on-surface-variant mb-8">Vos seguís trabajando. Nosotros resolvemos.</p>' + item_cards([
        ('Primero escuchamos.', 'Conocemos tu empresa y tu flujo antes de proponer cualquier solución.'),
        ('Tu tiempo, cuidado.', 'Una reunión para entender el problema y seguimiento por WhatsApp. El desarrollo lo hacemos nosotros.'),
        ('No necesitás equipo técnico.', 'Nos ocupamos de la implementación y de que quede funcionando.'),
        ('Nos adaptamos a tu forma de trabajar.', 'Partimos de las herramientas y los procesos que tu empresa ya tiene.'),
        ('Entendemos tu operación.', 'Más de 10 años en procesos comerciales, administrativos y logísticos de pymes y distribuidoras.'),
        ('Tu equipo queda preparado.', 'Capacitación de buenas prácticas y manual de funcionamiento.'),
        ('Se adapta a tu presupuesto.', 'Desde algo simple hasta un sistema completo, sin contrato inicial.'),
    ]), bg='dim')

    c += section(h2('¿Por qué a medida y no una herramienta genérica?') + table(
        ['Herramienta genérica', 'IA a Medida'],
        [['Vos adaptás tu empresa a ella', 'La adaptamos a tu proceso'],
         ['Funciones que quizá nunca uses', 'Solo lo que resuelve tu problema'],
         ['Empieza por la tecnología', 'Empieza por conocer tu flujo de trabajo'],
         ['Configurarla queda a tu cargo', 'La implementa un equipo con experiencia en tu operación']]), width='max-w-4xl')

    c += section(dual_cards('groups', 'Para quién es', 'Pymes, distribuidoras, mayoristas y fábricas que quieren resolver un proceso concreto, sin armar un equipo técnico. Se trabaja 100% online, en Argentina, Paraguay, Bolivia y Uruguay.', 'tune', 'A tu medida, también en presupuesto', 'La reunión inicial y la evaluación no tienen costo. Cotizamos cada proyecto según su alcance, desde algo simple hasta un sistema completo. Sin contrato inicial.') +
                 '<p class="mt-8 text-center text-sm text-on-surface-variant">¿Querés entender primero cómo vendés? Conocé nuestra <a href="/consultoria-inteligencia-comercial" class="underline accent hover:text-white">consultoría de inteligencia comercial</a>. ¿Pedidos por WhatsApp? Mirá <a href="/wa-ventas" class="underline accent hover:text-white">WA Ventas</a>.</p>', bg='dim')

    c += faq_section(faqs)
    c += cta_final('¿Qué proceso de tu empresa te gustaría dejar de hacer a mano?',
                   'Resolvemos lo que tu empresa necesita. Contanos cuál es el problema y te presentamos tres mejoras concretas.',
                   [btn(meet, CAL, 'primary', 'calendar_today'), btn('Escribinos por WhatsApp', wa_ia, 'secondary', 'chat')],
                   PHONE + ' · 100% online · Sin contrato inicial')
    write('ia-a-medida.html', shell('ia', title, desc, path, ld, c))


def wa_ventas():
    name, path = 'WA Ventas', '/wa-ventas'
    title = 'Pedidos por WhatsApp para distribuidoras | WA Ventas'
    desc = ('Ordená pedidos, consultas y prospectos de tus clientes en un solo WhatsApp, con catálogo digital y panel '
            'de control. Para distribuidoras y mayoristas.')
    faqs = [
        ('¿Qué es WA Ventas?',
         'WA Ventas es el sistema de Lezac Consultoría para ordenar los pedidos, consultas, reclamos y prospectos que llegan por WhatsApp, con catálogo digital y un panel de control. Está pensado para distribuidoras, mayoristas y fábricas.'),
        ('¿Cómo funciona?',
         'Tus clientes siguen escribiéndote por WhatsApp. El sistema los reconoce, los guía según su situación (pedido, consulta, reclamo o prospecto nuevo) y deja todo registrado. Los pedidos los validás vos en un panel.'),
        ('¿Mis clientes tienen que instalar algo?',
         'No. Le escriben directamente a tu WhatsApp y hacen sus pedidos desde ahí.'),
        ('¿Trabajan con la API oficial de WhatsApp?',
         'Sí. Trabajamos con la API oficial de WhatsApp, un canal profesional y estable para tu empresa.'),
        ('¿Tengo que cambiar mi número o mi forma de trabajar?',
         'Lo definimos en la reunión inicial, según cómo trabaje hoy tu empresa. Nos adaptamos a tu operación.'),
        ('¿Reemplaza a mis vendedores?',
         'No. Les saca la carga manual y las consultas repetitivas para que se dediquen a vender.'),
        ('¿Funciona con mi sistema de gestión?',
         'Si tu sistema cuenta con una API, nos conectamos y lo configuramos para que funcione correctamente. Si no, lo vemos en la reunión inicial.'),
        ('¿Cuánto cuesta?',
         'La reunión inicial no tiene costo. Después, el servicio se contrata con una modalidad de pago mensual, con todas las prestaciones incluidas. Escribinos y te contamos las condiciones.'),
        ('¿Cuánto tarda la puesta en marcha?',
         'Aproximadamente entre 10 y 15 días hábiles, desde que recibimos la información que te solicitamos.'),
        ('¿Qué diferencia hay con WhatsApp Business o un bot de menús?',
         'Esas herramientas responden mensajes. WA Ventas ordena la operación completa: pedidos, consultas, reclamos, prospectos y seguimiento, con flujos distintos según quién escribe.'),
    ]
    service = {
        "@type": "Service", "@id": SITE + path + "#service",
        "name": "WA Ventas: pedidos y ventas por WhatsApp para distribuidoras, mayoristas y fábricas",
        "serviceType": "Gestión de pedidos y ventas por WhatsApp",
        "description": "Sistema online para distribuidoras, mayoristas y fábricas que centraliza pedidos, consultas, reclamos y prospectos en un solo número de WhatsApp (API oficial), con catálogo digital y panel de control para validar y hacer seguimiento.",
        "provider": org_min(), "areaServed": ["AR", "PY", "BO", "UY"],
        "audience": {"@type": "BusinessAudience", "audienceType": "Distribuidoras, mayoristas y fábricas"},
        "url": SITE + path}
    ld = jsonld(org_min(), service, faq_ld(faqs), breadcrumb_ld(name, path))
    meet = 'Agendá tu reunión inicial sin costo'
    wa_w = wa('Hola, quiero consultar por WA Ventas. Mi empresa recibe pedidos por WhatsApp.')

    c = hero(name, 'Ventas por WhatsApp · Pedidos B2B · Sistema WA Ventas',
             'Pedidos y ventas por WhatsApp, ordenados en un solo canal,', 'para distribuidoras y mayoristas.',
             subtitle='Tus clientes ya te piden por WhatsApp. Nosotros hacemos que cada pedido, consulta y reclamo llegue ordenado, se registre solo y no dependa de que un vendedor esté disponible.',
             paragraph='WA Ventas es el sistema de Lezac Consultoría para distribuidoras, mayoristas y fábricas que reciben pedidos por WhatsApp. Centraliza pedidos, consultas, reclamos y prospectos en un solo número, con catálogo digital y un panel de control para validar y hacer seguimiento. Trabajamos con la API oficial de WhatsApp y lo ponemos en marcha en 10 a 15 días hábiles aproximadamente.',
             eslogan='Que ningún mensaje se quede sin respuesta.',
             bl=['Reunión inicial sin costo', 'API oficial de WhatsApp', 'Puesta en marcha en 10 a 15 días hábiles', '100% online'],
             buttons=[btn(meet, CAL, 'primary', 'calendar_today'), btn('Ver cómo funciona', '#como-funciona', 'secondary')],
             vid=youtube('36Lhzc72YTE', 'WA Ventas: presentación del servicio'))
    c += prueba('Más de 100 empresas asesoradas en 4 países', '10+ años · 100+ empresas asesoradas · Argentina, Paraguay, Bolivia y Uruguay')

    c += section(h2('¿Te pasa que los pedidos se pierden entre chats?') + item_cards([
        ('Los pedidos llegan a distintos WhatsApp y se anotan a mano.', 'Cada vendedor, su chat; cada chat, su desorden.'),
        ('Audios y mensajes sueltos que alguien tiene que cargar.', 'Cada carga manual es una chance de error.'),
        ('Si el vendedor no está, el cliente espera.', 'O le compra a otro.'),
        ('Fuera de horario, nadie responde.', 'Y el pedido se pierde o se enfría.'),
        ('Pedidos, reclamos y consultas de prospectos, todo mezclado.', 'Nadie sabe qué es urgente.'),
        ('No sabés cuántos clientes te escribieron y no se atendieron.', 'Ni cuántos pedidos se perdieron en el camino.'),
        ('A los clientes inactivos nadie los recuerda.', 'Dejaron de comprar y nunca los contactaron.'),
        ('Se acepta un pedido sin ver crédito ni stock.', 'Después hay que volver atrás y explicarle al cliente.'),
    ]) + closing('Tu problema no son los mensajes. Es que WhatsApp se volvió tu canal de ventas sin ser un sistema.'), bg='dim')

    c += section(h2('Un solo WhatsApp para toda tu empresa') +
                 p('WA Ventas ordena la conversación y la convierte en venta registrada. Tus clientes no instalan nada: le escriben a tu WhatsApp y hacen sus pedidos desde ahí. Según quién escribe, cada contacto sigue su camino:') +
                 '<ul class="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">'
                 '<li class="liquid-glass rounded-xl p-5"><p class="text-white font-bold mb-1">Clientes que compran seguido:</p><p class="text-sm text-on-surface-variant leading-relaxed">hacen su pedido con un catálogo digital.</p></li>'
                 '<li class="liquid-glass rounded-xl p-5"><p class="text-white font-bold mb-1">Clientes con una consulta o un reclamo:</p><p class="text-sm text-on-surface-variant leading-relaxed">se derivan a la persona que corresponde.</p></li>'
                 '<li class="liquid-glass rounded-xl p-5"><p class="text-white font-bold mb-1">Prospectos nuevos:</p><p class="text-sm text-on-surface-variant leading-relaxed">se califican automáticamente y quedan cargados para que tu equipo los siga.</p></li></ul>' +
                 p('Antes de confirmar un pedido, lo validás en un panel con la información de crédito y stock que necesitás.', 'mt-6 text-on-surface-variant leading-relaxed') +
                 '<p class="mt-4 text-white font-semibold leading-relaxed">Todo queda registrado: pedidos, reclamos y prospectos, con métricas de tiempos de respuesta y conversión.</p>', sid='funciona')

    c += section(h2('Qué incluye WA Ventas') + '<ul class="grid grid-cols-1 md:grid-cols-2 gap-3 md:[&>li:last-child:nth-child(odd)]:col-span-2 md:[&>li:last-child:nth-child(odd)]:w-[calc(50%-0.375rem)] md:[&>li:last-child:nth-child(odd)]:justify-self-center">' + ''.join(
        f'<li class="liquid-glass rounded-xl p-4 flex items-start gap-3 text-sm text-white/90"><span class="material-symbols-outlined accent" style="font-size:20px">check_circle</span>{E(t)}</li>' for t in [
            'Número central de WhatsApp para tu empresa, con flujos de atención a medida', 'Trabajamos con la API oficial de WhatsApp',
            'Catálogo digital para que tus clientes hagan sus pedidos', 'Panel de control para validar y hacer seguimiento de pedidos',
            'Calificación automática de prospectos', 'Derivación de reclamos y consultas', 'Recordatorios para clientes inactivos',
            'Métricas de tiempos de respuesta y conversión', 'Conexión con tu sistema de gestión, si cuenta con una API',
            'Capacitación para tu equipo y manual de funcionamiento']) + '</ul><p class="mt-6 text-sm text-on-surface-variant">Todas las prestaciones, con pago mensual.</p>', bg='dim')

    c += section(h2('De la reunión a la puesta en marcha, en 10 a 15 días hábiles') + steps([
        ('Reunión inicial sin costo.', 'Conocemos cómo recibís y gestionás hoy los pedidos.'),
        ('Confirmás que querés empezar.', 'Te pedimos la información que necesitamos de tu empresa.'),
        ('Lo ponemos a punto.', 'Una vez que recibimos esa información, configuramos todo para tu operación, en aproximadamente 10 a 15 días hábiles.'),
        ('Empezás a usarlo.', 'Tu equipo queda capacitado y con un manual de funcionamiento.'),
    ]), sid='como-funciona', width='max-w-4xl')

    c += section(h2('Un servicio concreto, que no te ocupa tiempo') +
                 '<p class="text-on-surface-variant mb-8">Vos seguís vendiendo. Nosotros lo dejamos funcionando.</p>' + item_cards([
        ('Primero escuchamos.', 'Conocemos cómo vendés hoy antes de configurar nada.'),
        ('Tu tiempo, cuidado.', 'Una reunión para entender tu operación y seguimiento por WhatsApp. La puesta en marcha la hacemos nosotros.'),
        ('Tus clientes no instalan nada.', 'Siguen escribiéndote por WhatsApp, como siempre.'),
        ('Menos errores y menos carga manual.', 'Tu equipo deja de pasar pedidos a mano.'),
        ('Más tiempo para vender.', 'Tus vendedores dejan de responder lo mismo todo el día.'),
        ('Información para decidir.', 'Sabés cuántos pedidos entran, cuánto tardás en responder y cuántos prospectos se convierten.'),
        ('Con la API oficial de WhatsApp.', 'Un canal profesional y estable para tu empresa.'),
    ]), bg='dim')

    c += section(h2('¿Por qué no alcanza con WhatsApp Business o un bot de menús?') + table(
        ['WhatsApp Business o un bot de menús', 'WA Ventas'],
        [['Responde mensajes', 'Ordena pedidos, consultas y prospectos'],
         ['Cada chat es un caso aparte', 'Todo queda registrado y medido'],
         ['Vos lo configurás', 'Lo implementa un equipo que conoce tu operación'],
         ['El mismo flujo para todos', 'Flujos distintos según quién escribe']]), width='max-w-4xl')

    c += section(dual_cards('groups', 'Para quién es', 'Distribuidoras, mayoristas y fábricas que reciben pedidos y consultas de sus clientes por WhatsApp. Se trabaja 100% online, en Argentina, Paraguay, Bolivia y Uruguay.', 'handshake', 'Cómo se contrata', 'Modalidad de pago mensual, con todas las prestaciones incluidas. La reunión inicial no tiene costo. Escribinos y te contamos las condiciones.') +
                 '<p class="mt-8 text-center text-sm text-on-surface-variant">¿Necesitás algo distinto a WhatsApp? Conocé <a href="/ia-a-medida" class="underline accent hover:text-white">IA a Medida</a>. ¿Querés ordenar primero tus datos de venta? Conocé nuestra <a href="/consultoria-inteligencia-comercial" class="underline accent hover:text-white">consultoría de inteligencia comercial</a>.</p>', bg='dim')

    c += faq_section(faqs)
    c += cta_final('¿Cuántos pedidos se te pierden entre chats?',
                   'Que ningún mensaje se quede sin respuesta. Contanos cómo recibís hoy los pedidos y te mostramos cómo ordenarlos.',
                   [btn(meet, CAL, 'primary', 'calendar_today'), btn('Escribinos por WhatsApp', wa_w, 'secondary', 'chat')],
                   PHONE + ' · 100% online · API oficial de WhatsApp')
    write('wa-ventas.html', shell('wa', title, desc, path, ld, c))


def partner():
    name, path = 'Programa de Partners', '/partner'
    title = 'Programa de Partners para consultores y contadores | Lezac'
    desc = ('Recomendá a Lezac a distribuidoras, mayoristas y fábricas y recibí una comisión por cada cliente que se '
            'activa. Sin costo ni permanencia. Argentina y Latinoamérica.')
    faqs = [
        ('¿Qué es el Programa de Partners de Lezac?',
         'Es una alianza para que profesionales que asesoran a distribuidoras, mayoristas y fábricas recomienden a Lezac y reciban una comisión por cada cliente que se activa.'),
        ('¿Quién puede ser partner?',
         'Contadores, consultores de gestión, proveedores de software, ex gerentes comerciales con red de contactos y proveedores o fabricantes que venden a distribuidoras.'),
        ('¿Tengo que vender?',
         'No. Como Referidor, presentás el contacto y participás de la primera reunión. Nosotros explicamos el servicio y lo cerramos.'),
        ('¿Cuánto cobro?',
         'Recibís una comisión por cada cliente que se activa. Las condiciones se definen en una conversación, según la propuesta y el alcance de cada empresa, y se ponen por escrito.'),
        ('¿Cuándo se paga?',
         'Dentro de los 2 días hábiles de acreditado el pago del cliente.'),
        ('¿Cómo me aseguro de que el cliente quede a mi nombre?',
         'Registrás el contacto antes de la primera reunión y queda protegido a tu nombre. Si ya estaba en contacto con Lezac o con otro partner, decide lo que el cliente confirme por escrito.'),
        ('¿Tiene costo o exclusividad?',
         'No. Es gratuito, sin permanencia y sin exclusividad obligatoria.'),
        ('¿Puedo ser partner desde otro país de Latinoamérica?',
         'Sí. Trabajamos 100% online, en Argentina, Paraguay, Bolivia, Uruguay y el resto de Latinoamérica.'),
        ('¿Qué pasa con las empresas que ya contacté?',
         'Si no están en contacto con Lezac ni con otro partner, podés registrarlas antes de la primera reunión.'),
    ]
    webpage = {"@type": "WebPage", "@id": SITE + path + "#webpage",
               "name": "Programa de Partners para consultores y contadores | Lezac",
               "description": "Programa de alianza para profesionales que asesoran a distribuidoras, mayoristas y fábricas: recomiendan a Lezac Consultoría y reciben una comisión por cada cliente que se activa.",
               "url": SITE + path, "inLanguage": "es-AR",
               "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#organization"}}
    ld = jsonld(org_min(), website_min(), webpage, faq_ld(faqs), breadcrumb_ld(name, path))
    partner_wa = wa('Hola, quiero ser partner de Lezac. Asesoro a empresas de ___')

    c = hero(name, 'Programa de Partners · Argentina y Latinoamérica',
             'Programa de Partners de Lezac:', 'una alianza para crecer junto a tus clientes.',
             subtitle='Sumás servicios de inteligencia comercial a tu oferta sin desarrollarlos, y seguís al lado de tu cliente mientras crece.',
             paragraph='El Programa de Partners de Lezac Consultoría es una alianza para contadores, consultores, proveedores de software y otros profesionales que asesoran a distribuidoras, mayoristas y fábricas. Vos recomendás a Lezac, nosotros implementamos los servicios y recibís una comisión por cada cliente que se activa. Sin costo y sin permanencia.',
             bl=['Sin costo', 'Sin permanencia', 'No tenés que vender', '100% online'],
             buttons=[btn('Quiero ser partner', partner_wa, 'primary', 'chat'), btn('Cómo funciona', '#como-funciona', 'secondary')])

    c += section(h2('Una alianza donde ganan los tres') + '<ul class="grid grid-cols-1 md:grid-cols-3 gap-4">' + ''.join(
        f'<li class="liquid-glass rounded-xl p-6"><p class="text-white font-bold mb-2">{E(t)}</p><p class="text-sm text-on-surface-variant leading-relaxed">{E(s)}</p></li>' for t, s in [
            ('Para vos:', 'sumás servicios de alto valor a tu oferta sin invertir en desarrollarlos, y fortalecés la relación con tus clientes.'),
            ('Para tu cliente:', 'accede a una consultoría especializada, recomendada por alguien en quien ya confía.'),
            ('Para ambos:', 'acompañamos el proyecto y vos seguís al lado de tu cliente mientras crece.')]) + '</ul>', bg='dim')

    c += section(h2('¿Para quién es el programa?') + '<ul class="grid grid-cols-1 md:grid-cols-2 gap-3 md:[&>li:last-child:nth-child(odd)]:col-span-2 md:[&>li:last-child:nth-child(odd)]:w-[calc(50%-0.375rem)] md:[&>li:last-child:nth-child(odd)]:justify-self-center">' + ''.join(
        f'<li class="liquid-glass rounded-xl p-4 text-sm text-white/90 flex items-center gap-3"><span class="material-symbols-outlined accent" style="font-size:20px">{ic}</span>{E(t)}</li>' for ic, t in [
            ('calculate', 'Contadores y estudios contables'), ('insights', 'Consultores de gestión'),
            ('devices', 'Proveedores de software (ERP, preventa, ruteo)'), ('work_history', 'Ex gerentes comerciales con red de contactos'),
            ('factory', 'Proveedores y fabricantes que venden a distribuidoras')]) + '</ul>' +
                 p('Si tus clientes son distribuidoras, mayoristas o fábricas de Argentina, Paraguay, Bolivia, Uruguay o el resto de Latinoamérica, hablemos. ¿Asesorás a esas empresas y no estás en esta lista? Escribinos igual.', 'mt-6 text-on-surface-variant leading-relaxed'))

    c += section(h2('Elegí cuánto querés involucrarte') + '<div class="grid grid-cols-1 md:grid-cols-2 gap-5">'
                 '<div class="liquid-glass rounded-2xl p-7"><h3 class="text-xl font-black text-white mb-3">Referidor.</h3><p class="text-sm text-on-surface-variant leading-relaxed">Presentás el contacto y participás de la primera reunión. No necesitás vender ni explicar el servicio.</p></div>'
                 '<div class="liquid-glass rounded-2xl p-7"><h3 class="text-xl font-black text-white mb-3">Aliado.</h3><p class="text-sm text-on-surface-variant leading-relaxed">Además de presentar el contacto, acompañás el proyecto junto al equipo de Lezac.</p></div></div>', bg='dim')

    c += section(h2('Cómo funciona, en 4 pasos') + steps([
        ('Registrás el contacto', 'antes de la primera reunión. Queda protegido a tu nombre.'),
        ('Reunión conjunta', 'con el dueño o gerente comercial, presentada por Lezac.'),
        ('Propuesta a medida', 'según el servicio que mejor encaje con esa empresa.'),
        ('Inicio del proyecto,', 'con seguimiento tuyo.'),
    ]), sid='como-funciona', width='max-w-4xl')

    c += section(h2('Qué recibís como partner') + item_cards([
        ('Una comisión por cada cliente que se activa.', 'Las condiciones se definen en una conversación, según la propuesta y el alcance de cada empresa y la forma en que quieras trabajar.'),
        ('Pago rápido:', 'se abona dentro de los 2 días hábiles de acreditado el pago del cliente.'),
        ('Capacitación, material y preparación', 'para presentar los servicios y negociar con seguridad.'),
        ('Seguimiento cercano:', 'una reunión de seguimiento semanal con Lezac.'),
        ('Crecimiento conjunto:', 'a partir del quinto proyecto, derivación de referidos y publicidad conjunta en tu zona.'),
    ]) + '<p class="mt-6 text-sm text-on-surface-variant">Cada alianza es distinta. Por eso las condiciones se acuerdan con vos y se ponen por escrito.</p>', bg='dim')

    def svc(t, s, href):
        return (f'<li class="liquid-glass rounded-xl p-5"><a href="{href}" class="text-white font-bold underline decoration-white/20 hover:decoration-white">{E(t)}</a>'
                f'<p class="text-sm text-on-surface-variant leading-relaxed mt-1">{E(s)}</p></li>')
    c += section(h2('Qué servicios podés recomendar') + '<ul class="grid grid-cols-1 md:grid-cols-2 gap-4">' +
                 svc('Consultoría de inteligencia comercial', 'empresas con equipo de ventas activo y base de clientes histórica.', '/consultoria-inteligencia-comercial') +
                 svc('+Clientes Activos', 'empresas con al menos 300 puntos de venta en su base.', '/mas-clientes-activos') +
                 svc('IA a Medida', 'cualquier empresa con un proceso que consume tiempo o dinero.', '/ia-a-medida') +
                 svc('WA Ventas', 'distribuidoras y mayoristas que reciben pedidos por WhatsApp.', '/wa-ventas') + '</ul>')

    c += section(h2('Reglas claras desde el primer día') + '<ul class="space-y-3">' + ''.join(
        f'<li class="flex items-start gap-3 text-white/85 leading-relaxed"><span class="material-symbols-outlined accent mt-0.5" style="font-size:20px">verified</span><span>{E(t)}</span></li>' for t in [
            'El contacto queda protegido a tu nombre desde que lo registrás.', 'Sin costo de ingreso y sin permanencia.',
            'Sin exclusividad obligatoria.',
            'Si el contacto ya estaba en contacto con Lezac o con otro partner, no queda a tu nombre. Ante cualquier duda, decide lo que el cliente confirme por escrito.',
            'Las condiciones de cada acuerdo se ponen por escrito.']) + '</ul>', bg='dim')

    c += prueba('Más de 100 empresas asesoradas en 4 países', '10+ años · 100+ empresas asesoradas · Argentina, Paraguay, Bolivia y Uruguay')
    c += faq_section(faqs)
    c += cta_final('¿Tenés clientes que necesitan crecer?',
                   'Sumate al programa y crezcamos juntos. Contanos a quién asesorás y te mostramos cómo trabajar juntos.',
                   [btn('Quiero ser partner', partner_wa, 'primary', 'chat'), btn('Agendar una reunión', CAL, 'secondary', 'calendar_today')],
                   PHONE + ' · 100% online · Argentina y Latinoamérica')
    write('partner.html', shell('partner', title, desc, path, ld, c))
