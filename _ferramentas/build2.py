import os
OUT = r"G:\Meu Drive\02 PROJETOS\cemevi-site"
SP = "http://meu.simplespet.com.br/#/access/login?a=centro-medico-veterinario-icar"
WA = "https://wa.me/5521967520101"
TEL = "tel:+552136282484"

NAV = [("index.html", "Início"), ("clinica-veterinaria.html", "Clínica"),
       ("internacao-24-horas.html", "Internação 24h"), ("banho-e-tosa.html", "Banho e tosa"),
       ("farmacia-veterinaria.html", "Farmácia"), ("contato.html", "Contato")]

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></symbol>
  <symbol id="i-car" viewBox="0 0 24 24"><path d="M5 17H3v-5l2-5h14l2 5v5h-2"/><path d="M3 12h18"/><circle cx="7.5" cy="17.5" r="2"/><circle cx="16.5" cy="17.5" r="2"/><path d="M9.5 17.5h5"/></symbol>
  <symbol id="i-heart" viewBox="0 0 24 24"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></symbol>
  <symbol id="i-steth" viewBox="0 0 24 24"><path d="M5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 12 0V4a2 2 0 0 0-2-2h-1"/><path d="M8 15v1a6 6 0 0 0 12 0v-4"/><circle cx="20" cy="10" r="2"/></symbol>
  <symbol id="i-scissors" viewBox="0 0 24 24"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.12 15.88M14.47 14.48 20 20M8.12 8.12 12 12"/></symbol>
  <symbol id="i-pill" viewBox="0 0 24 24"><path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/><path d="m8.5 8.5 7 7"/></symbol>
  <symbol id="i-syringe" viewBox="0 0 24 24"><path d="m18 2 4 4M17 7l3-3M19 9 8.7 19.3a2.4 2.4 0 0 1-3.4 0l-.6-.6a2.4 2.4 0 0 1 0-3.4L15 5M9 11l4 4M5 19l-3 3M14 4l6 6"/></symbol>
  <symbol id="i-bed" viewBox="0 0 24 24"><path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20M6 8v9"/></symbol>
  <symbol id="i-pulse" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></symbol>
  <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></symbol>
  <symbol id="i-cal" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></symbol>
  <symbol id="i-file" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></symbol>
  <symbol id="i-scale" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 9a5 5 0 0 1 8 0l-3 3"/></symbol>
  <symbol id="i-drop" viewBox="0 0 24 24"><path d="M12 2.7 6.3 9.4a7 7 0 1 0 11.4 0z"/></symbol>
  <symbol id="i-sparkle" viewBox="0 0 24 24"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.5 8.5 0 0 1 8 8z"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zM12 0a12 12 0 0 0-10.3 18l-1.7 6 6.2-1.6A12 12 0 1 0 12 0z"/></symbol>
  <symbol id="i-paw" viewBox="0 0 24 24"><ellipse cx="5.2" cy="9.6" rx="2.2" ry="2.9" transform="rotate(-18 5.2 9.6)"/><ellipse cx="9.4" cy="5" rx="2.3" ry="3.1" transform="rotate(-6 9.4 5)"/><ellipse cx="14.6" cy="5" rx="2.3" ry="3.1" transform="rotate(6 14.6 5)"/><ellipse cx="18.8" cy="9.6" rx="2.2" ry="2.9" transform="rotate(18 18.8 9.6)"/><path d="M12 11.2c-2.9 0-6.3 4.4-6.3 7 0 1.9 1.4 2.8 3 2.8 1.4 0 2.2-.9 3.3-.9s1.9.9 3.3.9c1.6 0 3-.9 3-2.8 0-2.6-3.4-7-6.3-7z"/></symbol>
</svg>'''

def i(name, cls="ico"):
    fill = " ico-fill" if name in ("paw", "wa") else ""
    return f'<svg class="{cls}{fill}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def paw(style, cls="paw-deco"):
    return f'<svg class="{cls} ico-fill" style="{style}" aria-hidden="true"><use href="#i-paw"/></svg>'

def head(title, desc, page):
    act = ' class="active" aria-current="page"'
    items = "\n".join(f'          <li><a href="{h}"{act if h == page else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#bee8e6">
  <title>{title}</title>
  <link rel="icon" type="image/png" href="img/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,500..800&family=DM+Sans:opsz,wght@9..40,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
{SPRITE}

  <div class="topbar">
    <div class="wrap">
      <div class="topbar-l">
        <span>{i("clock")}Aberto 24 horas, todos os dias</span>
        <span class="sep hide-sm"></span>
        <span class="hide-sm">{i("pin")}Rua Dr. Tavares de Macedo, 141 — Icaraí, Niterói</span>
      </div>
      <div class="topbar-r">
        <a href="{TEL}">{i("phone")}(21) 3628-2484</a>
        <span class="sep"></span>
        <a href="https://www.instagram.com/cemeviniteroi" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.facebook.com/cemeviniteroi" target="_blank" rel="noopener">Facebook</a>
      </div>
    </div>
  </div>

  <header class="header">
    <div class="wrap">
      <a href="index.html" class="brand"><img src="img/logo.png" alt="Cemevi — Centro Médico Veterinário Icaraí" width="97" height="60"></a>
      <nav class="nav" id="nav" aria-label="Principal">
        <ul>
{items}
          <li class="only-mobile"><a href="{SP}" target="_blank" rel="noopener">Área do cliente</a></li>
        </ul>
      </nav>
      <div class="header-actions">
        <a class="header-login" href="{SP}" target="_blank" rel="noopener">Área do cliente</a>
        <a class="btn btn-coral btn-sm" href="contato.html">Agendar</a>
        <button class="menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Abrir menu"><span></span></button>
      </div>
    </div>
  </header>
'''

FOOT = f'''
  <footer class="footer">
    {paw("width:120px;height:120px;right:6%;top:40px;transform:rotate(20deg)", "footer-paw")}
    {paw("width:70px;height:70px;left:44%;bottom:90px;transform:rotate(-24deg)", "footer-paw")}
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="img/logo.png" alt="Cemevi — Centro Médico Veterinário Icaraí" width="136" height="84">
          <p>Clínica médica e cirúrgica, emergência e internação 24 horas, banho e tosa. Em Icaraí, com estacionamento próprio.</p>
          <div class="social">
            <a href="https://www.instagram.com/cemeviniteroi" target="_blank" rel="noopener" aria-label="Instagram">{i("ig")}</a>
            <a href="https://www.facebook.com/cemeviniteroi" target="_blank" rel="noopener" aria-label="Facebook">{i("fb")}</a>
            <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{i("wa")}</a>
          </div>
        </div>
        <div>
          <h3>Serviços</h3>
          <ul>
            <li><a href="clinica-veterinaria.html">Clínica médica e cirúrgica</a></li>
            <li><a href="internacao-24-horas.html">Internação 24 horas</a></li>
            <li><a href="banho-e-tosa.html">Banho e tosa</a></li>
            <li><a href="farmacia-veterinaria.html">Farmácia veterinária</a></li>
          </ul>
        </div>
        <div>
          <h3>Cemevi</h3>
          <ul>
            <li><a href="index.html#estrutura">Nossa estrutura</a></li>
            <li><a href="{SP}" target="_blank" rel="noopener">Área do cliente</a></li>
            <li><a href="contato.html">Contato</a></li>
            <li><a href="contato.html#mapa">Como chegar</a></li>
          </ul>
        </div>
        <div>
          <h3>Fale com a gente</h3>
          <ul>
            <li>Rua Dr. Tavares de Macedo, 141, Casa 3<br>Icaraí — Niterói/RJ</li>
            <li><a href="{TEL}">(21) 3628-2484</a></li>
            <li><a href="{WA}" target="_blank" rel="noopener">(21) 96752-0101 (WhatsApp)</a></li>
            <li><a href="mailto:simonek-22@hotmail.com">simonek-22@hotmail.com</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Cemevi — Centro Médico Veterinário Icaraí</span>
        <span>Segunda a domingo, 24 horas</span>
      </div>
    </div>
  </footer>

  <a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">{i("wa")}<span>WhatsApp</span></a>

  <script src="js/main.js"></script>
</body>
</html>
'''

def phero(page, color, img, pos, title, lead, pills, actions):
    crumb = dict(NAV)[page]
    pill_html = "\n".join(f'          <span class="pill {c}" style="{s}">{i(ic)} {t}</span>' for c, s, ic, t in pills)
    return f'''
    <section class="phero">
      <div class="wrap">
        <div class="phero-card phero-{color}">
          <div class="phero-copy">
            <div class="crumbs"><a href="index.html">Início</a> / {crumb}</div>
            <h1>{title}</h1>
            <p>{lead}</p>
            <div class="hero-actions">{actions}</div>
          </div>
          <div class="phero-img">
            <img src="img/{img}" alt="" style="object-position:{pos}">
{pill_html}
          </div>
        </div>
      </div>
    </section>'''

def cards(items):
    return "\n".join(f'''          <article class="card reveal">
            <div class="card-ico">{i(ic)}</div>
            <h3>{t}</h3>
            <p>{d}</p>
          </article>''' for ic, t, d in items)

def faq(items):
    return "\n".join(f'''        <details class="reveal"><summary>{q}</summary><p>{a}</p></details>''' for q, a in items)

def band(color, title, text, actions):
    return f'''
    <section class="section" style="padding-top:0;padding-bottom:0">
      <div class="wrap">
        <div class="band band-{color} reveal">
          {paw("", "band-paw")}
          <div>
            <h2>{title}</h2>
            <p>{text}</p>
          </div>
          <div class="actions">{actions}</div>
        </div>
      </div>
    </section>'''

BTN_CALL = f'<a href="{TEL}" class="btn btn-coral">{i("phone")} Ligar agora</a>'
BTN_WA_W = f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-white">{i("wa")} WhatsApp</a>'

pages = {}

# ============================ HOME ============================
pages["index.html"] = head("Cemevi — Centro Médico Veterinário Icaraí | Clínica veterinária 24h em Niterói",
  "Cemevi — Centro Médico Veterinário Icaraí. Clínica médica e cirúrgica, emergência e internação 24 horas, banho e tosa em Niterói/RJ.",
  "index.html") + f'''
  <main>
    <section class="hero">
      <div class="wrap">
        <div class="hero-card">
          {paw("width:90px;height:90px;left:44%;top:40px;transform:rotate(18deg)", "hero-paw")}
          {paw("width:54px;height:54px;left:6%;bottom:36px;transform:rotate(-20deg)", "hero-paw")}
          <div class="hero-copy">
            <span class="hero-tag"><span class="dot"></span> Aberto agora · 24 horas</span>
            <h1>Cuidado <span class="chip-img"><img src="img/beagle.jpg" alt=""></span><br><span class="red">de verdade</span><br>pro seu pet.</h1>
            <p class="hero-lead">Clínica médica e cirúrgica, emergência e internação 24 horas, banho e tosa. Uma equipe altamente qualificada, que trata seu animal com muito carinho e profissionalismo.</p>
            <div class="hero-actions">
              <a href="contato.html" class="btn btn-coral">Agendar consulta</a>
              <a href="#servicos" class="btn btn-plain">Ver serviços {i("arrow")}</a>
            </div>
          </div>
          <div class="hero-photo">
            <div class="hero-call">Estamos aqui 24h por dia<a href="{TEL}">(21) 3628-2484</a></div>
            <img src="img/gatinho-menta.jpg" alt="Gatinho levantando a pata" fetchpriority="high">
            <div class="hero-rings"></div>
            <span class="pill pill-lime p1">{i("syringe")} Vacinas em dia</span>
            <span class="pill pill-white p2">{i("car")} Estacionamento próprio</span>
            <span class="pill pill-coral p3">{i("heart")} Emergência 24h</span>
          </div>
        </div>

        <div class="blocks" id="servicos">
          <a href="banho-e-tosa.html" class="block block-orange reveal">
            <div class="block-img"><img src="img/corgi-laranja.jpg" alt="Filhote de corgi"></div>
            <div class="block-copy">
              <span class="flag" style="align-self:flex-start">Novidade</span>
              <h3>Banho<br>e tosa</h3>
              <p>Banhos terapêuticos, hidratação e tosa na tesoura.</p>
            </div>
            <div class="block-foot"><span><strong>3 tipos de tosa</strong><small>higiênica, racial e tesoura</small></span><span class="block-btn">{i("arrow")}</span></div>
          </a>
          <a href="internacao-24-horas.html" class="block block-green reveal">
            <div class="block-img"><img src="img/bulldog-verde.jpg" alt="Buldogue francês"></div>
            <div class="block-copy">
              <span class="flag" style="align-self:flex-start">24 horas</span>
              <h3>Internação</h3>
              <p>Acompanhamento veterinário em tempo integral, dia e noite.</p>
            </div>
            <div class="block-foot"><span><strong>Cães e gatos</strong><small>em alas separadas</small></span><span class="block-btn">{i("arrow")}</span></div>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head head-center reveal">
          <span class="kicker">{i("paw")} O que fazemos</span>
          <h2>Tudo o que seu pet precisa, <span class="mark">num só lugar</span></h2>
        </div>
        <div class="cats">
          <a class="cat reveal" href="clinica-veterinaria.html" style="--bg:#dff3f1"><div class="cat-img"><img src="img/beagle.jpg" alt="Beagle" loading="lazy"></div><h3>Consultas</h3><span>Cães e gatos</span></a>
          <a class="cat reveal" href="clinica-veterinaria.html" style="--bg:#ffe7e6"><div class="cat-img"><img src="img/schnauzer.jpg" alt="Schnauzer" loading="lazy"></div><h3>Cirurgias</h3><span>Centro cirúrgico</span></a>
          <a class="cat reveal" href="clinica-veterinaria.html" style="--bg:#fff3cc"><div class="cat-img"><img src="img/gato-azul.jpg" alt="Gato" loading="lazy"></div><h3>Vacinas</h3><span>E vermifugação</span></a>
          <a class="cat reveal" href="internacao-24-horas.html" style="--bg:#e6f0ff"><div class="cat-img"><img src="img/cavalier.jpg" alt="Cavalier descansando" loading="lazy"></div><h3>Internação</h3><span>24 horas</span></a>
          <a class="cat reveal" href="banho-e-tosa.html" style="--bg:#ffe3ea"><div class="cat-img"><img src="img/samoieda.jpg" alt="Samoieda" loading="lazy"></div><h3>Banho e tosa</h3><span>Estética animal</span></a>
          <a class="cat reveal" href="farmacia-veterinaria.html" style="--bg:#fff3cc"><div class="cat-img"><img src="img/pug-amarelo.jpg" alt="Pug" loading="lazy"></div><h3>Farmácia</h3><span>Em breve</span></a>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="wrap twins">
        <div class="twin twin-dark reveal">
          <h2>Clínica médica e cirúrgica completa</h2>
          <p>Salas de atendimento confortáveis e climatizadas e um centro cirúrgico com todo o suporte para procedimentos em padrão de excelência.</p>
          <a href="clinica-veterinaria.html" class="btn btn-orange">Conhecer a clínica</a>
          <img src="img/vet-gato.jpg" alt="Veterinária examinando um gato" loading="lazy">
        </div>
        <div class="twin twin-yellow reveal">
          <h2>Farmácia veterinária própria</h2>
          <p>Em breve: um mix de medicamentos diferenciados, com os melhores preços, sem precisar sair da clínica.</p>
          <a href="farmacia-veterinaria.html" class="btn btn-ink">Saiba mais</a>
          <img src="img/pug-amarelo.jpg" alt="Pug de blusa de lã" loading="lazy">
        </div>
      </div>
    </section>

    <section class="section" id="estrutura" style="background:#fff">
      <div class="wrap">
        <div class="head reveal">
          <div>
            <span class="kicker">{i("pin")} Nossa casa</span>
            <h2>Conheça a estrutura do Cemevi</h2>
            <p>Cada espaço foi pensado para oferecer a você e ao seu animal a melhor experiência que vocês já tiveram em uma clínica veterinária.</p>
          </div>
          <div class="chips" role="group" aria-label="Filtrar fotos">
            <button class="chip active" data-filter="all" aria-pressed="true">Todos</button>
            <button class="chip" data-filter="atendimento" aria-pressed="false">Atendimento</button>
            <button class="chip" data-filter="internacao" aria-pressed="false">Internação</button>
          </div>
        </div>
        <div class="gallery">
          <figure class="shot reveal" data-cat="atendimento"><div class="shot-frame"><img src="img/fachada.jpg" alt="Fachada do Cemevi" loading="lazy"></div><figcaption>Fachada <span>Icaraí</span></figcaption></figure>
          <figure class="shot reveal" data-cat="atendimento"><div class="shot-frame"><img src="img/recepcao.jpg" alt="Recepção" loading="lazy"></div><figcaption>Recepção <span>Acolhimento</span></figcaption></figure>
          <figure class="shot reveal" data-cat="atendimento"><div class="shot-frame"><img src="img/consultorio.jpg" alt="Consultório" loading="lazy"></div><figcaption>Consultório <span>Climatizado</span></figcaption></figure>
          <figure class="shot reveal" data-cat="internacao"><div class="shot-frame"><img src="img/internacao-b.jpg" alt="Sala de internação" loading="lazy"></div><figcaption>Internação <span>24 horas</span></figcaption></figure>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="head head-center reveal">
          <span class="kicker">{i("heart")} Por que o Cemevi</span>
          <h2>Pensado para o seu pet e para você</h2>
        </div>
        <div class="tiles">
          <div class="tile reveal"><div class="tile-top"><span class="tile-ico">{i("clock")}</span>Horário</div><strong>24<small>horas</small></strong><p>Todos os dias, inclusive fins de semana e feriados.</p></div>
          <div class="tile reveal"><div class="tile-top"><span class="tile-ico">{i("car")}</span>Comodidade</div><strong>Vaga<small>própria</small></strong><p>Estacionamento em uma das principais ruas de Icaraí.</p></div>
          <div class="tile reveal"><div class="tile-top"><span class="tile-ico">{i("bed")}</span>Internação</div><strong>2<small>alas</small></strong><p>Cães e gatos separados, com menos estresse para cada espécie.</p></div>
          <div class="tile reveal"><div class="tile-top"><span class="tile-ico">{i("users")}</span>Parceiros</div><strong>Aberta<small>a colegas</small></strong><p>Internamos pacientes de colegas, em contato com o médico de origem.</p></div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="wrap">
        <div class="app reveal">
          {paw("width:140px;height:140px;right:4%;top:30px;transform:rotate(20deg)", "app-bgpaw")}
          {paw("width:70px;height:70px;left:46%;bottom:40px;transform:rotate(-16deg)", "app-bgpaw")}
          <div class="app-copy">
            <span class="kicker">{i("heart")} Área do cliente</span>
            <h2>A saúde do seu pet na palma da mão</h2>
            <p>Pelo SimplesPet você acompanha tudo o que acontece com seu animal aqui no Cemevi.</p>
            <ul class="app-list">
              <li>{i("scale")} Histórico de peso</li>
              <li>{i("syringe")} Caderneta de vacina</li>
              <li>{i("pulse")} Resultados de exames</li>
              <li>{i("file")} Receitas</li>
              <li>{i("cal")} Agendamentos</li>
            </ul>
            <a href="{SP}" target="_blank" rel="noopener" class="btn btn-ink btn-pill">{i("paw")} Acessar o SimplesPet</a>
          </div>
          <div class="app-stage">
            <svg class="bigpaw ico-fill" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-paw"/></svg>
            <div class="phone" aria-hidden="true">
              <div class="phone-bar"><span>9:41</span><span>SimplesPet</span></div>
              <div class="phone-pet"><img src="img/gatinho-menta.jpg" alt=""></div>
              <div class="phone-body">
                <div class="phone-name"><strong>Nina</strong><span>Gata · SRD</span></div>
                <div class="phone-grid">
                  <div>Idade<b>1 ano</b></div>
                  <div>Peso<b>2,7 kg</b></div>
                </div>
                <div class="phone-row"><b>Vacinas em dia</b>Próxima dose em 12/2026</div>
                <div class="phone-actions">
                  <span>{i("phone")}</span><span>{i("chat")}</span>
                  <em><i>{i("paw")}</i> Agendar retorno</em>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="pals">
      <div class="pals-side pals-left reveal"><img src="img/gato-laranja.jpg" alt="Gato laranja" loading="lazy"></div>
      <div class="pals-side pals-right reveal"><img src="img/jack-rosa.jpg" alt="Cachorro jack russell" loading="lazy"></div>
      {paw("width:40px;height:40px;left:22%;top:30%;transform:rotate(-20deg)")}
      {paw("width:30px;height:30px;left:18%;top:62%;transform:rotate(14deg)")}
      {paw("width:44px;height:44px;right:21%;top:66%;transform:rotate(22deg)")}
      <div class="wrap reveal">
        <h2>Seu melhor amigo em boas mãos</h2>
        <p>Estrutura excelente, equipe qualificada e muito carinho. Venha nos conhecer: estamos na Rua Dr. Tavares de Macedo, 141, em Icaraí.</p>
        <div class="hero-actions" style="justify-content:center">
          <a href="contato.html" class="btn btn-coral">Agendar agora</a>
          <a href="{TEL}" class="btn btn-plain">{i("phone")} (21) 3628-2484</a>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0;padding-bottom:0">
      <div class="wrap visit">
        <div class="visit-card reveal">
          <h2>Venha nos visitar</h2>
          <ul class="visit-list">
            <li><span class="vi">{i("pin")}</span><div><b>Endereço</b>Rua Dr. Tavares de Macedo, 141, Casa 3<br>Icaraí — Niterói/RJ</div></li>
            <li><span class="vi">{i("phone")}</span><div><b>Telefones</b><a href="{TEL}">(21) 3628-2484</a> · <a href="{WA}" target="_blank" rel="noopener">(21) 96752-0101</a></div></li>
            <li><span class="vi">{i("clock")}</span><div><b>Horário</b>Segunda a domingo, 24 horas</div></li>
            <li><span class="vi">{i("mail")}</span><div><b>E-mail</b><a href="mailto:simonek-22@hotmail.com">simonek-22@hotmail.com</a></div></li>
          </ul>
          <a href="https://www.google.com/maps/dir/?api=1&destination=Rua+Dr.+Tavares+de+Macedo,+141,+Icara%C3%AD,+Niter%C3%B3i+-+RJ" target="_blank" rel="noopener" class="btn btn-coral">Traçar rota</a>
        </div>
        <iframe class="map reveal" title="Mapa: Cemevi em Icaraí" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=Rua+Dr.+Tavares+de+Macedo,+141,+Icara%C3%AD,+Niter%C3%B3i+-+RJ&output=embed"></iframe>
      </div>
    </section>
  </main>
''' + FOOT

# ============================ CLÍNICA ============================
pages["clinica-veterinaria.html"] = head("Clínica veterinária — Cemevi, Icaraí",
  "Clínica médica e cirúrgica do Cemevi em Icaraí, Niterói. Consultórios climatizados, centro cirúrgico e emergência 24 horas.",
  "clinica-veterinaria.html") + "\n  <main>" + phero("clinica-veterinaria.html", "blue", "bulldog-azul.jpg", "50% 40%",
  "Clínica<br>médica e<br>cirúrgica",
  "Salas de atendimento confortáveis e climatizadas e um centro cirúrgico com todo o suporte para procedimentos em padrão de excelência.",
  [("pill-lime", "top:18%;right:10%", "steth", "Consultas"), ("pill-white", "bottom:16%;right:18%", "shield", "Centro cirúrgico")],
  f'<a href="contato.html" class="btn btn-coral">Agendar consulta</a>{BTN_WA_W}') + f'''

    <section class="section">
      <div class="wrap split">
        <div class="stack reveal">
          <span class="pill pill-coral">{i("heart")} Atendimento com carinho</span>
          <img src="img/vet-gato.jpg" alt="Veterinária examinando um gato" loading="lazy">
          <img src="img/consultorio.jpg" alt="Consultório do Cemevi" loading="lazy">
        </div>
        <div class="reveal">
          <span class="kicker">{i("steth")} Atendimento clínico</span>
          <h2>A saúde do seu pet em dia, do check-up à cirurgia</h2>
          <p>No Cemevi você encontra tudo o que precisa para cuidar do seu cão ou gato. Nossa equipe é altamente qualificada e trata cada animal com muito carinho e profissionalismo.</p>
          <p>E quando o paciente precisa ficar em observação, a internação 24 horas fica na mesma estrutura, sem transferências.</p>
          <div class="hero-actions" style="margin-top:28px">
            <a href="contato.html" class="btn btn-ink">Marcar um horário</a>
            <a href="internacao-24-horas.html" class="btn btn-plain">Internação 24h {i("arrow")}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="wrap">
        <div class="head head-center reveal">
          <span class="kicker">{i("paw")} Serviços</span>
          <h2>O que fazemos na clínica</h2>
        </div>
        <div class="cards">
{cards([
  ("steth", "Consultas", "Atendimento clínico para cães e gatos, com salas confortáveis e climatizadas."),
  ("shield", "Cirurgias", "Centro cirúrgico com todo o suporte necessário para procedimentos em padrão de excelência."),
  ("syringe", "Vacinação e vermifugação", "Protocolos em dia e registrados na caderneta digital do SimplesPet."),
  ("pulse", "Exames", "Resultados disponíveis para você na área do cliente."),
  ("heart", "Emergência 24 horas", "Atendimento de urgência a qualquer hora, todos os dias da semana."),
  ("bed", "Pós-operatório", "Acompanhamento e internação na mesma estrutura, quando necessário."),
])}
        </div>
      </div>
    </section>
''' + band("coral", "Seu pet precisa de atendimento agora?", "Estamos abertos 24 horas. Ligue antes de sair de casa para agilizar a chegada.",
      f'<a href="{TEL}" class="btn btn-white">{i("phone")} (21) 3628-2484</a>') + f'''

    <section class="section">
      <div class="wrap">
        <div class="head head-center reveal"><span class="kicker">{i("chat")} Dúvidas</span><h2>Perguntas frequentes</h2></div>
        <div class="faq">
{faq([
  ("Vocês atendem sem hora marcada?", "Emergências são atendidas a qualquer hora, 24 horas por dia. Para consultas de rotina, recomendamos agendar pelo telefone ou WhatsApp para evitar espera."),
  ("Quais animais vocês atendem?", "Atendemos cães e gatos. Na internação, as duas espécies ficam em instalações separadas."),
  ("Onde vejo exames e vacinas do meu pet?", "Na área do cliente SimplesPet, onde ficam o histórico de peso, a caderneta de vacina, os resultados de exames, as receitas e os agendamentos."),
  ("Tem estacionamento?", "Sim. O Cemevi tem estacionamento próprio, na Rua Dr. Tavares de Macedo, 141, em Icaraí."),
])}
        </div>
      </div>
    </section>
  </main>
''' + FOOT

# ============================ INTERNAÇÃO ============================
pages["internacao-24-horas.html"] = head("Internação 24 horas — Cemevi, Icaraí",
  "Internação veterinária 24 horas no Cemevi, em Icaraí, Niterói. Cães e gatos em instalações separadas e acompanhamento em tempo integral.",
  "internacao-24-horas.html") + "\n  <main>" + phero("internacao-24-horas.html", "green", "bulldog-verde.jpg", "50% 30%",
  "Internação<br>24 horas",
  "Acompanhamento veterinário em tempo integral e muitas doses de carinho para acelerar a recuperação do seu pet.",
  [("pill-white", "top:20%;right:8%", "bed", "Cães e gatos separados"), ("pill-coral", "bottom:18%;right:20%", "heart", "Plantão dia e noite")],
  f'{BTN_CALL}{BTN_WA_W}') + f'''

    <section class="section">
      <div class="wrap split">
        <div class="reveal">
          <span class="kicker">{i("bed")} Tratamento assistido</span>
          <h2>Cuidado integral durante toda a estadia</h2>
          <p>Nossa equipe prioriza o bem-estar dos pacientes que precisam de tratamento assistido. Além dos cuidados médicos necessários, oferecemos também muitas doses de carinho para acelerar ainda mais o processo de recuperação.</p>
          <p>A internação conta com profissionais especializados e extremamente competentes, para oferecer o máximo conforto ao seu pet. E o mais importante: aqui todos nós amamos animais.</p>
        </div>
        <div class="stack reveal">
          <span class="pill pill-lime">{i("clock")} Acompanhamento 24h</span>
          <img src="img/internacao-a.jpg" alt="Baias da internação" loading="lazy">
          <img src="img/internacao-cao.jpg" alt="Cão em recuperação" loading="lazy">
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:40px">
      <div class="wrap">
        <div class="cards">
{cards([
  ("bed", "Alas separadas", "Instalações separadas para cães e gatos, reduzindo o estresse e respeitando as particularidades de cada espécie."),
  ("users", "Pacientes de parceiros", "Internamos também pacientes de colegas, com comunicação estreita com o médico veterinário de origem."),
  ("clock", "Tempo integral", "Acompanhamento veterinário 24 horas, inclusive fins de semana e feriados."),
])}
        </div>
      </div>
    </section>
''' + band("ink", "É veterinário e precisa internar um paciente?", "Recebemos pacientes de colegas parceiros e mantemos você informado durante toda a internação.",
      f'<a href="{TEL}" class="btn btn-coral">{i("phone")} Falar com a equipe</a>') + f'''

    <section class="section">
      <div class="wrap">
        <div class="head head-center reveal"><span class="kicker">{i("chat")} Dúvidas</span><h2>Perguntas frequentes</h2></div>
        <div class="faq">
{faq([
  ("Meu pet fica acompanhado à noite?", "Sim. A internação tem acompanhamento veterinário em tempo integral, 24 horas por dia."),
  ("Cães e gatos ficam no mesmo espaço?", "Não. A sala de internação tem instalações separadas para cães e gatos."),
  ("Meu veterinário não é do Cemevi. Posso internar aí?", "Pode. Recebemos pacientes de colegas parceiros e mantemos contato próximo com o médico de origem."),
])}
        </div>
      </div>
    </section>
  </main>
''' + FOOT

# ============================ BANHO E TOSA ============================
pages["banho-e-tosa.html"] = head("Banho e tosa — Cemevi, Icaraí",
  "Banho e tosa no Cemevi, em Icaraí, Niterói. Banhos terapêuticos, hidratação, tosa higiênica, padrão racial e na tesoura.",
  "banho-e-tosa.html") + "\n  <main>" + phero("banho-e-tosa.html", "orange", "corgi-laranja.jpg", "50% 35%",
  "Banho<br>e tosa",
  "Um setor de estética animal que cuida da higiene e do conforto do seu pet. Ele sai daqui impecável.",
  [("pill-lime", "top:20%;right:10%", "drop", "Hidratação"), ("pill-white", "bottom:18%;right:16%", "scissors", "Tosa na tesoura")],
  f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-white">{i("wa")} Agendar pelo WhatsApp</a>') + f'''

    <section class="section">
      <div class="wrap split">
        <div class="stack reveal">
          <span class="pill pill-coral">{i("drop")} Banho</span>
          <img src="img/banho-gato.jpg" alt="Gato tomando banho" loading="lazy" style="object-position:50% 15%">
          <img src="img/samoieda.jpg" alt="Samoieda depois do banho" loading="lazy">
        </div>
        <div class="reveal">
          <span class="kicker">{i("drop")} Banho</span>
          <h2>Diversos tipos de banho, para cada pele e pelagem</h2>
          <p>Nosso setor de estética animal oferece os mais diversos tipos de banho para a higiene e o conforto do seu pet, como banhos terapêuticos, hidratações e tratamentos diferenciados.</p>
          <div class="chips" style="margin-top:24px">
            <span class="chip">Terapêutico</span><span class="chip">Hidratação</span><span class="chip">Tratamentos</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:40px">
      <div class="wrap split">
        <div class="reveal">
          <span class="kicker">{i("scissors")} Tosa</span>
          <h2>Tosa estética ou higiênica, na máquina ou na tesoura</h2>
          <p>A tosa é feita tanto com objetivo estético quanto para a higiene do seu cão ou gato. Nossos profissionais de estética animal são habilitados para diversas modalidades.</p>
          <p>Para escolher o tipo de tosa, leve em conta as características do pelo do animal e o tempo que você pode dedicar à escovação. Na dúvida, a gente ajuda a decidir.</p>
        </div>
        <div class="stack reveal">
          <span class="pill pill-lime">{i("scissors")} Tosa</span>
          <img src="img/tosa.jpg" alt="Shih-tzu sendo tosado na tesoura" loading="lazy" style="object-position:50% 20%">
          <img src="img/bulldog-amarelo.jpg" alt="Buldogue francês" loading="lazy">
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:40px">
      <div class="wrap">
        <div class="cards">
{cards([
  ("scissors", "Tosa higiênica", "Limpeza das regiões íntimas, patas e rosto, para o dia a dia com mais conforto."),
  ("sparkle", "Tosa padrão racial", "O corte característico de cada raça, feito por profissionais habilitados."),
  ("heart", "Tosa especial na tesoura", "Acabamento feito à mão, para quem quer um visual mais caprichado."),
])}
        </div>
      </div>
    </section>
''' + band("purple", "Agende o banho do seu pet", "Chame no WhatsApp e escolha o melhor horário.",
      f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-white">{i("wa")} (21) 96752-0101</a>') + '''
  </main>
''' + FOOT

# ============================ FARMÁCIA ============================
pages["farmacia-veterinaria.html"] = head("Farmácia veterinária — Cemevi, Icaraí",
  "Farmácia veterinária do Cemevi em Icaraí, Niterói. Em breve, medicamentos diferenciados com os melhores preços.",
  "farmacia-veterinaria.html") + "\n  <main>" + phero("farmacia-veterinaria.html", "yellow", "pug-amarelo.jpg", "50% 40%",
  "Farmácia<br>veterinária",
  "Em breve teremos uma farmácia própria, com tudo o que você precisa para manter a saúde do seu pet em dia.",
  [("pill-coral", "top:20%;right:10%", "pill", "Em breve")],
  f'<a href="contato.html" class="btn btn-ink">Quero ser avisado</a>') + f'''

    <section class="section">
      <div class="wrap split">
        <div class="stack reveal">
          <span class="pill pill-lime">{i("pill")} Medicamentos</span>
          <img src="img/farmacia-a.jpg" alt="Prateleiras de medicamentos" loading="lazy">
          <img src="img/farmacia-gato.jpg" alt="Gato recebendo petisco" loading="lazy">
        </div>
        <div class="reveal">
          <span class="kicker">{i("pill")} Em breve</span>
          <h2>A receita resolvida sem sair da clínica</h2>
          <p>Vamos oferecer um mix de medicamentos diferenciados com os melhores preços, dentro da mesma estrutura em que seu pet é atendido.</p>
          <p>Enquanto isso, as receitas emitidas pelos nossos veterinários ficam disponíveis na área do cliente SimplesPet.</p>
          <div class="hero-actions" style="margin-top:28px">
            <a href="{SP}" target="_blank" rel="noopener" class="btn btn-ink">Ver minhas receitas</a>
          </div>
        </div>
      </div>
    </section>
''' + band("coral", "Quer saber quando a farmácia abrir?", "Mande uma mensagem e avisamos você.",
      f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-white">{i("wa")} Me avise</a>') + '''
  </main>
''' + FOOT

# ============================ CONTATO ============================
pages["contato.html"] = head("Contato — Cemevi, Icaraí",
  "Contato do Cemevi: Rua Dr. Tavares de Macedo, 141, Icaraí, Niterói/RJ. (21) 3628-2484. Aberto 24 horas.",
  "contato.html") + "\n  <main>" + phero("contato.html", "pink", "jack-rosa.jpg", "60% 40%",
  "Fale com<br>a gente",
  "Estamos abertos 24 horas, todos os dias. Para emergências, ligue direto para a clínica.",
  [("pill-coral", "top:18%;right:10%", "clock", "Aberto agora")],
  f'{BTN_CALL}<a href="{WA}" target="_blank" rel="noopener" class="btn btn-ink">{i("wa")} WhatsApp</a>') + f'''

    <section class="section">
      <div class="wrap contact">
        <div class="visit-card reveal">
          <h2>Informações</h2>
          <ul class="visit-list">
            <li><span class="vi">{i("pin")}</span><div><b>Endereço</b>Rua Dr. Tavares de Macedo, 141, Casa 3<br>Icaraí — Niterói/RJ</div></li>
            <li><span class="vi">{i("phone")}</span><div><b>Telefone</b><a href="{TEL}">(21) 3628-2484</a></div></li>
            <li><span class="vi">{i("wa")}</span><div><b>WhatsApp</b><a href="{WA}" target="_blank" rel="noopener">(21) 96752-0101</a></div></li>
            <li><span class="vi">{i("mail")}</span><div><b>E-mail</b><a href="mailto:simonek-22@hotmail.com">simonek-22@hotmail.com</a></div></li>
            <li><span class="vi">{i("clock")}</span><div><b>Horário</b>Segunda a domingo, 24 horas</div></li>
            <li><span class="vi">{i("car")}</span><div><b>Estacionamento</b>Próprio, no local</div></li>
          </ul>
          <div class="social">
            <a href="https://www.instagram.com/cemeviniteroi" target="_blank" rel="noopener" aria-label="Instagram">{i("ig")}</a>
            <a href="https://www.facebook.com/cemeviniteroi" target="_blank" rel="noopener" aria-label="Facebook">{i("fb")}</a>
          </div>
        </div>

        <div class="form-card reveal">
          <h2>Envie uma mensagem</h2>
          <p>Preencha e sua mensagem abre pronta no nosso WhatsApp.</p>
          <form class="form" id="contato-form">
            <div class="form-row">
              <div><label for="nome">Seu nome</label><input id="nome" name="nome" required autocomplete="name"></div>
              <div><label for="telefone">Telefone</label><input id="telefone" name="telefone" type="tel" autocomplete="tel" placeholder="(21) 90000-0000"></div>
            </div>
            <div>
              <label>Seu pet é</label>
              <div class="pets">
                <label><input type="radio" name="especie" value="Cachorro"><span>Cachorro</span></label>
                <label><input type="radio" name="especie" value="Gato"><span>Gato</span></label>
                <label><input type="radio" name="especie" value="Outro"><span>Outro</span></label>
              </div>
            </div>
            <div class="form-row">
              <div><label for="pet">Nome do pet</label><input id="pet" name="pet" placeholder="Ex.: Nina"></div>
              <div><label for="assunto">Assunto</label>
                <select id="assunto" name="assunto">
                  <option value="">Selecione</option>
                  <option>Consulta</option>
                  <option>Cirurgia</option>
                  <option>Internação</option>
                  <option>Banho e tosa</option>
                  <option>Outro</option>
                </select>
              </div>
            </div>
            <div><label for="mensagem">Mensagem</label><textarea id="mensagem" name="mensagem" required></textarea></div>
            <div><button type="submit" class="btn btn-coral">{i("wa")} Enviar pelo WhatsApp</button></div>
            <p class="form-note">Em emergências, não espere resposta por mensagem: ligue para (21) 3628-2484.</p>
          </form>
        </div>
      </div>
    </section>

    <section class="section" id="mapa" style="padding-top:0;padding-bottom:0">
      <div class="wrap">
        <iframe class="map reveal" title="Mapa: Cemevi em Icaraí" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=Rua+Dr.+Tavares+de+Macedo,+141,+Icara%C3%AD,+Niter%C3%B3i+-+RJ&output=embed"></iframe>
      </div>
    </section>
  </main>
''' + FOOT

for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
print("ok", list(pages))
