/* Tılsım-ı Kâinat v3 — Dijital Ontoloji, Kuantum ve Tefekkür Gözlemevi */

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
  },
  {
    q: "Bahar mevsiminde birkaç gün içinde yüz binlerce haşir numunesini gözümüz önünde icra eden Kudret'e, haşr-i âzam ağır gelemez.",
    src: "10. Söz (Haşir Risalesi)",
    phys: "⚛️ Paralel: Kuantum Unitarity (Bilgi Korunumu Yasası)"
  }
];

/* 61 Mertebe Kozmik Ölçek Verisi */
const COSMOS_SCALES = [
  {
    scale: "10^-35 m",
    short: "Planck (10⁻³⁵)",
    era: "Kuantum Köpüğü · Âlem-i Emir Sınırı",
    title: "Planck Uzunluğu & Tekvînî Nokta",
    desc: "Uzay ve zamanın klasik anlamını yitirdiği, geometrinin doğrudan enformasyon ve emr-i İlâhî ('Kün!') ile dokunduğu en temel fiziksel sınır.",
    esma: "El-Bâri · El-Mübdi · El-Kayyûm",
    law: "Kuantum Kütleçekimi & Holografik Sınır (l_P)",
    twin: "Levh-i Mahfuz'un en küçük pikseli / Nokta-i Nuraniye",
    risale: "29. Söz & 30. Söz (Âlem-i Emir)",
    mode: "foam"
  },
  {
    scale: "10^-15 m",
    short: "Zerre (10⁻¹⁵)",
    era: "Atomaltı Âlem · Tahavvülât-ı Zerrât",
    title: "Proton, Kuark ve Kudret Zerreleri",
    desc: "Katı madde sanılan varlığın aslında %99.9999 boşluk ve durmaksızın titreşen kuantum alan dalgalarından ibaret olduğu tekvînî yazı tahtası.",
    esma: "El-Kadîr · El-Muharrik · El-Ferd",
    law: "Kuantum Renk Dinamiği (QCD) & Wheeler 'It from Bit'",
    twin: "Mevlevî gibi dönen yıldız ve gezegen yörüngeleri",
    risale: "30. Söz, İkinci Maksad (Zerre Risalesi)",
    mode: "quarks"
  },
  {
    scale: "10^-10 m",
    short: "Atom (10⁻¹⁰)",
    era: "Kuantum Yörünge · Sikke-i Vahdet",
    title: "Atom ve Elektron Bulutları",
    desc: "Çekirdek etrafında belirli enerji seviyelerinde dönen elektron bulutları; her bir hidrojen ve karbon atomunda aynı evrensel kanunun mührü.",
    esma: "El-Hakem · El-Adl · El- Mukaddir",
    law: "Schrödinger Dalga Denklemi & Pauli Dışarlama İlkesi",
    twin: "Güneş Sistemi (Şems ve Seyyareler)",
    risale: "32. Söz & 30. Lem'a",
    mode: "atom"
  },
  {
    scale: "10^-9 m",
    short: "DNA (10⁻⁹)",
    era: "Moleküler Kitap · Negentropi Mührü",
    title: "DNA Çift Sarmalı (3.2 Milyar Harflik İmam-ı Mübîn)",
    desc: "Termodinamik dağılmaya rağmen milyarlarca nükleotidin hatasız dizilimiyle bütün canlının planını saklayan moleküler kader defteri.",
    esma: "El-Alîm · El-Hakîm · El-Musavvir",
    law: "Shannon Enformasyon Teorisi & Schrödinger Negentropisi",
    twin: "Kâinat Kitabı'nın satırları ve İmam-ı Mübîn",
    risale: "23. Lem'a (Tabiat) & 26. Söz (Kader)",
    mode: "dna"
  },
  {
    scale: "10^-5 m",
    short: "Hücre (10⁻⁵)",
    era: "Biyolojik Şehir · Kesrette Vahdet",
    title: "Canlı Hücre (Saniyede Binlerce Reaksiyonluk Fabrika)",
    desc: "Trilyonlarca atomun tek bir gaye etrafında yardımlaşarak (teavün) hayat nurunu yansıttığı mikroskobik şehir.",
    esma: "El-Hayy · Er-Rezzâk · El-Müdebbir",
    law: "Öz-Örgütlenme & Biyokimyasal Ağ Dinamiği",
    twin: "İnsan şehri ve küresel ekosistem",
    risale: "29. Söz & 30. Lem'a (İsm-i Hayy)",
    mode: "cell"
  },
  {
    scale: "10^-2 m",
    short: "Çekirdek (10⁻²)",
    era: "Program Kutusu · Fihriste",
    title: "Tohum ve Çekirdek (Ağacın Manevî Kutusu)",
    desc: "Koca bir çınar ağacının bütün dallarını, yapraklarını ve meyvelerini kuvve halinde saklayan sıkıştırılmış fıtrat algoritması.",
    esma: "El-Fâtır · El-Bâis · El-Hâlık",
    law: "Mandelbrot Fraktal Dallanma (L-Sistemleri)",
    twin: "İnsan kalbi ve kâinatın ilk yaratılış çekirdeği",
    risale: "10. Söz (Haşir) & 30. Lem'a",
    mode: "seed"
  },
  {
    scale: "10^0 m",
    short: "İnsan (10⁰)",
    era: "Mezo Merkez · Âlem-i Asgar",
    title: "İnsan — Kâinatın Misâl-i Musaggarı ve Halifesi",
    desc: "Emanet-i Kübrâ'yı (Ene) yüklenen, bütün Esmâ-i Hüsnâ'ya en câmi ayna olan, şuur (IIT Φ) ve cüz-i iradesiyle kâinatın fihristesi kılınan merkez varlık.",
    esma: "İsm-i Âzam & Bütün Esmâ-i Hüsnâ (99 İsim)",
    law: "Entegre Bilgi (IIT Φ) & Vâhid-i Kıyasî Referans Noktası",
    twin: "Âlem-i Ekber (Bütün Kâinat Sarayı)",
    risale: "11. Söz, 23. Söz & 30. Söz",
    mode: "human"
  },
  {
    scale: "10^7 m",
    short: "Dünya (10⁷)",
    era: "Gezegen Beşiği · Sefine-i Rabbaniye",
    title: "Küre-i Arz — Saniyede 30 km Hızla Yüzen Rabbanî Gemi",
    desc: "Yüz binlerce canlı türünü (bahar haşirlerini) erzakıyla birlikte uzay denizinde sarsmadan gezdiren muhteşem yaşam gemisi.",
    esma: "Er-Rahmân · Er-Rahîm · El-Hafîz",
    law: "Manyetosfer Kalkanı & İnce Ayarlı Biyosfer Dengesi",
    twin: "Canlı hücrenin koruyucu zarı ve iç dengesi",
    risale: "10. Söz & 32. Söz",
    mode: "earth"
  },
  {
    scale: "10^12 m",
    short: "Güneş (10¹²)",
    era: "Yıldız Ocağı · Ehadiyet Temsili",
    title: "Güneş Sistemi (Sirâc-ı Münîr & Gezegenler)",
    desc: "16. Söz'deki Ehadiyet temsilinin maddî aynası: Tek bir Güneş'in trilyonlarca şeffaf katrede bölünmeden ışık ve yedi rengiyle görünmesi.",
    esma: "En-Nûr · El-Celîl · El-Vâhid · El-Ehad",
    law: "Genel Görelilik (Uzay-Zaman Eğriliği) & Nükleer Füzyon",
    twin: "Atom çekirdeği ve elektron yörüngeleri",
    risale: "16. Söz & 19. Mektup",
    mode: "solar"
  },
  {
    scale: "10^21 m",
    short: "Galaksi (10²¹)",
    era: "Kozmik Şehir · Semâvât Ordusu",
    title: "Samanyolu Galaksisi (200 Milyar Yıldızlık Ordu)",
    desc: "Yüz milyarlarca güneşin tek bir merkez etrafında kusursuz logaritmik sarmal geometriyle döndüğü muazzam semâvî ordugâh.",
    esma: "El-Azîz · El-Cebbâr · Rabbü's-Semâvât",
    law: "Logaritmik Altın Sarmal & Karanlık Madde Halesi",
    twin: "DNA sarmalı ve kasırga/deniz kabuğu fraktalleri",
    risale: "29. Söz & Âyetü'l-Kübrâ",
    mode: "galaxy"
  },
  {
    scale: "10^26 m",
    short: "Kozmos (10²⁶)",
    era: "Âlem-i Ekber · Kozmik Ağ",
    title: "Gözlemlenebilir Kâinat (Kozmik Ağ / Şecere-i Hilkat)",
    desc: "2 trilyon galaksinin oluşturduğu kozmik filament ağı; insan beynindeki nöron ağıyla çarpıcı bir fraktal öz-benzerlik taşıyan Şecere-i Hilkat.",
    esma: "Allâh · Ferd · Hayy · Kayyûm · Hakem · Adl · Kuddûs",
    law: "Renormalizasyon Sabit Noktası & AdS/CFT Kozmolojisi",
    twin: "İnsan beynindeki nöral ağ (86 milyar nöron)",
    risale: "30. Lem'a (İsm-i Âzam) & 11. Söz",
    mode: "web"
  }
];

/* İnteraktif Kavram Ağı Düğümleri ve Bağlantıları */
const GRAPH_NODES_DEF = [
  { id: "tilsim", label: "TILSIM-I KÂİNAT", group: "merkez", r: 24, desc: "Kâinatın kilitli kapılarını açan iki anahtar: Enfüsî âlemde Ene, âfâkî âlemde Zerre.", doc: "docs/tilsim-i-kainat-kullî-cozum.md", tab: "tab-ene" },
  { id: "ene", label: "Ene (Vâhid-i Kıyasî)", group: "risale", r: 17, desc: "30. Söz 1. Maksad: Mutlak İlâhî sıfatları idrak için konulmuş farazî ölçü birimi.", doc: "docs/ene-ontolojisi/01-vahid-i-kiyasi.md", tab: "tab-ene" },
  { id: "zerre", label: "Tahavvülât-ı Zerrât", group: "risale", r: 17, desc: "30. Söz 2. Maksad: Kudret Kalemi'nin tekvînî âyetleri yazarkenki titreşimleri.", doc: "docs/zerre-dinamikleri/01-tahavvulat-i-zerrat.md", tab: "tab-zerre" },
  { id: "ihlas", label: "İhlas & 4444 Sırrı", group: "risale", r: 16, desc: "21. Lem'a: Enaniyet buzunun şahs-ı manevî havuzunda erimesiyle doğan üstel kuvvet.", doc: "docs/ene-ontolojisi/03-eneden-nahnuya.md", tab: "tab-ihlas" },
  { id: "ehadiyet", label: "Ehadiyet & Aynalar", group: "risale", r: 16, desc: "16. Söz: Güneş'in trilyonlarca katrede bölünmeden (%0 tecezzi) tam tecellisi.", doc: "docs/holografik-alem-ve-ehadiyet.md", tab: "tab-holografi" },
  { id: "harfi", label: "Mânâ-yı Harfî", group: "risale", r: 16, desc: "Mesnevî-i Nuriye: Varlığa kendisi adına değil, Sâni'ine ayna olması cihetiyle bakmak.", doc: "docs/dort-kelime-dort-kelam.md", tab: "tab-nazar" },
  { id: "kader", label: "Kader & 1-Bit Kesb", group: "risale", r: 15, desc: "26. Söz: Ezelî ilmin zorlamayışı (P(Cebir)=0) ve cüz-i ihtiyarînin sorumluluğu.", doc: "docs/kader-ve-irade-tilsimi.md", tab: "tab-kader" },
  { id: "hasir", label: "Haşir & Ebediyet", group: "risale", r: 15, desc: "10. Söz: Levh-i Mahfuz kaydıyla dağılmış zerrelerin bahar gibi yeniden iadesi.", doc: "docs/hasir-ve-ebediyet-tilsimi.md", tab: "tab-hasir" },
  { id: "hayat", label: "Hayat & Ruh", group: "risale", r: 15, desc: "29. Söz: Kesreti vahdete çeviren hayat nuru ve âlem-i emirden gelen zîşuur kanun.", doc: "docs/hayat-ve-ruh-tilsimi.md", tab: "tab-hayat" },
  { id: "mirac", label: "Mirac & Ân-ı Dâim", group: "risale", r: 15, desc: "31. Söz: Nuraniyet ile zamanın dürülmesi ve ezel-ebed seyrine tarfetü'l-aynda eriş.", doc: "docs/mirac-ve-tayy-i-zaman.md", tab: "tab-mirac" },
  { id: "tayy", label: "Belkıs'ın Tahtı", group: "risale", r: 15, desc: "20. Söz: Maddenin bilgiye ve letafete tercümesiyle göz açıp kapayıncaya kadar nakli.", doc: "docs/gelecegin-teknolojileri-ve-tilsim-i-kainat.md", tab: "tab-teleport" },
  { id: "ismiazam", label: "İsm-i Âzam & Fihriste", group: "risale", r: 16, desc: "30. Lem'a: Çekirdekten galaksiye 41 mertebede okunan aynı Sikke-i Vahdet mührü.", doc: "docs/esma-fraktal-ve-olcek-degismezligi.md", tab: "tab-fraktal" },
  // Fizik düğümleri
  { id: "godel", label: "Gödel & Referans", group: "fizik", r: 13, desc: "Sistemin içinden mutlak olanı ölçmek için haricî/farazî bir referans noktası gerekliliği.", doc: "docs/ene-ontolojisi/01-vahid-i-kiyasi.md", tab: "tab-ene" },
  { id: "wheeler", label: "Wheeler: It from Bit", group: "fizik", r: 14, desc: "Fiziksel varlığın temelinde katı madde değil, kuantum enformasyon bitlerinin bulunması.", doc: "docs/modern-fizik-ve-tilsim-i-kainat.md", tab: "tab-entropi" },
  { id: "rqm", label: "Rovelli RQM & ITP", group: "fizik", r: 14, desc: "İlişkisel Kuantum Mekaniği ve Hoffman Arayüz Kuramı: Bağımsız mânâ-yı ismî yoktur.", doc: "docs/dort-kelime-dort-kelam.md", tab: "tab-nazar" },
  { id: "adscft", label: "AdS/CFT & ER=EPR", group: "fizik", r: 14, desc: "Holografik İlke: 3B hacim bilgisinin sınırda korunması ve dolanıklıkla mesafesiz kurb.", doc: "docs/holografik-alem-ve-ehadiyet.md", tab: "tab-holografi" },
  { id: "iit", label: "Tononi IIT (Φ)", group: "fizik", r: 13, desc: "Entegre Bilgi Teorisi: Parçalara indirgenemeyen bütünleşik şuur ölçüsü (Φ >> 0).", doc: "docs/hayat-ve-ruh-tilsimi.md", tab: "tab-hayat" },
  { id: "lorentz", label: "Özel Görelilik", group: "fizik", r: 13, desc: "Einstein zaman genişlemesi (Lorentz faktörü γ) ve ışık hızı sınırında zamanın büzülmesi.", doc: "docs/mirac-ve-tayy-i-zaman.md", tab: "tab-mirac" },
  { id: "unitarity", label: "Kuantum Unitarity", group: "fizik", r: 13, desc: "Kuantum evriminde bilginin asla yok olmaması (tersinir bilgi korunumu).", doc: "docs/hasir-ve-ebediyet-tilsimi.md", tab: "tab-hasir" },
  { id: "teleport", label: "Kuantum Işınlanma", group: "fizik", r: 13, desc: "Dolanık kanallar üzerinden 10^32 qubitlik durum matrisinin 0.0 G ile aktarımı.", doc: "docs/gelecegin-teknolojileri-ve-tilsim-i-kainat.md", tab: "tab-teleport" },
  { id: "fractal", label: "Mandelbrot Fraktal D_f", group: "fizik", r: 14, desc: "Ölçekten bağımsız öz-benzerlik ve Wilson Renormalizasyon Grubu sabit noktası.", doc: "docs/esma-fraktal-ve-olcek-degismezligi.md", tab: "tab-fraktal" }
];

const GRAPH_EDGES_DEF = [
  ["tilsim", "ene"], ["tilsim", "zerre"], ["tilsim", "ihlas"], ["tilsim", "ehadiyet"],
  ["tilsim", "harfi"], ["tilsim", "kader"], ["tilsim", "hasir"], ["tilsim", "hayat"],
  ["tilsim", "mirac"], ["tilsim", "tayy"], ["tilsim", "ismiazam"],
  ["ene", "godel"], ["ene", "harfi"], ["ene", "ihlas"], ["ene", "kader"],
  ["zerre", "wheeler"], ["zerre", "hasir"], ["zerre", "ismiazam"],
  ["harfi", "rqm"], ["ehadiyet", "adscft"], ["ehadiyet", "ihlas"],
  ["hayat", "iit"], ["hayat", "ismiazam"],
  ["mirac", "lorentz"], ["mirac", "tayy"],
  ["tayy", "teleport"], ["tayy", "wheeler"],
  ["hasir", "unitarity"], ["kader", "unitarity"],
  ["ismiazam", "fractal"], ["adscft", "fractal"], ["rqm", "wheeler"]
];

/* 4 Rehberli Tefekkür Yolculuğu */
const LEARNING_PATHS = [
  {
    id: "path-ene",
    badge: "1. Rota · Enfüsî Âlem",
    title: "Ene'den Nahnu'ya: İç Tılsımın Fethi",
    desc: "Benlik çekirdeğinin ölçü biriminden (Vâhid-i Kıyasî) şahs-ı manevî havuzuna uzanan dönüşümü.",
    steps: [
      { id: "p1-s1", label: "Makale: Vâhid-i Kıyasî ve Sırr-ı Hilkat (30. Söz)", action: () => openDocByPath("docs/ene-ontolojisi/01-vahid-i-kiyasi.md") },
      { id: "p1-s2", label: "Deney: 1. Ene Kalınlaşma Simülasyonunu Test Et", action: () => openLabTab("tab-ene") },
      { id: "p1-s3", label: "Makale: Dört Kelime & Mânâ-yı Harfî (Mesnevî)", action: () => openDocByPath("docs/dort-kelime-dort-kelam.md") },
      { id: "p1-s4", label: "Deney: 3. İhlas ve 4444 Sinerjisi Simülasyonu", action: () => openLabTab("tab-ihlas") }
    ]
  },
  {
    id: "path-zerre",
    badge: "2. Rota · Âfâkî Âlem",
    title: "Zerre'den Galaksiye: Sikke-i Vahdet",
    desc: "Atomaltı titreşimlerden 41 mertebe kozmik ağlara uzanan Kudret Kalemi ve fraktal nizam.",
    steps: [
      { id: "p2-s1", label: "Makale: Tahavvülât-ı Zerrât ve Kudret Kalemi", action: () => openDocByPath("docs/zerre-dinamikleri/01-tahavvulat-i-zerrat.md") },
      { id: "p2-s2", label: "Makale: Tabiat Risalesi — 3 Bâtıl Yolun 9 Muhali", action: () => openDocByPath("docs/tabiat-ve-esbab-elestirisi.md") },
      { id: "p2-s3", label: "Keşif: 61 Mertebe Kozmik Ölçek Gezgini'ni İncele", action: () => navigateTo("cosmos") },
      { id: "p2-s4", label: "Deney: 12. Esmâ Fraktal & Ölçek Değişmezliği", action: () => openLabTab("tab-fraktal") }
    ]
  },
  {
    id: "path-quantum",
    badge: "3. Rota · 21. YY Fiziği",
    title: "Kuantum, Holografi ve Tayy-ı Zaman",
    desc: "RQM, AdS/CFT Holografik İlke, Kuantum Işınlanma ve Mirac göreliliğinin analitik sentezi.",
    steps: [
      { id: "p3-s1", label: "Makale: Holografik Âlem-i Misâl ve Ehadiyet (16. Söz)", action: () => openDocByPath("docs/holografik-alem-ve-ehadiyet.md") },
      { id: "p3-s2", label: "Deney: 11. Holografik Ayna & %0 Tecezzi Testi", action: () => openLabTab("tab-holografi") },
      { id: "p3-s3", label: "Makale: Geleceğin Teknolojileri & Belkıs'ın Tahtı", action: () => openDocByPath("docs/gelecegin-teknolojileri-ve-tilsim-i-kainat.md") },
      { id: "p3-s4", label: "Deney: 9. Mirac, Lorentz ve Ân-ı Dâim Simülasyonu", action: () => openLabTab("tab-mirac") }
    ]
  },
  {
    id: "path-ebediyet",
    badge: "4. Rota · Hayat, İrade & Bekâ",
    title: "Şuur, Cüz-i İhtiyarî ve Ebedî Haşir",
    desc: "İnsanın üç büyük sualine (Necisin? Nereden? Nereye?) verilen küllî cevap.",
    steps: [
      { id: "p4-s1", label: "Makale: Kâinat Sarayı ve Üç Büyük Sual (11. Söz)", action: () => openDocByPath("docs/kainat-sarayi-ve-uc-sual.md") },
      { id: "p4-s2", label: "Deney: 8. Hayat, Şuur ve IIT Φ Simülasyonu", action: () => openLabTab("tab-hayat") },
      { id: "p4-s3", label: "Deney: 6. Kader ve 1-Bitlik Kesb Matrisi", action: () => openLabTab("tab-kader") },
      { id: "p4-s4", label: "Makale & Deney: Haşir ve Kuantum Bilgi Korunumu", action: () => openLabTab("tab-hasir") }
    ]
  }
];

/* 20 Soruluk Kategorili Tefekkür Testi */
const QUIZ_QUESTIONS = [
  { cat: "Ene & İhlas", q: "30. Söz'e göre Ene'nin (benliğin) yaratılıştaki aslî ve fıtrî vazifesi nedir?", opts: ["Müstakil rububiyet iddia etmek", "Mutlak İlâhî sıfatları anlamak için farazî bir ölçü birimi (Vâhid-i Kıyasî) olmak", "Maddî sebeplerin yaratıcılığını göstermek", "Hareketi durdurmak"], ans: 1, exp: "Ene, coğrafyadaki ekvator hattı gibi farazî bir ölçü birimidir (Vâhid-i Kıyasî); mutlak sıfatları idrak ettirir." },
  { cat: "Ene & İhlas", q: "21. Lem'a'daki '4444 Sırrı' (İhlas ve Şahs-ı Manevî) modern fizikte hangi ilkeyle yapısal paralellik taşır?", opts: ["Klasik sürtünme kanunu", "Kuantum süperpozisyon ve üstel ağ sinerjisi (10^N / 2^N)", "Termodinamik ısı ölümü", "Klasik soğuma yasası"], ans: 1, exp: "Enaniyet buzunun eriyerek şahs-ı manevî havuzunda birleşmesiyle N birimlik güç doğrusal toplamdan üstel kapasiteye sıçrar." },
  { cat: "Ene & İhlas", q: "Mesnevî-i Nuriye'deki 'Dört Kelime' içinde eşyaya kendi nefsi hesabına değil, Sâni'ine delâleti cihetiyle bakmaya ne denir?", opts: ["Mânâ-yı İsmî", "Mânâ-yı Harfî", "Gaflet Nazarı", "İstibdad-ı Aklî"], ans: 1, exp: "Mânâ-yı Harfî, her varlığı Hâlık'ını tanıtan bir harf ve ayna olarak okumaktır." },
  { cat: "Ene & İhlas", q: "30. Söz'de Ene'nin gaflet ve felsefeyle kalınlaşmasının 5 fazlı temsili nasıldır?", opts: ["Toprak → Taş → Demir", "Hava → Buhar → Sıvı → Buz → Sahibini Yutma", "Ateş → Duman → Kül", "Tohum → Filiz → Ağaç"], ans: 1, exp: "Hava gibi şeffaf olan Ene, gafletle buharlaşır, sıvılaşır, buzlaşır ve nihayet sahibini yutan firavuniyete dönüşür." },
  { cat: "Ene & İhlas", q: "12. Söz'de Kur'ân şakirdi 'Abd-i Azîz' olarak tanımlanırken, esbabperest felsefe talebesi nasıl tavsif edilir?", opts: ["Cebbâr-ı Hodfürûş / Firavun-u Zelîl", "Hakîm-i Mutlak", "Sâlik-i Münevver", "Sultan-ı Kâinat"], ans: 0, exp: "Kalbinde istinad noktası olmayan nefis her şeye boyun eğdiği için zillet içinde kibir satan bir 'firavun-u zelîl' olur." },
  { cat: "Kuantum & Kozmos", q: "30. Söz İkinci Maksad'daki 'Tahavvülât-ı Zerrât' kavramı, John A. Wheeler'ın hangi ilkesiyle örtüşür?", opts: ["It from Bit (Madde enformasyondan doğar)", "Sabit Durum Kozmolojisi", "Mutlak Eter Teorisi", "Mekanik Determinizm"], ans: 0, exp: "Zerre katı bir töz değil; Kudret Kalemi'nin tekvînî âyetleri (enformasyonu) yazarkenki titreşimidir." },
  { cat: "Kuantum & Kozmos", q: "16. Söz'deki Güneş–Ayna (Ehadiyet) temessülünde ayna sayısı 1'den 10^24'e çıktığında kaynakta ne kadar bölünme (tecezzi) olur?", opts: ["%99.9 kayıp", "Mesafenin karesiyle azalır", "Sıfır (%0.0) — Nuraniyet bölünmeden her katrede tam tecelli eder", "Yalnızca okyanusta görünür"], ans: 2, exp: "Nuraniyet için sayı ve mesafe engel değildir; kaynak bölünmeden (%0 tecezzi) her şeffaf aynada tecelli eder." },
  { cat: "Kuantum & Kozmos", q: "Mesnevî-i Nuriye'deki 'Mânâ-yı Harfî' (nisbet) kavramı 21. yüzyıl fiziğinde hangi kuramla paralellik kurar?", opts: ["Carlo Rovelli — İlişkisel Kuantum Mekaniği (RQM)", "Klasik Mutlak Uzay", "Mekanik Materyalizm", "Sabit Atomculuk"], ans: 0, exp: "RQM'ye göre hiçbir nesnenin tek başına mutlak özelliği yoktur; özellikler yalnızca ilişkiler (nisbet) içinde doğar." },
  { cat: "Kuantum & Kozmos", q: "31. Söz (Mirac Risalesi) ve Özel Görelilik sentezinde 'Ân-ı Dâim' ve 'Tarfetü'l-Ayn' neyi ifade eder?", opts: ["Maddenin yok olmasını", "Nuraniyet kesbederek Higgs eylemsizliğinin sıfırlanması ve zamanın dürülerek ezel-ebed seyrine erilmesi", "Ses hızının aşılmasını", "Yalnızca rüyayı"], ans: 1, exp: "Letâfet ve nuraniyetle eylemsizlik (0.0 G) aşılır; zaman dürülerek birkaç dakikada binlerce senelik seyir gerçekleşir." },
  { cat: "Kuantum & Kozmos", q: "20. Söz'de Belkıs'ın Tahtı'nın nakli (Neml: 40) için 'It from Bit' ve Tayy-ı Mekân modelinin öngördüğü en kritik fark nedir?", opts: ["Kütlesel nakilde G-kuvveti varken, enformasyonel / nuranî nakilde 0.0 G ile tarfetü'l-ayn hızına ulaşılır", "Klasik nakil daha hızlıdır", "Bilgi kütleden ağırdır", "Fark yoktur"], ans: 0, exp: "10^32 qubitlik enformasyonel rekonstrüksiyon ve nuraniyet sürüşü eylemsizliksiz (0.0 G) milisaniyeler içinde nakil sağlar." },
  { cat: "Kuantum & Kozmos", q: "30. Lem'a ve 32. Söz'deki 'İnsan kâinatın misâl-i musaggarıdır' hakikati 12. modelde ne ile modellenir?", opts: ["Doğrusal Regresyon", "Mandelbrot Fraktal Boyutu (D_f) ve Renormalizasyon Grubu (Ölçek Değişmezliği)", "Rastgele Yürüyüş", "Öklid Düzlemi"], ans: 1, exp: "Zerre → İnsan → Galaksi arasında 41 mertebe boyunca korunan öz-benzerlik (D_f) tek bir Sâni'nin Sikke-i Vahdet'idir." },
  { cat: "Kuantum & Kozmos", q: "Donald Hoffman'ın 'Arayüz Algı Kuramı (ITP)' Risale-i Nur'daki hangi kavramla derin bir epistemolojik benzerlik taşır?", opts: ["Şehadet Perdesi ve Mânâ-yı Harfî Nazarı", "Evcedethü'l-Esbâb", "Teşekkele Binefsihî", "Ülfet"], ans: 0, exp: "ITP'ye göre uzay-zaman şuurun muhatap olduğu bir arayüzdür (Şehadet Perdesi); hakikat perde arkasındaki Esmâ-i Hüsnâ'dır." },
  { cat: "Kuantum & Kozmos", q: "Maldacena ve Susskind'in 'ER = EPR' hipotezi 16. Söz'deki hangi sırra fiziksel bir analoji sunar?", opts: ["Kurb ve Bu'd Sırrı (Mesafeden bağımsız anlık yakınlık)", "Termodinamik soğuma", "Klasik kırılma indisi", "Kütle korunumu"], ans: 0, exp: "ER=EPR dolanıklık ile uzay-zaman mesafesi ne kadar büyük olursa olsun mekân ötesi yakınlığa (kurb) işaret eder." },
  { cat: "Kader, Hayat & Haşir", q: "26. Söz (Kader Risalesi) ışığında ezelî ilmin insan iradesini zorlama (cebir) olasılığı P(Cebir) kaçtır?", opts: ["1.0", "0.5", "0.0 (İlim malûma tâbidir; bilmek zorlamak değildir)", "0.9"], ans: 2, exp: "İlim malûma tâbi olduğu için insanın 1-bitlik kesbini zorlamaz (P(Cebir)=0)." },
  { cat: "Kader, Hayat & Haşir", q: "10. Söz (Haşir Risalesi) ile kuantum mekaniğindeki 'Unitarity (Bilgi Korunumu)' ilkesinin ortak neticesi nedir?", opts: ["Evrende fiziksel enformasyon yok olmaz; Levh-i Mahfuz kaydıyla iade mümkündür", "Ölümle bilgi silinir", "Haşir yalnızca semboldür", "Zerreler tek kullanımlıktır"], ans: 0, exp: "Kuantum Unitarity bilginin yok olmadığını gösterir; 10. Söz'de her varlığın planı Levh-i Mahfuz'da korunur." },
  { cat: "Kader, Hayat & Haşir", q: "29. Söz ve 30. Lem'a'daki 'Hayatın Sırr-ı Câmii' ve Ruh hakikati, Giulio Tononi'nin hangi kuramıyla kesişir?", opts: ["Entegre Bilgi Teorisi (IIT — Bütünleşik Bilgi Φ >> 0)", "Gaz Kinetik Teorisi", "Jeosantrik Model", "Saf Davranışçılık"], ans: 0, exp: "Canlılık ve şuur parçalara indirgenemeyen yüksek bütünleşik bilgi (Φ >> 0) ile kesreti vahdete çevirir." },
  { cat: "Kader, Hayat & Haşir", q: "23. Lem'a (Tabiat Risalesi) kâinattaki sanatı açıklamak isteyen maddeci felsefenin kaç bâtıl yolunu çürütür?", opts: ["1 yol", "3 bâtıl yol (Sebepler yapıyor, Kendi kendine oluyor, Tabiat icad ediyor) — her birinde 3 muhal ile", "7 yol", "12 yol"], ans: 1, exp: "Evcedethü'l-esbâb, Teşekkele binefsihî ve İktezathü't-tabiat yollarının her biri muhallerle çürütülerek Vâcibü'l-Vücud ispatlanır." },
  { cat: "Kader, Hayat & Haşir", q: "26. Söz'e göre insanı hem gururdan (fahr) hem de ümitsizlikten (yeis) kurtaran denge formülü nedir?", opts: ["İyilikleri nefisten, kötülükleri kaderden bilmek", "Hasenâtı Allah'tan bilip şükretmek; seyyiâtı nefsin kesbinden bilip istiğfar etmek", "İradeyi tamamen inkâr etmek", "Sebeplere güvenmek"], ans: 1, exp: "İcad Allah'a ait olduğu için hasenâtta şükür; kötü tercihi (kesb) nefis istediği için seyyiâtta istiğfar esastır." },
  { cat: "Kader, Hayat & Haşir", q: "11. Söz'de Kâinat Sarayı'na gelen her insanın ruhunu sızlatan 'Üç Müthiş Sual' hangileridir?", opts: ["Kaç yaşındasın? Ne iş yaparsın? Nerelisin?", "Necisin? Nereden geliyorsun? Nereye gidiyorsun?", "Madde nedir? Enerji nedir? Hız nedir?", "Dün ne oldu? Bugün ne var? Yarın ne olacak?"], ans: 1, exp: "Necisin? (Abd ve misafir), Nereden geliyorsun? (Ezelî Rahmetten), Nereye gidiyorsun? (Dâr-ı Bekâya)." },
  { cat: "Kader, Hayat & Haşir", q: "24. Mektup'a göre Cenâb-ı Hak hiçbir şeye muhtaç olmadığı (Samed) halde kâinattaki bu dâimî faaliyetin sırrı nedir?", opts: ["Mekanik zorunluluk", "Esmâ-i Hüsnâ'nın cemâl ve kemâlini şuhûd ve işhâd (görmek ve göstermek) istemesi, Rahmet ve Şevk-i Mukaddes", "Tesadüfî çarpışmalar", "Enerji tükenmesi"], ans: 1, exp: "Her cemâl ve kemâl sahibi kendi cemâl ve kemâlini görmek ve göstermek ister; bu Şuûnât-ı İlâhiye dâimî faaliyeti doğurur." }
];

/* Global Durum */
let ALL_DOCS = [];
let ALL_DIAGRAMS = [];
let ALL_GLOSSARY = [];
let ALL_SIMULATIONS = [];
let activeDocCategory = "Tümü";
let activeDocId = null;
let activeLabTab = "tab-ene";
let activeGlossaryLetter = "Tümü";
let glossaryMode = "list";
let diagramsRendered = false;
let currentWisdomIdx = 0;
let modalZoom = 1.0;
let proseSize = 1.0;
let cmdSelectedIdx = 0;
let currentCmdItems = [];
let activeModalSim = null;

// Flashcard State
let fcDeck = [];
let fcIdx = 0;

// Quiz State
let activeQuizCat = "Tümü";
let filteredQuiz = [];
let quizIdx = 0;
let quizScore = 0;
let quizAnswered = false;

// Audio & TTS State
let audioCtx = null;
let audioMaster = null;
let isAmbientPlaying = false;
let isSpeakingTTS = false;

// Graph State
let graphNodes = [];
let graphEdges = [];
let graphFilter = "all";
let selectedGraphNode = null;
let draggedNode = null;
let graphAnimRunning = false;

// Cosmos Canvas State
let currentCosmosIdx = 6;
let cosmosPhase = 0;

/* Toast */
let toastTimer = null;
function showToast(msg) {
  const el = document.getElementById('toast');
  el.textContent = msg;
  el.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove('show'), 2200);
}

/* LocalStorage Helpers */
function getBookmarks() {
  try { return JSON.parse(localStorage.getItem('tk_bookmarks') || '[]'); } catch { return []; }
}
function saveBookmarks(list) { localStorage.setItem('tk_bookmarks', JSON.stringify(list)); }

function getPathDone() {
  try { return JSON.parse(localStorage.getItem('tk_path_done') || '[]'); } catch { return []; }
}
function savePathDone(list) { localStorage.setItem('tk_path_done', JSON.stringify(list)); }

function getNotes() {
  try { return JSON.parse(localStorage.getItem('tk_notes') || '[]'); } catch { return []; }
}
function saveNotes(list) { localStorage.setItem('tk_notes', JSON.stringify(list)); }

function getKnownCards() {
  try { return JSON.parse(localStorage.getItem('tk_fc_known') || '[]'); } catch { return []; }
}
function saveKnownCards(list) { localStorage.setItem('tk_fc_known', JSON.stringify(list)); }

/* Tema */
function initTheme() {
  const saved = localStorage.getItem('tk_theme');
  if (saved === 'tezhip') {
    document.body.classList.add('theme-tezhip');
    document.getElementById('theme-toggle').textContent = '🌙';
  }
}

function toggleTheme() {
  const isTezhip = document.body.classList.toggle('theme-tezhip');
  const themeName = isTezhip ? 'tezhip' : 'cosmic';
  localStorage.setItem('tk_theme', themeName);
  document.getElementById('theme-toggle').textContent = isTezhip ? '🌙' : '📜';
  const iframe = document.getElementById('lab-iframe');
  if (iframe && iframe.contentWindow) {
    iframe.contentWindow.postMessage({ type: 'setTheme', theme: themeName }, '*');
  }
  showToast(isTezhip ? '📜 Tezhip okuma teması aktif' : '🌌 Kozmik karanlık tema aktif');
}

function toggleMobileMenu() {
  document.getElementById('nav-links').classList.toggle('open');
}

/* Web Audio — Kozmik Tefekkür Ambiyansı (432 Hz / 528 Hz Harmonik) */
function toggleAmbientAudio() {
  const btn = document.getElementById('audio-toggle');
  if (!isAmbientPlaying) {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) {
      showToast('Tarayıcınız Web Audio desteklemiyor.');
      return;
    }
    if (!audioCtx) {
      audioCtx = new AudioContextClass();
      audioMaster = audioCtx.createGain();
      audioMaster.gain.setValueAtTime(0.0001, audioCtx.currentTime);

      const filter = audioCtx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(480, audioCtx.currentTime);

      const freqs = [108, 216, 324, 432];
      freqs.forEach((f, idx) => {
        const osc = audioCtx.createOscillator();
        const g = audioCtx.createGain();
        osc.type = idx % 2 === 0 ? 'sine' : 'triangle';
        osc.frequency.setValueAtTime(f, audioCtx.currentTime);
        g.gain.setValueAtTime(idx === 0 ? 0.35 : 0.14 / idx, audioCtx.currentTime);
        osc.connect(g);
        g.connect(filter);
        osc.start();
      });

      filter.connect(audioMaster);
      audioMaster.connect(audioCtx.destination);
    }
    if (audioCtx.state === 'suspended') audioCtx.resume();
    audioMaster.gain.cancelScheduledValues(audioCtx.currentTime);
    audioMaster.gain.exponentialRampToValueAtTime(0.08, audioCtx.currentTime + 1.4);
    isAmbientPlaying = true;
    btn.classList.add('playing');
    showToast('🎵 Kozmik Tefekkür Ambiyansı (432 Hz) başlatıldı');
  } else {
    if (audioMaster && audioCtx) {
      audioMaster.gain.cancelScheduledValues(audioCtx.currentTime);
      audioMaster.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.8);
    }
    isAmbientPlaying = false;
    btn.classList.remove('playing');
    showToast('🔇 Ambiyans durduruldu');
  }
}

/* Yıldız Alanı */
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

/* Scroll Progress */
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
const VALID_VIEWS = ['home', 'lab', 'graph', 'cosmos', 'paths', 'docs', 'diagrams', 'glossary', 'matrix', 'quiz'];

function navigateTo(viewName) {
  if (!VALID_VIEWS.includes(viewName)) viewName = 'home';
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
  if (viewName === 'graph') {
    initGraphCanvas();
  }
}

/* Lab Deep-Linking & Python Source Viewer */
function openLabTab(tabId) {
  activeLabTab = tabId;
  navigateTo('lab');
  document.querySelectorAll('#lab-quick-pills .filter-pill').forEach(p => {
    p.classList.toggle('active', p.dataset.tab === tabId);
  });
  const iframe = document.getElementById('lab-iframe');
  if (iframe && iframe.contentWindow) {
    iframe.contentWindow.postMessage({ type: 'switchTab', tabId }, '*');
  }
}

window.addEventListener('message', (ev) => {
  if (ev.data && ev.data.type === 'tabChanged' && ev.data.tabId) {
    activeLabTab = ev.data.tabId;
    document.querySelectorAll('#lab-quick-pills .filter-pill').forEach(p => {
      p.classList.toggle('active', p.dataset.tab === activeLabTab);
    });
  }
});

function renderLabQuickPills() {
  const wrap = document.getElementById('lab-quick-pills');
  wrap.innerHTML = MODELS_CATALOG.map((m, idx) => `
    <button class="filter-pill ${idx === 0 ? 'active' : ''}" data-tab="${m.tab}" onclick="openLabTab('${m.tab}')">${m.num}. ${m.title}</button>
  `).join('');
}

function openPythonCodeModal(tabId) {
  const sim = ALL_SIMULATIONS.find(s => s.tab === tabId);
  if (!sim) {
    showToast('Simülasyon kodu yükleniyor...');
    return;
  }
  activeModalSim = sim;
  document.getElementById('code-modal-title').textContent = `🐍 ${sim.num}. ${sim.title} (${sim.file})`;
  document.getElementById('code-modal-meta').textContent = `${sim.risale} · ${sim.lines} satır Python · ${sim.tests} birim testi (${sim.testFile}) · Sıfır harici bağımlılık`;
  document.getElementById('code-modal-pre').textContent = sim.code;
  document.getElementById('code-modal').classList.add('open');
}

function openActiveLabPythonCode() {
  openPythonCodeModal(activeLabTab);
}

function closeCodeModal() {
  document.getElementById('code-modal').classList.remove('open');
}

function copyModalCli() {
  if (!activeModalSim) return;
  navigator.clipboard.writeText(activeModalSim.cli).then(() => showToast(`✓ CLI komutu kopyalandı: ${activeModalSim.cli}`));
}

function copyModalPython() {
  if (!activeModalSim) return;
  navigator.clipboard.writeText(activeModalSim.code).then(() => showToast('✓ Python kaynak kodu kopyalandı'));
}

function downloadModalPython() {
  if (!activeModalSim) return;
  const blob = new Blob([activeModalSim.code], { type: 'text/x-python;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = activeModalSim.file;
  a.click();
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
function saveWisdomToNotes() {
  const item = WISDOM_QUOTES[currentWisdomIdx];
  const notes = getNotes();
  notes.unshift({
    id: Date.now(),
    tag: item.src,
    text: `"${item.q}"\n(${item.phys})`,
    date: new Date().toLocaleDateString('tr-TR')
  });
  saveNotes(notes);
  renderNotes();
  showToast('📝 Hikmet Tefekkür Defteri’ne kaydedildi');
}

/* 12 Model Önizleme */
function renderModelsPreview() {
  const grid = document.getElementById('models-preview-grid');
  grid.innerHTML = MODELS_CATALOG.map(m => `
    <div class="model-card">
      <div class="model-top">
        <span class="model-num">MODEL ${m.num}</span>
        <span class="model-src">${m.src}</span>
      </div>
      <h4 style="cursor:pointer;" onclick="openLabTab('${m.tab}')">${m.title}</h4>
      <p>${m.desc}</p>
      <div class="model-card-actions">
        <button class="btn-mini" onclick="openPythonCodeModal('${m.tab}')">🐍 Python Kodu</button>
        <button class="btn-mini" style="border-color:var(--cyan); color:var(--cyan);" onclick="openLabTab('${m.tab}')">Simülasyonu Aç →</button>
      </div>
    </div>
  `).join('');
}

/* =========================================================
   İNTERAKTİF KAVRAM AĞI (FORCE-DIRECTED CANVAS GRAPH)
   ========================================================= */
function initGraphCanvas() {
  const canvas = document.getElementById('knowledge-canvas');
  if (!canvas) return;
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = Math.max(320, rect.width);
  canvas.height = 600;

  if (graphNodes.length === 0) {
    resetGraphPhysics();
  }
  if (!graphAnimRunning) {
    graphAnimRunning = true;
    setupGraphInteractions(canvas);
    requestAnimationFrame(stepGraphSimulation);
  }
}

function resetGraphPhysics() {
  const canvas = document.getElementById('knowledge-canvas');
  const cx = (canvas ? canvas.width : 800) / 2;
  const cy = 300;

  graphNodes = GRAPH_NODES_DEF.map((n, idx) => {
    const angle = (idx / GRAPH_NODES_DEF.length) * Math.PI * 2;
    const rad = n.group === 'merkez' ? 0 : (n.group === 'risale' ? 145 : 245);
    return {
      ...n,
      x: cx + Math.cos(angle) * rad + (Math.random() - 0.5) * 20,
      y: cy + Math.sin(angle) * rad + (Math.random() - 0.5) * 20,
      vx: 0,
      vy: 0
    };
  });

  graphEdges = GRAPH_EDGES_DEF.map(([s, t]) => ({ source: s, target: t }));
  selectGraphNode(graphNodes[0]);
}

function setGraphFilter(f, btn) {
  graphFilter = f;
  document.querySelectorAll('#graph-filters .filter-pill').forEach(p => p.classList.remove('active'));
  if (btn) btn.classList.add('active');
}

function isNodeVisible(n) {
  if (graphFilter === 'all') return true;
  if (graphFilter === 'merkez') return n.group === 'merkez' || n.group === 'risale';
  return n.group === graphFilter || n.group === 'merkez';
}

function stepGraphSimulation() {
  const canvas = document.getElementById('knowledge-canvas');
  if (canvas && document.getElementById('view-graph').classList.contains('active')) {
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    const visible = graphNodes.filter(isNodeVisible);
    const nodeMap = Object.fromEntries(visible.map(n => [n.id, n]));

    // Repulsion
    for (let i = 0; i < visible.length; i++) {
      for (let j = i + 1; j < visible.length; j++) {
        const a = visible[i], b = visible[j];
        let dx = b.x - a.x, dy = b.y - a.y;
        let dist2 = dx * dx + dy * dy + 1;
        let dist = Math.sqrt(dist2);
        let force = 2900 / dist2;
        let fx = (dx / dist) * force, fy = (dy / dist) * force;
        a.vx -= fx; a.vy -= fy;
        b.vx += fx; b.vy += fy;
      }
    }

    // Spring attraction
    for (const e of graphEdges) {
      const a = nodeMap[e.source], b = nodeMap[e.target];
      if (!a || !b) continue;
      let dx = b.x - a.x, dy = b.y - a.y;
      let dist = Math.sqrt(dx * dx + dy * dy) || 1;
      let targetDist = (a.group === 'merkez' || b.group === 'merkez') ? 145 : 115;
      let f = (dist - targetDist) * 0.018;
      let fx = (dx / dist) * f, fy = (dy / dist) * f;
      a.vx += fx; a.vy += fy;
      b.vx -= fx; b.vy -= fy;
    }

    // Center gravity & velocity update
    for (const n of visible) {
      if (n === draggedNode) continue;
      if (n.group === 'merkez') {
        n.vx += (w / 2 - n.x) * 0.04;
        n.vy += (h / 2 - n.y) * 0.04;
      } else {
        n.vx += (w / 2 - n.x) * 0.0025;
        n.vy += (h / 2 - n.y) * 0.0025;
      }
      n.vx *= 0.84;
      n.vy *= 0.84;
      n.x = Math.max(45, Math.min(w - 45, n.x + n.vx));
      n.y = Math.max(45, Math.min(h - 45, n.y + n.vy));
    }

    // Draw
    ctx.clearRect(0, 0, w, h);

    for (const e of graphEdges) {
      const a = nodeMap[e.source], b = nodeMap[e.target];
      if (!a || !b) continue;
      const isHi = selectedGraphNode && (selectedGraphNode.id === a.id || selectedGraphNode.id === b.id);
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.strokeStyle = isHi ? 'rgba(16, 185, 129, 0.85)' : 'rgba(148, 163, 184, 0.22)';
      ctx.lineWidth = isHi ? 2.2 : 1;
      ctx.stroke();
    }

    for (const n of visible) {
      const isSel = selectedGraphNode && selectedGraphNode.id === n.id;
      let fill = '#6366f1';
      if (n.group === 'merkez') fill = '#f59e0b';
      else if (n.group === 'fizik') fill = '#06b6d4';

      ctx.beginPath();
      ctx.arc(n.x, n.y, isSel ? n.r + 4 : n.r, 0, Math.PI * 2);
      ctx.fillStyle = fill;
      ctx.shadowColor = fill;
      ctx.shadowBlur = isSel ? 22 : 10;
      ctx.fill();
      ctx.shadowBlur = 0;

      if (isSel) {
        ctx.lineWidth = 2.5;
        ctx.strokeStyle = '#ffffff';
        ctx.stroke();
      }

      ctx.font = `${n.group === 'merkez' ? '700 12px' : '500 11px'} Inter, sans-serif`;
      ctx.fillStyle = '#f8fafc';
      ctx.textAlign = 'center';
      ctx.fillText(n.label, n.x, n.y + n.r + 14);
    }
  }
  requestAnimationFrame(stepGraphSimulation);
}

function setupGraphInteractions(canvas) {
  function getNodeAt(mx, my) {
    const visible = graphNodes.filter(isNodeVisible);
    for (let i = visible.length - 1; i >= 0; i--) {
      const n = visible[i];
      const dx = mx - n.x, dy = my - n.y;
      if (dx * dx + dy * dy <= (n.r + 8) * (n.r + 8)) return n;
    }
    return null;
  }

  canvas.addEventListener('mousedown', (e) => {
    const r = canvas.getBoundingClientRect();
    const hit = getNodeAt(e.clientX - r.left, e.clientY - r.top);
    if (hit) {
      draggedNode = hit;
      selectGraphNode(hit);
    }
  });

  window.addEventListener('mousemove', (e) => {
    if (!draggedNode) return;
    const r = canvas.getBoundingClientRect();
    draggedNode.x = e.clientX - r.left;
    draggedNode.y = e.clientY - r.top;
    draggedNode.vx = 0;
    draggedNode.vy = 0;
  });

  window.addEventListener('mouseup', () => { draggedNode = null; });

  canvas.addEventListener('touchstart', (e) => {
    const t = e.touches[0];
    const r = canvas.getBoundingClientRect();
    const hit = getNodeAt(t.clientX - r.left, t.clientY - r.top);
    if (hit) {
      e.preventDefault();
      draggedNode = hit;
      selectGraphNode(hit);
    }
  }, { passive: false });

  canvas.addEventListener('touchmove', (e) => {
    if (!draggedNode) return;
    e.preventDefault();
    const t = e.touches[0];
    const r = canvas.getBoundingClientRect();
    draggedNode.x = t.clientX - r.left;
    draggedNode.y = t.clientY - r.top;
  }, { passive: false });

  canvas.addEventListener('touchend', () => { draggedNode = null; });
}

function selectGraphNode(n) {
  selectedGraphNode = n;
  const typeLabel = n.group === 'merkez' ? 'Küllî Merkez' : (n.group === 'risale' ? 'Risale-i Nur Ontolojisi' : '21. Yüzyıl Fiziği & Matematik');
  document.getElementById('gi-type').textContent = typeLabel;
  document.getElementById('gi-title').textContent = n.label;
  document.getElementById('gi-desc').textContent = n.desc;

  const neighbors = GRAPH_EDGES_DEF
    .filter(([s, t]) => s === n.id || t === n.id)
    .map(([s, t]) => (s === n.id ? t : s))
    .map(id => GRAPH_NODES_DEF.find(x => x.id === id))
    .filter(Boolean);

  document.getElementById('gi-connections').innerHTML = `
    <div style="font-size:0.76rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:0.45rem;">Bağlantılı Düğümler (${neighbors.length})</div>
    <div class="pill-row">
      ${neighbors.map(nb => `<button class="filter-pill" onclick="focusGraphNodeById('${nb.id}')">${nb.label}</button>`).join('')}
    </div>
  `;

  document.getElementById('gi-actions').innerHTML = `
    <button class="btn-primary" style="justify-content:center; padding:0.62rem;" onclick="openLabTab('${n.tab}')">🔬 İlgili Simülasyonu Aç</button>
    <button class="btn-secondary" style="justify-content:center; padding:0.62rem;" onclick="openDocByPath('${n.doc}')">📚 Kaynak Makaleyi Oku</button>
  `;
}

function focusGraphNodeById(id) {
  const n = graphNodes.find(x => x.id === id);
  if (n) selectGraphNode(n);
}

/* =========================================================
   KOZMİK ÖLÇEK GEZGİNİ (61 MERTEBE VISUALIZER)
   ========================================================= */
function initCosmosExplorer() {
  const stopsWrap = document.getElementById('cosmos-stops');
  stopsWrap.innerHTML = COSMOS_SCALES.map((s, idx) => `
    <button class="filter-pill ${idx === currentCosmosIdx ? 'active' : ''}" onclick="updateCosmosScale(${idx})">${s.short}</button>
  `).join('');
  updateCosmosScale(currentCosmosIdx);
  requestAnimationFrame(drawCosmosCanvas);
}

function updateCosmosScale(idx) {
  currentCosmosIdx = idx;
  document.getElementById('cosmos-slider').value = idx;
  const s = COSMOS_SCALES[idx];
  document.getElementById('cosmos-scale-badge').textContent = s.scale;
  document.getElementById('cosmos-era-tag').textContent = s.era;
  document.getElementById('cosmos-title').textContent = s.title;
  document.getElementById('cosmos-desc').textContent = s.desc;
  document.getElementById('cosmos-esma').textContent = s.esma;
  document.getElementById('cosmos-law').textContent = s.law;
  document.getElementById('cosmos-twin').textContent = s.twin;
  document.getElementById('cosmos-risale').textContent = s.risale;
  document.getElementById('cosmos-visual-caption').textContent = `${s.scale} — ${s.title}`;

  document.querySelectorAll('#cosmos-stops .filter-pill').forEach((p, i) => {
    p.classList.toggle('active', i === idx);
  });
}

function drawCosmosCanvas() {
  const canvas = document.getElementById('cosmos-canvas');
  if (canvas && document.getElementById('view-cosmos').classList.contains('active')) {
    const ctx = canvas.getContext('2d');
    const w = canvas.width, h = canvas.height;
    const cx = w / 2, cy = h / 2;
    cosmosPhase += 0.022;
    ctx.clearRect(0, 0, w, h);

    const mode = COSMOS_SCALES[currentCosmosIdx].mode;

    // Outer subtle reference rings
    for (let r = 35; r <= 145; r += 36) {
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.14)';
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    if (mode === 'foam' || mode === 'quarks') {
      for (let i = 0; i < 18; i++) {
        const ang = cosmosPhase * (1 + (i % 3) * 0.4) + i * 0.9;
        const rad = 22 + (i * 6) % 110 + Math.sin(cosmosPhase * 2 + i) * 12;
        const x = cx + Math.cos(ang) * rad;
        const y = cy + Math.sin(ang) * rad;
        ctx.beginPath();
        ctx.arc(x, y, mode === 'foam' ? 4 : 7, 0, Math.PI * 2);
        ctx.fillStyle = i % 2 === 0 ? '#06b6d4' : '#f59e0b';
        ctx.shadowColor = ctx.fillStyle;
        ctx.shadowBlur = 12;
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    } else if (mode === 'atom' || mode === 'solar') {
      ctx.beginPath();
      ctx.arc(cx, cy, mode === 'solar' ? 22 : 12, 0, Math.PI * 2);
      ctx.fillStyle = '#f59e0b';
      ctx.shadowColor = '#f59e0b';
      ctx.shadowBlur = 25;
      ctx.fill();
      ctx.shadowBlur = 0;

      [52, 88, 126].forEach((r, idx) => {
        const ang = cosmosPhase * (1.5 - idx * 0.35) + idx * 2;
        const px = cx + Math.cos(ang) * r;
        const py = cy + Math.sin(ang) * (mode === 'atom' ? r * 0.55 : r);
        ctx.beginPath();
        ctx.arc(px, py, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#38bdf8';
        ctx.fill();
      });
    } else if (mode === 'dna') {
      for (let i = -110; i <= 110; i += 14) {
        const x1 = cx + Math.sin(cosmosPhase + i * 0.045) * 55;
        const x2 = cx - Math.sin(cosmosPhase + i * 0.045) * 55;
        const y = cy + i;
        ctx.beginPath();
        ctx.moveTo(x1, y);
        ctx.lineTo(x2, y);
        ctx.strokeStyle = 'rgba(99, 102, 241, 0.45)';
        ctx.stroke();

        ctx.beginPath(); ctx.arc(x1, y, 4.5, 0, Math.PI * 2); ctx.fillStyle = '#06b6d4'; ctx.fill();
        ctx.beginPath(); ctx.arc(x2, y, 4.5, 0, Math.PI * 2); ctx.fillStyle = '#f59e0b'; ctx.fill();
      }
    } else if (mode === 'galaxy' || mode === 'web') {
      for (let arm = 0; arm < 3; arm++) {
        for (let t = 0; t < 55; t++) {
          const r = t * 2.4;
          const ang = t * 0.16 + arm * ((Math.PI * 2) / 3) + cosmosPhase * 0.45;
          const x = cx + Math.cos(ang) * r;
          const y = cy + Math.sin(ang) * r;
          ctx.beginPath();
          ctx.arc(x, y, mode === 'web' ? 2.5 : 2, 0, Math.PI * 2);
          ctx.fillStyle = t < 12 ? '#fde68a' : '#38bdf8';
          ctx.fill();
        }
      }
    } else {
      // Fractal / Symmetric Mandala for Seed, Cell, Human, Earth
      const petals = mode === 'human' ? 12 : 8;
      for (let i = 0; i < petals; i++) {
        const ang = (i / petals) * Math.PI * 2 + cosmosPhase * 0.35;
        const x = cx + Math.cos(ang) * 48;
        const y = cy + Math.sin(ang) * 48;
        ctx.beginPath();
        ctx.arc(x, y, 42, 0, Math.PI * 2);
        ctx.strokeStyle = i % 2 === 0 ? 'rgba(245, 158, 11, 0.55)' : 'rgba(16, 185, 129, 0.55)';
        ctx.lineWidth = 1.6;
        ctx.stroke();
      }
      ctx.beginPath();
      ctx.arc(cx, cy, 16, 0, Math.PI * 2);
      ctx.fillStyle = '#10b981';
      ctx.fill();
    }
  }
  requestAnimationFrame(drawCosmosCanvas);
}

/* =========================================================
   REHBERLİ TEFEKKÜR YOLCULUKLARI (#paths)
   ========================================================= */
function renderPaths() {
  const done = getPathDone();
  const totalSteps = LEARNING_PATHS.reduce((acc, p) => acc + p.steps.length, 0);
  const doneCount = done.length;
  const pct = totalSteps > 0 ? Math.round((doneCount / totalSteps) * 100) : 0;

  document.getElementById('stat-progress').textContent = `%${pct}`;
  document.getElementById('paths-total-bar').style.width = `${pct}%`;
  document.getElementById('paths-progress-text').textContent = `${doneCount} / ${totalSteps} adım tamamlandı (%${pct})`;

  let rank = "Talib-i Hakikat (Başlangıç)";
  if (pct >= 90) rank = "🌌 Tılsım-ı Kâinat Kâşifi (Tam İhata)";
  else if (pct >= 55) rank = "✨ Ehl-i Tahkik & Mütefekkir";
  else if (pct >= 25) rank = "📖 Sâlik-i Hakikat";
  document.getElementById('paths-rank-title').textContent = `Keşif Mertebesi: ${rank}`;

  const grid = document.getElementById('paths-grid');
  grid.innerHTML = LEARNING_PATHS.map((p, pIdx) => {
    const pDone = p.steps.filter(s => done.includes(s.id)).length;
    return `
      <div class="path-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="doc-badge">${p.badge}</span>
          <span style="font-size:0.8rem; color:var(--emerald); font-weight:600;">${pDone} / ${p.steps.length}</span>
        </div>
        <h3 style="font-family:'Cinzel',serif; font-size:1.18rem;">${p.title}</h3>
        <p style="font-size:0.86rem; color:var(--text-muted);">${p.desc}</p>
        <div class="path-steps">
          ${p.steps.map((st, sIdx) => {
            const isDone = done.includes(st.id);
            return `
              <div class="path-step ${isDone ? 'done' : ''}">
                <div style="display:flex; align-items:center; gap:0.65rem; flex:1;">
                  <button class="step-check" onclick="togglePathStep('${st.id}')" title="Tamamlandı işaretle">${isDone ? '✓' : ''}</button>
                  <span style="font-size:0.86rem; cursor:pointer;" onclick="runPathStep(${pIdx}, ${sIdx})">${st.label}</span>
                </div>
                <button class="btn-mini" onclick="runPathStep(${pIdx}, ${sIdx})">Aç →</button>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }).join('');
}

function togglePathStep(stepId) {
  const done = getPathDone();
  const idx = done.indexOf(stepId);
  if (idx >= 0) done.splice(idx, 1);
  else {
    done.push(stepId);
    showToast('✓ Adım tamamlandı!');
  }
  savePathDone(done);
  renderPaths();
}

function runPathStep(pIdx, sIdx) {
  const st = LEARNING_PATHS[pIdx]?.steps[sIdx];
  if (st && typeof st.action === 'function') st.action();
}

function resetPathsProgress() {
  savePathDone([]);
  renderPaths();
  showToast('Yolculuk ilerlemesi sıfırlandı');
}

/* =========================================================
   TEFEKKÜR DEFTERİ (SLIDE-OVER NOTEBOOK)
   ========================================================= */
function toggleNotebook() {
  document.getElementById('notebook-backdrop').classList.toggle('open');
  document.getElementById('notebook-drawer').classList.toggle('open');
  renderNotes();
}

function openNotebookForCurrentDoc() {
  const doc = ALL_DOCS.find(d => d.id === activeDocId);
  if (doc) {
    document.getElementById('note-tag-input').value = doc.title;
  }
  toggleNotebook();
  document.getElementById('note-text-input').focus();
}

function addNote() {
  const tag = (document.getElementById('note-tag-input').value || 'Genel Tefekkür').trim();
  const text = (document.getElementById('note-text-input').value || '').trim();
  if (!text) {
    showToast('Lütfen önce bir not yazın.');
    return;
  }
  const notes = getNotes();
  notes.unshift({
    id: Date.now(),
    tag,
    text,
    date: new Date().toLocaleString('tr-TR', { dateStyle: 'short', timeStyle: 'short' })
  });
  saveNotes(notes);
  document.getElementById('note-text-input').value = '';
  renderNotes();
  showToast('📝 Not kaydedildi');
}

function deleteNote(id) {
  const notes = getNotes().filter(n => n.id !== id);
  saveNotes(notes);
  renderNotes();
}

function renderNotes() {
  const notes = getNotes();
  const badge = document.getElementById('notes-badge');
  if (notes.length > 0) {
    badge.style.display = 'grid';
    badge.textContent = notes.length;
  } else {
    badge.style.display = 'none';
  }

  const list = document.getElementById('notes-list');
  list.innerHTML = notes.map(n => `
    <div class="note-card">
      <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.75rem;">
        <span style="color:var(--gold); font-weight:700;">📌 ${n.tag}</span>
        <div style="display:flex; gap:0.5rem; align-items:center;">
          <span style="color:var(--text-muted);">${n.date}</span>
          <button class="btn-mini" style="padding:0.15rem 0.45rem;" onclick="deleteNote(${n.id})">Sil</button>
        </div>
      </div>
      <p style="font-size:0.86rem; color:var(--text-soft); white-space:pre-wrap;">${n.text}</p>
    </div>
  `).join('') || `<p style="font-size:0.85rem; color:var(--text-muted); text-align:center; padding:1.5rem 0;">Henüz kayıtlı tefekkür notunuz yok.</p>`;
}

function exportNotesMarkdown() {
  const notes = getNotes();
  if (notes.length === 0) {
    showToast('Dışa aktarılacak not bulunamadı.');
    return;
  }
  const md = `# 🌌 Tılsım-ı Kâinat — Kişisel Tefekkür Defteri\n\n` +
    notes.map(n => `## 📌 ${n.tag} (${n.date})\n\n${n.text}\n\n---`).join('\n\n');
  const blob = new Blob([md], { type: 'text/markdown;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'tilsim-i-kainat-tefekkur-defterim.md';
  a.click();
  showToast('📥 Notlarınız Markdown olarak indirildi');
}

/* =========================================================
   BİLİM MATRİSİ & CSV İNDİR
   ========================================================= */
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

function exportMatrixCSV() {
  const header = ['Risale-i Nur Kavramı', 'Kaynak Eser', 'Modern Bilim / Felsefe Karşılığı', 'Temel Sentez'];
  const rows = [header, ...SCIENCE_MATRIX].map(r => r.map(c => `"${c.replace(/"/g, '""')}"`).join(',')).join('\n');
  const blob = new Blob(['\uFEFF' + rows], { type: 'text/csv;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'tilsim-i-kainat-bilim-matrisi.csv';
  a.click();
}

/* =========================================================
   KÜLLİYAT KÜTÜPHANESİ + SESLİ OKUMA (TTS)
   ========================================================= */
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

function toggleArticleTTS() {
  if (!('speechSynthesis' in window)) {
    showToast('Tarayıcınız sesli okumayı desteklemiyor.');
    return;
  }
  const btn = document.getElementById('btn-tts');
  if (isSpeakingTTS) {
    window.speechSynthesis.cancel();
    isSpeakingTTS = false;
    btn.textContent = '🔊 Dinle';
    btn.classList.remove('active');
    return;
  }
  const text = document.getElementById('doc-content').innerText.slice(0, 6000);
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'tr-TR';
  utter.rate = 0.98;
  utter.onend = () => {
    isSpeakingTTS = false;
    btn.textContent = '🔊 Dinle';
    btn.classList.remove('active');
  };
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utter);
  isSpeakingTTS = true;
  btn.textContent = '⏹ Durdur';
  btn.classList.add('active');
  showToast('🔊 Sesli okuma başlatıldı');
}

async function selectDoc(docId) {
  if (isSpeakingTTS && 'speechSynthesis' in window) {
    window.speechSynthesis.cancel();
    isSpeakingTTS = false;
    const ttsBtn = document.getElementById('btn-tts');
    if (ttsBtn) { ttsBtn.textContent = '🔊 Dinle'; ttsBtn.classList.remove('active'); }
  }

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

  if (typeof renderMathInElement === 'function') {
    renderMathInElement(container, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false }
      ],
      throwOnError: false
    });
  }

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

/* =========================================================
   DİYAGRAM GALERİSİ & ZOOM MODAL
   ========================================================= */
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

/* =========================================================
   KAVRAMLAR SÖZLÜĞÜ & 3B FLASHCARD MODU
   ========================================================= */
function initGlossaryUI() {
  const letters = ["Tümü", ...new Set(ALL_GLOSSARY.map(g => g.letter))];
  const wrap = document.getElementById('glossary-letters');
  wrap.innerHTML = letters.map(l => `
    <button class="filter-pill ${l === activeGlossaryLetter ? 'active' : ''}" onclick="setGlossaryLetter('${l}')">${l}</button>
  `).join('');
  fcDeck = [...ALL_GLOSSARY];
  renderGlossary();
  renderFlashcard();
}

function setGlossaryMode(mode) {
  glossaryMode = mode;
  document.getElementById('glossary-list-view').style.display = mode === 'list' ? 'block' : 'none';
  document.getElementById('glossary-cards-view').style.display = mode === 'cards' ? 'block' : 'none';
  document.getElementById('btn-gloss-list').classList.toggle('active', mode === 'list');
  document.getElementById('btn-gloss-cards').classList.toggle('active', mode === 'cards');
  if (mode === 'cards') renderFlashcard();
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

function renderFlashcard() {
  if (fcDeck.length === 0) return;
  fcIdx = ((fcIdx % fcDeck.length) + fcDeck.length) % fcDeck.length;
  const card = fcDeck[fcIdx];
  document.getElementById('flashcard-box').classList.remove('flipped');
  document.getElementById('fc-letter').textContent = card.letter;
  document.getElementById('fc-term').textContent = card.term;
  document.getElementById('fc-term-back').textContent = card.term;
  document.getElementById('fc-def').textContent = card.definition;
  document.getElementById('fc-counter').textContent = `Kart ${fcIdx + 1} / ${fcDeck.length}`;
  document.getElementById('fc-known-count').textContent = getKnownCards().length;
}

function flipFlashcard() {
  document.getElementById('flashcard-box').classList.toggle('flipped');
}

function stepFlashcard(delta) {
  fcIdx += delta;
  renderFlashcard();
}

function shuffleFlashcards() {
  fcDeck = [...ALL_GLOSSARY].sort(() => Math.random() - 0.5);
  fcIdx = 0;
  renderFlashcard();
  showToast('🔀 Ezber kartları karıştırıldı');
}

function markFlashcardKnown() {
  if (fcDeck.length === 0) return;
  const card = fcDeck[fcIdx];
  const known = getKnownCards();
  if (!known.includes(card.term)) {
    known.push(card.term);
    saveKnownCards(known);
  }
  fcIdx++;
  renderFlashcard();
}

/* =========================================================
   20 SORULUK KATEGORİLİ BİLGİ & TEFEKKÜR TESTİ
   ========================================================= */
function initQuizUI() {
  const cats = ["Tümü", ...new Set(QUIZ_QUESTIONS.map(q => q.cat))];
  document.getElementById('quiz-cat-pills').innerHTML = cats.map(c => `
    <button class="filter-pill ${c === activeQuizCat ? 'active' : ''}" onclick="setQuizCategory('${c}')">${c}</button>
  `).join('');
  restartQuiz();
}

function setQuizCategory(cat) {
  activeQuizCat = cat;
  document.querySelectorAll('#quiz-cat-pills .filter-pill').forEach(p => {
    p.classList.toggle('active', p.textContent === cat);
  });
  restartQuiz();
}

function updateQuizHighScoreBadge() {
  const best = localStorage.getItem('tk_quiz_best_v3');
  document.getElementById('quiz-highscore-badge').textContent = best ? `En Yüksek Skor: ${best}` : 'En Yüksek Skor: —';
}

function renderQuiz() {
  const root = document.getElementById('quiz-root');
  if (quizIdx >= filteredQuiz.length) {
    const summaryStr = `${quizScore} / ${filteredQuiz.length} (${activeQuizCat})`;
    const prevBest = parseInt(localStorage.getItem('tk_quiz_best_num') || '0', 10);
    if (quizScore >= prevBest) {
      localStorage.setItem('tk_quiz_best_num', String(quizScore));
      localStorage.setItem('tk_quiz_best_v3', summaryStr);
    }
    updateQuizHighScoreBadge();

    const ratio = quizScore / filteredQuiz.length;
    let rank = "Sâlik (Yolculuk Başlangıcı)";
    if (ratio >= 0.9) rank = "🌌 Tılsım Kâşifi (Ehl-i Tahkik Zirvesi)";
    else if (ratio >= 0.7) rank = "✨ Mütefekkir (Mânâ-yı Harfî Nazarı)";
    else if (ratio >= 0.45) rank = "📖 Talib-i Hakikat";

    root.innerHTML = `
      <div style="text-align:center; padding:1rem 0;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">🏆</div>
        <h3 style="font-family:'Cinzel',serif; font-size:1.6rem; margin-bottom:0.5rem;">Test Tamamlandı!</h3>
        <p style="font-size:1.25rem; color:var(--cyan); font-weight:700; margin-bottom:0.5rem;">Skorunuz: ${quizScore} / ${filteredQuiz.length}</p>
        <p style="color:var(--gold); font-weight:600; margin-bottom:1.5rem;">Mertebe: ${rank}</p>
        <button class="btn-primary" onclick="restartQuiz()">↻ Testi Yeniden Çöz</button>
      </div>
    `;
    return;
  }

  const qObj = filteredQuiz[quizIdx];
  const pct = Math.round((quizIdx / filteredQuiz.length) * 100);
  root.innerHTML = `
    <div style="display:flex; justify-content:space-between; font-size:0.84rem; color:var(--text-muted);">
      <span>Soru ${quizIdx + 1} / ${filteredQuiz.length} · <em style="color:var(--gold);">${qObj.cat}</em></span>
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
  const qObj = filteredQuiz[quizIdx];
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
        ${quizIdx + 1 < filteredQuiz.length ? 'Sonraki Soru →' : 'Sonucu Gör 🏆'}
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
  filteredQuiz = activeQuizCat === "Tümü" ? [...QUIZ_QUESTIONS] : QUIZ_QUESTIONS.filter(q => q.cat === activeQuizCat);
  quizIdx = 0;
  quizScore = 0;
  quizAnswered = false;
  renderQuiz();
}

/* =========================================================
   EVRENSEL KOMUT PALETİ (CTRL+K)
   ========================================================= */
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

  if (!q || 'kavram ağı kozmik ölçek yolculuklar defter'.includes(q)) {
    items.push({ tag: 'Görünüm', title: '🕸️ İnteraktif Kavram & Hakikat Ağı', sub: 'Düğümleri sürükleyerek ontolojik bağlantıları keşfedin', action: () => navigateTo('graph') });
    items.push({ tag: 'Görünüm', title: '🔭 61 Mertebe Kozmik Ölçek Gezgini', sub: 'Planck (10^-35 m) → Gözlemlenebilir Evren (10^26 m)', action: () => navigateTo('cosmos') });
    items.push({ tag: 'Görünüm', title: '🧭 Rehberli Tefekkür Yolculukları', sub: '4 müfredat ve kişisel ilerleme takibi', action: () => navigateTo('paths') });
  }

  MODELS_CATALOG.forEach(m => {
    if (!q || m.title.toLowerCase().includes(q) || m.desc.toLowerCase().includes(q) || m.src.toLowerCase().includes(q)) {
      items.push({ tag: 'Model', title: `${m.num}. ${m.title}`, sub: m.src, action: () => openLabTab(m.tab) });
    }
    if (q && ('python'.includes(q) || m.title.toLowerCase().includes(q))) {
      items.push({ tag: 'Python', title: `🐍 ${m.title} — Kaynak Kodu`, sub: 'Python standart kütüphane simülasyon kodunu incele', action: () => openPythonCodeModal(m.tab) });
    }
  });

  COSMOS_SCALES.forEach((cs, idx) => {
    if (q && (cs.title.toLowerCase().includes(q) || cs.esma.toLowerCase().includes(q) || cs.scale.toLowerCase().includes(q))) {
      items.push({ tag: 'Ölçek', title: `🔭 ${cs.scale} — ${cs.title}`, sub: cs.esma, action: () => { navigateTo('cosmos'); updateCosmosScale(idx); } });
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
      items.push({ tag: 'Sözlük', title: g.term, sub: g.definition.slice(0, 90) + '…', action: () => { navigateTo('glossary'); setGlossaryMode('list'); document.getElementById('glossary-search').value = g.term; activeGlossaryLetter = 'Tümü'; renderGlossary(); } });
    }
  });

  currentCmdItems = items.slice(0, 16);
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
      closeCodeModal();
      return;
    }
    if (e.code === 'Space' && document.getElementById('view-glossary').classList.contains('active') && glossaryMode === 'cards' && document.activeElement.tagName !== 'INPUT') {
      e.preventDefault();
      flipFlashcard();
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

  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }

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
  initCosmosExplorer();
  renderPaths();
  renderNotes();
  updateQuizHighScoreBadge();
  initQuizUI();

  try {
    const [stats, docs, diagrams, glossary, simulations] = await Promise.all([
      fetch('data/stats.json').then(r => r.json()),
      fetch('data/docs.json').then(r => r.json()),
      fetch('data/diagrams.json').then(r => r.json()),
      fetch('data/glossary.json').then(r => r.json()),
      fetch('data/simulations.json').then(r => r.json())
    ]);

    ALL_DOCS = docs;
    ALL_DIAGRAMS = diagrams;
    ALL_GLOSSARY = glossary;
    ALL_SIMULATIONS = simulations;

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
  if (VALID_VIEWS.includes(hash)) {
    navigateTo(hash);
  }
}

window.addEventListener('DOMContentLoaded', bootstrap);
