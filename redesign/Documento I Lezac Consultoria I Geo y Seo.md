# Relanzamiento web de Lezac Consultoría: GEO/SEO actualizado, keywords, sección Partner, competencia y contenido on-page (septiembre 2026)

La auditoría previa sigue sirviendo en lo estratégico, pero en lo técnico hay que corregirla en tres puntos: el llms.txt pasó de "prioridad" a "opcional de bajo costo", el schema FAQPage ya no da resultados enriquecidos en Google (desde el 7 de mayo de 2026) y el "RAG chunking" dejó de ser una práctica recomendada por Google. Lo que sí se mantiene y se vuelve más importante es permitir los bots de búsqueda de IA en robots.txt, publicar contenido original con datos propios verificados y armar una entidad de marca consistente. En la competencia también hay cambios: Elit Latam no es competidor (es un mayorista de tecnología), Marketech LATAM y Affinitit se reposicionaron como agencias de "agentes de IA", y en 2026 aparecieron actores nuevos como Galo AI (IA + WhatsApp para mayoristas) y KIRI con gamificación. Ninguno ofrece lo que diferencia a Lezac: consultoría de campo con garantía de plazo (censo de 100 PDV en 7 días, victoria rápida en 15 días) y resultados medidos en clientes activos.

## TL;DR

- **Técnico:** robots.txt tiene que permitir de forma explícita OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot y Perplexity-User. El llms.txt se publica solo porque cuesta poco, sin esperar impacto. Hay que mantener Organization + Service en JSON-LD y dejar de venderle al cliente el FAQPage como táctica de visibilidad. Google publicó el 15 de mayo de 2026 su guía oficial de IA generativa: el llms.txt, el "chunking" y el schema especial no son necesarios.
- **Mercado y competencia:** el nicho de "inteligencia comercial para distribuidoras" se está llenando de software (KIRI, Nextbyn, Galo AI, Quadminds) y de agencias de IA genéricas (Marketech, Affinitit, Delenio). El espacio que nadie ocupa es "consultoría de campo con resultado medido en clientes activos", y el sitio de Lezac tiene que apropiarse de ese lenguaje en cada H1.
- **Partner:** conviene lanzar un programa de dos niveles, "Referidor" (presenta y cobra comisión) y "Aliado" (acompaña el proyecto). Las reglas tienen que estar escritas: ventana de protección del referido, comisión sobre lo efectivamente cobrado, pago a 30 días y resolución de conflictos por elección escrita del cliente. Así lo hacen hoy Quilsoft, Q10, Tiendanube y SimpliRoute.

## Key Findings

### 1. Validación técnica GEO/AEO: qué cambió desde la auditoría

| Recomendación de la auditoría | Estado a sept. 2026 | Acción para Lezac |
|---|---|---|
| Publicar llms.txt | **Degradada.** Google publicó el 15/5/2026 su guía de optimización para IA generativa, que dice que no hacen falta archivos legibles por máquina ni Markdown para aparecer. El 15/6/2026 aclaró que mantener un llms.txt no afecta la visibilidad ni el ranking, ni para bien ni para mal. Ahrefs (15/6/2026) analizó 137.210 dominios: de los ~38.000 con un archivo válido, el 97% no recibió ninguna solicitud en mayo de 2026, ni de bots ni de humanos. SE Ranking midió que solo el 10,13% de casi 300.000 dominios tenía llms.txt, y al quitar esa variable de su modelo XGBoost la precisión del modelo mejoró (es decir, no aporta a predecir citas en IA). | Publicarlo igual (20 minutos, riesgo cero) como "ficha de la empresa para agentes", pero sacarlo de la lista de prioridades. |
| Arquitectura "RAG chunking" | **Desaconsejada por Google.** La guía de mayo de 2026 dice que no hace falta partir el contenido en pedacitos y que armar páginas masivas para cada variante de consulta puede violar la política de "scaled content abuse". | Escribir páginas completas, bien estructuradas con H2/H3 y respuestas directas. No hacer una página por cada long-tail. |
| Schema FAQPage | **Sin resultado enriquecido.** Según el aviso de Google Search Central, desde el 7/5/2026 "FAQ rich results are no longer appearing in Google Search". El informe de Search Console y el soporte en Rich Results Test se retiraron en junio de 2026, y la API en agosto de 2026. El marcado sigue siendo válido en schema.org y no causa problemas. | Mantener los bloques FAQ visibles (sirven a humanos y a la extracción de IA). El JSON-LD FAQPage es opcional y no hay que venderlo como palanca. |
| Schema Organization + Service con areaServed en 4 países | **Vigente.** Google dice que los datos estructurados no son requisito para la IA generativa, pero recomienda seguir usándolos dentro de la estrategia SEO, siempre que coincidan con el texto visible. | Implementar Organization (con sameAs a LinkedIn, Google Business Profile, etc.), un Service por cada servicio con areaServed AR/PY/BO/UY y un BreadcrumbList. |
| Abrir crawlers de IA en robots.txt | **Vigente y más granular.** Ver detalle abajo. | Aplicar la configuración propuesta más abajo. |
| Densidad factual, BLUF, E-E-A-T, frescura | **Vigente.** Google pide contenido "no commodity", original y útil. Las fuentes de GEO coinciden en que las menciones de marca, la frescura y la estructura extraíble son lo que más correlaciona con las citas. | Usar solo las cifras verificadas de Lezac. Poner fecha de actualización visible en cada página. |

**Estado de los bots de IA (segundo semestre 2026):**

- **OpenAI:** opera tres agentes. GPTBot (entrenamiento), OAI-SearchBot (índice de ChatGPT Search) y ChatGPT-User (lecturas pedidas por un usuario). Bloquear OAI-SearchBot saca al sitio de ChatGPT Search. Un relevamiento actualizado al 8/8/2026 señala tres cosas: la documentación de OpenAI ahora dice que robots.txt puede no aplicarse a ChatGPT-User porque la visita la inicia un usuario, la documentación se mudó a developers.openai.com y el user-agent de OAI-SearchBot ahora arranca con un string completo de Chrome, así que los filtros de logs con el formato viejo lo pierden. Los cambios en robots.txt tardan unas 24 horas en reflejarse en la búsqueda.
- **Anthropic:** desde la actualización de su documentación (detectada por Pedro Dias y publicada por Search Engine Roundtable el 25/2/2026) tiene tres bots separados: ClaudeBot (entrenamiento), Claude-User (lecturas pedidas por usuarios) y Claude-SearchBot (indexación para búsqueda). Anthropic advierte que bloquear Claude-SearchBot "puede reducir la visibilidad y precisión" en las respuestas de búsqueda. Bloquear ClaudeBot no bloquea a los otros dos. Los tres respetan robots.txt y aceptan Crawl-delay.
- **Perplexity:** PerplexityBot (indexación) respeta robots.txt. Perplexity-User (recuperación en tiempo real) en general no lo aplica. El 4/8/2025 Cloudflare documentó que Perplexity usaba crawlers no declarados que se hacían pasar por Chrome en macOS (3-6 millones de solicitudes diarias) y la sacó de su lista de bots verificados.
- **Google-Extended:** no es un crawler sino un token. Controla el uso del contenido para entrenar Gemini y para el *grounding* en Gemini Apps y Vertex AI. **No afecta la inclusión en Google Search ni en AI Overviews/AI Mode**, que dependen de Googlebot. Para limitar lo que se muestra en funciones de IA de Search, las herramientas son nosnippet, data-nosnippet, max-snippet o noindex.
- **Riesgo oculto:** muchos sitios bloquean bots de IA sin saberlo por reglas de Cloudflare, WAF o rate limits (errores 429). Hay que revisarlo en el hosting de Lezac, además del robots.txt.

**robots.txt recomendado para lezacconsultoria.com** (decisión de negocio: Lezac *quiere* que los modelos la conozcan, así que se permite también el entrenamiento):

```
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: GPTBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: *
Disallow: /wp-admin/
Sitemap: https://lezacconsultoria.com/sitemap.xml
```

**llms.txt mínimo (opcional):** nombre, una línea de qué hace Lezac, los 3 servicios con URL y una línea de alcance cada uno, países atendidos, cifras verificadas (+Clientes Activos: 15-30% de incremento de clientes activos en 60 días como resultado histórico, meta orientativa de 10-15%), contacto y enlace a la página Partner.

### 2. Panorama competitivo actualizado

| Actor | ¿Activo en 2026? | Posicionamiento actual verificado | Cambio vs. auditoría | Implicancia para Lezac |
|---|---|---|---|---|
| **Delenio** (AR) | Sí | "Asistencia artificial" para decisiones comerciales en PyMEs. Consultoría comercial, CRM, chatbots, agentes de IA. Su fundador Emiliano Marchiori tiene prensa en Revista Mercado y columnas en El Cronista (2026). | Giró fuerte hacia la narrativa de IA. | Es el competidor narrativo más cercano. Lezac se diferencia con datos de campo (PDV, rutas) y garantías de plazo. |
| **KIRI / KIRI Ventas** (Córdoba, est. 2012) | Sí, en expansión | Suite de ventas y logística: app de ventas, ruteo LogisticO2, B2B, SmartPanel de KPIs, gamificación y un servicio "KIRI Asesoría". Su home dice "más de 350 clientes en 8 países" (la meta description dice 300: dato inconsistente en su propio sitio). Ganó CCU Innpacta 2026 (US$10.000 y piloto con CCU). | Suma asesoría y gamificación. Hace SEO comparativo agresivo contra Nextbyn, Persat, Mobiliza y Axxum. | Es software, no consultoría. Para Lezac puede ser un potencial aliado o partner más que un rival directo. |
| **Nextbyn** (Rosario) | Sí | CHESS ERP/Suite para distribuidoras de consumo masivo y Consolido (sell-in/sell-out, Power BI) para compañías. Dice tener "+1.000 empresas en +10 países". Ser Industria reportó facturación de más de US$10 millones, 75% de clientes argentinos. | Sin cambio de fondo. | Es ERP. Compite por el presupuesto de "tecnología comercial", no por el servicio. |
| **Marketech LATAM** | Sí | Se presenta como "primera agencia de agentes de IA en LATAM" (multi-agente, AutoGen/CrewAI). Declara "+150 empresas" y "ROI 500%+" (cifras de marketing no verificadas). | Pivote total a agentes de IA genéricos. | Compite con IA a Medida solo en búsquedas genéricas de "IA para empresas". No tiene foco en distribución. |
| **Affinitit** | Sí | Consultora boutique B2B: sistema comercial con IA en 4 semanas, scorecard ASCENDER®, Fractional CMO, agentes sobre HubSpot/Make. | Foco en pipeline B2B consultivo. | Otro ICP (ventas consultivas, CRM). Poca superposición con distribuidoras de PDV. |
| **Elit Latam** | Sí | **Mayorista/distribuidor de tecnología** desde 1989 (HP, Logitech), con warehouse en Doral y presencia en más de 30 países. | **No es competidor.** Probable error de clasificación de la auditoría. | Sacarlo del mapa competitivo. En todo caso es un ejemplo de ICP (mayorista). |
| **Galo AI** (nuevo, 2025-2026) | Sí | CRM con IA sobre WhatsApp para distribuidoras y mayoristas: toma de pedidos, recuperación de inactivos, predicción de recompra. Fundada en 2025, según Revista Mercado "trabaja con más de 50 clientes activos y gestiona más de US$ 5 millones mensuales" en AR/MX/CO/UY; su CEO Tomás Iakub sostiene que "WhatsApp ya concentra más del 60% del retail mayorista". Según la empresa, las recomendaciones suben las ventas entre 5% y 15% (dato propio, no auditado). | **Nuevo competidor relevante** en el discurso de "recuperar clientes inactivos". | Refuerza la urgencia de que +Clientes Activos se posicione con su método de campo (censo + ruteo) y con la prueba social verificada. |
| **Quadminds** | Sí | TMS de distribución con un "Dashboard Comercial" y contenido de blog titulado "Inteligencia Comercial en Distribución". | Compite por la keyword. | Disputa SERP en "inteligencia comercial distribución". |
| **Software de preventa** (Cair, Venttu, bcnsoft, Líder Gestión, Farandsoft) | Sí | Apps de preventa con facturación ARCA, trabajo offline y ruteo. | Mucho contenido SEO sobre "preventa" y "software para distribuidoras". | Lezac no tiene que pelear esas keywords de producto. Le conviene capturar el "después de tener el sistema, ¿cómo vendo más?". |
| **Censo de PDV** (CityTroops, Dichter & Neira "Locator") | Sí | Censos de puntos de venta para marcas y trade marketing. | Competencia indirecta para el censo digital. | Lezac se diferencia por el plazo garantizado (100 PDV en 7 días) y por integrar el censo al ruteo. |

### 3. Keywords objetivo por sección

**Advertencia metodológica:** no pude validar volúmenes de búsqueda con una herramienta de keywords. La lista sale del lenguaje real que usan los competidores y el sector en 2026 ("software para distribuidoras", "preventistas", "censo de puntos de venta", "ruta de ventas", "inteligencia comercial en distribución", "facturación ARCA", "clientes inactivos"). Antes de cerrar la arquitectura hay que validar volumen y dificultad en Google Keyword Planner (Argentina) y Search Console. La guía de Google de mayo 2026 dice que la IA entiende sinónimos, así que no hace falta una página por variante: cada página cubre su cluster de forma natural.

| Sección | Keyword principal | Long-tail (Argentina) | Variante dolor | Variante solución | Secundario PY/BO/UY |
|---|---|---|---|---|---|
| **Inicio** | consultora de inteligencia comercial para distribuidoras | consultoría comercial para mayoristas y distribuidoras pymes; cómo vender más en una distribuidora; consultora para fábricas pymes de alimentos | "mi distribuidora no crece", "tengo vendedores pero no crecen los clientes" | "aumentar clientes activos distribuidora", "ordenar el área comercial de una pyme" | consultora comercial distribuidoras Paraguay / Uruguay / Bolivia |
| **Brújula Comercial** | inteligencia comercial para pymes | análisis de datos de ventas para distribuidoras; qué clientes dejaron de comprarme; tablero comercial para mayoristas; análisis de cartera de clientes | "clientes que dejaron de comprar", "no sé qué clientes me rinden", "el vendedor dice que el cliente no quiere" | "detectar clientes en riesgo", "rentabilidad por cliente y vendedor", "sistema de inteligencia comercial" | inteligencia comercial Paraguay pymes |
| **+Clientes Activos** | aumentar clientes activos distribuidora | geolocalización de clientes; censo de puntos de venta; ruteo comercial de preventistas; expansión territorial distribuidora; cobertura de zona | "zonas sin cubrir", "preventistas que visitan siempre a los mismos", "costo logístico alto por cliente" | "optimizar rutas de preventa", "mapa de clientes y potenciales", "censo de comercios por zona" | censo de puntos de venta Bolivia / Paraguay |
| **IA Aplicada** | inteligencia artificial aplicada a pymes | automatizar tareas administrativas pyme; IA para distribuidoras; automatizar pedidos por WhatsApp; IA a medida para empresas Argentina | "perdemos horas cargando pedidos", "planillas de Excel que nadie entiende", "cuello de botella en administración" | "automatización con IA a medida", "victoria rápida con IA en 15 días", "diagnóstico de IA gratuito" | inteligencia artificial para empresas Uruguay |
| **Partner** | programa de partners consultoría | programa de referidos B2B Argentina; ganar comisión por recomendar clientes; alianzas para contadores y consultores; referir empresas y cobrar comisión | "tengo clientes con problemas comerciales y no sé a quién derivarlos" | "comisión por referido", "programa de aliados para contadores" | programa de referidos Paraguay / Uruguay |

**Recomendación de nomenclatura:** el menú dice "IA Aplicada" y el servicio se llama "IA a Medida". Hay que unificar. Sugiero URL /ia-aplicada, H1 con "IA a medida" y ambas expresiones en el texto, para que la entidad del servicio sea una sola.

### 4. Sección Partner: qué hacen los programas reales en LATAM

| Programa | Tipos de partner | Beneficio publicado | Reglas destacables |
|---|---|---|---|
| **Quilsoft** (AR, consultora IT) | Consultoras de gestión, agencias, estudios contables | Comisión por proyecto referido, pagada en un máximo de 30 días desde que Quilsoft cobra al cliente. Sin costo de ingreso ni cuotas. | Proceso en 5 pasos. Reunión conjunta con el cliente. "Vos referís, nosotros implementamos, y ambos ganamos." Portal de partners. |
| **SimpliRoute** (logística LATAM) | Revendedor y Referidor | Revendedor: hasta 20% en los primeros 12 meses y 10% después. Referidor empresa: 7-10% durante 12 meses. Referidor individual: 50% del primer mes. En el blog: "hasta U$500". | El referidor tiene que confirmar que el referido sabe que lo van a contactar. Hay términos y condiciones separados. |
| **Q10** (LATAM) | Referidor, que puede ascender a Revendedor | Referidor: 15% de la venta nueva y 10% de las renovaciones. Revendedor: 30%/20%. | Comisión sobre lo efectivamente recaudado. Oportunidad protegida 180 días. Hay que seguir activo (1 negocio cada 365 días). |
| **Tiendanube** (AR) | Niveles Silver a Blue Titanium | 20% recurrente (30% en plan Evolución) + US$25 por activaciones. | Oportunidad a cerrar en 90 días. Si dos agencias refieren al mismo cliente, gana la que el cliente elija por escrito. Saldos no retirados caducan a los 12 meses. Factura como monotributista o responsable inscripto. |
| **Alegra / Contabilium** | Referidor e Implementador | Comisión recurrente (sin % público). Alegra: mínimo de pago US$200. | Link de partner para atribución. Sin permanencia. Alta en 1-3 semanas. |

**Estructura recomendada para /partner:**

1. **H1 + BLUF:** "Programa de Partners Lezac: recomendá a una distribuidora o fábrica pyme y cobrá una comisión cuando el proyecto se concreta."
2. **Para quién es:** contadores y estudios contables, consultores de gestión, proveedores de software (ERP, preventa, ruteo), ex gerentes comerciales, proveedores y fabricantes que venden a distribuidoras.
3. **Dos niveles:** *Referidor* (presenta y participa de la primera reunión) y *Aliado* (acompaña el proyecto y co-vende; comisión mayor).
4. **Beneficio:** mostrar la estructura de comisión de forma explícita. **[PLACEHOLDER a definir por Leandro: % por servicio.]** Como referencia de mercado, los programas relevados pagan entre 7% y 20% recurrente o un único pago en el primer mes.
5. **Cómo funciona en 4 pasos:** registrás el contacto → reunión conjunta → propuesta de Lezac → cobrás cuando Lezac cobra.
6. **Reglas claras:** ventana de protección del referido (sugerido: 90-180 días), comisión sobre lo efectivamente cobrado, pago a 30 días, factura del partner, conflicto resuelto por elección escrita del cliente, requisito de consentimiento del referido.
7. **Qué servicios podés recomendar:** con criterios de elegibilidad (por ejemplo, +Clientes Activos requiere al menos 300 PDV en base histórica).
8. **FAQ + formulario corto** (nombre, empresa, rubro, cómo conocés a tus clientes).

Un matiz importante: Brújula Comercial es una relación continua. Hay que decidir si la comisión es única o recurrente por X meses, porque es la pregunta número uno que va a hacer un contador.

### 5. Meta titles, meta descriptions y encabezados

Solo se usan cifras verificadas. Los placeholders van marcados.

**Inicio**
- **Title:** Consultora de inteligencia comercial para distribuidoras | Lezac
- **Meta description:** Ayudamos a distribuidoras, mayoristas y fábricas pyme a sumar clientes activos con datos de sus ventas y trabajo de campo. +10 años, +100 empresas en AR, PY, BO y UY.
- **H1:** Más clientes activos para tu distribuidora, con datos de tus propias ventas
- H2: Qué hacemos (en una frase) → H3 por servicio: Brújula Comercial / +Clientes Activos / IA Aplicada
- H2: Resultados reales de clientes → H3: Distribución de consumo masivo (Buenos Aires): +20% productividad comercial, -15% costo logístico / H3: Fábrica de alimento balanceado (Buenos Aires): +15% ventas con la misma estructura, -20% costo logístico
- H2: Para quién trabajamos (facturación desde USD 100.000/mes, AR/PY/BO/UY)
- H2: Cómo empezamos a trabajar
- H2: Preguntas frecuentes
- H2: ¿Conocés una empresa que nos necesita? (enlace a Partner)

**Brújula Comercial**
- **Title:** Brújula Comercial: inteligencia comercial para pymes | Lezac
- **Meta description:** Sistema de inteligencia comercial sobre tu historial de ventas: qué clientes dejaron de comprar, quién rinde y dónde está la plata. Relación continua, no un informe.
- **H1:** Brújula Comercial: sabé qué clientes, productos y vendedores te hacen ganar plata
- H2: Qué es Brújula Comercial (definición de 2-3 líneas, formato BLUF)
- H2: Qué preguntas responde → H3: ¿Qué clientes dejaron de comprarme? / H3: ¿Qué vendedor sostiene la cartera? / H3: ¿Qué productos arrastran margen?
- H2: Qué datos necesitamos (los que ya tenés en tu sistema de facturación)
- H2: Por qué es una relación continua y no un proyecto
- H2: Resultados **[PLACEHOLDER: pedir a Leandro un caso con métricas propias de Brújula]**
- H2: Preguntas frecuentes

**+Clientes Activos**
- **Title:** +Clientes Activos: geolocalización, censo y ruteo comercial | Lezac
- **Meta description:** En 2 meses mapeamos tu cartera, censamos 100 PDV en 7 días y rediseñamos rutas. Históricamente, +15-30% de clientes activos en 60 días. Requiere 300+ PDV.
- **H1:** +Clientes Activos: más clientes comprando en 60 días, con tu misma estructura
- H2: Resultado histórico y meta del proyecto (15-30% histórico; meta orientativa 10-15%, no garantía)
- H2: Cómo funciona en 3 pasos → H3: Geolocalización de tu cartera histórica / H3: Censo digital de 100 PDV garantizado en 7 días / H3: Ruteo comercial
- H2: Casos reales (los dos casos verificados)
- H2: ¿Mi empresa califica? (mínimo 300 PDV en base histórica)
- H2: Cronograma de los 2 meses
- H2: Preguntas frecuentes

**IA Aplicada**
- **Title:** IA a medida para pymes: primera victoria en 15 días | Lezac
- **Meta description:** Detectamos un cuello de botella operativo y lo resolvemos con IA a medida. Relevamiento gratis, primera victoria en 15 días con garantía de 20 días hábiles. Desde USD 1.000.
- **H1:** IA aplicada a tu operación: resolvemos un cuello de botella concreto en 15 días
- H2: Qué es (y qué no es) IA a medida
- H2: Cómo trabajamos → H3: Reunión de relevamiento gratuita / H3: Victoria rápida en 15 días (garantía de 20 días hábiles) / H3: Proyecto de mayor alcance opcional (30-60 días)
- H2: Ejemplos de cuellos de botella que se pueden atacar (ejemplos genéricos claramente rotulados, **sin cifras de resultado**)
- H2: Precio: desde USD 1.000
- H2: Preguntas frecuentes

**Partner**
- **Title:** Programa de Partners: referí clientes y cobrá comisión | Lezac
- **Meta description:** ¿Conocés distribuidoras o fábricas pyme que necesitan vender más? Recomendalas a Lezac y cobrá una comisión cuando el proyecto se concreta. Reglas claras, pago a 30 días.
- **H1:** Programa de Partners Lezac: recomendá y ganá cuando tu cliente crece
- H2: Para quién es
- H2: Dos formas de participar → H3: Referidor / H3: Aliado
- H2: Cuánto y cuándo cobrás **[PLACEHOLDER %]**
- H2: Cómo funciona en 4 pasos
- H2: Reglas del programa
- H2: Qué empresas podés recomendar
- H2: Preguntas frecuentes

### 6. Bloques FAQ (en el lenguaje del dueño)

**Inicio**
1. ¿Qué hace exactamente Lezac? Nos metemos en los números de ventas y en la calle para que tu distribuidora, mayorista o fábrica sume clientes que compran seguido.
2. ¿Con qué tipo de empresa trabajan? Con distribuidoras, mayoristas y fábricas pyme que facturan desde USD 100.000 por mes, en Argentina, Paraguay, Bolivia y Uruguay.
3. ¿Tengo que cambiar mi sistema de facturación o comprar un software? No. Trabajamos con los datos que ya tenés.
4. ¿Cuánto tarda en verse algún resultado? Depende del servicio: +Clientes Activos se mide a los 60 días, y en IA Aplicada la primera victoria llega en 15 días.
5. ¿Ustedes venden software? No. Somos consultores. Usamos tecnología, pero lo que entregamos es un resultado comercial.
6. ¿Qué pasa si mi equipo de ventas es de la vieja escuela? Mejor: diseñamos todo para que lo use un preventista con experiencia, sin vueltas.

**Brújula Comercial**
1. ¿Qué es la inteligencia comercial, en criollo? Saber qué clientes te compran, cuáles dejaron de comprarte y por qué, antes de que te des cuenta por la caja.
2. ¿Qué datos necesitan? El historial de ventas de tu sistema de facturación o ERP: clientes, productos, fechas, montos y vendedor.
3. ¿Es un informe que me entregan y listo? No. Es una relación continua: los datos cambian todos los meses y las decisiones también.
4. ¿Sirve si mis datos están desordenados? Sí. Ordenarlos es parte del trabajo.
5. ¿En qué se diferencia de un tablero de Power BI? El tablero muestra números. Brújula te dice qué hacer con ellos esta semana.
6. ¿Cuánto cuesta? **[PLACEHOLDER: definir con Leandro si se publica un rango o "a consultar".]**

**+Clientes Activos**
1. ¿Qué resultado puedo esperar? Históricamente, nuestros clientes aumentaron entre 15% y 30% sus clientes activos en 60 días. En cada proyecto nuevo nos proponemos una meta orientativa de 10-15% en 2 meses (no es una garantía).
2. ¿Qué es un censo de puntos de venta y para qué me sirve? Es relevar comercio por comercio lo que hay en una zona: quién te compra, quién podría comprarte y quién le compra a la competencia. Nosotros censamos 100 PDV en 7 días, garantizado.
3. ¿Mi empresa califica? Necesitás al menos 300 puntos de venta en tu base histórica.
4. ¿Tengo que cambiar a mis preventistas? No. Les rediseñamos la ruta para que visiten mejor, no más.
5. ¿Qué pasa con el costo logístico? En los casos reales, el costo logístico bajó entre 15% y 20% con la misma estructura.
6. ¿Cuánto dura? Dos meses, con fecha de cierre.
7. ¿Sirve para Paraguay, Bolivia o Uruguay? Sí, trabajamos en los cuatro países.

**IA Aplicada**
1. ¿La IA me va a reemplazar gente? El foco es sacarle a tu equipo tareas repetitivas que hoy le comen horas.
2. ¿Tiene que ser algo comercial? No. Puede ser administración, pedidos, cobranzas, stock: cualquier cuello de botella puntual.
3. ¿Cuánto cuesta? Desde USD 1.000, según el alcance.
4. ¿Qué es la "victoria rápida"? Una primera solución funcionando en 15 días, con garantía de 20 días hábiles.
5. ¿Y si no sé qué necesito? Para eso está la reunión de relevamiento, que es gratuita.
6. ¿Necesito tener sistemas modernos? No necesariamente. Arrancamos con lo que ya usás (planillas, WhatsApp, tu sistema de gestión).

**Partner**
1. ¿Quién puede ser partner? Contadores, consultores, proveedores de software o insumos y cualquier persona que trate con dueños de distribuidoras o fábricas pyme.
2. ¿Cuánto cobro y cuándo? **[PLACEHOLDER %]** Cobrás cuando Lezac cobra al cliente, dentro de los 30 días.
3. ¿Tengo que vender yo? No. Vos presentás y nosotros hacemos la reunión, la propuesta y el proyecto.
4. ¿Cómo sé que el cliente queda a mi nombre? Lo registrás antes de la primera reunión y queda protegido durante **[PLACEHOLDER: 90-180 días]**.
5. ¿Qué pasa si el cliente ya estaba hablando con Lezac? Si ya estaba registrado, no genera comisión. Ante dudas, decide lo que el cliente informe por escrito.
6. ¿Tiene costo sumarse? No, es gratuito y sin permanencia.
7. ¿Tengo que facturar? Sí, como monotributista o responsable inscripto (o el equivalente en tu país).

## Recommendations

1. **Semana 1 (quick wins):** publicar el robots.txt propuesto, revisar reglas de Cloudflare/WAF, cargar el JSON-LD de Organization + Service y el BreadcrumbList, crear o verificar Google Business Profile y LinkedIn con los mismos datos (sameAs), y publicar un llms.txt mínimo.
2. **Semanas 2-4:** reescribir las 5 páginas con los H1 y FAQ de arriba. Cada página tiene que tener fecha de actualización visible y solo cifras verificadas.
3. **Mes 2:** lanzar /partner con los términos por escrito (PDF descargable) y un formulario de registro de referidos.
4. **Meses 2-6 (autoridad):** publicar 1 caso por trimestre con métricas auditables, conseguir menciones en prensa sectorial (Revista Mercado y El Cronista ya cubren a Delenio; Fortuna/Perfil publicó el 1/6/2026 una nota sobre Galo AI, que también tiene cobertura en El Cronista y Revista Mercado) y medir citas en ChatGPT, Perplexity y Gemini con prompts fijos.
5. **Descartar** de la auditoría previa: las cifras ilustrativas (+15% cobertura, 74%, -35%), Elit Latam como competidor y la creación de páginas por cada variante de keyword.

## Caveats

- No pude validar volúmenes de búsqueda. Las keywords son hipótesis basadas en el lenguaje del mercado y hay que confirmarlas en Keyword Planner y Search Console.
- Las cifras de competidores (KIRI 300 vs. 350 clientes, Nextbyn +1.000 empresas, Marketech "ROI 500%+", Galo AI 5-15% de aumento de ventas) son autodeclaradas y no están auditadas.
- Algunos datos técnicos (estudios de Ahrefs, SE Ranking, Limy; cambios en la documentación de OpenAI) vienen de fuentes secundarias del sector SEO que reportan la documentación oficial. La documentación de los proveedores cambia seguido, así que conviene revisar robots.txt cada trimestre.
- En SimpliRoute no se pudieron leer los términos y condiciones completos. Las comisiones publicadas pueden ser de 2024.
- IA Aplicada no tiene caso propio con métricas: no publicar cifras de resultado hasta tenerlas.