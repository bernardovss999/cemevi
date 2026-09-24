import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SP = "http://meu.simplespet.com.br/#/access/login?a=centro-medico-veterinario-icar"
WA = "https://wa.me/5521967520101"
TEL = "tel:+552136282484"
ROTA = "https://www.google.com/maps/dir/?api=1&destination=Rua+Dr.+Tavares+de+Macedo,+141,+Icara%C3%AD,+Niter%C3%B3i+-+RJ"
MAP = "https://www.google.com/maps?q=Rua+Dr.+Tavares+de+Macedo,+141,+Icara%C3%AD,+Niter%C3%B3i+-+RJ&output=embed"

src = open(os.path.join(HERE, "build2.py"), encoding="utf-8").read()
SPRITE = re.search(r"SPRITE = '''(.*?)'''", src, re.S).group(1)
SPRITE = SPRITE.replace("</svg>", '  <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>\n</svg>')

NAV = [("home.html", "Início"), ("clinica-veterinaria.html", "Clínica"),
       ("internacao-24-horas.html", "Internação 24h"), ("banho-e-tosa.html", "Banho e tosa"),
       ("farmacia-veterinaria.html", "Farmácia"), ("contato.html", "Contato")]

def i(name, extra=""):
    fill = " ico-fill" if name in ("paw", "wa") else ""
    return f'<svg class="ico{fill}{extra}" aria-hidden="true"><use href="#i-{name}"/></svg>'

ARROW = i("arrow", " ico-arrow")

def paw(style, cls="paw-deco"):
    return f'<svg class="{cls} ico-fill" style="{style}" aria-hidden="true"><use href="#i-paw"/></svg>'

def head(title, desc, page):
    act = ' class="active" aria-current="page"'
    items = "\n".join(f'            <li><a href="{h}"{act if h == page else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#22625e">
  <title>{title}</title>
  <link rel="icon" type="image/png" href="img/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
  <script>document.documentElement.classList.add('js', 'intro');</script>
</head>
<body>
  <div class="curtain" aria-hidden="true"><img src="img/logo-branco.png" alt="" width="120" height="82"></div>
{SPRITE}

  <header class="header">
    <p class="sett-faixa">Prévia feita pela <a href="https://www.sett.company/" target="_blank" rel="noopener"><img src="img/sett-branco.png" alt="Sett" width="254" height="96"></a> para <b>Cemevi</b> · não oficial</p>
    <div class="topbar">
      <div class="wrap">
        <div class="topbar-l">
          <span>{i("clock")}Aberto 24 horas, todos os dias</span>
          <span class="hide-md">{i("pin")}Rua Dr. Tavares de Macedo, 141 — Icaraí, Niterói</span>
        </div>
        <div class="topbar-r">
          <a href="{TEL}">{i("phone")}(21) 3628-2484</a>
          <a href="https://www.instagram.com/cemeviniteroi" target="_blank" rel="noopener">Instagram</a>
          <a href="https://www.facebook.com/cemeviniteroi" target="_blank" rel="noopener">Facebook</a>
        </div>
      </div>
    </div>
    <div class="bar">
      <div class="wrap">
        <a href="home.html" class="brand" aria-label="Cemevi — página inicial">
          <img class="logo-white" src="img/logo-branco.png" alt="" width="104" height="71">
          <img class="logo-color" src="img/logo.png" alt="Cemevi — Centro Médico Veterinário Icaraí" width="104" height="71">
        </a>
        <nav class="nav" id="nav" aria-label="Principal">
          <ul>
{items}
          </ul>
          <div class="nav-extra">
            <a href="{TEL}">(21) 3628-2484 · aberto 24 horas</a>
            <span>Rua Dr. Tavares de Macedo, 141 — Icaraí, Niterói</span>
            <a class="btn btn-light" href="{SP}" target="_blank" rel="noopener">Área do cliente</a>
          </div>
        </nav>
        <div class="header-actions">
          <a class="header-link" href="{SP}" target="_blank" rel="noopener">Área do cliente</a>
          <a class="btn btn-onphoto" href="contato.html">Agendar consulta</a>
          <button class="menu-btn" aria-expanded="false" aria-controls="nav"><span class="menu-label">Menu</span><span class="menu-lines"></span></button>
        </div>
      </div>
    </div>
  </header>
'''

FOOT = f'''
  <footer class="footer">
    {paw("width:320px;height:320px;right:-60px;top:-40px;transform:rotate(18deg)", "footer-paw")}
    <div class="wrap">
      <div class="footer-top">
        <h2>Precisa de atendimento? Estamos aqui 24 horas.</h2>
        <div class="split-actions" style="margin-top:0">
          <a href="{TEL}" class="btn btn-light">{i("phone")} (21) 3628-2484</a>
          <a href="{WA}" target="_blank" rel="noopener" class="btn btn-ghost">{i("wa")} WhatsApp</a>
        </div>
      </div>
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="img/logo-branco.png" alt="Cemevi — Centro Médico Veterinário Icaraí" width="130" height="89">
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
            <li><a href="home.html#estrutura">Nossa estrutura</a></li>
            <li><a href="{SP}" target="_blank" rel="noopener">Área do cliente</a></li>
            <li><a href="contato.html">Contato</a></li>
            <li><a href="{ROTA}" target="_blank" rel="noopener">Como chegar</a></li>
          </ul>
        </div>
        <div>
          <h3>Endereço</h3>
          <ul>
            <li>Rua Dr. Tavares de Macedo, 141, Casa 3<br>Icaraí — Niterói/RJ</li>
            <li><a href="mailto:simonek-22@hotmail.com">simonek-22@hotmail.com</a></li>
            <li>Segunda a domingo, 24 horas</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Cemevi — Centro Médico Veterinário Icaraí</span>
        <a class="credit" href="https://www.sett.company/" target="_blank" rel="noopener" aria-label="Site desenvolvido pela Sett Digital">Desenvolvido por <span class="sett">sett<i>.</i></span></a>
      </div>
    </div>
  </footer>

  <a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">{i("wa")}</a>
  <nav class="dock" aria-label="Contato rápido">
    <a class="dock-call" href="{TEL}">{i("phone")} Ligar</a>
    <a class="dock-wa" href="{WA}" target="_blank" rel="noopener">{i("wa")} WhatsApp</a>
  </nav>

  <script src="js/main.js"></script>
</body>
</html>
'''

def phero(page, img, pos, title, lead, actions):
    crumb = dict(NAV)[page]
    first = (img, pos, "Cemevi · " + crumb, "h1", title, lead, actions, crumb)
    return slider_html([first] + EXTRA[page], crumb) + FACTS

def cards(items):
    return "\n".join(f'''        <article class="card reveal">
          <div class="card-ico">{i(ic)}</div>
          <h3>{t}</h3>
          <p>{d}</p>
        </article>''' for ic, t, d in items)

def faq(title, lead, items):
    qs = "\n".join(f'          <details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'''
  <section class="section">
    <div class="wrap faq-layout">
      <div class="reveal">
        <span class="kicker">Dúvidas frequentes</span>
        <h2 class="h2">{title}</h2>
        <p class="lead">{lead}</p>
        <a href="{WA}" target="_blank" rel="noopener" class="link">Falar com a equipe {i("arrow")}</a>
      </div>
      <div class="faq reveal">
{qs}
      </div>
    </div>
  </section>'''

def band(title, text, actions):
    return f'''
  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="band reveal">
        {paw("", "band-paw")}
        <div>
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <div class="split-actions">{actions}</div>
      </div>
    </div>
  </section>'''

def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i('check')}<span>{t}</span></li>" for t in items) + "</ul>"

BTN_CALL_L = f'<a href="{TEL}" class="btn btn-light">{i("phone")} Ligar agora</a>'
BTN_WA_G = f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-ghost">{i("wa")} WhatsApp</a>'


def slider_html(slides, label):
    out = []
    for n, (img, pos, kick, tag, title, text, acts, _) in enumerate(slides):
        cls = "" if tag == "h1" else ' class="slide-title"'
        load = 'fetchpriority="high"' if n == 0 else 'loading="lazy"'
        out.append(f'''    <div class="slide{" is-active" if n == 0 else ""}" role="group" aria-roledescription="slide" aria-label="{n+1} de {len(slides)}">
      <img class="slide-img" src="img/{img}" alt="" style="object-position:{pos}" {load}>
      <div class="slide-content">
        <div class="wrap">
          <div class="slide-text">
            <span class="kicker">{kick}</span>
            <{tag}{cls}>{title}</{tag}>
            <p>{text}</p>
            <div class="slide-actions">{acts}</div>
          </div>
        </div>
      </div>
    </div>''')
    tabs = chr(10).join(f'          <button class="slider-tab" type="button"><span class="track"><i></i></span><b>0{n+1}</b>{sl[7]}</button>' for n, sl in enumerate(slides))
    dots = "".join(f'<button class="slider-dot" type="button" aria-label="Slide {n+1}"></button>' for n in range(len(slides)))
    return f'''
  <section class="slider" aria-roledescription="carrossel" aria-label="{label}" tabindex="-1">
{chr(10).join(out)}
    <div class="slider-ui">
      <div class="wrap">
        <div class="slider-tabs">
{tabs}
        </div>
        <div class="slider-dots">{dots}</div>
        <div class="slider-arrows">
          <button class="slider-arrow prev" type="button" aria-label="Anterior">{i("arrow")}</button>
          <button class="slider-arrow next" type="button" aria-label="Próximo">{i("arrow")}</button>
        </div>
      </div>
    </div>
  </section>'''

FACTS = f'''
  <section class="facts">
    <div class="wrap">
      <div class="fact"><span class="fact-ico">{i("clock")}</span><div><b>Aberto 24 horas</b><span>Todos os dias, inclusive fins de semana e feriados</span></div></div>
      <div class="fact"><span class="fact-ico">{i("phone")}</span><div><b><a href="{TEL}">(21) 3628-2484</a></b><span>Emergência e agendamentos</span></div></div>
      <div class="fact"><span class="fact-ico">{i("car")}</span><div><b>Estacionamento próprio</b><span>Em uma das principais ruas de Icaraí</span></div></div>
      <div class="fact"><span class="fact-ico">{i("heart")}</span><div><b>Cães e gatos</b><span>Com alas separadas na internação</span></div></div>
    </div>
  </section>'''

pages = {}

# ================================ HOME ================================
AGENDAR = f'<a href="contato.html" class="btn btn-light">Agendar consulta {ARROW}</a>'
AREA = f'<a href="{SP}" target="_blank" rel="noopener" class="btn btn-light">Área do cliente {ARROW}</a>'
ROTA_G = f'<a href="{ROTA}" target="_blank" rel="noopener" class="btn btn-ghost">Como chegar</a>'
EXTRA = {
  "clinica-veterinaria.html": [
    ("consulta-gato.jpg", "30% 40%", "Consultas", "h2", "Atendimento para cães e gatos, com carinho e atenção.",
     "Consultórios confortáveis e climatizados e uma equipe altamente qualificada.", AGENDAR + BTN_WA_G, "Consultas"),
    ("hd-filhotes.jpg", "50% 60%", "Vacinação", "h2", "Vacinas e vermifugação em dia.",
     "Tudo registrado na caderneta digital do SimplesPet, para você acompanhar de casa.", AREA + '<a href="contato.html" class="btn btn-ghost">Agendar</a>', "Vacinas"),
    ("slide-carinho.jpg", "50% 35%", "Emergência 24 horas", "h2", "Atendimento de urgência a qualquer hora.",
     "Se o seu pet precisa de ajuda agora, ligue e venha direto. Estamos abertos todos os dias.", BTN_CALL_L + ROTA_G, "Emergência"),
  ],
  "internacao-24-horas.html": [
    ("hd-cavalier.jpg", "50% 70%", "Alas separadas", "h2", "Cães e gatos em espaços separados.",
     "Instalações separadas reduzem o estresse e respeitam as particularidades de cada espécie.", BTN_CALL_L + BTN_WA_G, "Alas separadas"),
    ("hd-gato-laranja.jpg", "50% 45%", "Veterinários parceiros", "h2", "Internação também para pacientes de colegas.",
     "Sempre com comunicação próxima com o médico veterinário de origem.", f'<a href="{TEL}" class="btn btn-light">{i("phone")} Falar com a equipe</a>', "Parceiros"),
  ],
  "banho-e-tosa.html": [
    ("hd-retriever.jpg", "50% 35%", "Banho", "h2", "Banhos terapêuticos, hidratação e tratamentos.",
     "Diversos tipos de banho para a higiene e o conforto do seu pet.", f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">{i("wa")} Agendar banho</a>', "Banho"),
    ("hd-dois-caes.jpg", "50% 60%", "Tosa", "h2", "Tosa higiênica, padrão racial ou na tesoura.",
     "Profissionais de estética animal habilitados, na máquina ou na tesoura.", f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">{i("wa")} Agendar tosa</a>', "Tosa"),
  ],
  "farmacia-veterinaria.html": [
    ("hd-cao-oculos.jpg", "50% 40%", "Em breve", "h2", "Medicamentos diferenciados com os melhores preços.",
     "A receita resolvida no mesmo lugar em que seu pet é atendido.", f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">Quero ser avisado {ARROW}</a>', "Medicamentos"),
    ("hd-gato-sorriso.jpg", "50% 40%", "Enquanto isso", "h2", "Suas receitas ficam no SimplesPet.",
     "Acesse receitas, vacinas, exames e agendamentos do seu animal pela área do cliente.", AREA, "Receitas"),
  ],
  "contato.html": [
    ("hd-caes-gatos.jpg", "40% 50%", "WhatsApp", "h2", "Chame no <span style=\"white-space:nowrap\">(21) 96752-0101</span>.",
     "Tire dúvidas e agende consultas, banho e tosa pelo WhatsApp.", f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">{i("wa")} Abrir conversa</a>', "WhatsApp"),
    ("hd-cao-rua.jpg", "50% 45%", "Como chegar", "h2", "Rua Dr. Tavares de Macedo, 141, Icaraí.",
     "Estamos em uma das principais ruas de Icaraí, com estacionamento próprio.", f'<a href="{ROTA}" target="_blank" rel="noopener" class="btn btn-light">Traçar rota {ARROW}</a>', "Endereço"),
  ],
}

SLIDES = [
  ("slide-caes-gatos.jpg", "50% 60%", "Cemevi · Icaraí, Niterói", "h1",
   "Cuidado veterinário de verdade, 24 horas por dia.",
   "Clínica médica e cirúrgica, emergência, internação e banho e tosa. Uma equipe altamente qualificada, que trata seu animal com carinho e profissionalismo.",
   f'<a href="contato.html" class="btn btn-light">Agendar consulta {ARROW}</a><a href="#servicos" class="btn btn-ghost">Conhecer os serviços</a>',
   "Boas-vindas"),
  ("slide-clinica.jpg", "60% 40%", "Clínica médica e cirúrgica", "h2",
   "Consultórios climatizados e centro cirúrgico completo.",
   "Salas de atendimento confortáveis e todo o suporte para procedimentos em padrão de excelência.",
   f'<a href="clinica-veterinaria.html" class="btn btn-light">Conhecer a clínica {ARROW}</a><a href="contato.html" class="btn btn-ghost">Agendar</a>',
   "Clínica"),
  ("slide-internacao.jpg", "50% 60%", "Internação 24 horas", "h2",
   "Acompanhamento em tempo integral, dia e noite.",
   "Instalações separadas para cães e gatos e muitas doses de carinho para acelerar a recuperação.",
   f'<a href="internacao-24-horas.html" class="btn btn-light">Sobre a internação {ARROW}</a>{BTN_CALL_L.replace("btn-light", "btn-ghost")}',
   "Internação"),
  ("slide-banho.jpg", "60% 35%", "Banho e tosa", "h2",
   "Seu pet limpo, confortável e bem cuidado.",
   "Banhos terapêuticos, hidratação e tosa higiênica, padrão racial ou na tesoura.",
   f'<a href="banho-e-tosa.html" class="btn btn-light">Ver banho e tosa {ARROW}</a>{BTN_WA_G}',
   "Banho e tosa"),
  ("slide-carinho.jpg", "50% 35%", "Emergência", "h2",
   "Aberto agora. A qualquer hora, todos os dias.",
   "Se o seu pet precisa de atendimento urgente, ligue e venha direto. Temos estacionamento próprio.",
   f'{BTN_CALL_L}<a href="{ROTA}" target="_blank" rel="noopener" class="btn btn-ghost">Como chegar</a>',
   "Emergência"),
]

pages["home.html"] = head("Cemevi — Centro Médico Veterinário Icaraí | Clínica veterinária 24h em Niterói",
  "Cemevi — Centro Médico Veterinário Icaraí. Clínica médica e cirúrgica, emergência e internação 24 horas, banho e tosa em Niterói/RJ.",
  "home.html") + f'''
  <main>
{slider_html(SLIDES, 'Destaques do Cemevi')}
{FACTS}

  <section class="section">
    <div class="wrap split">
      <div class="reveal">
        <span class="kicker">Seja bem-vindo</span>
        <h2>Uma estrutura completa para cuidar do seu melhor amigo</h2>
        <p>O Cemevi dispõe de uma excelente estrutura e de uma equipe altamente qualificada, que vai tratar seu animal com muito carinho e profissionalismo. Tudo o que você espera de um atendimento veterinário de qualidade, em um só lugar.</p>
        <p class="quote">Cada espaço da clínica foi pensado para oferecer a você e ao seu animal a melhor experiência que vocês já tiveram em uma clínica veterinária.</p>
        <p>Além da clínica, você conta com um serviço de banho e tosa que vai deixar seu pet impecável. Venha nos conhecer.</p>
        <div class="split-actions">
          <a href="#estrutura" class="btn btn-primary">Ver a estrutura {ARROW}</a>
          <a href="{ROTA}" target="_blank" rel="noopener" class="btn btn-outline">Como chegar</a>
        </div>
      </div>
      <div class="duo reveal">
        <img src="img/vet-gato.jpg" alt="Veterinária examinando um gato" loading="lazy">
        <img src="img/fachada.jpg" alt="Fachada do Cemevi em Icaraí" loading="lazy">
        <p class="duo-note">Nossa sede fica na Rua Dr. Tavares de Macedo, 141, em Icaraí.</p>
      </div>
    </div>
  </section>

  <section class="section section-tint" id="servicos">
    <div class="wrap">
      <div class="head reveal">
        <div>
          <span class="kicker">Serviços</span>
          <h2>Da consulta ao banho, o cuidado acontece aqui dentro</h2>
        </div>
        <p>Tudo na mesma estrutura: se o seu pet precisar ficar em observação depois de uma consulta ou cirurgia, ele não precisa ser transferido.</p>
      </div>
      <div class="services">
        <a class="service reveal" href="clinica-veterinaria.html">
          <div class="service-img"><img src="img/vet-gato.jpg" alt="" loading="lazy"></div>
          <div class="service-body"><span class="service-num">01</span><h3>Clínica médica e cirúrgica</h3><p>Consultórios climatizados e centro cirúrgico com todo o suporte necessário.</p><span class="link">Saiba mais {i("arrow")}</span></div>
        </a>
        <a class="service reveal" href="internacao-24-horas.html">
          <div class="service-img"><img src="img/cat-internacao.jpg" alt="" loading="lazy"></div>
          <div class="service-body"><span class="service-num">02</span><h3>Internação 24 horas</h3><p>Acompanhamento em tempo integral, com cães e gatos em espaços separados.</p><span class="link">Saiba mais {i("arrow")}</span></div>
        </a>
        <a class="service reveal" href="banho-e-tosa.html">
          <div class="service-img"><img src="img/cat-banho.jpg" alt="" loading="lazy"></div>
          <div class="service-body"><span class="service-num">03</span><h3>Banho e tosa</h3><p>Banhos terapêuticos, hidratação e tosa higiênica, racial ou na tesoura.</p><span class="link">Saiba mais {i("arrow")}</span></div>
        </a>
        <a class="service reveal" href="farmacia-veterinaria.html">
          <div class="service-img"><img src="img/cat-farmacia.jpg" alt="" loading="lazy"></div>
          <div class="service-body"><span class="service-num">04</span><h3>Farmácia veterinária</h3><p>Em breve, medicamentos diferenciados com os melhores preços.</p><span class="link">Saiba mais {i("arrow")}</span></div>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="head head-center reveal">
        <span class="kicker">Atendimento</span>
        <h2>O que seu pet encontra no Cemevi</h2>
      </div>
      <div class="cats">
        <a class="cat reveal" href="clinica-veterinaria.html"><div class="cat-img"><img src="img/cat-consultas.jpg" alt="" loading="lazy"></div><h3>Consultas</h3><span>Cães e gatos</span></a>
        <a class="cat reveal" href="clinica-veterinaria.html"><div class="cat-img"><img src="img/schnauzer.jpg" alt="" loading="lazy"></div><h3>Cirurgias</h3><span>Centro cirúrgico</span></a>
        <a class="cat reveal" href="clinica-veterinaria.html"><div class="cat-img"><img src="img/cat-vacinas.jpg" alt="" loading="lazy"></div><h3>Vacinas</h3><span>E vermifugação</span></a>
        <a class="cat reveal" href="internacao-24-horas.html"><div class="cat-img"><img src="img/cavalier.jpg" alt="" loading="lazy"></div><h3>Internação</h3><span>24 horas</span></a>
        <a class="cat reveal" href="banho-e-tosa.html"><div class="cat-img"><img src="img/cat-banho.jpg" alt="" loading="lazy"></div><h3>Banho e tosa</h3><span>Estética animal</span></a>
        <a class="cat reveal" href="internacao-24-horas.html"><div class="cat-img"><img src="img/dois-caes.jpg" alt="" loading="lazy"></div><h3>Emergência</h3><span>A qualquer hora</span></a>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap twins">
      <div class="twin twin-dark reveal">
        <span class="kicker">Para veterinários parceiros</span>
        <h2>Internação para pacientes de colegas</h2>
        <p>Recebemos pacientes de outros veterinários, sempre em contato próximo com o médico de origem.</p>
        <a href="internacao-24-horas.html" class="btn btn-light">Saiba como funciona</a>
        <img src="img/gato-laranja.jpg" alt="" loading="lazy">
      </div>
      <div class="twin twin-light reveal">
        <span class="kicker">Em breve</span>
        <h2>Farmácia veterinária própria</h2>
        <p>A receita resolvida sem sair da clínica, com um mix de medicamentos e os melhores preços.</p>
        <a href="farmacia-veterinaria.html" class="btn btn-primary">Saiba mais</a>
        <img src="img/cao-oculos.jpg" alt="" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section section-white" id="estrutura">
    <div class="wrap">
      <div class="head reveal">
        <div>
          <span class="kicker">Nossa casa</span>
          <h2>Conheça a estrutura do Cemevi</h2>
          <p>Salas climatizadas, recepção acolhedora e uma internação preparada para cães e gatos.</p>
        </div>
        <div class="chips" role="group" aria-label="Filtrar fotos">
          <button class="chip active" data-filter="all" aria-pressed="true">Todos</button>
          <button class="chip" data-filter="atendimento" aria-pressed="false">Atendimento</button>
          <button class="chip" data-filter="internacao" aria-pressed="false">Internação</button>
        </div>
      </div>
      <div class="gallery">
        <figure class="shot reveal" data-cat="atendimento"><img src="img/fachada.jpg" alt="Fachada do Cemevi" loading="lazy"><figcaption>Fachada</figcaption></figure>
        <figure class="shot reveal" data-cat="atendimento"><img src="img/recepcao.jpg" alt="Recepção" loading="lazy"><figcaption>Recepção</figcaption></figure>
        <figure class="shot reveal" data-cat="atendimento"><img src="img/consultorio.jpg" alt="Consultório" loading="lazy"><figcaption>Consultório</figcaption></figure>
        <figure class="shot reveal" data-cat="internacao"><img src="img/internacao-b.jpg" alt="Sala de internação" loading="lazy"><figcaption>Sala de internação</figcaption></figure>
        <figure class="shot reveal" data-cat="internacao"><img src="img/internacao-a.jpg" alt="Baias da internação" loading="lazy"><figcaption>Baias</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="head head-center reveal">
        <span class="kicker">Como agendar</span>
        <h2>Simples do primeiro contato ao retorno</h2>
      </div>
      <div class="steps">
        <div class="step reveal"><h3>Fale com a gente</h3><p>Ligue para (21) 3628-2484 ou chame no WhatsApp. Atendemos 24 horas.</p></div>
        <div class="step reveal"><h3>Escolha o horário</h3><p>Marcamos a consulta, o banho ou a tosa no melhor momento para você.</p></div>
        <div class="step reveal"><h3>Traga seu pet</h3><p>Estamos em Icaraí, com estacionamento próprio para facilitar a chegada.</p></div>
        <div class="step reveal"><h3>Acompanhe tudo</h3><p>Vacinas, exames e receitas ficam na área do cliente SimplesPet.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="app reveal">
        <div class="app-copy">
          <span class="kicker">Área do cliente</span>
          <h2>A saúde do seu pet na palma da mão</h2>
          <p>Pelo SimplesPet você acompanha tudo o que acontece com seu animal aqui no Cemevi.</p>
          <ul class="app-list">
            <li>{i("scale")} Histórico de peso</li>
            <li>{i("syringe")} Caderneta de vacina</li>
            <li>{i("pulse")} Resultados de exames</li>
            <li>{i("file")} Receitas</li>
            <li>{i("cal")} Agendamentos</li>
          </ul>
          <a href="{SP}" target="_blank" rel="noopener" class="btn btn-light">Acessar o SimplesPet {ARROW}</a>
        </div>
        <div class="app-stage" aria-hidden="true">
          <svg class="bigpaw ico-fill" viewBox="0 0 24 24"><use href="#i-paw"/></svg>
          <div class="phone">
            <div class="phone-bar"><span>9:41</span><span>SimplesPet</span></div>
            <div class="phone-pet"><img src="img/cat-vacinas.jpg" alt="" loading="lazy"></div>
            <div class="phone-body">
              <div class="phone-name"><strong>Nina</strong><span>Gata · SRD</span></div>
              <div class="phone-grid"><div>Idade<b>1 ano</b></div><div>Peso<b>2,7 kg</b></div></div>
              <div class="phone-row"><b>Vacinas em dia</b>Próxima dose em 12/2026</div>
              <div class="phone-btn">{i("cal")} Agendar retorno</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
''' + faq("Perguntas que recebemos todos os dias", "Não encontrou sua dúvida? Fale com a equipe pelo WhatsApp.", [
  ("Vocês atendem a qualquer hora?", "Sim. O Cemevi funciona 24 horas, de segunda a domingo, inclusive feriados. Emergências são atendidas a qualquer momento."),
  ("Preciso agendar a consulta?", "Para consultas de rotina, banho e tosa, recomendamos agendar pelo telefone ou WhatsApp para evitar espera. Em emergências, venha direto."),
  ("Quais animais vocês atendem?", "Atendemos cães e gatos. Na internação, as duas espécies ficam em instalações separadas."),
  ("Onde vejo vacinas, exames e receitas?", "Na área do cliente SimplesPet, que reúne histórico de peso, caderneta de vacina, resultados de exames, receitas e agendamentos."),
  ("Tem estacionamento?", "Sim, estacionamento próprio, na Rua Dr. Tavares de Macedo, 141, em Icaraí."),
]) + f'''

  <section class="pals">
    <div class="pals-side pals-left reveal"><img src="img/gato-laranja.jpg" alt="" loading="lazy"></div>
    <div class="pals-side pals-right reveal"><img src="img/caes-gatos-juntos.jpg" alt="" loading="lazy" style="object-position:40% 50%"></div>
    <div class="wrap reveal">
      <span class="kicker">Venha nos conhecer</span>
      <h2>Seu melhor amigo em boas mãos</h2>
      <p>Estrutura excelente, equipe qualificada e muito carinho, a poucos minutos de você em Icaraí.</p>
      <div class="split-actions">
        <a href="contato.html" class="btn btn-primary">Agendar consulta {ARROW}</a>
        <a href="{TEL}" class="btn btn-outline">{i("phone")} (21) 3628-2484</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap visit">
      <div class="visit-card reveal">
        <span class="kicker">Visite</span>
        <h2>Estamos em Icaraí</h2>
        <ul class="visit-list">
          <li><span class="vi">{i("pin")}</span><div><b>Endereço</b>Rua Dr. Tavares de Macedo, 141, Casa 3<br>Icaraí — Niterói/RJ</div></li>
          <li><span class="vi">{i("phone")}</span><div><b>Telefones</b><a href="{TEL}">(21) 3628-2484</a> · <a href="{WA}" target="_blank" rel="noopener">(21) 96752-0101</a></div></li>
          <li><span class="vi">{i("clock")}</span><div><b>Horário</b>Segunda a domingo, 24 horas</div></li>
          <li><span class="vi">{i("mail")}</span><div><b>E-mail</b><a href="mailto:simonek-22@hotmail.com">simonek-22@hotmail.com</a></div></li>
        </ul>
        <a href="{ROTA}" target="_blank" rel="noopener" class="btn btn-primary">Traçar rota {ARROW}</a>
      </div>
      <div class="map-wrap reveal"><iframe class="map" title="Mapa: Cemevi em Icaraí" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP}"></iframe></div>
    </div>
  </section>
  </main>
''' + FOOT

# ================================ CLÍNICA ================================
pages["clinica-veterinaria.html"] = head("Clínica veterinária — Cemevi, Icaraí",
  "Clínica médica e cirúrgica do Cemevi em Icaraí, Niterói. Consultórios climatizados, centro cirúrgico e emergência 24 horas.",
  "clinica-veterinaria.html") + "\n  <main>" + phero("clinica-veterinaria.html", "slide-clinica.jpg", "60% 40%",
  "Clínica médica e cirúrgica",
  "Salas de atendimento confortáveis e climatizadas e um centro cirúrgico com todo o suporte para procedimentos em padrão de excelência.",
  f'<a href="contato.html" class="btn btn-light">Agendar consulta {ARROW}</a>{BTN_WA_G}') + f'''

  <section class="section">
    <div class="wrap split">
      <div class="duo reveal">
        <img src="img/consulta-gato.jpg" alt="Gato sendo examinado com estetoscópio" loading="lazy">
        <img src="img/consultorio.jpg" alt="Consultório do Cemevi" loading="lazy">
      </div>
      <div class="reveal">
        <span class="kicker">Atendimento clínico</span>
        <h2>A saúde do seu pet em dia, do check-up à cirurgia</h2>
        <p>No Cemevi você encontra tudo o que precisa para cuidar do seu cão ou gato. Nossa equipe é altamente qualificada e trata cada animal com muito carinho e profissionalismo.</p>
        <p>Quando o paciente precisa ficar em observação, a internação 24 horas fica na mesma estrutura.</p>
        {checks(["Consultórios confortáveis e climatizados", "Centro cirúrgico completo", "Emergência a qualquer hora", "Internação no mesmo local"])}
        <div class="split-actions">
          <a href="contato.html" class="btn btn-primary">Marcar um horário {ARROW}</a>
          <a href="internacao-24-horas.html" class="btn btn-outline">Internação 24h</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-tint">
    <div class="wrap">
      <div class="head reveal">
        <div><span class="kicker">Serviços</span><h2>O que fazemos na clínica</h2></div>
        <p>Atendimento completo para cães e gatos, com resultados e registros disponíveis para você no SimplesPet.</p>
      </div>
      <div class="cards">
{cards([
  ("steth", "Consultas", "Atendimento clínico para cães e gatos, em salas confortáveis e climatizadas."),
  ("shield", "Cirurgias", "Centro cirúrgico com todo o suporte necessário para procedimentos em padrão de excelência."),
  ("syringe", "Vacinação e vermifugação", "Protocolos em dia e registrados na caderneta digital do SimplesPet."),
  ("pulse", "Exames", "Resultados disponíveis para você na área do cliente."),
  ("heart", "Emergência 24 horas", "Atendimento de urgência a qualquer hora, todos os dias da semana."),
  ("bed", "Pós-operatório", "Acompanhamento e internação na mesma estrutura, quando necessário."),
])}
      </div>
    </div>
  </section>

  <div class="spacer"></div>''' + band("Seu pet precisa de atendimento agora?", "Estamos abertos 24 horas. Ligue antes de sair de casa para agilizar a chegada.",
      f'<a href="{TEL}" class="btn btn-light">{i("phone")} (21) 3628-2484</a>') + faq("Sobre a clínica", "Ficou com alguma dúvida sobre consultas e cirurgias? A gente responde.", [
  ("Vocês atendem sem hora marcada?", "Emergências são atendidas a qualquer hora. Para consultas de rotina, recomendamos agendar pelo telefone ou WhatsApp para evitar espera."),
  ("Quais animais vocês atendem?", "Atendemos cães e gatos."),
  ("Onde vejo exames e vacinas do meu pet?", "Na área do cliente SimplesPet, com histórico de peso, caderneta de vacina, exames, receitas e agendamentos."),
  ("Tem estacionamento?", "Sim. O Cemevi tem estacionamento próprio, na Rua Dr. Tavares de Macedo, 141, em Icaraí."),
]) + "\n  </main>\n" + FOOT

# ================================ INTERNAÇÃO ================================
pages["internacao-24-horas.html"] = head("Internação 24 horas — Cemevi, Icaraí",
  "Internação veterinária 24 horas no Cemevi, em Icaraí, Niterói. Cães e gatos em instalações separadas e acompanhamento em tempo integral.",
  "internacao-24-horas.html") + "\n  <main>" + phero("internacao-24-horas.html", "slide-internacao.jpg", "50% 60%",
  "Internação 24 horas",
  "Acompanhamento veterinário em tempo integral e muitas doses de carinho para acelerar a recuperação do seu pet.",
  f'{BTN_CALL_L}{BTN_WA_G}') + f'''

  <section class="section">
    <div class="wrap split">
      <div class="reveal">
        <span class="kicker">Tratamento assistido</span>
        <h2>Cuidado integral durante toda a estadia</h2>
        <p>Nossa equipe prioriza o bem-estar dos pacientes que precisam de tratamento assistido. Além dos cuidados médicos necessários, oferecemos também muitas doses de carinho para acelerar ainda mais a recuperação.</p>
        <p>A internação conta com profissionais especializados e extremamente competentes, para oferecer o máximo conforto ao seu pet. E o mais importante: aqui todos nós amamos animais.</p>
        {checks(["Acompanhamento 24 horas, inclusive feriados", "Instalações separadas para cães e gatos", "Contato com o veterinário de origem"])}
      </div>
      <div class="duo reveal">
        <img src="img/internacao-cao.jpg" alt="Cão em recuperação" loading="lazy">
        <img src="img/internacao-a.jpg" alt="Baias da internação" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section section-tint">
    <div class="wrap">
      <div class="head head-center reveal"><span class="kicker">Como funciona</span><h2>Uma internação pensada para cada espécie</h2></div>
      <div class="cards">
{cards([
  ("bed", "Alas separadas", "Instalações separadas para cães e gatos, reduzindo o estresse e respeitando as particularidades de cada espécie."),
  ("users", "Pacientes de parceiros", "Internamos também pacientes de colegas, com comunicação estreita com o médico veterinário de origem."),
  ("clock", "Tempo integral", "Acompanhamento veterinário 24 horas, inclusive fins de semana e feriados."),
])}
      </div>
    </div>
  </section>

  <div class="spacer"></div>''' + band("É veterinário e precisa internar um paciente?", "Recebemos pacientes de colegas parceiros e mantemos você informado durante toda a internação.",
      f'<a href="{TEL}" class="btn btn-light">{i("phone")} Falar com a equipe</a>') + faq("Sobre a internação", "Sabemos que deixar o pet internado gera dúvidas. Estas são as mais comuns.", [
  ("Meu pet fica acompanhado à noite?", "Sim. A internação tem acompanhamento veterinário em tempo integral, 24 horas por dia."),
  ("Cães e gatos ficam no mesmo espaço?", "Não. A sala de internação tem instalações separadas para cães e gatos."),
  ("Meu veterinário não é do Cemevi. Posso internar aí?", "Pode. Recebemos pacientes de colegas parceiros e mantemos contato próximo com o médico de origem."),
]) + "\n  </main>\n" + FOOT

# ================================ BANHO E TOSA ================================
pages["banho-e-tosa.html"] = head("Banho e tosa — Cemevi, Icaraí",
  "Banho e tosa no Cemevi, em Icaraí, Niterói. Banhos terapêuticos, hidratação, tosa higiênica, padrão racial e na tesoura.",
  "banho-e-tosa.html") + "\n  <main>" + phero("banho-e-tosa.html", "slide-banho.jpg", "60% 35%",
  "Banho e tosa",
  "Um setor de estética animal que cuida da higiene e do conforto do seu pet. Ele sai daqui impecável.",
  f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">{i("wa")} Agendar pelo WhatsApp</a>') + f'''

  <section class="section">
    <div class="wrap split">
      <div class="duo reveal">
        <img src="img/cat-banho.jpg" alt="Cachorro depois do banho" loading="lazy" style="object-position:50% 30%">
        <img src="img/banho-gato.jpg" alt="Gato tomando banho" loading="lazy" style="object-position:50% 15%">
      </div>
      <div class="reveal">
        <span class="kicker">Banho</span>
        <h2>Diversos tipos de banho, para cada pele e pelagem</h2>
        <p>Nosso setor de estética animal oferece os mais diversos tipos de banho para a higiene e o conforto do seu pet, como banhos terapêuticos, hidratações e tratamentos diferenciados.</p>
        {checks(["Banhos terapêuticos", "Hidratação", "Tratamentos diferenciados para pele e pelagem"])}
      </div>
    </div>
  </section>

  <section class="section section-white">
    <div class="wrap split split-rev">
      <div class="reveal">
        <span class="kicker">Tosa</span>
        <h2>Tosa estética ou higiênica, na máquina ou na tesoura</h2>
        <p>A tosa é feita tanto com objetivo estético quanto para a higiene do seu cão ou gato. Nossos profissionais de estética animal são habilitados para diversas modalidades.</p>
        <p>Para escolher o tipo de tosa, leve em conta as características do pelo do animal e o tempo que você pode dedicar à escovação. Na dúvida, a gente ajuda a decidir.</p>
      </div>
      <div class="duo reveal">
        <img src="img/samoieda.jpg" alt="Samoieda com a pelagem escovada" loading="lazy" style="object-position:50% 30%">
        <img src="img/tosa.jpg" alt="Shih-tzu sendo tosado na tesoura" loading="lazy" style="object-position:50% 20%">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="head head-center reveal"><span class="kicker">Modalidades</span><h2>Três tipos de tosa</h2></div>
      <div class="cards">
{cards([
  ("scissors", "Tosa higiênica", "Limpeza das regiões íntimas, patas e rosto, para o dia a dia com mais conforto."),
  ("sparkle", "Tosa padrão racial", "O corte característico de cada raça, feito por profissionais habilitados."),
  ("heart", "Tosa especial na tesoura", "Acabamento feito à mão, para quem quer um visual mais caprichado."),
])}
      </div>
    </div>
  </section>
''' + band("Agende o banho do seu pet", "Chame no WhatsApp e escolha o melhor horário.",
      f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">{i("wa")} (21) 96752-0101</a>') + "\n  </main>\n" + FOOT

# ================================ FARMÁCIA ================================
pages["farmacia-veterinaria.html"] = head("Farmácia veterinária — Cemevi, Icaraí",
  "Farmácia veterinária do Cemevi em Icaraí, Niterói. Em breve, medicamentos diferenciados com os melhores preços.",
  "farmacia-veterinaria.html") + "\n  <main>" + phero("farmacia-veterinaria.html", "hero-farmacia.jpg", "50% 50%",
  "Farmácia veterinária",
  "Em breve teremos uma farmácia própria, com tudo o que você precisa para manter a saúde do seu pet em dia.",
  f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">Quero ser avisado {ARROW}</a>') + f'''

  <section class="section">
    <div class="wrap split">
      <div class="duo reveal">
        <img src="img/farmacia-a.jpg" alt="Prateleiras de medicamentos" loading="lazy">
        <img src="img/farmacia-gato.jpg" alt="Gato recebendo petisco" loading="lazy">
      </div>
      <div class="reveal">
        <span class="kicker">Em breve</span>
        <h2>A receita resolvida sem sair da clínica</h2>
        <p>Vamos oferecer um mix de medicamentos diferenciados com os melhores preços, dentro da mesma estrutura em que seu pet é atendido.</p>
        <p>Enquanto isso, as receitas emitidas pelos nossos veterinários ficam disponíveis na área do cliente SimplesPet.</p>
        {checks(["Medicamentos diferenciados", "Os melhores preços", "Tudo no mesmo lugar da consulta"])}
        <div class="split-actions">
          <a href="{SP}" target="_blank" rel="noopener" class="btn btn-primary">Ver minhas receitas {ARROW}</a>
        </div>
      </div>
    </div>
  </section>
''' + band("Quer saber quando a farmácia abrir?", "Mande uma mensagem e avisamos você.",
      f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-light">{i("wa")} Me avise</a>') + "\n  </main>\n" + FOOT

# ================================ CONTATO ================================
pages["contato.html"] = head("Contato — Cemevi, Icaraí",
  "Contato do Cemevi: Rua Dr. Tavares de Macedo, 141, Icaraí, Niterói/RJ. (21) 3628-2484. Aberto 24 horas.",
  "contato.html") + "\n  <main>" + phero("contato.html", "hero-contato.jpg", "60% 40%",
  "Fale com a gente",
  "Estamos abertos 24 horas, todos os dias. Para emergências, ligue direto para a clínica.",
  f'{BTN_CALL_L}{BTN_WA_G}') + f'''

  <section class="section">
    <div class="wrap contact">
      <div class="visit-card reveal">
        <span class="kicker">Informações</span>
        <h2>Onde e quando</h2>
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
            <span class="label" id="lbl-esp">Seu pet é</span>
            <div class="pets" role="radiogroup" aria-labelledby="lbl-esp">
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
          <div><button type="submit" class="btn btn-primary">{i("wa")} Enviar pelo WhatsApp</button></div>
          <p class="form-note">Em emergências, não espere resposta por mensagem: ligue para (21) 3628-2484.</p>
        </form>
      </div>
    </div>
  </section>

  <section class="section" id="mapa" style="padding-top:0">
    <div class="wrap">
      <div class="map-wrap reveal"><iframe class="map" title="Mapa: Cemevi em Icaraí" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP}"></iframe></div>
    </div>
  </section>
  </main>
''' + FOOT

for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
print("ok", list(pages))
