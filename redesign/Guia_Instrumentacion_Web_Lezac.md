# Guía de instrumentación — Relanzamiento web Lezac Consultoría

Este documento explica para qué sirve cada uno de los dos documentos del proyecto y en qué orden y forma pasárselos al programador. No agrega contenido nuevo — es el mapa de uso de los otros dos.

## Los dos documentos

| | **Documento 1** — Auditoría SEO/GEO | **Documento 2** — Copy del sitio |
|---|---|---|
| **Nombre de archivo** | Relanzamiento web de Lezac Consultoría: GEO/SEO, keywords, programa Partner y competencia | Copy del sitio web — Lezac Consultoría (5 secciones) |
| **Qué es** | Configuración técnica e infraestructura: qué permitir en robots.txt, qué marcado de datos estructurados (schema.org) usar, si conviene un llms.txt, y por qué. Incluye también la investigación de fondo (competencia, keywords, estructura de la sección Partner). | El texto final, ya redactado, de las 5 páginas del sitio: Inicio, Brújula Comercial, +Clientes Activos, IA Aplicada y Partner. Títulos, meta description, H1/H2/H3, cuerpo y FAQ. |
| **A quién se lo mostrás** | Al programador (o a quien administre el hosting/CMS), para que configure el sitio. | Al programador (para que cargue el contenido) y a quien vaya a maquetar/diseñar cada sección. |
| **Qué hace el programador con él** | Copia y pega el robots.txt propuesto, agrega el JSON-LD de Organization y Service con `areaServed`, decide si sube el llms.txt, y revisa que el hosting/CDN no esté bloqueando bots de IA (Cloudflare, WAF). | Carga el texto tal cual en cada sección — no tiene que interpretarlo, resumirlo ni reescribirlo. Respeta la jerarquía de encabezados (H1 único por página, H2 y H3 en el orden dado) porque eso también es parte del SEO. |
| **Cuándo se usa** | Al principio del proyecto, en paralelo a lo demás — no depende del copy final. | Cuando el copy esté cerrado (sin placeholders pendientes) y el diseño de cada página esté definido. |
| **Contiene texto para publicar?** | No. Es configuración y estrategia. | Sí, íntegramente. |

## Orden de entrega al programador

1. **Ahora:** pasale el Documento 1. Que arranque con robots.txt, el schema JSON-LD y la revisión del hosting — es trabajo técnico que no frena a nadie mientras se termina de cerrar el copy.
2. **Antes de pasar el Documento 2:** cerrá con Leandro los 4 placeholders que quedaron pendientes (ver la tabla al final del Documento 2 — precio de Brújula Comercial, caso con métricas propias de Brújula, % de comisión de Partner, ventana de protección del contacto). Ninguno debería llegar al programador sin resolver.
3. **Cuando el copy esté cerrado:** pasale el Documento 2 junto con el diseño/maqueta de cada sección (si ya existe) o dejá que el programador maquete usando la jerarquía de encabezados del documento como guía de estructura.
4. **Después de publicar:** volvé al Documento 1 para la Fase 3 (autoridad y menciones externas) — es la única parte que sigue corriendo después del lanzamiento, no es tarea del programador.

## Una frase para resumir

El Documento 1 le dice al programador **cómo tiene que configurar el sitio** para que Google y las plataformas de IA lo entiendan. El Documento 2 le dice **qué texto exacto poner** en cada sección. Uno es infraestructura, el otro es contenido — y conviene pasárselos en ese orden, no juntos.
