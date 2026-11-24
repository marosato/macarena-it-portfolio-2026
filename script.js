(() => {
  const root = document.documentElement;
  const english = root.lang === 'en';
  const themeButton = document.querySelector('.theme-toggle');
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.getElementById('navigation');
  const themeKey = 'mar-editorial-theme';
  function setTheme(theme) {
    const dark = theme === 'dark';
    root.dataset.theme = dark ? 'dark' : 'light';
    themeButton?.setAttribute('aria-pressed', String(dark));
    themeButton?.setAttribute('aria-label', english
      ? `Switch to ${dark ? 'light' : 'dark'} mode`
      : `Activar modo ${dark ? 'claro' : 'oscuro'}`);
  }
  let savedTheme;
  try { savedTheme = localStorage.getItem(themeKey); } catch { /* El almacenamiento es opcional. */ }
  setTheme(savedTheme);
  if (themeButton) {
    themeButton.hidden = false;
    themeButton.addEventListener('click', () => {
      const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      setTheme(theme);
      try { localStorage.setItem(themeKey, theme); } catch { /* Continuar sin almacenamiento. */ }
    });
  }
  if (menuButton && navigation) {
    menuButton.hidden = false;
    const closeMenu = (restoreFocus = false) => {
      menuButton.setAttribute('aria-expanded', 'false');
      if (restoreFocus) menuButton.focus();
    };
    menuButton.addEventListener('click', () => {
      menuButton.setAttribute('aria-expanded', String(menuButton.getAttribute('aria-expanded') !== 'true'));
    });
    navigation.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') closeMenu(true);
    });
    document.addEventListener('click', event => {
      if (!event.target.closest('.site-header')) closeMenu();
    });
    matchMedia('(min-width: 901px)').addEventListener('change', () => closeMenu());
  }
  document.querySelectorAll('.languages a').forEach(link => {
    link.addEventListener('click', () => { link.hash = location.hash; });
  });
})();

/* Los detalles y la búsqueda de cursos complementan el HTML nativo. */
(() => {
  const openProject = (hash, focus = false) => {
    if (!/^#project-\d+$/.test(hash)) return;
    const detail = document.getElementById(hash.slice(1));
    if (!detail) return;
    detail.open = true;
    if (focus) detail.querySelector('summary')?.focus({preventScroll:true});
  };
  document.querySelectorAll('[data-project-link]').forEach(link => {
    link.addEventListener('click', () => openProject(link.hash, true));
  });
  openProject(location.hash);
  window.addEventListener('hashchange', () => openProject(location.hash));

  const search = document.querySelector('.course-search');
  if (!search) return;
  const input = search.querySelector('input');
  const clear = search.querySelector('[data-clear-search]');
  const status = search.querySelector('[role=status]');
  const courses = [...document.querySelectorAll('#course-results .course')];
  const en = document.documentElement.lang === 'en';
  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const index = courses.map(card => normalize(card.textContent));
  function filter() {
    const terms = normalize(input.value).trim().split(/\s+/).filter(Boolean);
    let count = 0;
    courses.forEach((card, i) => {
      card.hidden = !terms.every(term => index[i].includes(term));
      if (!card.hidden) count++;
    });
    status.textContent = count === 0
      ? (en ? 'No matching courses. Try another topic or clear the search.' : 'No hay cursos que coincidan. Prueba otro tema o limpia la búsqueda.')
      : en ? `${count} of ${courses.length} courses` : `${count} de ${courses.length} cursos`;
    clear.disabled = !input.value;
  }
  search.hidden = false;
  input.addEventListener('input', filter);
  clear.addEventListener('click', () => {input.value = ''; filter(); input.focus();});
  filter();
})();

(() => {
  const en = document.documentElement.lang === 'en';
  document.querySelectorAll('.project-gallery').forEach(gallery => {
    const slides = [...gallery.querySelectorAll('.gallery-slide')];
    const controls = gallery.querySelector('.gallery-controls');
    if (!controls || slides.length < 2) return;
    let current = 0;
    function show(index) {
      current = (index + slides.length) % slides.length;
      slides.forEach((slide, i) => { slide.hidden = i !== current; });
      controls.querySelector('.gallery-count').textContent = `${current + 1} / ${slides.length} · ${slides[current].querySelector('figcaption').textContent}`;
    }
    controls.hidden = false;
    controls.querySelector('[data-gallery-prev]').addEventListener('click', () => show(current - 1));
    controls.querySelector('[data-gallery-next]').addEventListener('click', () => show(current + 1));
    gallery.addEventListener('keydown', event => {
      if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
      event.preventDefault(); show(current + (event.key === 'ArrowRight' ? 1 : -1));
    });
    show(0);
  });
})();
