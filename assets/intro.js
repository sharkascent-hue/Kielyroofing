/* Opening animation. Inlined straight after the loader markup so it starts the moment
   the page arrives, without waiting for fonts or the animation libraries. */
(function () {
  const html = document.documentElement, loader = document.getElementById('loader');
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const rand = (a, b) => a + Math.random() * (b - a);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, touch = !matchMedia('(pointer: fine)').matches;
  const signal = n => { window['__intro_' + n] = 1; dispatchEvent(new Event('intro:' + n)); };
  function rainOn(host, o = {}) {
    if (reduce) return null;
    const cv = document.createElement('canvas'); cv.className = 'rain'; cv.setAttribute('aria-hidden', 'true');
    host.insertBefore(cv, host.firstElementChild ? host.firstElementChild.nextSibling : null);
    const ctx = cv.getContext('2d'); let w, h, drops = [], vis = true, raf;
    const dpr = 1;
    const size = () => { w = cv.clientWidth; h = cv.clientHeight; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.round(w * h / 10000 * (o.density || 1)); drops = Array.from({ length: n }, () => ({ x: rand(0, w), y: rand(0, h), l: rand(10, 24), v: rand(9, 16) * (o.speed || 1), a: rand(.08, .28) * (o.alpha || 1) })); };
    size(); let lw = innerWidth; addEventListener('resize', () => { if (innerWidth !== lw) { lw = innerWidth; size(); } }); // ignore the phone toolbar showing/hiding
    const tick = () => {
      ctx.clearRect(0, 0, w, h); ctx.lineWidth = 1;
      for (const d of drops) {
        ctx.strokeStyle = (o.color || 'rgba(170,215,255,') + d.a + ')';
        ctx.beginPath(); ctx.moveTo(d.x, d.y); ctx.lineTo(d.x - d.l * .18, d.y + d.l); ctx.stroke();
        d.y += d.v; d.x -= d.v * .18;
        if (d.y > h) { d.y = -d.l; d.x = rand(0, w * 1.15); }
      }
      if (vis || o.always) raf = requestAnimationFrame(tick);
    };
    if (!o.always) new IntersectionObserver(es => { const was = vis; vis = es[0].isIntersecting; if (vis && !was) raf = requestAnimationFrame(tick); }).observe(host);
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }
  /* ---------- intro: lightning strikes the logo, then the page lifts up ---------- */
  let stopIntroRain = null;
  function finishIntro() { if (typeof stopIntroRain === 'function') stopIntroRain(); if (loader) loader.remove(); html.classList.remove('intro', 'intro-out'); signal('done'); }
  function boltPath(x0, y0, x1, y1, rough) {
    // midpoint displacement gives a natural jagged bolt
    let pts = [[x0, y0], [x1, y1]], d = rough;
    for (let k = 0; k < 6; k++) {
      const nx = [];
      for (let i = 0; i < pts.length - 1; i++) {
        const [ax, ay] = pts[i], [bx, by] = pts[i + 1];
        nx.push(pts[i], [(ax + bx) / 2 + rand(-d, d), (ay + by) / 2 + rand(-d, d) * .3]);
      }
      nx.push(pts[pts.length - 1]); pts = nx; d *= .55;
    }
    return pts;
  }
  const toD = pts => 'M' + pts.map(p => p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' L');
  function runIntro() {
    try { sessionStorage.setItem('kiely_intro', '1'); } catch (e) {}
    if (!loader || !html.classList.contains('intro') || reduce) { finishIntro(); return; }
    stopIntroRain = rainOn(loader, { always: true, density: touch ? 1.6 : 3, speed: 1.5, alpha: 1.6 });
    const svg = $('svg.bolt', loader), flash = $('.flash', loader), logo = $('.logo', loader);
    const W = innerWidth, H = innerHeight;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    const r = logo.getBoundingClientRect();
    const pt = k => loader.dataset[k].split(',').map(Number);
    const [ax, ay] = pt('apex'), tx = r.left + r.width * ax, ty = r.top + r.height * ay; // the roof peak of the logo
    $$('.ring, .glow', loader).forEach(el => { el.style.left = tx + 'px'; el.style.top = ty + 'px'; });
    const flashTo = (o, ms) => { flash.style.transition = `opacity ${ms}ms ease-out`; flash.style.opacity = o; };
    const addBolt = (pts, wd, cls) => {
      const d = toD(pts);
      const g = document.createElementNS('http://www.w3.org/2000/svg', 'g'); g.setAttribute('class', cls || '');
      g.innerHTML = `<path d="${d}" stroke="rgba(255,140,70,.28)" stroke-width="${wd * 9}"/><path d="${d}" stroke="rgba(255,150,90,.5)" stroke-width="${wd * 4.5}"/><path d="${d}" stroke="#ffe4d2" stroke-width="${wd * 2.2}"/><path d="${d}" stroke="#fff" stroke-width="${wd}"/>`;
      svg.appendChild(g);
      $$('path', g).forEach(p => { const L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = L; p.getBoundingClientRect(); p.style.transition = 'stroke-dashoffset .26s cubic-bezier(.3,.6,.4,1)'; p.style.strokeDashoffset = 0; });
      return g;
    };
    // distant flicker first
    setTimeout(() => { flashTo(.07, 160); setTimeout(() => flashTo(0, 400), 180); }, 100);
    
    // the strike
    setTimeout(() => {
      const sx = tx + rand(-W * .18, W * .18);
      const main = boltPath(sx, -20, tx, ty, Math.max(60, W * .07));
      const groups = [addBolt(main, 2.6)];
      // forks off the main bolt
      for (let b = 0; b < 3; b++) {
        const i = Math.floor(rand(main.length * .2, main.length * .7)), [bx, by] = main[i];
        groups.push(addBolt(boltPath(bx, by, bx + rand(-W * .22, W * .22), by + rand(H * .08, H * .22), 30), 1.1, 'fork'));
      }
      setTimeout(() => {
        flashTo(.5, 80); loader.classList.add('struck');
        // sparks from the peak
        for (let s = 0; s < 26; s++) {
          const sp = document.createElement('i'); sp.className = 'spark'; sp.style.left = tx + 'px'; sp.style.top = ty + 'px'; loader.appendChild(sp);
          const a = rand(Math.PI * 1.05, Math.PI * 1.95), dist = rand(60, 220);
          sp.animate([{ transform: 'translate(0,0) scale(1)', opacity: 1 }, { transform: `translate(${Math.cos(a) * dist}px,${Math.sin(a) * dist * .6 + rand(40, 120)}px) scale(.2)`, opacity: 0 }], { duration: rand(500, 900), easing: 'cubic-bezier(.2,.7,.3,1)', fill: 'forwards' });
        }
        setTimeout(() => flashTo(0, 900), 90);
        // electricity crackles down both slopes of the logo's roof
        const [lx, ly] = pt('l'), [rx, ry] = pt('r'), L = [r.left + r.width * lx, r.top + r.height * ly], R = [r.left + r.width * rx, r.top + r.height * ry];
        [0, 140, 300].forEach(t => setTimeout(() => {
          const arcs = [addBolt(boltPath(tx, ty, L[0], L[1], 14), .8, 'fork'), addBolt(boltPath(tx, ty, R[0], R[1], 14), .8, 'fork')];
          setTimeout(() => arcs.forEach(g => g.remove()), 110);
        }, t));
        // bolt flickers out
        groups.forEach(g => { g.style.transition = 'opacity .45s ease-out'; });
        setTimeout(() => groups.forEach(g => g.style.opacity = 0), 220);
        
      }, 150);
    }, 380);
    // lift the whole intro up to reveal the home page
    setTimeout(() => { html.classList.add('intro-out'); signal('open'); setTimeout(finishIntro, 950); }, 2200);
  }

  runIntro();
})();
