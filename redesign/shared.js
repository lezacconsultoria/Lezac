/**
 * Lezac Consultoria — Shared JS (versión redesign)
 * Nav + Footer + Chatbot + Scroll Reveal para las 5 páginas nuevas:
 *   Inicio · Brújula Comercial · +Clientes Activos · IA Aplicada · Partner
 *
 * Uso: cada página inyecta contenedores <div id="lezac-nav"></div>,
 *      <div id="lezac-footer"></div> y este script los rellena en DOMContentLoaded.
 *
 * Chatbot: mismo webhook y misma memoria Pocketbase que el widget de bio.html
 *          — se preservan las claves de localStorage lezac_chat y lezac_chat_dismissed
 *          para que un usuario que ya conversó en el sitio viejo no vea el saludo de nuevo.
 */

// ─── URLs y constantes ────────────────────────────────────────────────────────

const LZ_CALENDLY = 'https://calendly.com/lezacconsultoria/asesoria-comercial';
const LZ_WHATSAPP = 'https://api.whatsapp.com/send?phone=5491154107921&text=%E2%9C%85%20Lezac%20Consultoria%20I%20Me%20interesa%20conocer%20m%C3%A1s%20de%20sus%20servicios.';
const LZ_LINKEDIN = 'https://www.linkedin.com/company/lezac-consultoria';
const LZ_INSTAGRAM = 'https://instagram.com/lezacconsultoria';

const LZ_CHAT_WEBHOOK = 'https://n8n.lezacconsultoria.com/webhook/lezac-chat';
const LZ_CHAT_STORAGE = 'lezac_chat';
const LZ_CHAT_DISMISSED = 'lezac_chat_dismissed';
const LZ_CHAT_MAX = 30;
const LZ_CHAT_WELCOME = 'Soy Lezac, tu asistente comercial 👋 contame en qué te gustaría que te ayude en tu negocio.';

// ─── NAV ──────────────────────────────────────────────────────────────────────

function getLezacNav() {
  return `
<nav class="fixed top-0 left-0 right-0 z-40 px-4 md:px-8" style="background:rgba(13,13,13,0.72);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.05);">
  <div class="max-w-[1200px] mx-auto flex items-center justify-between h-16">

    <a href="./index.html" class="flex items-center gap-2 group" aria-label="Inicio">
      <img src="/logo-lezac-completo.png" alt="Lezac Consultoría" class="h-7 w-auto" />
    </a>

    <div class="hidden lg:flex items-center gap-1">
      <a href="./index.html" data-nav="home" class="lz-nav-link">Inicio</a>
      <a href="./brujula-comercial.html" data-nav="brujula" class="lz-nav-link">Brújula Comercial</a>
      <a href="./mas-clientes-activos.html" data-nav="clientes" class="lz-nav-link">+Clientes Activos</a>
      <a href="./ia-aplicada.html" data-nav="ia" class="lz-nav-link">IA Aplicada</a>
      <a href="./partner.html" data-nav="partner" class="lz-nav-link">Partner</a>
    </div>

    <div class="hidden md:flex items-center gap-2">
      <a href="${LZ_CALENDLY}" target="_blank" rel="noopener" class="lz-cta-secondary hidden lg:inline-flex">Agendar reunión</a>
      <a href="${LZ_WHATSAPP}" target="_blank" rel="noopener" class="lz-cta-wa" title="WhatsApp" aria-label="WhatsApp">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      </a>
    </div>

    <button id="lz-menu-toggle" class="lg:hidden flex flex-col gap-1.5 p-2" aria-label="Menú" aria-expanded="false">
      <span class="block w-5 h-0.5 bg-white transition-all duration-300"></span>
      <span class="block w-5 h-0.5 bg-white transition-all duration-300"></span>
      <span class="block w-5 h-0.5 bg-white transition-all duration-300"></span>
    </button>
  </div>

  <div id="lz-mobile-menu" class="lg:hidden hidden pb-4 border-t border-white/5">
    <div class="flex flex-col gap-0.5 pt-3">
      <a href="./index.html" data-nav="home" class="lz-nav-link-m">Inicio</a>
      <a href="./brujula-comercial.html" data-nav="brujula" class="lz-nav-link-m">Brújula Comercial</a>
      <a href="./mas-clientes-activos.html" data-nav="clientes" class="lz-nav-link-m">+Clientes Activos</a>
      <a href="./ia-aplicada.html" data-nav="ia" class="lz-nav-link-m">IA Aplicada</a>
      <a href="./partner.html" data-nav="partner" class="lz-nav-link-m">Partner</a>
      <a href="${LZ_CALENDLY}" target="_blank" rel="noopener" class="mt-3 mx-2 text-center px-4 py-3 rounded-lg text-sm font-semibold text-white" style="background:#8C52FF;">Agendar reunión</a>
    </div>
  </div>
</nav>

<style>
  .lz-nav-link{padding:8px 14px;border-radius:8px;font-size:13.5px;color:#A79FB3;font-weight:500;transition:color .15s, background .15s; text-decoration:none;}
  .lz-nav-link:hover{color:#fff;background:rgba(255,255,255,0.04);}
  .lz-nav-link.active{color:#fff;background:rgba(140,82,255,0.14);}
  .lz-nav-link-m{padding:12px 14px;border-radius:8px;font-size:14px;color:#A79FB3;font-weight:500; text-decoration:none;}
  .lz-nav-link-m:hover{color:#fff;background:rgba(255,255,255,0.04);}
  .lz-nav-link-m.active{color:#fff;background:rgba(140,82,255,0.14);}
  .lz-cta-secondary{padding:8px 16px;border-radius:8px;font-size:13px;font-weight:600;color:#F2EFF6;border:1px solid rgba(255,255,255,0.1);transition:border-color .15s, color .15s; text-decoration:none;}
  .lz-cta-secondary:hover{border-color:rgba(255,255,255,0.25); color:#fff;}
  .lz-cta-wa{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:9999px;background:rgba(37,211,102,0.15);color:#25D366;transition:transform .15s; text-decoration:none;}
  .lz-cta-wa:hover{transform:scale(1.08);}
</style>
`;
}

// ─── FOOTER ──────────────────────────────────────────────────────────────────

function getLezacFooter() {
  const year = new Date().getFullYear();
  return `
<footer class="mt-32 pt-16 pb-10 px-6" style="background:#0A0A0A;border-top:1px solid rgba(255,255,255,0.05);">
  <div class="max-w-[1200px] mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">

      <div class="md:col-span-2">
        <img src="/logo-lezac-completo.png" alt="Lezac Consultoría" class="h-8 w-auto mb-4" />
        <p style="font-family:'DM Mono',monospace;font-size:11px;color:#726B7D;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:14px;">Al cuidado de tu negocio.</p>
        <p style="font-size:13.5px;color:#A79FB3;max-width:44ch;line-height:1.6;">Consultora de inteligencia comercial B2B para distribuidoras, mayoristas y fábricas pyme en Argentina, Paraguay, Bolivia y Uruguay.</p>
      </div>

      <div>
        <h4 style="font-size:11px;color:#726B7D;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:14px;font-weight:700;">Servicios</h4>
        <ul class="flex flex-col gap-2.5">
          <li><a href="./brujula-comercial.html" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">Brújula Comercial</a></li>
          <li><a href="./mas-clientes-activos.html" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">+Clientes Activos</a></li>
          <li><a href="./ia-aplicada.html" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">IA Aplicada</a></li>
          <li><a href="./partner.html" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">Programa Partner</a></li>
        </ul>
      </div>

      <div>
        <h4 style="font-size:11px;color:#726B7D;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:14px;font-weight:700;">Contacto</h4>
        <ul class="flex flex-col gap-2.5">
          <li><a href="${LZ_WHATSAPP}" target="_blank" rel="noopener" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">WhatsApp +54 9 11 5410-7921</a></li>
          <li><a href="mailto:lezacconsultoria@gmail.com" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">lezacconsultoria@gmail.com</a></li>
          <li><a href="${LZ_CALENDLY}" target="_blank" rel="noopener" style="font-size:13.5px;color:#A79FB3;text-decoration:none;">Agendar una charla</a></li>
          <li class="flex gap-3 mt-2">
            <a href="${LZ_LINKEDIN}" target="_blank" rel="noopener" style="color:#A79FB3;" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.063 2.063 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
            <a href="${LZ_INSTAGRAM}" target="_blank" rel="noopener" style="color:#A79FB3;" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
          </li>
        </ul>
      </div>
    </div>

    <div class="pt-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4" style="border-top:1px solid rgba(255,255,255,0.05);">
      <p style="font-size:12px;color:#726B7D;">© ${year} Lezac Consultoría. Todos los derechos reservados.</p>
      <p style="font-family:'DM Mono',monospace;font-size:11px;color:#726B7D;letter-spacing:0.06em;">AR · PY · BO · UY</p>
    </div>
  </div>
</footer>
`;
}

// ─── CHATBOT (widget + lógica) ──────────────────────────────────────────────

function getLezacChatbot() {
  return `
<style>
  @keyframes lz-pulse{0%,100%{box-shadow:0 4px 24px rgba(37,245,164,.45),0 0 0 0 rgba(37,245,164,.4);}50%{box-shadow:0 4px 24px rgba(37,245,164,.45),0 0 0 10px rgba(37,245,164,0);}}
  @keyframes lz-bounce{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-7px)}}
  #lz-chat-bubble{position:fixed;bottom:24px;right:24px;z-index:9999;background:linear-gradient(135deg,#25F5A4,#00C87E);border:none;border-radius:9999px;height:52px;padding:0 22px;display:flex;align-items:center;gap:10px;cursor:pointer;color:#0A0A0B;font-family:Inter,sans-serif;font-weight:600;font-size:14px;animation:lz-pulse 2.2s ease-in-out infinite;}
  #lz-chat-bubble:hover{filter:brightness(1.08);}
  #lz-chat-panel{position:fixed;bottom:90px;right:24px;width:360px;height:640px;max-height:calc(100vh - 120px);background:rgba(21,19,24,0.94);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(255,255,255,.08);box-shadow:0 24px 48px rgba(0,0,0,.6);border-radius:16px;display:flex;flex-direction:column;z-index:9998;overflow:hidden;transform:scale(.95) translateY(10px);opacity:0;pointer-events:none;transition:transform .25s ease,opacity .25s ease;font-family:Inter,sans-serif;}
  #lz-chat-panel.lz-open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}
  #lz-chat-head{padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.07);display:flex;align-items:center;gap:10px;}
  #lz-chat-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;}
  .lz-msg-user{align-self:flex-end;background:#25F5A4;color:#0A0A0B;border-radius:16px 16px 4px 16px;padding:10px 14px;max-width:80%;font-size:14px;line-height:1.5;white-space:pre-wrap;word-break:break-word;}
  .lz-msg-bot{align-self:flex-start;background:#1B181F;color:#F2EFF6;border-radius:16px 16px 16px 4px;padding:10px 14px;max-width:80%;font-size:14px;line-height:1.5;white-space:pre-wrap;word-break:break-word;}
  .lz-typing{align-self:flex-start;display:flex;gap:5px;padding:12px 16px;background:#1B181F;border-radius:16px 16px 16px 4px;}
  .lz-dot{width:7px;height:7px;background:#25F5A4;border-radius:50%;animation:lz-bounce 1.2s infinite;}
  .lz-dot:nth-child(2){animation-delay:.2s;}
  .lz-dot:nth-child(3){animation-delay:.4s;}
  #lz-chat-row{padding:10px 12px;border-top:1px solid rgba(255,255,255,.07);display:flex;align-items:flex-end;gap:8px;}
  #lz-chat-input{flex:1;background:#0D0D0D;border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:8px 12px;color:#F2EFF6;font-size:14px;resize:none;outline:none;line-height:1.5;max-height:120px;overflow-y:auto;font-family:inherit;}
  #lz-chat-input:focus{border-color:rgba(37,245,164,.5);}
  #lz-chat-input::placeholder{color:#726B7D;}
  #lz-chat-send{background:#25F5A4;border:none;border-radius:10px;padding:8px 12px;cursor:pointer;flex-shrink:0;transition:filter .15s;}
  #lz-chat-send:hover{filter:brightness(1.08);}
  @media(max-width:480px){#lz-chat-panel{right:8px;left:8px;width:auto;bottom:88px;}}
</style>

<div id="lz-chat-panel">
  <div id="lz-chat-head">
    <div style="width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#25F5A4,#00C87E);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0A0A0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    </div>
    <div style="flex:1;">
      <div style="color:#F2EFF6;font-weight:700;font-size:14px;">Asistente Lezac</div>
      <div style="color:#25F5A4;font-size:11px;display:flex;align-items:center;gap:4px;">
        <span style="width:6px;height:6px;border-radius:50%;background:#25F5A4;display:inline-block;"></span>en línea
      </div>
    </div>
    <button id="lz-chat-close" style="background:none;border:none;cursor:pointer;color:#A79FB3;padding:4px;border-radius:6px;line-height:1;" aria-label="Cerrar chat">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>

  <div id="lz-chat-messages"></div>

  <div id="lz-chat-row">
    <textarea id="lz-chat-input" rows="1" placeholder="Escribí tu mensaje..."></textarea>
    <button id="lz-chat-send" aria-label="Enviar">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0A0A0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
    </button>
  </div>
</div>

<button id="lz-chat-bubble" aria-label="Abrir chat">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0A0A0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
  <span>Asistente Lezac</span>
</button>
`;
}

function getChatSession() {
  try {
    const raw = localStorage.getItem(LZ_CHAT_STORAGE);
    if (raw) return JSON.parse(raw);
  } catch (e) {}
  const id = (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function')
    ? crypto.randomUUID()
    : Math.random().toString(36).slice(2) + Date.now().toString(36);
  return { id: id, messages: [] };
}

function saveChatSession(s) {
  try { localStorage.setItem(LZ_CHAT_STORAGE, JSON.stringify({ id: s.id, messages: s.messages.slice(-LZ_CHAT_MAX) })); } catch (e) {}
}

function initLezacChat() {
  const session = getChatSession();
  let typing = false;

  const panel = document.getElementById('lz-chat-panel');
  const bubble = document.getElementById('lz-chat-bubble');
  const closeBtn = document.getElementById('lz-chat-close');
  const messagesEl = document.getElementById('lz-chat-messages');
  const inputEl = document.getElementById('lz-chat-input');
  const sendBtn = document.getElementById('lz-chat-send');
  if (!panel || !bubble) return;

  function scrollDown() { messagesEl.scrollTop = messagesEl.scrollHeight; }

  function renderMessages() {
    messagesEl.innerHTML = session.messages.map(function (m) {
      const cls = m.role === 'user' ? 'lz-msg-user' : 'lz-msg-bot';
      const div = document.createElement('div');
      div.textContent = m.content;
      return '<div class="' + cls + '">' + div.innerHTML + '</div>';
    }).join('') + (typing
      ? '<div class="lz-typing"><div class="lz-dot"></div><div class="lz-dot"></div><div class="lz-dot"></div></div>'
      : '');
    scrollDown();
  }

  function pushMessage(role, content) {
    session.messages.push({ role: role, content: content, timestamp: Date.now() });
    saveChatSession(session);
    renderMessages();
  }

  function openPanel() {
    panel.classList.add('lz-open');
    if (session.messages.length === 0) pushMessage('bot', LZ_CHAT_WELCOME);
    else renderMessages();
  }

  bubble.addEventListener('click', function () {
    if (panel.classList.contains('lz-open')) panel.classList.remove('lz-open');
    else openPanel();
  });

  closeBtn.addEventListener('click', function () {
    try { localStorage.setItem(LZ_CHAT_DISMISSED, '1'); } catch (e) {}
    panel.classList.remove('lz-open');
  });

  function sendMessage() {
    const text = inputEl.value.trim();
    if (!text) return;
    pushMessage('user', text);
    inputEl.value = '';
    inputEl.style.height = 'auto';
    typing = true;
    renderMessages();

    fetch(LZ_CHAT_WEBHOOK, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sessionId: session.id, message: text })
    })
      .then(function (res) { return res.json(); })
      .then(function (data) {
        typing = false;
        pushMessage('bot', data.response || data.output || 'No pude procesar la respuesta.');
      })
      .catch(function () {
        typing = false;
        pushMessage('bot', 'Hubo un error al conectar. Intentá de nuevo.');
      });
  }

  sendBtn.addEventListener('click', sendMessage);
  inputEl.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  });
  inputEl.addEventListener('input', function () {
    inputEl.style.height = 'auto';
    inputEl.style.height = Math.min(inputEl.scrollHeight, 120) + 'px';
  });

  // Auto-abrir después de 10s si el usuario no lo cerró antes
  let dismissed = false;
  try { dismissed = !!localStorage.getItem(LZ_CHAT_DISMISSED); } catch (e) {}
  if (!dismissed) {
    setTimeout(function () {
      let stillDismissed = false;
      try { stillDismissed = !!localStorage.getItem(LZ_CHAT_DISMISSED); } catch (e) {}
      if (!stillDismissed) openPanel();
    }, 10000);
  }
}

// ─── SCROLL REVEAL ───────────────────────────────────────────────────────────

function initScrollReveal() {
  const els = document.querySelectorAll('.lezac-reveal');
  if (!els.length) return;
  const io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });
  els.forEach(function (el) { io.observe(el); });
}

// ─── MENU MOBILE TOGGLE ──────────────────────────────────────────────────────

function initMobileMenu() {
  const toggle = document.getElementById('lz-menu-toggle');
  const menu = document.getElementById('lz-mobile-menu');
  if (!toggle || !menu) return;
  toggle.addEventListener('click', function () {
    const open = !menu.classList.contains('hidden');
    if (open) {
      menu.classList.add('hidden');
      toggle.setAttribute('aria-expanded', 'false');
    } else {
      menu.classList.remove('hidden');
      toggle.setAttribute('aria-expanded', 'true');
    }
  });
}

// ─── ACTIVE NAV ──────────────────────────────────────────────────────────────

function markActiveNav() {
  const page = document.documentElement.dataset.page;
  if (!page) return;
  document.querySelectorAll('[data-nav="' + page + '"]').forEach(function (el) { el.classList.add('active'); });
}

// ─── BOOT ────────────────────────────────────────────────────────────────────

function bootLezacShared() {
  const navMount = document.getElementById('lezac-nav');
  if (navMount) navMount.innerHTML = getLezacNav();

  const footerMount = document.getElementById('lezac-footer');
  if (footerMount) footerMount.innerHTML = getLezacFooter();

  const chatMount = document.getElementById('lezac-chatbot');
  if (chatMount) chatMount.innerHTML = getLezacChatbot();

  markActiveNav();
  initMobileMenu();
  initScrollReveal();
  initLezacChat();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', bootLezacShared);
} else {
  bootLezacShared();
}
