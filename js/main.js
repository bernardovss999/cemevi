(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Transição entre páginas: a cortina cobre a tela antes de trocar de página
  var root = document.documentElement;
  var curtain = document.querySelector('.curtain');
  setTimeout(function () { root.classList.remove('intro'); }, 1900);

  function isInternalPage(a, e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return false;
    if (a.target && a.target !== '_self') return false;
    if (a.hasAttribute('download')) return false;
    var url = new URL(a.href, location.href);
    if (url.origin !== location.origin || !/\.html$|\/$/.test(url.pathname)) return false;
    // mesmo documento (âncora na própria página): deixa rolar normalmente
    if (url.pathname === location.pathname && url.hash) return false;
    return url.href !== location.href;
  }
  if (curtain && !reduce) {
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a || !isInternalPage(a, e)) return;
      e.preventDefault();
      curtain.classList.add('leave');
      setTimeout(function () { location.href = a.href; }, 560);
    });
    // Voltar pelo navegador (página restaurada do cache): tira a cortina
    window.addEventListener('pageshow', function (e) {
      if (e.persisted) curtain.classList.remove('leave');
    });
  }

  // Header: transparente sobre a foto, sólido depois de rolar
  var header = document.querySelector('.header');
  function onScroll() { if (header) header.classList.toggle('solid', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Menu em tela cheia (celular e tablet)
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav');
  function setMenu(open) {
    nav.classList.toggle('open', open);
    header.classList.toggle('menu-active', open);
    document.body.classList.toggle('menu-open', open);
    btn.setAttribute('aria-expanded', open);
    btn.querySelector('.menu-label').textContent = open ? 'Fechar' : 'Menu';
  }
  if (btn && nav) {
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 960 && nav.classList.contains('open')) setMenu(false); });
  }

  // Slider da página inicial
  var slider = document.querySelector('.slider');
  if (slider) {
    var slides = slider.querySelectorAll('.slide');
    var tabs = slider.querySelectorAll('.slider-tab');
    var dots = slider.querySelectorAll('.slider-dot');
    var DUR = 7000;
    var current = 0, timer = null, paused = false, started = 0, remaining = DUR;
    slider.style.setProperty('--dur', DUR / 1000 + 's');

    function show(n) {
      current = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) {
        s.classList.toggle('is-active', i === current);
        s.setAttribute('aria-hidden', i !== current);
      });
      [tabs, dots].forEach(function (list) {
        list.forEach(function (t, i) {
          t.classList.remove('is-active');
          if (i === current) { void t.offsetWidth; t.classList.add('is-active'); }
          t.setAttribute('aria-current', i === current ? 'true' : 'false');
        });
      });
      schedule(DUR);
    }
    function schedule(ms) {
      clearTimeout(timer);
      if (reduce) return;
      remaining = ms; started = Date.now();
      if (!paused) timer = setTimeout(function () { show(current + 1); }, ms);
    }
    function pause() {
      if (paused || reduce) return;
      paused = true; slider.classList.add('paused');
      clearTimeout(timer); remaining -= Date.now() - started;
    }
    function resume() {
      if (!paused) return;
      paused = false; slider.classList.remove('paused');
      schedule(Math.max(remaining, 800));
    }

    tabs.forEach(function (t, i) { t.addEventListener('click', function () { show(i); }); });
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); }); });
    slider.querySelector('.slider-arrow.prev').addEventListener('click', function () { show(current - 1); });
    slider.querySelector('.slider-arrow.next').addEventListener('click', function () { show(current + 1); });
    slider.addEventListener('mouseenter', pause);
    slider.addEventListener('mouseleave', resume);
    slider.addEventListener('focusin', pause);
    slider.addEventListener('focusout', resume);
    document.addEventListener('visibilitychange', function () { document.hidden ? pause() : resume(); });
    slider.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') show(current + 1);
      if (e.key === 'ArrowLeft') show(current - 1);
    });

    // arrastar no celular
    var x0 = null, y0 = null;
    slider.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
    slider.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) show(current + (dx < 0 ? 1 : -1));
      x0 = null;
    }, { passive: true });

    show(0);
  }

  // Entrada dos blocos ao rolar
  var items = document.querySelectorAll('.reveal');
  items.forEach(function (el) {
    var sibs = Array.prototype.filter.call(el.parentElement.children, function (c) { return c.classList.contains('reveal'); });
    var i = sibs.indexOf(el);
    if (i > 0) el.style.setProperty('--d', Math.min(i, 5) * 0.08 + 's');
  });
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Filtro da galeria
  var chips = document.querySelectorAll('.chip[data-filter]');
  var gallery = document.querySelector('.gallery');
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var f = chip.getAttribute('data-filter');
      chips.forEach(function (c) { c.classList.toggle('active', c === chip); c.setAttribute('aria-pressed', c === chip); });
      gallery.classList.toggle('filtered', f !== 'all');
      gallery.querySelectorAll('.shot').forEach(function (s) { s.classList.toggle('is-hidden', f !== 'all' && s.getAttribute('data-cat') !== f); });
    });
  });

  // Formulário: monta a mensagem e abre o WhatsApp da clínica
  var form = document.querySelector('#contato-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var txt = 'Olá! Meu nome é ' + d.get('nome') + '.';
      var esp = d.get('especie'), pet = d.get('pet');
      if (pet || esp) txt += ' Meu pet: ' + (pet || '') + (pet && esp ? ' (' + esp.toLowerCase() + ')' : (esp || '').toLowerCase()) + '.';
      if (d.get('assunto')) txt += ' Assunto: ' + d.get('assunto') + '.';
      txt += '\n\n' + d.get('mensagem');
      if (d.get('telefone')) txt += '\n\nMeu telefone: ' + d.get('telefone');
      window.open('https://wa.me/5521967520101?text=' + encodeURIComponent(txt), '_blank');
    });
  }
})();
