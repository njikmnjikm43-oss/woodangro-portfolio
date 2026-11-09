/* 안원빈 · 우당로 포트폴리오 */
(() => {
  'use strict';
  const $ = (q, el = document) => el.querySelector(q);
  const $$ = (q, el = document) => [...el.querySelectorAll(q)];

  /* 서울 시각 */
  const clock = $('#clock');
  if (clock) {
    const fmt = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Seoul', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false });
    const tick = () => { clock.innerHTML = fmt.format(new Date()) + ' <span>KST · 서울</span>'; };
    tick(); setInterval(tick, 1000);
  }

  /* 화면에 들어오면 나타나기 */
  const rv = $$('.rv');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(el => io.observe(el));
  } else rv.forEach(el => el.classList.add('in'));

  /* 유튜브: 누르면 그 자리에서 재생 */
  $$('.yt[data-id]').forEach(a => {
    const id = a.dataset.id;
    const img = $('img', a);
    if (img && !img.getAttribute('src')) img.src = `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
    a.addEventListener('click', e => {
      e.preventDefault();
      const f = document.createElement('iframe');
      f.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
      f.title = a.getAttribute('aria-label') || '유튜브 영상';
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      a.replaceChildren(f);
      a.removeAttribute('href');
    }, { once: true });
  });

  /* 크게 보기 */
  const items = $$('[data-gallery]');
  if (!items.length) return;
  const dlg = document.createElement('dialog');
  dlg.className = 'lb';
  dlg.setAttribute('aria-label', '크게 보기');
  dlg.innerHTML = `
    <div class="top mono"><span class="ttl"></span><button class="close mono" type="button">닫기 ×</button></div>
    <div class="stage"><img alt=""></div>
    <button class="nav prev" type="button" aria-label="이전"><svg viewBox="0 0 24 24"><path d="M15 4l-8 8 8 8"/></svg></button>
    <button class="nav next2" type="button" aria-label="다음"><svg viewBox="0 0 24 24"><path d="M9 4l8 8-8 8"/></svg></button>
    <p class="cap mono"></p>`;
  document.body.appendChild(dlg);
  const im = $('.stage img', dlg), ttl = $('.ttl', dlg), cap = $('.cap', dlg);
  let group = [], idx = 0;
  function show(i) {
    idx = (i + group.length) % group.length;
    const el = group[idx];
    im.src = el.dataset.full || $('img', el)?.src || '';
    im.alt = $('img', el)?.alt || '';
    ttl.textContent = el.dataset.title || '';
    cap.textContent = `${String(idx + 1).padStart(2, '0')} / ${String(group.length).padStart(2, '0')}`;
  }
  items.forEach(el => el.addEventListener('click', e => {
    e.preventDefault();
    group = items.filter(x => x.dataset.gallery === el.dataset.gallery);
    show(group.indexOf(el));
    dlg.showModal();
  }));
  $('.close', dlg).addEventListener('click', () => dlg.close());
  $('.prev', dlg).addEventListener('click', () => show(idx - 1));
  $('.next2', dlg).addEventListener('click', () => show(idx + 1));
  dlg.addEventListener('click', e => { if (e.target === dlg || e.target.classList.contains('stage')) dlg.close(); });
  dlg.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight') show(idx + 1);
    if (e.key === 'ArrowLeft') show(idx - 1);
  });
  let sx = null;
  dlg.addEventListener('pointerdown', e => { sx = e.clientX; });
  dlg.addEventListener('pointerup', e => {
    if (sx === null) return;
    const dx = e.clientX - sx; sx = null;
    if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
  });
})();
