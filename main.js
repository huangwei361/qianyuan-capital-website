// ===== 厚待众生 · 个人创业志 · main.js =====

// 实时时钟
function tick() {
  const d = new Date();
  const pad = n => n.toString().padStart(2, '0');
  const weekdays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
  const dateEl = document.getElementById('hero-date');
  if (dateEl) {
    dateEl.textContent =
      d.getFullYear() + '年' + pad(d.getMonth() + 1) + '月' + pad(d.getDate()) + '日 · ' + weekdays[d.getDay()];
  }
}
tick();
setInterval(tick, 60000);

// 移动端导航
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');
if (navToggle) {
  navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('open');
  });
}

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      navMenu.classList.remove('open');
    }
  });
});

// ============ 黄金价格（占位 · 用户可替换为真实API）============
// 真实数据更新于 2026-09-04 上午 · 用户可在 gold-data.js 替换
const goldData = {
  sgeAu9999:  { price: 968.50, change: +11.30, changePct: +1.18, time: '10:00' },
  london:     { price: 4479.59, change: +6.60,   changePct: +0.15, time: '10:00', unit: 'USD/oz' },
  retail:     { price: 1329.00, change: +6.00,   changePct: +0.45, time: '10:00' },
  recycle:    { price: 957.00,  change: +9.00,   changePct: +0.95, time: '10:00' },
  updatedAt: '2026-09-04 10:00',
  source: '上海黄金交易所 / 品牌终端'
};

function fmt(v, d = 2) { return Number(v).toFixed(d); }
function renderGold() {
  const setCard = (id, data, unit) => {
    const el = document.getElementById(id);
    if (!el) return;
    const v = el.querySelector('.gc-value');
    const c = el.querySelector('.gc-change');
    const t = el.querySelector('.gc-meta');
    if (v) v.innerHTML = fmt(data.price) + (unit ? `<span class="gc-unit">${unit}</span>` : '');
    if (c) {
      const sign = data.change > 0 ? '+' : '';
      const cls = data.change > 0 ? 'up' : (data.change < 0 ? 'down' : '');
      c.className = 'gc-change ' + cls;
      c.textContent = `${sign}${fmt(data.change)} (${sign}${fmt(data.changePct)}%) 较昨日`;
    }
    if (t) t.textContent = '更新于 ' + data.time + ' · ' + goldData.source;
  };
  setCard('gc-sge',   goldData.sgeAu9999, '元/克');
  setCard('gc-london', goldData.london, 'USD/oz');
  setCard('gc-retail', goldData.retail, '元/克');
  setCard('gc-recycle', goldData.recycle, '元/克');
}
renderGold();

// ============ 滚动渐入 ============
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('section, .arch-item, .jc, .bv, .gc, .cc, .about-card').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});
