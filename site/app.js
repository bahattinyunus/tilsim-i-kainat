/* Tılsım-ı Kâinat Web Portalı — Uygulama Mantığı */

const MODELS_CATALOG = [
  { num: "01", title: "Ene Kalınlaşma Modeli", src: "30. Söz · 1. Maksad", desc: "Ene'nin gaflet ve şirket ile hava fazından buzlaşıp sahibini yutma (firavuniyet) dinamiği." },
  { num: "02", title: "Tahavvülât-ı Zerrât", src: "30. Söz · 2. Maksad", desc: "Zerrelerin Kudret Kalemi'nin titreşimi olarak mertebeler arası seyahati ve iki şahidi." },
  { num: "03", title: "İhlas ve 4444 Sinerjisi", src: "21. Lem'a · İhlas", desc: "Enaniyet buzunun erimesiyle N ferdin toplamdan 10^N / 2^N üstel şahs-ı manevî gücüne sıçraması." },
  { num: "04", title: "Kozmik Entropi & Negentropi", src: "23. Lem'a & Wheeler", desc: "Termodinamik dağılmaya karşı DNA ve canlılık nizamındaki haricî İlim ve İrade mührü." },
  { num: "05", title: "Tayy-ı Mekân & Işınlanma", src: "20. Söz · Belkıs'ın Tahtı", desc: "Kuantum rekonstrüksiyon (10^32 qubit) ve nuraniyet sürüşüyle tarfetü'l-ayn hızında nakil." },
  { num: "06", title: "Kader & İrade Matrisi", src: "26. Söz · Kader", desc: "Ezelî ilmin zorlamayışı (P(Cebir)=0) ve 1-bitlik cüz-i ihtiyarî kesb anahtarı." },
  { num: "07", title: "Haşir & Bilgi Korunumu", src: "10. Söz · Haşir", desc: "Kuantum Unitarity ilkesi ve Levh-i Mahfuz kaydıyla dağılmış zerrelerin iadesi." },
  { num: "08", title: "Hayat, Şuur & IIT Φ", src: "29. Söz & 30. Lem'a", desc: "Entegre Bilgi Teorisi (Tononi IIT Φ) ile hayatın kesrette vahdet sırrı ve ruh kanunu." },
  { num: "09", title: "Mirac, Görelilik & Ân-ı Dâim", src: "31. Söz · Mirac", desc: "Lorentz zaman genişlemesi, nuraniyetle Higgs eylemsizliğinin sıfırlanması ve zamanın dürülmesi." },
  { num: "10", title: "Mânâ-yı Harfî & RQM / ITP", src: "Mesnevî-i Nuriye", desc: "Rovelli İlişkisel Kuantum Mekaniği ve Hoffman Arayüz Kuramı ile niyet-nazar simyası." },
  { num: "11", title: "Holografik Âlem & Ehadiyet", src: "16. Söz & AdS/CFT", desc: "Güneş-ayna temessülü, tecezzisiz tecelli (%0 bölünme) ve ER=EPR mesafesiz kurb." },
  { num: "12", title: "Esmâ Fraktal & Ölçek Değişmezliği", src: "30. Lem'a & Mandelbrot", desc: "41 mertebe ölçek boyunca (zerre → insan → galaksi) korunan Sikke-i Vahdet ve Fraktal Boyut D_f." }
];

const SCIENCE_MATRIX = [
  ["Ene (Vâhid-i Kıyasî)", "30. Söz, 1. Maksad", "Gödel Eksiklik Teoremi / Referans Çerçevesi", "Sistem kendi içinden kendini tam tanımlayamaz; mutlak olanı ölçmek için farazî bir referans hattı (ene) gerekir."],
  ["Tahavvülât-ı Zerrât", "30. Söz, 2. Maksad", "Wheeler 'It from Bit' & Kuantum Alanlar", "Madde katı bir töz değil, sürekli güncellenen tekvînî bir enformasyon akışı ve Kudret Kalemi'nin titreşimidir."],
  ["İhlas & 4444 Sırrı", "21. Lem'a", "Kuantum Süperpozisyon & Ağ Sinerjisi", "Enaniyet buzunun erimesiyle N birimin gücü N toplamından 10^N / 2^N üstel kapasiteye sıçrar."],
  ["Kudret İntizamı", "30. Söz & 23. Lem'a", "Negentropi (Schrödinger) & Öz-Örgütlenme", "Termodinamik dağılmaya (ΔS > 0) karşı canlılıktaki DNA ve hücresel nizam haricî bir İlim ve İrade mührüdür."],
  ["Belkıs'ın Tahtı / Tayy-ı Mekân", "20. Söz (Neml: 40)", "Kuantum Teleportasyon & Alcubierre Metriği", "Cisim 10^32 qubitlik bilgiye tercüme edilirse veya letâfetle uzay metriği büzülürse tarfetü'l-ayn hızında nakledilir."],
  ["Cüz-i İhtiyarî (Kesb)", "26. Söz & Nisa: 79", "1-Bitlik Kontrol Anahtarı & Determinizm Aşımı", "Ezelî ilim zamandan münezzeh olduğundan zorlamaz (P(Cebir)=0); 1-bitlik kesb sonsuz kudreti yönlendirir."],
  ["Haşir ve İade", "10. Söz", "Kuantum Bilgi Korunumu (Unitarity)", "Evrende fiziksel enformasyon yok olmaz; dağılmış zerreler Levh-i Mahfuz kaydıyla tek bir Sur emriyle iade edilir."],
  ["Mânâ-yı Harfî (Nisbet)", "Mesnevî & 30. Söz", "İlişkisel Kuantum Mekaniği (RQM - C. Rovelli)", "Hiçbir nesnenin kendi başına (mânâ-yı ismî) mutlak özelliği yoktur; özellikler yalnızca ilişkilerde ve ayinedarlıkta doğar."],
  ["Âlem-i Misâl & Ehadiyet", "16. Söz & 28. Mektup", "Holografik İlke (AdS/CFT) & ER=EPR (Susskind)", "3B maddî hacim (bulk), düşük boyutlu sınır (boundary) bilgisinin projeksiyonudur; uzay-zaman dolanıklıktan örülür."],
  ["Hayatın Sırr-ı Câmii & Ruh", "29. Söz & 30. Lem'a", "Entegre Bilgi Teorisi (IIT Φ - G. Tononi)", "Parçalara indirgenemeyen bütünleşik bilgi (Φ >> 0), cansız zerratı tek bir kâinata muhatap zîşuur bir öze çevirir."],
  ["Mirac-ı Nebevî & Ân-ı Dâim", "31. Söz & 24. Mektup", "Özel Görelilik (Einstein) & Lorentz Dilation", "Cismin nuraniyet kesbetmesiyle Higgs eylemsizliği sıfırlanır (0.0 G); zaman dürülerek tarfetü'l-aynda ezel-ebed seyrine erilir."],
  ["Şehadet Perdesi & Nazar", "Mesnevî & 11. Söz", "Arayüz Algı Kuramı (ITP - D. Hoffman)", "Uzay-zaman ve madde mutlak hakikat değil, şuurun muhatap olduğu bir 'arayüz'dür; hakikat perde arkasındaki esmâdır."],
  ["İsm-i Âzam & Misâl-i Musaggar", "30. Lem'a & 32. Söz", "Fraktal Geometri (Mandelbrot) & Renormalizasyon (Wilson)", "41 mertebe ölçek boyunca (zerre → insan → galaksi) korunan öz-benzerlik ve ölçek değişmezliği, tek bir Sâni'nin Sikke-i Vahdet'idir."]
];

let ALL_DOCS = [];
let ALL_DIAGRAMS = [];
let ALL_GLOSSARY = [];
let activeDocCategory = "Tümü";
let activeGlossaryLetter = "Tümü";
let diagramsRendered = false;

/* Kozmik Yıldız Alanı Animasyonu */
function initStarfield() {
  const canvas = document.getElementById('starfield');
  const ctx = canvas.getContext('2d');
  let w, h, stars = [];

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
    const count = Math.min(160, Math.floor((w * h) / 11000));
    stars = Array.from({ length: count }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 1.4 + 0.3,
      a: Math.random() * 0.7 + 0.2,
      s: (Math.random() - 0.5) * 0.015,
      vy: Math.random() * 0.12 + 0.03
    }));
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    for (const st of stars) {
      st.a += st.s;
      if (st.a > 0.9 || st.a < 0.15) st.s *= -1;
      st.y -= st.vy;
      if (st.y < -2) { st.y = h + 2; st.x = Math.random() * w; }
      ctx.beginPath();
      ctx.arc(st.x, st.y, st.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(226, 232, 240, ${st.a.toFixed(2)})`;
      ctx.fill();
    }
    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  resize();
  draw();
}

/* Navigasyon */
function navigateTo(viewName) {
  document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));

  const sec = document.getElementById(`view-${viewName}`);
  const btn = document.querySelector(`.nav-btn[data-view="${viewName}"]`);
  if (sec) sec.classList.add('active');
  if (btn) btn.classList.add('active');

  if (location.hash !== `#${viewName}`) {
    history.replaceState(null, "", `#${viewName}`);
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });

  if (viewName === 'diagrams' && !diagramsRendered) {
    renderDiagramsGrid();
  }
}

/* 12 Model Önizleme */
function renderModelsPreview() {
  const grid = document.getElementById('models-preview-grid');
  grid.innerHTML = MODELS_CATALOG.map(m => `
    <div class="model-card" onclick="navigateTo('lab')">
      <div class="model-top">
        <span class="model-num">MODEL ${m.num}</span>
        <span class="model-src">${m.src}</span>
      </div>
      <h4>${m.title}</h4>
      <p>${m.desc}</p>
    </div>
  `).join('');
}

/* Bilim Matrisi */
function renderMatrix(query = "") {
  const q = query.trim().toLowerCase();
  const tbody = document.getElementById('matrix-body');
  const filtered = SCIENCE_MATRIX.filter(row =>
    !q || row.some(cell => cell.toLowerCase().includes(q))
  );
  tbody.innerHTML = filtered.map(r => `
    <tr>
      <td class="matrix-concept">${r[0]}</td>
      <td style="color:var(--text-muted); white-space:nowrap;">${r[1]}</td>
      <td class="matrix-science">${r[2]}</td>
      <td style="color:var(--text-soft);">${r[3]}</td>
    </tr>
  `).join('');
}

/* Doküman Kütüphanesi */
function initDocsUI() {
  const cats = ["Tümü", ...new Set(ALL_DOCS.map(d => d.category))];
  const catWrap = document.getElementById('doc-categories');
  catWrap.innerHTML = cats.map(c => `
    <button class="filter-pill ${c === activeDocCategory ? 'active' : ''}" onclick="setDocCategory('${c}')">${c}</button>
  `).join('');
  renderDocsList();
  if (ALL_DOCS.length > 0) {
    const preferred = ALL_DOCS.find(d => d.path.includes('kullî-cozum')) || ALL_DOCS[0];
    selectDoc(preferred.id);
  }
}

function setDocCategory(cat) {
  activeDocCategory = cat;
  document.querySelectorAll('#doc-categories .filter-pill').forEach(p => {
    p.classList.toggle('active', p.textContent === cat);
  });
  renderDocsList();
}

function renderDocsList() {
  const q = (document.getElementById('doc-search').value || "").trim().toLowerCase();
  const list = document.getElementById('docs-list');
  const filtered = ALL_DOCS.filter(d => {
    const matchCat = activeDocCategory === "Tümü" || d.category === activeDocCategory;
    const matchQ = !q || d.title.toLowerCase().includes(q) || d.excerpt.toLowerCase().includes(q);
    return matchCat && matchQ;
  });

  list.innerHTML = filtered.map(d => `
    <div class="doc-item" data-doc-id="${d.id}" onclick="selectDoc('${d.id}')">
      <div class="doc-item-title">${d.title}</div>
      <div class="doc-item-meta">${d.category} · ${d.readMin} dk okuma</div>
    </div>
  `).join('') || `<p style="color:var(--text-muted); font-size:0.85rem;">Eşleşen makale bulunamadı.</p>`;
}

async function selectDoc(docId) {
  const doc = ALL_DOCS.find(d => d.id === docId);
  if (!doc) return;

  document.querySelectorAll('.doc-item').forEach(el => {
    el.classList.toggle('active', el.dataset.docId === docId);
  });

  document.getElementById('doc-meta-bar').innerHTML = `
    <span class="doc-badge">${doc.category}</span>
    <span>📄 ${doc.path}</span>
    <span>⏱️ ~${doc.readMin} dakika okuma (${doc.words} kelime)</span>
  `;

  const container = document.getElementById('doc-content');
  container.innerHTML = marked.parse(doc.content);

  // KaTeX math rendering
  if (typeof renderMathInElement === 'function') {
    renderMathInElement(container, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false }
      ],
      throwOnError: false
    });
  }

  // Inline mermaid blocks inside markdown
  const mermaidBlocks = container.querySelectorAll('pre code.language-mermaid');
  for (let i = 0; i < mermaidBlocks.length; i++) {
    const codeEl = mermaidBlocks[i];
    const pre = codeEl.parentElement;
    const wrapper = document.createElement('div');
    wrapper.className = 'diagram-stage';
    wrapper.style.margin = '1.25rem 0';
    try {
      const { svg } = await mermaid.render(`doc-mmd-${Date.now()}-${i}`, codeEl.textContent);
      wrapper.innerHTML = svg;
      pre.replaceWith(wrapper);
    } catch (_) {}
  }
}

function openDocByPath(path) {
  navigateTo('docs');
  const doc = ALL_DOCS.find(d => d.path === path);
  if (doc) selectDoc(doc.id);
}

/* Diyagram Galerisi */
async function renderDiagramsGrid(query = "") {
  diagramsRendered = true;
  const q = query.trim().toLowerCase();
  const grid = document.getElementById('diagrams-grid');
  const filtered = ALL_DIAGRAMS.filter(d =>
    !q || d.title.toLowerCase().includes(q) || d.description.toLowerCase().includes(q)
  );

  grid.innerHTML = filtered.map(d => `
    <div class="diagram-card">
      <div class="diagram-head">
        <div>
          <h3>${d.title}</h3>
          <p class="diagram-desc">${d.description}</p>
        </div>
      </div>
      <div class="diagram-stage" id="diag-stage-${d.id}" onclick="openDiagramModal('${d.id}')" title="Yakınlaştırmak için tıklayın">
        <span style="color:var(--text-muted); font-size:0.85rem;">Diyagram çiziliyor...</span>
      </div>
      <div class="diagram-actions">
        <button class="btn-mini" onclick="copyDiagramCode('${d.id}', this)">📋 Mermaid Kodu</button>
        <button class="btn-mini" onclick="openDiagramModal('${d.id}')">🔍 Tam Ekran</button>
      </div>
    </div>
  `).join('');

  for (const d of filtered) {
    const el = document.getElementById(`diag-stage-${d.id}`);
    if (!el) continue;
    try {
      const { svg } = await mermaid.render(`mmd-${d.id}-${Date.now()}`, d.code);
      el.innerHTML = svg;
    } catch (err) {
      el.innerHTML = `<pre style="font-size:0.75rem; color:var(--text-muted);">${d.code}</pre>`;
    }
  }
}

async function openDiagramModal(diagId) {
  const d = ALL_DIAGRAMS.find(x => x.id === diagId);
  if (!d) return;
  document.getElementById('modal-title').textContent = `🗺️ ${d.title}`;
  const body = document.getElementById('modal-body');
  body.innerHTML = '<span style="color:var(--text-muted);">Yükleniyor...</span>';
  document.getElementById('diagram-modal').classList.add('open');
  try {
    const { svg } = await mermaid.render(`modal-mmd-${Date.now()}`, d.code);
    body.innerHTML = svg;
  } catch (_) {
    body.innerHTML = `<pre>${d.code}</pre>`;
  }
}

function closeModal() {
  document.getElementById('diagram-modal').classList.remove('open');
}

function copyDiagramCode(diagId, btn) {
  const d = ALL_DIAGRAMS.find(x => x.id === diagId);
  if (!d) return;
  navigator.clipboard.writeText(d.code).then(() => {
    const orig = btn.textContent;
    btn.textContent = "✓ Kopyalandı";
    setTimeout(() => (btn.textContent = orig), 1500);
  });
}

/* Kavramlar Sözlüğü */
function initGlossaryUI() {
  const letters = ["Tümü", ...new Set(ALL_GLOSSARY.map(g => g.letter))];
  const wrap = document.getElementById('glossary-letters');
  wrap.innerHTML = letters.map(l => `
    <button class="filter-pill ${l === activeGlossaryLetter ? 'active' : ''}" onclick="setGlossaryLetter('${l}')">${l}</button>
  `).join('');
  renderGlossary();
}

function setGlossaryLetter(letter) {
  activeGlossaryLetter = letter;
  document.querySelectorAll('#glossary-letters .filter-pill').forEach(p => {
    p.classList.toggle('active', p.textContent === letter);
  });
  renderGlossary();
}

function renderGlossary() {
  const q = (document.getElementById('glossary-search').value || "").trim().toLowerCase();
  const grid = document.getElementById('glossary-grid');
  const filtered = ALL_GLOSSARY.filter(g => {
    const matchL = activeGlossaryLetter === "Tümü" || g.letter === activeGlossaryLetter;
    const matchQ = !q || g.term.toLowerCase().includes(q) || g.definition.toLowerCase().includes(q);
    return matchL && matchQ;
  });

  document.getElementById('glossary-count').textContent = `${filtered.length} / ${ALL_GLOSSARY.length} Kavram`;

  grid.innerHTML = filtered.map(g => `
    <div class="gloss-card">
      <div class="gloss-term">${g.term}</div>
      <div class="gloss-def">${g.definition}</div>
    </div>
  `).join('') || `<p style="color:var(--text-muted);">Aramanızla eşleşen kavram bulunamadı.</p>`;
}

/* Başlatma */
async function bootstrap() {
  initStarfield();
  mermaid.initialize({
    startOnLoad: false,
    theme: 'dark',
    securityLevel: 'loose',
    themeVariables: {
      primaryColor: '#1e1b4b',
      primaryTextColor: '#f8fafc',
      primaryBorderColor: '#06b6d4',
      lineColor: '#94a3b8',
      secondaryColor: '#0f172a',
      tertiaryColor: '#1e293b'
    }
  });

  renderModelsPreview();
  renderMatrix();

  try {
    const [stats, docs, diagrams, glossary] = await Promise.all([
      fetch('data/stats.json').then(r => r.json()),
      fetch('data/docs.json').then(r => r.json()),
      fetch('data/diagrams.json').then(r => r.json()),
      fetch('data/glossary.json').then(r => r.json())
    ]);

    ALL_DOCS = docs;
    ALL_DIAGRAMS = diagrams;
    ALL_GLOSSARY = glossary;

    document.getElementById('stat-models').textContent = stats.models;
    document.getElementById('stat-tests').textContent = stats.tests;
    document.getElementById('stat-docs').textContent = stats.docs;
    document.getElementById('stat-diagrams').textContent = stats.diagrams;
    document.getElementById('stat-glossary').textContent = stats.glossary + '+';

    initDocsUI();
    initGlossaryUI();
  } catch (err) {
    console.error("Veri yükleme hatası:", err);
  }

  document.getElementById('doc-search').addEventListener('input', renderDocsList);
  document.getElementById('glossary-search').addEventListener('input', renderGlossary);
  document.getElementById('diagram-search').addEventListener('input', e => renderDiagramsGrid(e.target.value));
  document.getElementById('matrix-search').addEventListener('input', e => renderMatrix(e.target.value));

  const hash = location.hash.replace('#', '');
  if (['home', 'lab', 'docs', 'diagrams', 'glossary', 'matrix'].includes(hash)) {
    navigateTo(hash);
  }
}

window.addEventListener('DOMContentLoaded', bootstrap);
