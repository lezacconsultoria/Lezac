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
      <a href="./smart-brujula" data-nav="brujula" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Brújula Comercial</a>
      <a href="./wa-smart-ventas" data-nav="wa" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">WA Ventas</a>
      <a href="./censo-comercial" data-nav="censo" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Censo</a>
      <a href="./geolocalizacion" data-nav="geo" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Geolocalización</a>
      <a href="./ruteo-comercial" data-nav="ruteo" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white">Ruteo</a>
      <a href="./partners" data-nav="partners" class="nav-link px-3 py-1.5 text-xs font-body font-medium tracking-wide rounded transition-all duration-200 hover:text-white" style="color:#F5C842">Partners</a>
    </div>

    <!-- Desktop CTAs -->
    <div class="hidden md:flex items-center gap-3">
      <a href="https://calendly.com/asesoriacomercial" target="_blank" rel="noopener" class="flex items-center gap-2 px-4 py-2 text-xs font-body font-semibold tracking-wide rounded transition-all duration-200 text-on-surface-variant hover:text-white" style="border: 1px solid rgba(255,255,255,0.1);">
        Agendar Reunión
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
      <a href="./smart-brujula" data-nav="brujula" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Brújula Comercial</a>
      <a href="./wa-smart-ventas" data-nav="wa" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">WA Ventas</a>
      <a href="./censo-comercial" data-nav="censo" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Censo Comercial</a>
      <a href="./geolocalizacion" data-nav="geo" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Geolocalización de Clientes</a>
      <a href="./ruteo-comercial" data-nav="ruteo" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium text-on-surface-variant hover:text-white hover:bg-surface-container rounded transition-all">Ruteo Comercial</a>
      <a href="./partners" data-nav="partners" class="nav-link mobile-nav-link px-4 py-3 text-sm font-body font-medium hover:bg-surface-container rounded transition-all" style="color:#F5C842">Partners</a>
      <div class="mt-3 px-4">
        <a href="https://calendly.com/asesoriacomercial" target="_blank" rel="noopener" class="block w-full text-center px-4 py-3 text-sm font-semibold rounded transition-all" style="background: var(--color-accent, #8C52FF); color: white;">
          Agendar Reunión
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
            <span class="w-1.5 h-1.5 rounded-full inline-block" style="background:#25F5A4;"></span>Brújula Comercial
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
          <a href="https://calendly.com/asesoriacomercial" target="_blank" rel="noopener" class="flex items-center gap-3 px-4 py-3 rounded text-sm font-semibold text-black transition-all hover:opacity-90" style="background: var(--color-accent, #8C52FF); color: white;">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
            Agendar Reunión
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

// ─── TOOLS MARQUEE DATA ───────────────────────────────────────────────────────

const LEZAC_TOOLS = [
  { name: 'Power BI',     file: 'logos-trabajo/1200px-Power_bi_logo_black.svg_-300x300.png' },
  { name: 'SAP',          file: 'logos-trabajo/sap-300x100.png' },
  { name: 'Meta',         file: 'logos-trabajo/Meta_logo.png' },
  { name: 'Odoo',         file: 'logos-trabajo/odo-300x167.png' },
  { name: 'n8n',          file: 'logos-trabajo/n8n-color.png' },
  { name: 'Shopify',      file: 'logos-trabajo/shopi-300x169.png' },
  { name: 'Contabilium',  file: 'logos-trabajo/logo_contabilium.png' },
  { name: 'Auto',         file: 'logos-trabajo/auto-300x300.png' },
  { name: 'Hostinger',    file: 'logos-trabajo/Hostinger_Logo.png' },
];

function getToolsMarqueeHTML() {
  const items = [...LEZAC_TOOLS, ...LEZAC_TOOLS]
    .map(t => `<span class="flex items-center gap-2 px-4">
      <img src="./${t.file}" alt="${t.name}" title="${t.name}"
        style="height:28px;max-width:90px;object-fit:contain;filter:grayscale(1) brightness(2) opacity(0.45);" />
    </span>`)
    .join('');

  return `
<div class="lezac-marquee-wrapper overflow-hidden py-1" aria-label="Herramientas">
  <div class="lezac-marquee-track flex gap-6 items-center" style="width: max-content; animation: lezac-marquee 60s linear infinite;">
    ${items}
  </div>
</div>
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
    .map(name => `<span class="whitespace-nowrap text-base font-body font-semibold text-white/70 tracking-wide flex items-center gap-3">
      <span class="w-1 h-1 rounded-full inline-block opacity-40" style="background: var(--color-accent, #8C52FF);"></span>
      ${name}
    </span>`)
    .join('');

  return `
<div class="lezac-marquee-wrapper overflow-hidden py-1" aria-label="Empresas clientes">
  <div class="lezac-marquee-track flex gap-8 items-center" style="width: max-content; animation: lezac-marquee 90s linear infinite;">
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

    /* ── Lezac Chatbot Widget ── */
    @keyframes lz-pulse {
      0%,100% { box-shadow: 0 8px 24px rgba(37,245,164,0.45), 0 0 0 0 rgba(37,245,164,0.4); }
      50%      { box-shadow: 0 8px 24px rgba(37,245,164,0.45), 0 0 0 10px rgba(37,245,164,0); }
    }
    #lz-chat-bubble {
      position:fixed;bottom:28px;right:28px;z-index:9999;
      width:auto;height:52px;border-radius:9999px;padding:0 22px;gap:10px;
      background:#25F5A4;border:none;cursor:pointer;
      box-shadow:0 8px 24px rgba(37,245,164,0.45);
      display:flex;align-items:center;justify-content:center;
      animation:lz-pulse 2.2s ease-in-out infinite;
      transition:transform 0.2s,box-shadow 0.2s;
    }
    #lz-chat-bubble:hover{transform:scale(1.06);animation:none;box-shadow:0 12px 36px rgba(37,245,164,0.6);}
    #lz-chat-panel {
      position:fixed;bottom:92px;right:24px;z-index:9998;
      width:360px;height:680px;max-height:calc(100vh - 120px);border-radius:12px;
      background:rgba(17,17,18,0.96);backdrop-filter:blur(20px);
      border:1px solid rgba(255,255,255,0.08);
      box-shadow:0 24px 48px rgba(0,0,0,0.55);
      display:flex;flex-direction:column;
      transform:translateY(16px) scale(0.97);opacity:0;
      pointer-events:none;
      transition:transform 0.22s cubic-bezier(0.4,0,0.2,1),opacity 0.22s ease;
    }
    #lz-chat-panel.lz-open{transform:translateY(0) scale(1);opacity:1;pointer-events:all;}
    #lz-chat-header{
      padding:14px 16px;flex-shrink:0;
      border-bottom:1px solid rgba(255,255,255,0.07);
      display:flex;align-items:center;justify-content:space-between;
    }
    #lz-chat-header-info{display:flex;flex-direction:column;gap:2px;}
    #lz-chat-header-name{font-family:Montserrat,Manrope,sans-serif;font-size:14px;font-weight:600;color:#E5E2E3;}
    #lz-chat-header-status{font-size:11px;color:#25F5A4;display:flex;align-items:center;gap:4px;}
    #lz-chat-close{background:none;border:none;color:#958DA1;cursor:pointer;font-size:20px;line-height:1;padding:4px 6px;border-radius:4px;}
    #lz-chat-close:hover{background:rgba(255,255,255,0.05);color:#E5E2E3;}
    #lz-chat-messages{
      flex:1;overflow-y:auto;padding:14px 16px;
      display:flex;flex-direction:column;gap:10px;
      scroll-behavior:smooth;
      scrollbar-width:thin;scrollbar-color:rgba(255,255,255,0.1) transparent;
    }
    .lz-msg{
      max-width:84%;padding:9px 13px;border-radius:10px;
      font-size:13.5px;line-height:1.55;font-family:Inter,sans-serif;
      word-break:break-word;
    }
    .lz-msg-bot{align-self:flex-start;background:#1A1A1B;color:#E5E2E3;border-bottom-left-radius:3px;}
    .lz-msg-user{align-self:flex-end;background:#25F5A4;color:#0A0A0B;border-bottom-right-radius:3px;}
    .lz-msg img{max-width:100%;border-radius:6px;margin-top:6px;display:block;}
    .lz-typing{display:inline-flex;align-items:center;gap:5px;padding:11px 14px;background:#1A1A1B;border-radius:10px;border-bottom-left-radius:3px;align-self:flex-start;}
    .lz-dot{width:6px;height:6px;border-radius:9999px;background:#958DA1;animation:lz-blink 1.3s infinite;}
    .lz-dot:nth-child(2){animation-delay:0.2s;}
    .lz-dot:nth-child(3){animation-delay:0.4s;}
    @keyframes lz-blink{0%,80%,100%{opacity:0.3;transform:scale(0.8);}40%{opacity:1;transform:scale(1);}}
    #lz-img-preview{padding:6px 16px 0;flex-shrink:0;display:none;align-items:center;gap:8px;}
    #lz-img-preview img{height:50px;width:50px;object-fit:cover;border-radius:6px;border:1px solid rgba(255,255,255,0.1);}
    #lz-img-preview-remove{background:none;border:none;color:#EC0543;cursor:pointer;font-size:20px;line-height:1;padding:2px;}
    #lz-chat-input-row{
      padding:10px 12px 12px;flex-shrink:0;
      border-top:1px solid rgba(255,255,255,0.07);
      display:flex;align-items:flex-end;gap:8px;
    }
    #lz-chat-input{
      flex:1;background:#111112;border:1px solid rgba(255,255,255,0.1);
      border-radius:8px;color:#E5E2E3;font-size:13px;font-family:Inter,sans-serif;
      padding:9px 12px;resize:none;max-height:96px;min-height:38px;
      line-height:1.45;overflow-y:auto;
    }
    #lz-chat-input:focus{outline:none;border-color:rgba(37,245,164,0.5);}
    #lz-chat-input::placeholder{color:#958DA1;}
    #lz-attach-label{
      cursor:pointer;color:#958DA1;display:flex;align-items:center;
      padding:8px;border-radius:6px;transition:color 0.15s,background 0.15s;flex-shrink:0;
    }
    #lz-attach-label:hover{color:#E5E2E3;background:rgba(255,255,255,0.05);}
    #lz-attach-input{display:none;}
    #lz-chat-send{
      background:#25F5A4;border:none;border-radius:8px;color:#0A0A0B;
      width:36px;height:36px;cursor:pointer;flex-shrink:0;
      display:flex;align-items:center;justify-content:center;
      transition:background 0.15s;padding:0;
    }
    #lz-chat-send:hover{background:#00C87E;}
    #lz-chat-send:disabled{background:rgba(37,245,164,0.35);cursor:not-allowed;}
    @media(max-width:480px){
      #lz-chat-panel{width:calc(100vw - 16px);right:8px;bottom:82px;max-height:calc(100vh - 100px);}
      #lz-chat-bubble{bottom:16px;right:16px;padding:0 14px;}
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

// ─── CHATBOT WIDGET ──────────────────────────────────────────────────────────

function getLezacChatbotHTML() {
  return `
<button id="lz-chat-bubble" aria-label="Abrir asistente" aria-expanded="false">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0A0A0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
  </svg>
  <span style="font-family:Montserrat,sans-serif;font-size:13px;font-weight:700;color:#0A0A0B;letter-spacing:0.05em;">Asistente Comercial</span>
</button>
<div id="lz-chat-panel" role="dialog" aria-label="Asistente Lezac">
  <div id="lz-chat-header">
    <div id="lz-chat-header-info">
      <div id="lz-chat-header-name">Asistente Lezac</div>
      <div id="lz-chat-header-status">
        <span style="width:6px;height:6px;border-radius:9999px;background:#25F5A4;display:inline-block;flex-shrink:0;"></span>
        En línea
      </div>
    </div>
    <button id="lz-chat-close" aria-label="Cerrar chat">×</button>
  </div>
  <div id="lz-chat-messages"></div>
  <div id="lz-img-preview">
    <img src="" alt="Vista previa" />
    <button id="lz-img-preview-remove" aria-label="Quitar imagen">×</button>
  </div>
  <div id="lz-chat-input-row">
    <label id="lz-attach-label" title="Adjuntar imagen">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
      </svg>
      <input type="file" id="lz-attach-input" accept="image/*">
    </label>
    <textarea id="lz-chat-input" rows="1" placeholder="Escribí tu mensaje..."></textarea>
    <button id="lz-chat-send" aria-label="Enviar">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <line x1="22" y1="2" x2="11" y2="13"/>
        <polygon points="22 2 15 22 11 13 2 9 22 2"/>
      </svg>
    </button>
  </div>
</div>
`;
}

function initChatbot() {
  const WEBHOOK = 'https://n8n.lezacconsultoria.com/webhook/lezac-chat';
  const STORAGE_KEY = 'lezac_chat';
  let pendingImage = null;

  function getSession() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) return JSON.parse(raw);
    } catch(e) {}
    const id = (typeof crypto !== 'undefined' && crypto.randomUUID)
      ? crypto.randomUUID()
      : Date.now().toString(36) + Math.random().toString(36).slice(2);
    const s = { id, messages: [] };
    saveSession(s);
    return s;
  }

  function saveSession(s) {
    s.messages = s.messages.slice(-30);
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(s)); } catch(e) {}
  }

  const bubble = document.getElementById('lz-chat-bubble');
  const panel  = document.getElementById('lz-chat-panel');
  const closeBtn = document.getElementById('lz-chat-close');
  const messagesEl = document.getElementById('lz-chat-messages');
  const inputEl = document.getElementById('lz-chat-input');
  const sendBtn = document.getElementById('lz-chat-send');
  const attachInput = document.getElementById('lz-attach-input');
  const imgPreview = document.getElementById('lz-img-preview');
  const imgPreviewRemove = document.getElementById('lz-img-preview-remove');
  if (!bubble || !panel) return;

  function appendMsg(role, text, imgDataUrl) {
    const div = document.createElement('div');
    div.className = 'lz-msg lz-msg-' + role;
    if (imgDataUrl) {
      const img = document.createElement('img');
      img.src = imgDataUrl;
      img.alt = 'Imagen adjunta';
      div.appendChild(img);
    }
    if (text) {
      const span = document.createElement('span');
      span.innerHTML = text
        .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
        .replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')
        .replace(/\*(.+?)\*/g,'<strong>$1</strong>')
        .replace(/\n/g,'<br>');
      div.appendChild(span);
    }
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'lz-typing'; div.id = 'lz-typing';
    div.innerHTML = '<span class="lz-dot"></span><span class="lz-dot"></span><span class="lz-dot"></span>';
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }
  function removeTyping() { const t = document.getElementById('lz-typing'); if (t) t.remove(); }

  function renderHistory(session) {
    messagesEl.innerHTML = '';
    session.messages.forEach(m => appendMsg(m.role, m.content, m.imgDataUrl || null));
  }

  let isOpen = false, initialized = false;

  function openChat() {
    isOpen = true;
    panel.classList.add('lz-open');
    bubble.setAttribute('aria-expanded', 'true');
    if (!initialized) {
      initialized = true;
      const session = getSession();
      if (session.messages.length === 0) {
        const welcome = 'Soy Lezac, tu asistente comercial 👋 si deseas me puedes contar en que te gustaría que te ayude en tu negocio.';
        appendMsg('bot', welcome);
        session.messages.push({ role: 'bot', content: welcome });
        saveSession(session);
      } else {
        renderHistory(session);
      }
    }
    setTimeout(() => inputEl && inputEl.focus(), 150);
  }

  function closeChat() {
    isOpen = false;
    panel.classList.remove('lz-open');
    bubble.setAttribute('aria-expanded', 'false');
  }

  bubble.addEventListener('click', () => isOpen ? closeChat() : openChat());
  closeBtn.addEventListener('click', closeChat);

  setTimeout(openChat, 10000);

  async function sendMessage() {
    const text = inputEl.value.trim();
    const imgToSend = pendingImage;
    if (!text && !imgToSend) return;
    const session = getSession();

    appendMsg('user', text || null, imgToSend ? imgToSend.dataUrl : null);
    session.messages.push({ role: 'user', content: text, imgDataUrl: imgToSend ? imgToSend.dataUrl : null });
    saveSession(session);

    inputEl.value = '';
    inputEl.style.height = '';
    pendingImage = null;
    imgPreview.style.display = 'none';
    sendBtn.disabled = true;
    showTyping();

    try {
      const body = { sessionId: session.id, message: text || '' };
      if (imgToSend) body.imageBase64 = imgToSend.base64;
      const res = await fetch(WEBHOOK, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
      const data = await res.json();
      removeTyping();
      const reply = data.response || 'Tuve un problema técnico, intentá en unos minutos.';
      appendMsg('bot', reply);
      session.messages.push({ role: 'bot', content: reply });
      saveSession(session);
    } catch(err) {
      removeTyping();
      appendMsg('bot', 'Tuve un problema técnico, intentá en unos minutos.');
    } finally {
      sendBtn.disabled = false;
    }
  }

  sendBtn.addEventListener('click', sendMessage);
  inputEl.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  });
  inputEl.addEventListener('input', () => {
    inputEl.style.height = 'auto';
    inputEl.style.height = Math.min(inputEl.scrollHeight, 96) + 'px';
  });

  attachInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (ev) => {
      const dataUrl = ev.target.result;
      const base64 = dataUrl.split(',')[1];
      pendingImage = { base64, dataUrl };
      const img = imgPreview.querySelector('img');
      img.src = dataUrl;
      imgPreview.style.display = 'flex';
    };
    reader.readAsDataURL(file);
    e.target.value = '';
  });

  imgPreviewRemove.addEventListener('click', () => {
    pendingImage = null;
    imgPreview.style.display = 'none';
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
  document.querySelectorAll('[data-lezac-tools-marquee]').forEach(el => {
    el.innerHTML = getToolsMarqueeHTML();
  });

  // Add padding-top to first section to account for fixed nav
  const firstSection = document.querySelector('main, section, .hero-section, [data-hero]');
  if (firstSection && !firstSection.dataset.noPad) {
    const currentPt = parseInt(getComputedStyle(firstSection).paddingTop || '0');
    if (currentPt < 80) firstSection.style.paddingTop = '80px';
  }

  // Inject chatbot widget
  const chatWrapper = document.createElement('div');
  chatWrapper.innerHTML = getLezacChatbotHTML();
  while (chatWrapper.firstChild) document.body.appendChild(chatWrapper.firstChild);

  initActiveNav();
  initHamburger();
  initMarquees();
  initScrollReveal();
  initVSL();
  initChatbot();
});
