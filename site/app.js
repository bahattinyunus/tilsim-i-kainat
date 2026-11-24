/* Tılsım-ı Kâinat Web Portalı — Gelişmiş Uygulama Mantığı */

const MODELS_CATALOG = [
  { num: "01", tab: "tab-ene", title: "Ene Kalınlaşma Modeli", src: "30. Söz · 1. Maksad", desc: "Ene'nin gaflet ve şirket ile hava fazından buzlaşıp sahibini yutma (firavuniyet) dinamiği." },
  { num: "02", tab: "tab-zerre", title: "Tahavvülât-ı Zerrât", src: "30. Söz · 2. Maksad", desc: "Zerrelerin Kudret Kalemi'nin titreşimi olarak mertebeler arası seyahati ve iki şahidi." },
  { num: "03", tab: "tab-ihlas", title: "İhlas ve 4444 Sinerjisi", src: "21. Lem'a · İhlas", desc: "Enaniyet buzunun erimesiyle N ferdin toplamdan 10^N / 2^N üstel şahs-ı manevî gücüne sıçraması." },
  { num: "04", tab: "tab-entropi", title: "Kozmik Entropi & Negentropi", src: "23. Lem'a & Wheeler", desc: "Termodinamik dağılmaya karşı DNA ve canlılık nizamındaki haricî İlim ve İrade mührü." },
  { num: "05", tab: "tab-teleport", title: "Tayy-ı Mekân & Işınlanma", src: "20. Söz · Belkıs'ın Tahtı", desc: "Kuantum rekonstrüksiyon (10^32 qubit) ve nuraniyet sürüşüyle tarfetü'l-ayn hızında nakil." },
  { num: "06", tab: "tab-kader", title: "Kader & İrade Matrisi", src: "26. Söz · Kader", desc: "Ezelî ilmin zorlamayışı (P(Cebir)=0) ve 1-bitlik cüz-i ihtiyarî kesb anahtarı." },
  { num: "07", tab: "tab-hasir", title: "Haşir & Bilgi Korunumu", src: "10. Söz · Haşir", desc: "Kuantum Unitarity ilkesi ve Levh-i Mahfuz kaydıyla dağılmış zerrelerin iadesi." },
  { num: "08", tab: "tab-hayat", title: "Hayat, Şuur & IIT Φ", src: "29. Söz & 30. Lem'a", desc: "Entegre Bilgi Teorisi (Tononi IIT Φ) ile hayatın kesrette vahdet sırrı ve ruh kanunu." },
  { num: "09", tab: "tab-mirac", title: "Mirac, Görelilik & Ân-ı Dâim", src: "31. Söz · Mirac", desc: "Lorentz zaman genişlemesi, nuraniyetle Higgs eylemsizliğinin sıfırlanması ve zamanın dürülmesi." },
  { num: "10", tab: "tab-nazar", title: "Mânâ-yı Harfî & RQM / ITP", src: "Mesnevî-i Nuriye", desc: "Rovelli İlişkisel Kuantum Mekaniği ve Hoffman Arayüz Kuramı ile niyet-nazar simyası." },
  { num: "11", tab: "tab-holografi", title: "Holografik Âlem & Ehadiyet", src: "16. Söz & AdS/CFT", desc: "Güneş-ayna temessülü, tecezzisiz tecelli (%0 bölünme) ve ER=EPR mesafesiz kurb." },
  { num: "12", tab: "tab-fraktal", title: "Esmâ Fraktal & Ölçek Değişmezliği", src: "30. Lem'a & Mandelbrot", desc: "41 mertebe ölçek boyunca (zerre → insan → galaksi) korunan Sikke-i Vahdet ve Fraktal Boyut D_f." }
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

const WISDOM_QUOTES = [
  {
    q: "Ene, bir vâhid-i kıyasîdir; Cenâb-ı Hakk'ın mutlak ve muhit sıfatlarını fehmetmek için konulmuş farazî bir hattır.",
    src: "30. Söz, Birinci Maksad (Ene Risalesi)",
    phys: "⚛️ Paralel: Gödel Eksiklik Teoremi & Referans Çerçevesi"
  },
  {
    q: "Nasıl ki güneş, nuraniyeti cihetiyle bir iken, her bir katre suda ve her bir cam parçasında bütün sıfatlarıyla tecezzi etmeden bulunur...",
    src: "16. Söz, İkinci Şua (Ehadiyet Sırrı)",
    phys: "⚛️ Paralel: AdS/CFT Holografik İlke & ER=EPR Dolanıklığı"
  },
  {
    q: "Güzel gören güzel düşünür; güzel düşünen hayatından lezzet alır. Mânâ-yı harfî ile bakan, her zerrede Sâni'in cemâlini okur.",
    src: "Mektubat & Mesnevî-i Nuriye (Dört Kelime)",
    phys: "⚛️ Paralel: Carlo Rovelli İlişkisel Kuantum Mekaniği (RQM)"
  },
  {
    q: "Dört ayrı 1 yan yana gelirse 1111 kuvvetinde olur; enaniyet buzunu kevser havuzunda eritenler 4444 sırrına mazhar olur.",
    src: "21. Lem'a (İhlas Risalesi)",
    phys: "⚛️ Paralel: Kuantum Süperpozisyon (2^N Üstel Kapasite)"
  },
  {
    q: "Zerre kimin ise, gezdiği bütün kâinat da Onundur; zira zerrenin hareketi Kudret Kalemi'nin tekvînî âyetleri yazarkenki titreşimidir.",
    src: "30. Söz, İkinci Maksad (Tahavvülât-ı Zerrât)",
    phys: "⚛️ Paralel: John Archibald Wheeler — 'It from Bit'"
  },
  {
    q: "Nasıl ki bir çekirdek, bütün ağacın fihristesini taşır; öyle de zerre güneş sisteminin, insan ise bütün kâinatın misâl-i musaggarıdır.",
    src: "30. Lem'a (İsm-i Âzam) & 32. Söz",
    phys: "⚛️ Paralel: Mandelbrot Fraktal Boyut (D_f) & Renormalizasyon"
  },
  {
    q: "Kader ilim nev'indendir; ilim ise malûma tâbidir. İlim, malûmun vücudunu zorlamaz; bilâkis tercih edilen 1-bitlik kesbi ezelden bilir.",
    src: "26. Söz (Kader Risalesi)",
    phys: "⚛️ Paralel: Determinizm Aşımı & 1-Bitlik Kontrol Anahtarı"
  }
];

const QUIZ_QUESTIONS = [
  {
    q: "30. Söz'e göre Ene'nin (benliğin) yaratılıştaki aslî ve fıtrî vazifesi nedir?",
    opts: [
      "Kendi başına müstakil bir malikiyet ve rububiyet iddia etmek",
      "Mutlak İlâhî sıfatları anlamak için farazî bir ölçü birimi (Vâhid-i Kıyasî) olmak",
      "Maddî sebeplerin kendi kendine yaratma gücünü ispatlamak",
      "Kâinattaki hareketi durdurarak sabitlik sağlamak"
    ],
    ans: 1,
    exp: "Ene, tıpkı coğrafyadaki ekvator hattı gibi farazî bir ölçü birimidir (Vâhid-i Kıyasî). 'Ben şu odaya mâlikim, öyleyse Hâlık dahi şu kâinata mâliktir' kıyasıyla mutlak sıfatları idrak ettirir."
  },
  {
    q: "21. Lem'a'daki '4444 Sırrı' (İhlas ve Şahs-ı Manevî) modern fizikte hangi ilkeyle yapısal paralellik taşır?",
    opts: [
      "Klasik sürtünme ve eylemsizlik kanunu",
      "Kuantum süperpozisyon ve üstel ağ sinerjisi (10^N / 2^N)",
      "Termodinamik ısı ölümü (entropi artışı)",
      "Klasik Newton soğuma yasası"
    ],
    ans: 1,
    exp: "Enaniyet buzunun eriyerek şahs-ı manevî havuzunda birleşmesiyle N birimlik güç doğrusal toplamdan (4) üstel kapasiteye (1111 / 4444) sıçrar."
  },
  {
    q: "30. Söz İkinci Maksad'daki 'Tahavvülât-ı Zerrât' (atomların durmaksızın hareketi) kavramı, John A. Wheeler'ın hangi ilkesiyle örtüşür?",
    opts: [
      "It from Bit (Madde enformasyondan doğar)",
      "Sabit Durum (Steady State) kozmolojisi",
      "Mutlak Eter teorisi",
      "Klasik mekanik determinizm"
    ],
    ans: 0,
    exp: "Zerre katı ve kör bir töz değil; Kudret Kalemi'nin tekvînî âyetleri (enformasyonu) yazarken meydana gelen titreşim ve akıştır."
  },
  {
    q: "16. Söz'deki Güneş–Ayna (Ehadiyet) temessülünde ayna sayısı 1'den 10^24'e çıktığında kaynakta ne kadar bölünme (tecezzi) olur?",
    opts: [
      "Ayna sayısı kadar bölünür (%99.9 kayıp)",
      "Mesafenin karesiyle ters orantılı azalır",
      "Sıfır (%0.0) — Nuraniyet bölünmeden her bir katrede tam tecelli eder",
      "Yalnızca en büyük aynada (okyanusta) tam görünür"
    ],
    ans: 2,
    exp: "16. Söz'ün temel teoremi ve holografik bütünlük: Nuraniyet için sayı ve mesafe engel değildir; kaynak bölünmeden (%0 tecezzi) her şeffaf aynada bütün sıfatlarıyla tecelli eder."
  },
  {
    q: "26. Söz (Kader Risalesi) ışığında ezelî ilmin insan iradesini zorlama (cebir) olasılığı P(Cebir) kaçtır?",
    opts: [
      "1.0 (Mutlak zorlama)",
      "0.5 (Yarı determinizm)",
      "0.0 (İlim malûma tâbidir; zamandan münezzeh bilmek zorlamak değildir)",
      "Zamanla artar"
    ],
    ans: 2,
    exp: "Ezelî ilim geçmiş-şimdi-geleceği tek bir ân-ı dâimde görür. İlim malûma tâbi olduğu için insanın 1-bitlik kesbini zorlamaz (P(Cebir)=0)."
  },
  {
    q: "10. Söz (Haşir Risalesi) ile modern kuantum mekaniğindeki 'Unitarity (Bilgi Korunumu)' ilkesinin ortak neticesi nedir?",
    opts: [
      "Evrende fiziksel enformasyon yok olmaz; Levh-i Mahfuz kaydıyla iade mümkündür",
      "Ölümle birlikte bütün bilgi evrenden tamamen silinir",
      "Haşir yalnızca ruhsal bir semboldür",
      "Zerreler sadece bir kez yaratılabilir"
    ],
    ans: 0,
    exp: "Kuantum Unitarity ilkesi bilginin evrende asla yok olmadığını gösterir; 10. Söz'de ise her varlığın programı Levh-i Mahfuz'da kayıtlıdır ve bahar ihyası gibi iade edilir."
  },
  {
    q: "29. Söz ve 30. Lem'a'daki 'Hayatın Sırr-ı Câmii' ve Ruh hakikati, Giulio Tononi'nin hangi kuramıyla kesişir?",
    opts: [
      "Entegre Bilgi Teorisi (IIT — Bütünleşik Bilgi Φ >> 0)",
      "Klasik Gaz Kinetik Teorisi",
      "Jeosantrik Astronomi",
      "Saf Davranışçılık"
    ],
    ans: 0,
    exp: "Canlılık ve şuur parçalara indirgenemeyen yüksek bütünleşik bilgi (Φ >> 0) ile cansız zerratı tek bir kâinata muhatap bir öze dönüştürür."
  },
  {
    q: "Mesnevî-i Nuriye'deki 'Mânâ-yı Harfî' (başkasına ayna olarak anlam kazanma) kavramı 21. yüzyıl fiziğinde hangi kuramla paralellik kurar?",
    opts: [
      "Carlo Rovelli — İlişkisel Kuantum Mekaniği (RQM)",
      "Klasik Mutlak Uzay-Zaman",
      "Mekanik Materyalizm",
      "Sabit Atomculuk"
    ],
    ans: 0,
    exp: "RQM'ye göre hiçbir fiziksel sistemin kendi başına (mânâ-yı ismî) mutlak özellikleri yoktur; özellikler yalnızca ilişkiler ve etkileşimler (nisbet) içinde doğar."
  },
  {
    q: "31. Söz (Mirac Risalesi) ve Özel Görelilik sentezinde 'Ân-ı Dâim' ve 'Tarfetü'l-Ayn' neyi ifade eder?",
    opts: [
      "Zamanın tamamen durup maddenin yok olmasını",
      "Nuraniyet kesbederek Higgs eylemsizliğinin sıfırlanması ve zamanın dürülerek ezel-ebed seyrine erilmesi",
      "Ses hızının iki katına çıkılmasını",
      "Yalnızca rüyada görülen bir hayali"
    ],
    ans: 1,
    exp: "Cismin nuraniyet ve letâfet kesbetmesiyle eylemsizlik direnci (0.0 G) aşılır; Lorentz zaman genişlemesinin ötesinde zaman dürülerek birkaç dakikada binlerce senelik seyir gerçekleşir."
  },
  {
    q: "20. Söz'de Belkıs'ın Tahtı'nın nakli (Neml: 40) için 'It from Bit' ve Tayy-ı Mekân modelinin öngördüğü en kritik fark nedir?",
    opts: [
      "Kütlesel nakilde G-kuvveti ve sürtünme varken, enformasyonel / nuranî nakilde 0.0 G ile tarfetü'l-ayn hızına ulaşılır",
      "Klasik nakil her zaman daha hızlıdır",
      "Bilgi transferi kütleden daha ağırdır",
      "Hiçbir fiziksel fark yoktur"
    ],
    ans: 0,
    exp: "Klasik balistik nakil saatler sürerken, 10^32 qubitlik enformasyonel rekonstrüksiyon ve nuraniyet sürüşü eylemsizliksiz (0.0 G) milisaniyeler içinde nakil sağlar."
  },
  {
    q: "30. Lem'a ve 32. Söz'deki 'İnsan kâinatın misâl-i musaggarıdır' hakikati, 12. modelde hangi matematiksel kavramla modellenir?",
    opts: [
      "Doğrusal Regresyon",
      "Mandelbrot Fraktal Boyutu (D_f) ve Renormalizasyon Grubu (Ölçek Değişmezliği)",
      "Rastgele Yürüyüş (Random Walk)",
      "Öklid Düzlem Geometrisi"
    ],
    ans: 1,
    exp: "Zerre (10^-15 m) → İnsan (10^0 m) → Galaksi (10^26 m) arasında 41 mertebe boyunca korunan öz-benzerlik (D_f) ve ölçek değişmezliği, tek bir Sâni'nin Sikke-i Vahdet'idir."
  },
  {
    q: "Donald Hoffman'ın 'Arayüz Algı Kuramı (ITP)' Risale-i Nur'daki hangi kavramla derin bir epistemolojik benzerlik taşır?",
    opts: [
      "Şehadet Perdesi ve Mânâ-yı Harfî Nazarı",
      "Evcedethü'l-Esbâb (Sebeplerin yaratması)",
      "Teşekkele Binefsihî (Kendi kendine oluş)",
      "Gaflet ve Ülfet"
    ],
    ans: 0,
    exp: "ITP'ye göre uzay-zaman ve fiziksel nesneler mutlak hakikat değil, şuurun muhatap olduğu bir arayüzdür (Şehadet Perdesi); hakikat perde arkasındaki Esmâ-i Hüsnâ'dır."
  }
];

let ALL_DOCS = [];
let ALL_DIAGRAMS = [];
let ALL_GLOSSARY = [];
let activeDocCategory = "Tümü";
let activeDocId = null;
let activeGlossaryLetter = "Tümü";
let diagramsRendered = false;
let currentWisdomIdx = 0;
let modalZoom = 1.0;
let proseSize = 1.0;
let cmdSelectedIdx = 0;
let currentCmdItems = [];

// Quiz State
let quizIdx = 0;
let quizScore = 0;
let quizAnswered = false;

/* Toast Helper */
let toastTimer = null;
function showToast(msg) {
  const el = document.getElementById('toast');
  el.textContent = msg;
  el.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove('show'), 2100);
}

/* Bookmarks (localStorage) */
function getBookmarks() {
  try { return JSON.parse(localStorage.getItem('tk_bookmarks') || '[]'); } catch { return []; }
}
function saveBookmarks(list) {
  localStorage.setItem('tk_bookmarks', JSON.stringify(list));
}

/* Theme Toggle */
function initTheme() {
  const saved = localStorage.getItem('tk_theme');
  if (saved === 'tezhip') {
    document.body.classList.add('theme-tezhip');
    document.getElementById('theme-toggle').textContent = '🌙';
  }
}
function toggleTheme() {
  const isTezhip = document.body.classList.toggle('theme-tezhip');
  localStorage.setItem('tk_theme', isTezhip ? 'tezhip' : 'cosmic');
  document.getElementById('theme-toggle').textContent = isTezhip ? '🌙' : '📜';
  showToast(isTezhip ? '📜 Tezhip okuma teması aktif' : '🌌 Kozmik karanlık tema aktif');
}

/* Mobile Menu */
function toggleMobileMenu() {
  document.getElementById('nav-links').classList.toggle('open');
}

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

/* Reading Progress & Back-to-Top */
function initScrollUX() {
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
    document.getElementById('read-progress').style.width = pct + '%';
    document.getElementById('back-top').classList.toggle('visible', scrollTop > 420);
  });
}

/* Navigasyon */
function navigateTo(viewName) {
  document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('nav-links').classList.remove('open');

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

/* Lab Deep-Linking */
function openLabTab(tabId) {
  navigateTo('lab');
  const iframe = document.getElementById('lab-iframe');
  document.querySelectorAll('#lab-quick-pills .filter-pill').forEach(p => {
    p.classList.toggle('active', p.dataset.tab === tabId);
  });
  if (iframe && iframe.contentWindow) {
    iframe.contentWindow.postMessage({ type: 'switchTab', tabId }, '*');
  }
}

function renderLabQuickPills() {
  const wrap = document.getElementById('lab-quick-pills');
  wrap.innerHTML = MODELS_CATALOG.map((m, idx) => `
    <button class="filter-pill ${idx === 0 ? 'active' : ''}" data-tab="${m.tab}" onclick="openLabTab('${m.tab}')">${m.num}. ${m.title}</button>
  `).join('');
}

/* Wisdom Card */
function renderWisdom() {
  const item = WISDOM_QUOTES[currentWisdomIdx];
  document.getElementById('wisdom-quote').textContent = `“${item.q}”`;
  document.getElementById('wisdom-source').textContent = `— ${item.src}`;
  document.getElementById('wisdom-physics').textContent = item.phys;
}
function nextWisdom() {
  currentWisdomIdx = (currentWisdomIdx + 1) % WISDOM_QUOTES.length;
  renderWisdom();
}
function copyCurrentWisdom() {
  const item = WISDOM_QUOTES[currentWisdomIdx];
  navigator.clipboard.writeText(`"${item.q}" — ${item.src} (${item.phys})`).then(() => showToast('✓ Hikmet panoya kopyalandı'));
}

/* 12 Model Önizleme */
function renderModelsPreview() {
  const grid = document.getElementById('models-preview-grid');
  grid.innerHTML = MODELS_CATALOG.map(m => `
    <div class="model-card" onclick="openLabTab('${m.tab}')">
      <div class="model-top">
        <span class="model-num">MODEL ${m.num}</span>
        <span class="model-src">${m.src}</span>
      </div>
      <h4>${m.title}</h4>
      <p>${m.desc}</p>
      <span class="model-cta">Simülasyonu Aç →</span>
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
  const cats = ["Tümü", "★ Kaydedilenler", ...new Set(ALL_DOCS.map(d => d.category))];
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
  const bookmarks = getBookmarks();
  const filtered = ALL_DOCS.filter(d => {
    const matchCat =
      activeDocCategory === "Tümü" ||
      (activeDocCategory === "★ Kaydedilenler" ? bookmarks.includes(d.id) : d.category === activeDocCategory);
    const matchQ = !q || d.title.toLowerCase().includes(q) || d.excerpt.toLowerCase().includes(q);
    return matchCat && matchQ;
  });

  list.innerHTML = filtered.map(d => `
    <div class="doc-item ${d.id === activeDocId ? 'active' : ''}" data-doc-id="${d.id}" onclick="selectDoc('${d.id}')">
      <div class="doc-item-title">${d.title}</div>
      <div class="doc-item-meta">
        <span>${d.category} · ${d.readMin} dk</span>
        <span>${bookmarks.includes(d.id) ? '★' : ''}</span>
      </div>
    </div>
  `).join('') || `<p style="color:var(--text-muted); font-size:0.85rem;">Eşleşen makale bulunamadı.</p>`;
}

function changeFontSize(delta) {
  proseSize = Math.max(0.85, Math.min(1.35, proseSize + delta));
  document.documentElement.style.setProperty('--prose-size', proseSize.toFixed(2) + 'rem');
}

function toggleFocusMode() {
  const layout = document.getElementById('docs-layout');
  const active = layout.classList.toggle('focus-mode');
  document.getElementById('btn-focus').classList.toggle('active', active);
}

function toggleCurrentBookmark() {
  if (!activeDocId) return;
  const bm = getBookmarks();
  const idx = bm.indexOf(activeDocId);
  if (idx >= 0) {
    bm.splice(idx, 1);
    showToast('☆ Kaydedilenlerden çıkarıldı');
  } else {
    bm.push(activeDocId);
    showToast('★ Makale kaydedildi');
  }
  saveBookmarks(bm);
  updateBookmarkBtn();
  renderDocsList();
}

function updateBookmarkBtn() {
  const btn = document.getElementById('btn-bookmark');
  const saved = getBookmarks().includes(activeDocId);
  btn.textContent = saved ? '★ Kayıtlı' : '☆ Kaydet';
  btn.classList.toggle('active', saved);
}

async function selectDoc(docId) {
  const idx = ALL_DOCS.findIndex(d => d.id === docId);
  if (idx < 0) return;
  const doc = ALL_DOCS[idx];
  activeDocId = doc.id;
  updateBookmarkBtn();

  document.querySelectorAll('.doc-item').forEach(el => {
    el.classList.toggle('active', el.dataset.docId === docId);
  });

  document.getElementById('doc-meta-bar').innerHTML = `
    <span class="doc-badge">${doc.category}</span>
    <span>📄 ${doc.path}</span>
    <span>⏱️ ~${doc.readMin} dk (${doc.words} kelime)</span>
  `;

  const container = document.getElementById('doc-content');
  container.innerHTML = marked.parse(doc.content);

  // Build auto Table of Contents
  const headings = Array.from(container.querySelectorAll('h2, h3'));
  const tocWrap = document.getElementById('doc-toc-wrap');
  if (headings.length >= 2) {
    headings.forEach((h, i) => { h.id = `sec-${i}`; });
    tocWrap.innerHTML = `
      <div class="doc-toc">
        <div class="doc-toc-title">📑 İçindekiler</div>
        <ul>${headings.map((h, i) => `<li><a href="#sec-${i}" onclick="document.getElementById('sec-${i}').scrollIntoView({behavior:'smooth'}); return false;">${h.textContent}</a></li>`).join('')}</ul>
      </div>
    `;
  } else {
    tocWrap.innerHTML = '';
  }

  // Intercept internal .md links inside articles
  container.querySelectorAll('a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (href && href.endsWith('.md')) {
      a.addEventListener('click', (e) => {
        e.preventDefault();
        const fname = href.split('/').pop();
        const target = ALL_DOCS.find(d => d.path.endsWith(fname));
        if (target) {
          selectDoc(target.id);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }
  });

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

  // Prev / Next article navigation
  const prevDoc = idx > 0 ? ALL_DOCS[idx - 1] : null;
  const nextDoc = idx < ALL_DOCS.length - 1 ? ALL_DOCS[idx + 1] : null;
  document.getElementById('doc-nav-footer').innerHTML = `
    ${prevDoc ? `<button class="btn-secondary" style="padding:0.55rem 1.1rem; font-size:0.84rem;" onclick="selectDoc('${prevDoc.id}'); window.scrollTo({top:0,behavior:'smooth'});">← ${prevDoc.title}</button>` : '<span></span>'}
    ${nextDoc ? `<button class="btn-secondary" style="padding:0.55rem 1.1rem; font-size:0.84rem;" onclick="selectDoc('${nextDoc.id}'); window.scrollTo({top:0,behavior:'smooth'});">${nextDoc.title} →</button>` : '<span></span>'}
  `;
}

function openDocByPath(path) {
  navigateTo('docs');
  const doc = ALL_DOCS.find(d => d.path === path);
  if (doc) selectDoc(doc.id);
}

/* Diyagram Galerisi & Zoom Modal */
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
        <button class="btn-mini" onclick="copyDiagramCode('${d.id}')">📋 Mermaid Kodu</button>
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
    } catch (_) {
      el.innerHTML = `<pre style="font-size:0.75rem; color:var(--text-muted);">${d.code}</pre>`;
    }
  }
}

async function openDiagramModal(diagId) {
  const d = ALL_DIAGRAMS.find(x => x.id === diagId);
  if (!d) return;
  resetModalZoom();
  document.getElementById('modal-title').textContent = `🗺️ ${d.title}`;
  const wrap = document.getElementById('modal-zoom-wrap');
  wrap.innerHTML = '<span style="color:var(--text-muted);">Yükleniyor...</span>';
  document.getElementById('diagram-modal').classList.add('open');
  try {
    const { svg } = await mermaid.render(`modal-mmd-${Date.now()}`, d.code);
    wrap.innerHTML = svg;
  } catch (_) {
    wrap.innerHTML = `<pre>${d.code}</pre>`;
  }
}

function zoomModal(delta) {
  modalZoom = Math.max(0.5, Math.min(2.6, modalZoom + delta));
  document.getElementById('modal-zoom-wrap').style.transform = `scale(${modalZoom.toFixed(2)})`;
  document.getElementById('modal-zoom-label').textContent = `%${Math.round(modalZoom * 100)}`;
}

function resetModalZoom() {
  modalZoom = 1.0;
  document.getElementById('modal-zoom-wrap').style.transform = 'scale(1)';
  document.getElementById('modal-zoom-label').textContent = '%100';
}

function closeModal() {
  document.getElementById('diagram-modal').classList.remove('open');
}

function copyDiagramCode(diagId) {
  const d = ALL_DIAGRAMS.find(x => x.id === diagId);
  if (!d) return;
  navigator.clipboard.writeText(d.code).then(() => showToast('✓ Mermaid kodu kopyalandı'));
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

/* İnteraktif Tılsım Bilgi & Tefekkür Testi */
function updateQuizHighScoreBadge() {
  const best = localStorage.getItem('tk_quiz_best');
  document.getElementById('quiz-highscore-badge').textContent = best ? `En Yüksek Skor: ${best} / ${QUIZ_QUESTIONS.length}` : 'En Yüksek Skor: —';
}

function renderQuiz() {
  const root = document.getElementById('quiz-root');
  if (quizIdx >= QUIZ_QUESTIONS.length) {
    const prevBest = parseInt(localStorage.getItem('tk_quiz_best') || '0', 10);
    if (quizScore > prevBest) localStorage.setItem('tk_quiz_best', String(quizScore));
    updateQuizHighScoreBadge();

    let rank = "Sâlik (Yolculuk Başlangıcı)";
    if (quizScore >= 11) rank = "🌌 Tılsım Kâşifi (Ehl-i Tahkik Zirvesi)";
    else if (quizScore >= 8) rank = "✨ Mütefekkir (Mânâ-yı Harfî Nazarı)";
    else if (quizScore >= 5) rank = "📖 Talib-i Hakikat";

    root.innerHTML = `
      <div style="text-align:center; padding:1rem 0;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">🏆</div>
        <h3 style="font-family:'Cinzel',serif; font-size:1.6rem; margin-bottom:0.5rem;">Test Tamamlandı!</h3>
        <p style="font-size:1.25rem; color:var(--cyan); font-weight:700; margin-bottom:0.5rem;">Skorunuz: ${quizScore} / ${QUIZ_QUESTIONS.length}</p>
        <p style="color:var(--gold); font-weight:600; margin-bottom:1.5rem;">Mertebe: ${rank}</p>
        <button class="btn-primary" onclick="restartQuiz()">↻ Testi Yeniden Çöz</button>
      </div>
    `;
    return;
  }

  const qObj = QUIZ_QUESTIONS[quizIdx];
  const pct = Math.round((quizIdx / QUIZ_QUESTIONS.length) * 100);
  root.innerHTML = `
    <div style="display:flex; justify-content:space-between; font-size:0.84rem; color:var(--text-muted);">
      <span>Soru ${quizIdx + 1} / ${QUIZ_QUESTIONS.length}</span>
      <span>Doğru: <strong style="color:var(--emerald);">${quizScore}</strong></span>
    </div>
    <div class="quiz-progress-bar"><div class="quiz-progress-fill" style="width:${pct}%;"></div></div>
    <div class="quiz-question">${qObj.q}</div>
    <div class="quiz-options" id="quiz-options">
      ${qObj.opts.map((opt, i) => `<button class="quiz-opt" onclick="answerQuiz(${i})">${String.fromCharCode(65 + i)}) ${opt}</button>`).join('')}
    </div>
    <div id="quiz-feedback-area"></div>
  `;
}

function answerQuiz(choice) {
  if (quizAnswered) return;
  quizAnswered = true;
  const qObj = QUIZ_QUESTIONS[quizIdx];
  const btns = document.querySelectorAll('#quiz-options .quiz-opt');
  btns.forEach((b, i) => {
    b.disabled = true;
    if (i === qObj.ans) b.classList.add('correct');
    else if (i === choice) b.classList.add('wrong');
  });
  if (choice === qObj.ans) quizScore++;

  document.getElementById('quiz-feedback-area').innerHTML = `
    <div class="quiz-feedback">
      <strong>${choice === qObj.ans ? '✅ Doğru!' : '💡 Açıklama:'}</strong> ${qObj.exp}
    </div>
    <div style="margin-top:1.1rem; text-align:right;">
      <button class="btn-primary" style="padding:0.6rem 1.3rem;" onclick="nextQuizQuestion()">
        ${quizIdx + 1 < QUIZ_QUESTIONS.length ? 'Sonraki Soru →' : 'Sonucu Gör 🏆'}
      </button>
    </div>
  `;
}

function nextQuizQuestion() {
  quizIdx++;
  quizAnswered = false;
  renderQuiz();
}

function restartQuiz() {
  quizIdx = 0;
  quizScore = 0;
  quizAnswered = false;
  renderQuiz();
}

/* Global Command Palette (Ctrl+K) */
function openCmdPalette() {
  document.getElementById('cmd-modal').classList.add('open');
  const inp = document.getElementById('cmd-input');
  inp.value = '';
  inp.focus();
  renderCmdResults('');
}

function closeCmdPalette() {
  document.getElementById('cmd-modal').classList.remove('open');
}

function renderCmdResults(query) {
  const q = query.trim().toLowerCase();
  const items = [];

  MODELS_CATALOG.forEach(m => {
    if (!q || m.title.toLowerCase().includes(q) || m.desc.toLowerCase().includes(q) || m.src.toLowerCase().includes(q)) {
      items.push({ tag: 'Model', title: `${m.num}. ${m.title}`, sub: m.src, action: () => openLabTab(m.tab) });
    }
  });

  ALL_DOCS.forEach(d => {
    if (!q || d.title.toLowerCase().includes(q) || d.category.toLowerCase().includes(q) || d.excerpt.toLowerCase().includes(q)) {
      items.push({ tag: 'Makale', title: d.title, sub: `${d.category} · ${d.readMin} dk`, action: () => { navigateTo('docs'); selectDoc(d.id); } });
    }
  });

  ALL_DIAGRAMS.forEach(dg => {
    if (!q || dg.title.toLowerCase().includes(q) || dg.description.toLowerCase().includes(q)) {
      items.push({ tag: 'Diyagram', title: dg.title, sub: dg.description, action: () => { navigateTo('diagrams'); setTimeout(() => openDiagramModal(dg.id), 150); } });
    }
  });

  ALL_GLOSSARY.forEach(g => {
    if (q && (g.term.toLowerCase().includes(q) || g.definition.toLowerCase().includes(q))) {
      items.push({ tag: 'Sözlük', title: g.term, sub: g.definition.slice(0, 90) + '…', action: () => { navigateTo('glossary'); document.getElementById('glossary-search').value = g.term; activeGlossaryLetter = 'Tümü'; renderGlossary(); } });
    }
  });

  currentCmdItems = items.slice(0, 14);
  cmdSelectedIdx = 0;

  const box = document.getElementById('cmd-results');
  box.innerHTML = currentCmdItems.map((it, i) => `
    <div class="cmd-item ${i === 0 ? 'selected' : ''}" onclick="executeCmdItem(${i})">
      <div>
        <div class="cmd-item-title">${it.title}</div>
        <div class="cmd-item-sub">${it.sub}</div>
      </div>
      <span class="cmd-tag">${it.tag}</span>
    </div>
  `).join('') || `<p style="padding:1rem; color:var(--text-muted); font-size:0.88rem;">Sonuç bulunamadı.</p>`;
}

function executeCmdItem(idx) {
  const item = currentCmdItems[idx];
  if (!item) return;
  closeCmdPalette();
  item.action();
}

function initKeyboardShortcuts() {
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openCmdPalette();
      return;
    }
    if (e.key === 'Escape') {
      closeCmdPalette();
      closeModal();
      return;
    }
    const cmdOpen = document.getElementById('cmd-modal').classList.contains('open');
    if (cmdOpen && currentCmdItems.length > 0) {
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        cmdSelectedIdx = (cmdSelectedIdx + 1) % currentCmdItems.length;
        updateCmdSelection();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        cmdSelectedIdx = (cmdSelectedIdx - 1 + currentCmdItems.length) % currentCmdItems.length;
        updateCmdSelection();
      } else if (e.key === 'Enter') {
        e.preventDefault();
        executeCmdItem(cmdSelectedIdx);
      }
    }
  });
}

function updateCmdSelection() {
  document.querySelectorAll('#cmd-results .cmd-item').forEach((el, i) => {
    el.classList.toggle('selected', i === cmdSelectedIdx);
  });
}

/* Başlatma */
async function bootstrap() {
  initTheme();
  initStarfield();
  initScrollUX();
  initKeyboardShortcuts();

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

  currentWisdomIdx = Math.floor(Math.random() * WISDOM_QUOTES.length);
  renderWisdom();
  renderModelsPreview();
  renderLabQuickPills();
  renderMatrix();
  updateQuizHighScoreBadge();
  renderQuiz();

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
  document.getElementById('cmd-input').addEventListener('input', e => renderCmdResults(e.target.value));

  const hash = location.hash.replace('#', '');
  if (['home', 'lab', 'docs', 'diagrams', 'glossary', 'matrix', 'quiz'].includes(hash)) {
    navigateTo(hash);
  }
}

window.addEventListener('DOMContentLoaded', bootstrap);
