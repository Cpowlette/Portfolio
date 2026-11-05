(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  const close = () => { toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); };
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  nav.addEventListener('click', event => { if (event.target.closest('a')) close(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) { close(); toggle.focus(); }
  });
  matchMedia('(min-width: 1101px)').addEventListener('change', close);
  if ('IntersectionObserver' in window) {
    const links = [...nav.querySelectorAll('a[href^="#"]')];
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        links.forEach(link => {
          if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-15% 0px -55% 0px' });
    links.forEach(link => { const section = document.querySelector(link.hash); if (section) observer.observe(section); });
  }

  // Original evidence files remain ordinary links when dialogs are unsupported.
  const viewer = document.querySelector('#evidence-viewer');
  if (viewer && typeof viewer.showModal === 'function') {
    const fullImage = viewer.querySelector('#evidence-full-image');
    const caption = viewer.querySelector('#evidence-caption');
    const original = viewer.querySelector('#evidence-original');
    let opener;
    document.querySelectorAll('a[data-evidence]').forEach(link => {
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        opener = link;
        fullImage.src = link.href;
        fullImage.alt = link.querySelector('img')?.alt || '';
        caption.textContent = link.dataset.caption || fullImage.alt;
        original.href = link.href;
        viewer.showModal();
        document.body.classList.add('evidence-open');
        viewer.querySelector('[data-close-evidence]').focus();
      });
    });
    viewer.querySelector('[data-close-evidence]').addEventListener('click', () => viewer.close());
    viewer.addEventListener('click', event => {
      if (event.target !== viewer) return;
      const bounds = viewer.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) viewer.close();
    });
    viewer.addEventListener('close', () => {
      document.body.classList.remove('evidence-open');
      opener?.focus();
    });
  }
})();
