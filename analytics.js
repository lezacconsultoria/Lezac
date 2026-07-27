/**
 * Lezac Consultoria — Google Analytics 4
 * Cargar en el <head> de todas las páginas: <script src="analytics.js"></script>
 *
 * ID de medición: GA4 → Admin → Flujos de datos → Web.
 */

var GA4_ID = 'G-ESN0ZJP0GN';

(function () {
  if (!/^G-[A-Z0-9]+$/.test(GA4_ID)) return;

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', GA4_ID);

  document.addEventListener('DOMContentLoaded', function () {
    var page = document.documentElement.dataset.page || 'success';

    // Clicks en WhatsApp y Calendly (delegado: cubre nav/footer inyectados por shared.js)
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      var href = a.getAttribute('href') || '';

      if (href.indexOf('whatsapp.com') !== -1 || href.indexOf('wa.me') !== -1) {
        window.gtag('event', 'contacto_whatsapp', { pagina: page, ubicacion: a.textContent.trim().slice(0, 40) });
      } else if (href.indexOf('calendly.com') !== -1) {
        window.gtag('event', 'agendar_reunion', { pagina: page, ubicacion: a.textContent.trim().slice(0, 40) });
      }
    }, true);

    // Conversión confirmada (página de gracias post-Calendly)
    if (/success/.test(location.pathname)) {
      window.gtag('event', 'generate_lead', { pagina: 'success', metodo: 'calendly' });
    }
  });
})();
