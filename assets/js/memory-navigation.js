(() => {
  const links = [...document.querySelectorAll('.place-jumps a[href^="#"]')];
  const index = document.querySelector('.memory-index');
  index?.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link) return;
    const target = document.getElementById(link.hash.slice(1));
    if (target) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    }
    index.open = false;
  });
  if (!('IntersectionObserver' in window)) return;
  const active = new Map();
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => active.set(entry.target.id, entry.isIntersecting));
    const current = links.find(link => active.get(link.hash.slice(1)));
    links.forEach(link => {
      if (link === current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }, { rootMargin: '-80px 0px -55% 0px' });
  links.forEach(link => {
    const section = document.getElementById(link.hash.slice(1));
    if (section) observer.observe(section);
  });
})();
