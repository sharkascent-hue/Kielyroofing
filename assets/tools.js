/* Kiely Roofing & Construction — interactive tools:
   quote wizard, roof health check, area checker, live opening hours, gallery & review filters. */
(function () {
  const WA = '353873592163', EMAIL = 'info@kielyroofing.ie';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const html = document.documentElement;

  /* top bar slides away once the page scrolls */
  const tb = () => html.classList.toggle('scrolled-past', scrollY > 40);
  addEventListener('scroll', tb, { passive: true }); tb();

  /* mobile menu: Roofing / Home Improvements open as drop-downs */
  $$('.mtog').forEach(b => b.addEventListener('click', () => {
    const acc = b.closest('.macc'), open = !acc.classList.contains('open');
    $$('.macc').forEach(x => { x.classList.remove('open'); $('.mtog', x).setAttribute('aria-expanded', 'false'); });
    acc.classList.toggle('open', open); b.setAttribute('aria-expanded', String(open));
  }));

  /* ---------- drop-down quote panel under the header (like vantageroofing.ie) ---------- */
  const qd = $('#qdrop');
  if (qd) {
    const setQ = open => {
      html.classList.toggle('qdrop-open', open); qd.setAttribute('aria-hidden', String(!open));
      $$('.qbtn').forEach(b => b.setAttribute('aria-expanded', String(open)));
      if (open && matchMedia('(pointer:fine)').matches) setTimeout(() => { const f = $('input:not(.hp)', qd); if (f) f.focus({ preventScroll: true }); }, 380);
    };
    $$('[data-qdrop]').forEach(b => b.addEventListener('click', e => {
      e.preventDefault(); html.classList.remove('menu-open');
      const sel = $('select[name=service]', qd); if (sel && b.dataset.svc) sel.value = b.dataset.svc;
      setQ(b.classList.contains('qbtn') ? !html.classList.contains('qdrop-open') : true);
    }));
    $$('[data-qclose]', qd).forEach(b => b.addEventListener('click', () => setQ(false)));
    $$('[data-wizard]', qd).forEach(b => b.addEventListener('click', () => setQ(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape') setQ(false); });
    document.addEventListener('click', e => { if (html.classList.contains('qdrop-open') && !e.target.closest('.hdr, [data-qdrop], .wiz')) setQ(false); });
    if (location.hash === '#quote') setQ(true);
  }

  /* ---------- live opening hours (Mon–Sun 7am–10pm, Irish time) ---------- */
  function openState() {
    const parts = new Intl.DateTimeFormat('en-IE', { timeZone: 'Europe/Dublin', hour: 'numeric', minute: 'numeric', hour12: false }).formatToParts(new Date());
    const h = +parts.find(p => p.type === 'hour').value % 24, m = +parts.find(p => p.type === 'minute').value;
    const t = h + m / 60, open = t >= 7 && t < 22;
    return open ? { open, text: 'Open now · until 10pm' } : { open, text: 'Closed · opens 7am' };
  }
  const os = openState();
  $$('[data-open]').forEach(el => { el.textContent = os.text; el.classList.toggle('closed', !os.open); });

  /* ---------- area checker ---------- */
  const AREAS = {
    Meath: ['Longwood', 'Navan', 'Trim', 'Ashbourne', 'Ratoath', 'Dunboyne', 'Kells', 'Laytown', 'Bettystown', 'Enfield', 'Athboy', 'Dunshaughlin', 'Clonee', 'Stamullen', 'Duleek', 'Slane', 'Summerhill', 'Kilcock', 'Ballivor', 'Oldcastle', 'Nobber', 'Kilmessan', 'Julianstown', 'Donore', 'Johnstown', 'Rathmolyon'],
    Kildare: ['Maynooth', 'Celbridge', 'Leixlip', 'Naas', 'Newbridge', 'Kildare', 'Clane', 'Kilcock', 'Edenderry', 'Carbury', 'Johnstownbridge', 'Prosperous', 'Sallins', 'Kill', 'Straffan', 'Athy', 'Monasterevin', 'Rathangan', 'Allenwood', 'Robertstown', 'Derrinturn', 'Kilcullen'],
    Dublin: ['Dublin', 'Lucan', 'Blanchardstown', 'Castleknock', 'Clonsilla', 'Ongar', 'Swords', 'Malahide', 'Finglas', 'Clondalkin', 'Tallaght', 'Saggart', 'Rathcoole', 'Balbriggan', 'Skerries', 'Rush', 'Lusk', 'Donabate', 'Santry', 'Glasnevin', 'Drumcondra', 'Cabra', 'Palmerstown', 'Chapelizod', 'Ballyfermot', 'Mulhuddart', 'Tyrrelstown', 'Dundrum', 'Rathfarnham', 'Terenure', 'Crumlin', 'Raheny', 'Clontarf', 'Howth', 'Portmarnock']
  };
  const ALL = Object.entries(AREAS).flatMap(([c, ts]) => ts.map(t => [t, c]));
  const NEAR = ['Westmeath', 'Mullingar', 'Offaly', 'Tullamore', 'Kinnegad', 'Louth', 'Drogheda', 'Dundalk', 'Cavan', 'Wicklow', 'Bray', 'Laois'];
  $$('[data-area]').forEach(box => {
    const inp = $('input', box), out = $('.area-out', box), dl = $('datalist', box);
    if (dl) dl.innerHTML = ALL.map(([t]) => `<option value="${t}">`).join('');
    const check = () => {
      const v = inp.value.trim().toLowerCase().replace(/^co\.?\s+|county\s+/, '');
      if (!v) { out.className = 'area-out'; out.textContent = ''; return; }
      const hit = ALL.find(([t]) => t.toLowerCase() === v) || ALL.find(([t]) => t.toLowerCase().startsWith(v) && v.length > 2);
      const county = Object.keys(AREAS).find(c => c.toLowerCase() === v);
      if (hit || county) { out.className = 'area-out yes'; out.innerHTML = `<b>Yes, we cover ${hit ? hit[0] + ', Co. ' + hit[1] : 'Co. ' + county}.</b> Free callout and free quote.`; }
      else if (NEAR.some(n => n.toLowerCase().startsWith(v) && v.length > 2)) { out.className = 'area-out maybe'; out.innerHTML = `<b>Very likely.</b> We regularly work in surrounding areas. Call <a href="tel:+353873592163">087 359 2163</a> to confirm.`; }
      else { out.className = 'area-out maybe'; out.innerHTML = `<b>Give us a call to check.</b> We cover Meath, Kildare, Dublin and surrounding areas: <a href="tel:+353873592163">087 359 2163</a>`; }
    };
    inp.addEventListener('input', check); box.addEventListener('submit', e => { e.preventDefault(); check(); });
  });

  /* ---------- quote wizard ---------- */
  const wiz = $('#wiz');
  if (wiz) {
    const steps = $$('.wstep', wiz), bar = $('.wbar i', wiz), lbl = $('.wcount', wiz);
    const data = {}; let i = 0;
    const show = n => {
      i = Math.max(0, Math.min(steps.length - 1, n));
      steps.forEach((s, k) => s.classList.toggle('on', k === i));
      bar.style.width = ((i + 1) / steps.length * 100) + '%'; lbl.textContent = `Step ${i + 1} of ${steps.length}`;
      $('.wback', wiz).style.visibility = i ? 'visible' : 'hidden';
      if (i === steps.length - 1) summary();
    };
    $$('.wopt', wiz).forEach(b => b.addEventListener('click', () => {
      const k = b.closest('.wstep').dataset.key; data[k] = b.dataset.v;
      $$('.wopt', b.closest('.wstep')).forEach(x => x.classList.toggle('sel', x === b));
      setTimeout(() => show(i + 1), 180);
    }));
    $('.wback', wiz).addEventListener('click', () => show(i - 1));
    const summary = () => { $('.wsum', wiz).innerHTML = [['Service', data.service], ['Property', data.property], ['When', data.urgency]].filter(r => r[1]).map(([a, b]) => `<span><small>${a}</small>${b}</span>`).join(''); };
    const msg = () => {
      const f = Object.fromEntries(new FormData($('form', wiz)).entries());
      return `Hi Kiely Roofing, I'd like a free quote.\n\nService: ${data.service || '-'}\nProperty: ${data.property || '-'}\nWhen: ${data.urgency || '-'}\nName: ${f.name}\nPhone: ${f.phone}\nArea: ${f.town}\n${f.details ? 'Details: ' + f.details + '\n' : ''}`;
    };
    const valid = () => {
      let ok = true;
      $$('[required]', $('form', wiz)).forEach(x => { const g = x.value.trim() && x.checkValidity(); x.closest('label').classList.toggle('bad', !g); if (!g) ok = false; });
      return ok;
    };
    $('.wwa', wiz).addEventListener('click', e => { e.preventDefault(); if (!valid()) return; window.open(`https://wa.me/${WA}?text=${encodeURIComponent(msg() + '\n(I can send photos of the roof here.)')}`, '_blank', 'noopener'); done(); });
    $('.wmail', wiz).addEventListener('click', e => { e.preventDefault(); if (!valid()) return; location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Free quote request: ' + (data.service || 'Roofing'))}&body=${encodeURIComponent(msg())}`; done(); });
    const done = () => { $('.wdone', wiz).classList.add('on'); };
    const open = (svc, e) => {
      if (e) e.preventDefault(); html.classList.add('wiz-open');
      $('.wdone', wiz).classList.remove('on');
      if (svc) { data.service = svc; $$('.wstep[data-key="service"] .wopt', wiz).forEach(x => x.classList.toggle('sel', x.dataset.v === svc)); show(1); } else show(0);
    };
    $$('[data-wizard]').forEach(b => b.addEventListener('click', e => open(b.dataset.wizard, e)));
    $$('[data-wclose]', wiz).forEach(b => b.addEventListener('click', () => html.classList.remove('wiz-open')));
    addEventListener('keydown', e => { if (e.key === 'Escape') html.classList.remove('wiz-open'); });
    if (location.hash === '#quote-wizard') open();
  }

  /* ---------- roof health check ---------- */
  const hc = $('#health');
  if (hc) {
    const qs = $$('.hq', hc), res = $('.hres', hc), prog = $('.hprog i', hc); const ans = {};
    const upd = () => {
      const n = Object.keys(ans).length; prog.style.width = (n / qs.length * 100) + '%';
      $('.hcount', hc).textContent = `${n} of ${qs.length} answered`;
      if (n < qs.length) { res.classList.remove('on'); return; }
      const score = Object.values(ans).reduce((a, b) => a + b, 0);
      let k = score <= 3 ? 'repair' : score <= 7 ? 'watch' : 'replace';
      const R = {
        repair: ['Likely a repair', 'From what you’ve told us, a focused repair may be enough to sort the problem and extend the life of your roof. Not every damaged roof needs to be replaced.', 'roof-repairs'],
        watch: ['Repair now, plan ahead', 'A repair should deal with the immediate problem, but your roof is showing signs of age. We’ll tell you honestly whether repairs are still worthwhile or whether it’s time to start planning a new roof.', 'roof-repairs'],
        replace: ['A new roof is worth considering', 'Leaks in different places, widespread slipped or cracked tiles, sagging or damp in the attic usually mean it’s time to stop paying for repairs and start planning a replacement.', 'roof-replacement']
      }[k];
      $('h3', res).textContent = R[0]; $('p', res).textContent = R[1];
      $('.hlink', res).href = $('.hlink', res).dataset.base + R[2] + '/'; $('.hlink', res).textContent = R[2] === 'roof-replacement' ? 'About roof replacement' : 'About roof repairs';
      res.dataset.k = k; res.classList.add('on');
      $('.hscore i', res).style.width = Math.min(100, score / 12 * 100) + '%';
    };
    qs.forEach((q, qi) => $$('button', q).forEach(b => b.addEventListener('click', () => {
      ans[qi] = +b.dataset.s; $$('button', q).forEach(x => x.classList.toggle('sel', x === b)); q.classList.add('done'); upd();
      const nx = qs[qi + 1]; if (nx && !nx.classList.contains('done') && innerWidth < 900) nx.scrollIntoView({ behavior: 'smooth', block: 'center' });
    })));
    $('.hreset', hc).addEventListener('click', () => { Object.keys(ans).forEach(k => delete ans[k]); $$('.hq', hc).forEach(q => { q.classList.remove('done'); $$('button', q).forEach(x => x.classList.remove('sel')); }); upd(); });
    upd();
  }

  /* ---------- filters (gallery & reviews) ---------- */
  $$('[data-filters]').forEach(bar => {
    const target = $(bar.dataset.filters);
    $$('button', bar).forEach(b => b.addEventListener('click', () => {
      $$('button', bar).forEach(x => x.classList.toggle('on', x === b));
      const f = b.dataset.f;
      $$('[data-cat]', target).forEach(el => { el.hidden = !(f === 'all' || el.dataset.cat.split(' ').includes(f)); });
    }));
  });
})();
