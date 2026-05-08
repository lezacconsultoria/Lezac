/**
 * Lezac Consultoria — Shared Components
 * Nav, Footer y utilidades comunes para todas las páginas
 */

// ─── NAV HTML ────────────────────────────────────────────────────────────────

function getLezacNav() {
  return `
<nav id="lezac-nav" class="fixed top-0 left-0 right-0 z-50 px-4 md:px-8 lg:px-12" style="background: rgba(10,10,11,0.85); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(255,255,255,0.05);">
  <div class="max-w-7xl mx-auto flex items-center justify-between h-16">

    <!-- Logo -->
    <a href="./" class="flex items-center group">
      <img src="./Logo Lezac (500 x 500 px) (3).png" alt="Lezac Consultoría" class="h-10 w-auto" />
    </a>

    <!-- Desktop Nav Links -->
    <div class="hidden md:flex items-center gap-1">
      <a href="./" data-nav="home" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Inicio</a>
      <a href="./smart-brujula" data-nav="brujula" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Smart Brújula</a>
      <a href="./wa-smart-ventas" data-nav="wa" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">WA Smart Ventas</a>
      <a href="./censo-comercial" data-nav="censo" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Censo</a>
      <a href="./geolocalizacion" data-nav="geo" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Geolocalización</a>
      <a href="./ruteo-comercial" data-nav="ruteo" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Ruteo</a>
    </div>

    <!-- Desktop CTAs -->
    <div class="hidden md:flex items-center gap-3">
      <a href="https://api.whatsapp.com/send?phone=5491154107921&text=%E2%9C%85%20Lezac%20Consultoria%20I%20Me%20interesa%20conocer%20m%C3%A1s%20de%20sus%20servicios." target="_blank" rel="noopener" class="flex items-center gap-2 px-4 py-2 text-xs font-body font-semibold tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white" style="border: 1px solid rgba(255,255,255,0.1);">
        Agendar diagnóstico
      </a>
      <a href="https://api.whatsapp.com/send?phone=5491154107921&text=%E2%9C%85%20Lezac%20Consultoria%20I%20Me%20interesa%20conocer%20m%C3%A1s%20de%20sus%20servicios." target="_blank" rel="noopener" class="flex items-center justify-center w-9 h-9 rounded-full transition-all duration-200 hover:scale-110" style="background: rgba(37,211,102,0.15); color: #25D366;" title="WhatsApp">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
          <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
      </a>
    </div>

    <!-- Mobile Hamburger -->
    <button id="nav-toggle" class="md:hidden flex flex-col gap-1.5 p-2" aria-label="Menú">
      <span class="hamburger-line block w-5 h-0.5 bg-white transition-all duration-300"></span>
      <span class="hamburger-line block w-5 h-0.5 bg-white transition-all duration-300"></span>
      <span class="hamburger-line block w-5 h-0.5 bg-white transition-all duration-300"></span>
    </button>
  </div>

  <!-- Mobile Menu -->
  <div id="mobile-menu" class="md:hidden hidden pb-4 border-t border-white/5 mt-1">
    <div class="flex flex-col gap-1 pt-3">
      <a href="./" data-nav="home" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Inicio</a>
      <a href="./smart-brujula" data-nav="brujula" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Smart Brújula Comercial</a>
      <a href="./wa-smart-ventas" data-nav="wa" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">WA Smart Ventas</a>
      <a href="./censo-comercial" data-nav="censo" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Censo Comercial</a>
      <a href="./geolocalizacion" data-nav="geo" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Geolocalización de Clientes</a>
      <a href="./ruteo-comercial" data-nav="ruteo" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Ruteo Comercial</a>
      <div class="mt-3 px-4">
        <a href="https://api.whatsapp.com/send?phone=5491154107921&text=%E2%9C%85%20Lezac%20Consultoria%20I%20Me%20interesa%20conocer%20m%C3%A1s%20de%20sus%20servicios." target="_blank" rel="noopener" class="block w-full text-center px-4 py-3 text-sm font-semibold rounded transition-all" style="background: var(--color-accent, #8C52FF); color: white;">
          Agendar diagnóstico
        </a>
      </div>
    </div>
  </div>
</nav>
`;
}

// ─── FOOTER HTML ─────────────────────────────────────────────────────────────

function getLezacFooter() {
  return `
<footer id="lezac-footer" class="relative mt-20 border-t border-white/5" style="background: #050506;">
  <div class="max-w-7xl mx-auto px-4 md:px-8 lg:px-12 py-16">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">

      <!-- Brand Column -->
      <div class="space-y-4">
        <div class="flex items-center">
          <img src="./Logo Lezac (500 x 500 px) (3).png" alt="Lezac Consultoría" class="h-10 w-auto" />
        </div>
        <p class="text-[10px] font-semibold uppercase tracking-widest" style="color: rgba(255,255,255,0.25);">Consultoría Comercial B2B · LATAM</p>
        <p class="text-sm text-on-surface-variant leading-relaxed max-w-xs">
          Consultoría Comercial B2B especializada en distribuidoras, mayoristas y fábricas.
        </p>
        <div class="flex flex-wrap gap-2 pt-2">
          <span class="text-xs text-on-surface-variant px-2 py-1 rounded" style="background: rgba(255,255,255,0.04);">Argentina</span>
          <span class="text-xs text-on-surface-variant px-2 py-1 rounded" style="background: rgba(255,255,255,0.04);">Paraguay</span>
          <span class="text-xs text-on-surface-variant px-2 py-1 rounded" style="background: rgba(255,255,255,0.04);">Bolivia</span>
          <span class="text-xs text-on-surface-variant px-2 py-1 rounded" style="background: rgba(255,255,255,0.04);">Uruguay</span>
        </div>
      </div>

      <!-- Services Column -->
      <div class="space-y-4">
        <h4 class="text-xs font-body font-semibold tracking-widest uppercase text-on-surface-variant">Servicios</h4>
        <ul class="space-y-2.5">
          <li><a href="./smart-brujula" class="text-sm text-on-surface-variant hover:text-white transition-colors flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#25F5A4;"></span>Smart Brújula Comercial
          </a></li>
          <li><a href="./wa-smart-ventas" class="text-sm text-on-surface-variant hover:text-white transition-colors flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#25D366;"></span>WA Smart Ventas
          </a></li>
          <li><a href="./censo-comercial" class="text-sm text-on-surface-variant hover:text-white transition-colors flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#B08AFF;"></span>Censo Comercial
          </a></li>
          <li><a href="./geolocalizacion" class="text-sm text-on-surface-variant hover:text-white transition-colors flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#38BDF8;"></span>Geolocalización de Clientes
          </a></li>
          <li><a href="./ruteo-comercial" class="text-sm text-on-surface-variant hover:text-white transition-colors flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#F97316;"></span>Ruteo Comercial
          </a></li>
          <li><a href="./partners" class="text-sm text-on-surface-variant hover:text-white transition-colors flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#F5C842;"></span>Partners
          </a></li>
        </ul>
      </div>

      <!-- Contact Column -->
      <div class="space-y-4" id="contacto">
        <h4 class="text-xs font-body font-semibold tracking-widest uppercase text-on-surface-variant">Contacto</h4>
        <p class="text-sm text-on-surface-variant">¿Listo para ordenar tu gestión comercial?</p>
        <div class="space-y-3">
          <a href="https://api.whatsapp.com/send?phone=5491154107921&text=%E2%9C%85%20Lezac%20Consultoria%20I%20Me%20interesa%20conocer%20m%C3%A1s%20de%20sus%20servicios." target="_blank" rel="noopener" class="flex items-center gap-3 px-4 py-3 rounded text-sm font-semibold text-black transition-all hover:opacity-90" style="background: var(--color-accent, #8C52FF); color: white;">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
            Agendar diagnóstico
          </a>
          <a href="https://api.whatsapp.com/send?phone=5491154107921&text=%E2%9C%85%20Lezac%20Consultoria%20I%20Me%20interesa%20conocer%20m%C3%A1s%20de%20sus%20servicios." target="_blank" rel="noopener" class="flex items-center gap-3 px-4 py-3 rounded text-sm font-medium text-white transition-all hover:bg-white/5" style="border: 1px solid rgba(255,255,255,0.1);">
            <svg class="w-4 h-4" style="color:#25D366;" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Hablar por WhatsApp
          </a>
        </div>
        <a href="https://www.linkedin.com/company/lezac-consultoria" target="_blank" rel="noopener" class="inline-flex items-center gap-2 text-xs text-on-surface-variant hover:text-white transition-colors mt-2">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          LinkedIn
        </a>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="pt-8 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4">
      <p class="text-xs text-on-surface-variant">© 2025 Lezac Consultoria. Todos los derechos reservados.</p>
      <div class="flex items-center gap-6">
        <a href="#" class="text-xs text-on-surface-variant hover:text-white transition-colors">Privacidad</a>
        <a href="#" class="text-xs text-on-surface-variant hover:text-white transition-colors">Términos</a>
      </div>
    </div>
  </div>
</footer>
`;
}

// ─── CLIENTES MARQUEE DATA ────────────────────────────────────────────────────

const LEZAC_CLIENTS = [
  'Bacardi', 'Distribuidora Gloria', 'Codisa', 'Indega', 'Pluscar',
  'McCain', 'Vaca Fría', 'Iglú', 'Vitalcan', 'Madersa',
  'Transporte Bogdan', 'Comercial Baci', 'Termoplástica', 'Alco Distribuciones',
  'Proquim', 'Weilen'
];

function getMarqueeHTML() {
  const items = [...LEZAC_CLIENTS, ...LEZAC_CLIENTS]
    .map(name => `<span class="whitespace-nowrap text-sm font-body font-medium text-on-surface-variant tracking-wide flex items-center gap-3">
      <span class="w-1 h-1 rounded-full inline-block opacity-40" style="background: var(--color-accent, #8C52FF);"></span>
      ${name}
    </span>`)
    .join('');

  return `
<div class="lezac-marquee-wrapper overflow-hidden py-1" aria-label="Empresas clientes">
  <div class="lezac-marquee-track flex gap-8 items-center" style="width: max-content; animation: lezac-marquee 50s linear infinite;">
    ${items}
  </div>
</div>
`;
}

// ─── INIT FUNCTIONS ───────────────────────────────────────────────────────────

function initActiveNav() {
  const page = document.documentElement.dataset.page || '';
  const navLinks = document.querySelectorAll('.nav-link[data-nav]');
  navLinks.forEach(link => {
    const target = link.dataset.nav;
    const isActive = target === page;
    if (isActive) {
      link.style.color = 'var(--color-accent, #8C52FF)';
      link.style.borderBottom = '1px solid var(--color-accent, #8C52FF)';
      link.style.paddingBottom = '2px';
    }
  });
}

function initHamburger() {
  const toggle = document.getElementById('nav-toggle');
  const menu = document.getElementById('mobile-menu');
  if (!toggle || !menu) return;
  toggle.addEventListener('click', () => {
    const isOpen = !menu.classList.contains('hidden');
    menu.classList.toggle('hidden', isOpen);
    const lines = toggle.querySelectorAll('.hamburger-line');
    if (!isOpen) {
      lines[0].style.transform = 'translateY(8px) rotate(45deg)';
      lines[1].style.opacity = '0';
      lines[2].style.transform = 'translateY(-8px) rotate(-45deg)';
    } else {
      lines.forEach(l => { l.style.transform = ''; l.style.opacity = ''; });
    }
  });
}

function initMarquees() {
  const wrappers = document.querySelectorAll('.lezac-marquee-wrapper');
  wrappers.forEach(wrapper => {
    wrapper.addEventListener('mouseenter', () => {
      const track = wrapper.querySelector('.lezac-marquee-track');
      if (track) track.style.animationPlayState = 'paused';
    });
    wrapper.addEventListener('mouseleave', () => {
      const track = wrapper.querySelector('.lezac-marquee-track');
      if (track) track.style.animationPlayState = 'running';
    });
  });
}

function initScrollReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('lezac-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  );
  document.querySelectorAll('.lezac-reveal').forEach(el => observer.observe(el));
}

// ─── MARQUEE CSS ──────────────────────────────────────────────────────────────

function injectSharedStyles() {
  const style = document.createElement('style');
  style.textContent = `
    @keyframes lezac-marquee {
      from { transform: translateX(0); }
      to   { transform: translateX(-50%); }
    }
    .lezac-reveal {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .lezac-visible {
      opacity: 1;
      transform: translateY(0);
    }
    #lezac-nav .nav-link {
      border-bottom: 1px solid transparent;
    }
  `;
  document.head.appendChild(style);
}

// ─── VSL AUTOPLAY MUTED ───────────────────────────────────────────────────────

function initVSL() {
  document.querySelectorAll('iframe[src*="youtube.com/embed"]').forEach(iframe => {
    const url = new URL(iframe.src);
    url.searchParams.set('autoplay', '1');
    url.searchParams.set('mute', '1');
    url.searchParams.set('enablejsapi', '1');
    iframe.src = url.toString();

    const container = iframe.parentElement;
    if (!container) return;

    const overlay = document.createElement('div');
    overlay.style.cssText = 'position:absolute;inset:0;z-index:10;cursor:pointer;display:flex;align-items:flex-end;justify-content:flex-start;padding:16px;';
    overlay.innerHTML = `
      <div style="display:flex;align-items:center;gap:8px;background:rgba(0,0,0,0.65);backdrop-filter:blur(10px);border-radius:9999px;padding:8px 14px;border:1px solid rgba(255,255,255,0.12);transition:opacity 0.2s;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="white" style="flex-shrink:0"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
        <span style="font-size:11px;font-weight:600;color:white;letter-spacing:0.06em;text-transform:uppercase;font-family:Inter,sans-serif;">Activar sonido</span>
      </div>`;

    overlay.addEventListener('click', () => {
      overlay.remove();
      iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'unMute', args: [] }), '*');
      iframe.contentWindow.postMessage(JSON.stringify({ event: 'command', func: 'setVolume', args: [100] }), '*');
    });

    container.appendChild(overlay);
  });
}

// ─── BOOTSTRAP ───────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  injectSharedStyles();

  // Inject nav before first child of body
  const navWrapper = document.createElement('div');
  navWrapper.innerHTML = getLezacNav();
  document.body.insertBefore(navWrapper.firstElementChild, document.body.firstChild);

  // Inject footer at end of body
  const footerWrapper = document.createElement('div');
  footerWrapper.innerHTML = getLezacFooter();
  document.body.appendChild(footerWrapper.firstElementChild);

  // Inject marquees
  document.querySelectorAll('[data-lezac-marquee]').forEach(el => {
    el.innerHTML = getMarqueeHTML();
  });

  // Add padding-top to first section to account for fixed nav
  const firstSection = document.querySelector('main, section, .hero-section, [data-hero]');
  if (firstSection && !firstSection.dataset.noPad) {
    firstSection.style.paddingTop = Math.max(
      parseInt(getComputedStyle(firstSection).paddingTop || '0') + 64,
      80
    ) + 'px';
  }

  initActiveNav();
  initHamburger();
  initMarquees();
  initScrollReveal();
  initVSL();
});
