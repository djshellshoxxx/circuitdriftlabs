(() => {
  const extraStyles = document.createElement('link');
  extraStyles.rel = 'stylesheet';
  extraStyles.href = 'tools.css';
  document.head.append(extraStyles);

  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  const menu = document.querySelector('.tools-menu');
  const trigger = document.querySelector('.tools-trigger');
  if (menu && trigger) {
    const close = () => { menu.classList.remove('open'); trigger.setAttribute('aria-expanded', 'false'); };
    trigger.addEventListener('click', (event) => {
      event.stopPropagation();
      const open = !menu.classList.contains('open');
      menu.classList.toggle('open', open);
      trigger.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', (event) => { if (!menu.contains(event.target)) close(); });
    document.addEventListener('keydown', (event) => { if (event.key === 'Escape') { close(); trigger.focus(); } });
  }

  const items = Array.isArray(window.CDL_PRODUCTS) ? window.CDL_PRODUCTS : [];
  const section = document.getElementById('catalogue');
  const grid = document.getElementById('product-grid');
  if (!section || !grid || !items.length) return;

  for (const item of items) {
    if (!item || !item.name || !item.description) continue;
    const card = document.createElement('article');
    card.className = 'product-card';
    const type = document.createElement('span');
    type.className = 'product-card-type';
    type.textContent = item.type || 'Audio tool';
    const name = document.createElement('h4');
    name.textContent = item.name;
    const description = document.createElement('p');
    description.textContent = item.description;
    card.append(type, name, description);

    if (item.url) {
      try {
        const url = new URL(item.url, location.href);
        if (url.protocol === 'https:' || url.protocol === 'http:') {
          const link = document.createElement('a');
          link.href = url.href;
          link.textContent = 'Explore ' + item.name + ' ↗';
          if (url.origin !== location.origin) {
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
          }
          card.append(link);
        }
      } catch (_) { /* Skip malformed links without hiding the product. */ }
    }
    grid.append(card);
  }
  section.hidden = !grid.children.length;
})();
