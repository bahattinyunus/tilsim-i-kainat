# 🧪 Tılsım-ı Kâinat Simülasyon Laboratuvarı

> [!CAUTION]
> Bu simülasyonlar **sembolik tefekkür araçlarıdır**. Manevî hakikatler maddî sayılarla ölçülemez;
> parametreler, kavramlar arasındaki dinamik ilişkileri (artırıcı/azaltıcı etkiler, eşikler, geri besleme
> döngüleri, sinerji kanunları) zihne yaklaştırmak için kullanılan modelleme metaforlarıdır.

Laboratuvar bünyesinde dokuz tamamlayıcı simülasyon motoru ve bir interaktif web arayüzü yer almaktadır:

1. **`ene-thickening-model.py`** — Ene Kalınlaşma ve Faz Değişimi Modeli (30. Söz, 1. Maksad)
2. **`zerre-simulation.py`** — Tahavvülât-ı Zerrât ve Kudret Kalemi Dinamikleri (30. Söz, 2. Maksad)
3. **`ihlas-synergy-model.py`** — İhlas ve Şahs-ı Manevî Sinerji Modeli (21. Lem'a)
4. **`entropy-information-model.py`** — Kozmik Entropi vs. Negentropik Kudret İntizamı (30. Söz & Wheeler: "It from Bit")
5. **`teleportation-information-model.py`** — Tayy-ı Mekân ve Kuantum Işınlanma Modeli (20. Söz, Belkıs'ın Tahtı)
6. **`kader-irade-matrix-model.py`** — Kader, İrade ve Levh-i Mahfuz Karar Matrisi (26. Söz & Nisa 79)
7. **`hasir-ebediyet-model.py`** — Haşir, Bahar İhyası ve Bilgi Korunumu Modeli (10. Söz & Unitarity)
8. **`hayat-suur-model.py`** — Hayat, Şuur ve Bütünleşik Bilgi Modeli (29. Söz, 30. Lem'a & Tononi IIT $\Phi$)
9. **`mirac-relativity-model.py`** — Mirac, Görelilik ve Tayy-ı Zaman Modeli (31. Söz & Özel Görelilik)
10. **`dashboard/index.html`** — 9 Modelin tamamını görselleştiren İnteraktif Web Laboratuvarı (Chart.js SPA)

Tüm modelleri tek bir komutla icra etmek için:
```bash
python simulations/run_all.py
```

---

## 1. `ene-thickening-model.py` — Ene Kalınlaşma Modeli

30. Söz'deki *"Ene zâtında hava gibi şeffaftır; gaflet, inkâr ve isyanla kalınlaşır, sahibini yutar"*
sürecini diferansiyel sistemle modeller.

### Durum Değişkenleri
| Sembol | Anlamı | Değer Aralığı |
|:---:|:---|:---:|
| **K** | **Kalınlık (Kesafet):** 0 = hava gibi şeffaf, 1 = taş gibi katı | [0, 1] |
| **S** | **Şeffafiyet (1 - K):** Marifet nurunun geçirgenliği | [0, 1] |
| **H** | **Harfî Nazar Oranı:** Eşyaya Sâni' hesabına bakma meyli | [0, 1] |

### Diferansiyel Denklemler
$$
\begin{aligned}
\text{tekâsüf} &= \tfrac{1}{4}(\text{gaflet} + \text{inkâr} + \text{isyan} + \text{malikiyet}) \\
\text{tasfiye} &= \tfrac{1}{4}\big(\text{tefekkür}\cdot(1-\text{inkâr}) + \text{şükür} + \text{dua} + \text{ihlas}\big) \\
\frac{dK}{dt} &= a\cdot\text{tekâsüf}\cdot(1 - H + e)(K + e)(1 - K) \;-\; b\cdot\text{tasfiye}\cdot H\cdot K \\
\frac{dH}{dt} &= c\cdot\text{tasfiye}\cdot(1 - H) \;-\; d\cdot\text{tekâsüf}\cdot K\cdot H
\end{aligned}
$$

* **Pozitif Geri Besleme:** `K` arttıkça `H` düşer, `H` düştükçe `K`'nin artışı hızlanır (Sahibini yutma).
* **Esbabperest Tefekkür:** `tefekkur * (1 - inkar)`: Felsefenin akıl yürütmesi eşyaya sebepler hesabına baktıkça tasfiye sağlamaz.
* **`e` (Vehmî Çizgi):** En şeffaf halinde dahi ene farazî bir hat olarak kıyas için baki kalır.

---

## 2. `zerre-simulation.py` — Tahavvülât-ı Zerrât Simülasyonu

30. Söz'ün İkinci Maksadında anlatılan, zerrelerin mebdeden hitâma seyahatindeki iki sadık şahidini modeller:

* **1. Vücud Şehadeti (Acz ve Cümûd):** Zerre sonsuz derecede câmid (şuursuz) ve âciz olduğu halde, Bismillah sırrıyla boyundan binlerce kat büyük vazifeleri sırtlar.
* **2. Vahdet Şehadeti (Nizam-ı Umumiye Tevfik):** Zerre topraktan bitkiye, kandan dimağa ve Tevfik'in gözbebeğine kadar her girdiği yerde oranın nizamına tam mutabık yerleşir. *"Zerre kimin ise, gezdiği bütün kâinat da Onundur."*

### Hazır Senaryolar
| Senaryo | Tahlil Edilen Hadise | Netice |
|:---|:---|:---|
| `tevfikin_gozu` | Gözbebeğindeki zerrenin damar ve sinirlerle mükemmel intizamı | Kudret İntizamı & Elhamdülillah |
| `nebat_ruku` | Çekirdekteki zerrenin koca çam ağacını omuzlaması | Yüksek Yük & Vücud Şehadeti |
| `dimag_tefekkur` | İnsan beyninde marifet ve şuur aynası olan zerrenin vazifesi | Azamî Hikmet Skoru |
| `camid_madde` | Toprakta henüz canlanmamış zerre | Gizli İstidad |
| `tesaduf_cikmazi` | Materyalist varsayım (Kör sebepler ve tesadüf) | Kaos, Çöküş & Nizam Kaybı |

```bash
python simulations/zerre-simulation.py --senaryo tevfikin_gozu
python simulations/zerre-simulation.py --karsilastir
```

---

## 3. `ihlas-synergy-model.py` — İhlas ve Şahs-ı Manevî Modeli

21. Lem'a (İhlas Risalesi) ekseninde, bireysel enaniyet buzlarının kevser havuzunda erimesi ve 4 ferdin 4444 kuvvetine ulaşması dinamiğidir:

$$\frac{dB}{dt} = - k_{\text{erime}} \cdot I \cdot T \cdot B + k_{\text{donma}} \cdot R \cdot (1 - B)$$

$$K_{\text{manevi}} = N + (K_{\text{tavan}} - N) \cdot \big[ I \cdot T \cdot (1 - B) \cdot (1 - R) \big]$$

* **$N=3$ Fert:** Sırr-ı adediyet ile yan yana gelince $111$ kıymeti alır.
* **$N=4$ Fert:** Sırr-ı uhuvvet ve ittihad-ı maksat ile $4444$ kuvvetine baliğ olur.
* **Rekabet ve Haset ($R$):** Devreye girdiğinde enaniyet buzlaşır; kuvvet sıradan adî toplamın dahi altına düşer.

```bash
python simulations/ihlas-synergy-model.py --senaryo dort_elif
python simulations/ihlas-synergy-model.py --karsilastir
```

---

## 4. `entropy-information-model.py` — Kozmik Entropi vs. Negentropik Kudret İntizamı

Termodinamiğin 2. kanunu (Entropi artışı / $\Delta S \ge 0$) ile canlılığın negentropik intizamı (Wheeler: "It from Bit") arasındaki metafizik ve fiziksel ilişkiyi modeller:

$$\frac{d(\text{İntizam})}{dt} = 1.5 \cdot \text{Kudret} \cdot \text{Hayat} \cdot (1 - \text{İntizam}) - 1.2 \cdot \text{Kaos} \cdot \text{İntizam}$$

Shannon bilgi yoğunluğu ile genetik kod ve göz gibi organlardaki tekvînî kelimelerin bit derinliği simüle edilir.

```bash
python simulations/entropy-information-model.py --senaryo canlilik_ve_dna
python simulations/entropy-information-model.py --karsilastir
```

---

## 5. `teleportation-information-model.py` — Tayy-ı Mekân ve Kuantum Işınlanma Modeli

20. Söz'ün (Mucizât-ı Enbiya — Neml 40 / Belkıs'ın Tahtı), Wheeler'ın *"It from Bit"* teorisinin, Bekenstein sınırının ve Alcubierre uzay-zaman metrik bükülmesinin analitik modelidir:

* **Bekenstein Bilgi Sınırı:** $I \le \frac{2\pi R E}{\hbar c \ln 2}$
* **Landauer Enerji Maliyeti:** $E_{\text{silme}} = k_B T \ln(2) \cdot I_{\text{bit}}$
* **Üç Nakil Paradigması Mukayesesi:**
  1. *Klasik Kütlesel Nakil:* Mekanik balistik intikal (saatler sürer, kesif sürtünme).
  2. *Kuantum Rekonstrüksiyon (It from Bit):* Maddenin dalga/enformasyon koduna ayrışıp ışık hızında nakli ve hedefte tekvînî inşası.
  3. *Tayy-ı Mekân & Nuraniyet Sürüşü:* Letafet fazında kütlesel eylemsizliğin sıfırlanması ve uzay-zaman katlanması ile *tarfetü'l-ayn* (< 0.1 saniye) mertebesinde nakil.

```bash
python simulations/teleportation-information-model.py --mesafe 2500 --kutle 500
```

---

## 6. `kader-irade-matrix-model.py` — Kader, İrade ve Levh-i Mahfuz Karar Matrisi

26. Söz'ün (Kader Risalesi), Nisa Sûresi 79. Âyetin ve modern karar teorisinin analitik sentezidir:

* **1-Bitlik İrade (Kesb):** $E \approx 0$ enerjili yönlendirici anahtar.
* **Kudret Halkı:** Kesbin kanalıyla yaratılan sonsuz ilâhî fiil enerjisi ($E = f(Kudret, I)$).
* **Levh-i Mahv ve İspat Kalkanı:** Dua ve sadakanın şartlı kazadaki koruyucu tebdil katsayısı.
* **Hakikat Terazisi (İstikamet İndisi):** Hasenatı kadere verip şükretme ($\alpha$), seyyiatı nefse isnad edip tövbe etme ($\beta$) dengesi. Kibir ve Yeis uçurumlarından korunma metriği.

```bash
python simulations/kader-irade-matrix-model.py --senaryo istikamet_ehli
python simulations/kader-irade-matrix-model.py --karsilastir
```

---

## 7. `hasir-ebediyet-model.py` — Haşir, Bahar İhyası ve Bilgi Korunumu

10. Söz (Haşir Risalesi) ve modern kuantum bilgi korunumu (*Unitarity*) ilkelerinin sentezidir:

* **İbdâ vs. İade:** Yoktan var etmeye göre dağılmış zerreleri tek bir "Kün / Sur" emriyle toplamanın 100x+ kolaylığı.
* **Levh-i Mahfuz Enformasyon Korunumu:** Madde dağılsa da ruh ve amel bilgisi kaybolmaz.
* **Adalet ve Hikmet İndisi:** Haşirsiz bir kâinatın abesiyet ve zulme dönüşmesinin matematiksel gösterimi.

```bash
python simulations/hasir-ebediyet-model.py --senaryo hasir_i_ecsad
python simulations/hasir-ebediyet-model.py --karsilastir
```

---

## 🌐 İnteraktif Web Laboratuvarı (`dashboard/index.html`)

Kurulum gerektirmeyen, tarayıcıda doğrudan (`file:///` veya yerel sunucu) çalışan modern, Chart.js tabanlı, minimalist karanlık tema (dark mode) SPA arayüzü:

* **7 Simülasyonun Dinamik Kontrolleri:** Slider'lar üzerinden parametreleri canlı değiştirme.
* **Anlık Reaktif Grafikler:** Ene faz geçiş çizgisi, Zerre şahitlik radarı, Şahs-ı manevî kuvvet çubukları, Entropi/Negentropi eğrileri, Nakil süreleri logaritmik barı ve İstikamet mizanı çemberi.
* **Hazır Senaryo Butonları:** Tek tıkla Fıtrat, Firavun, 4444 Sırrı, Tayy-ı Mekân, İstikamet Ehli senaryolarını yükleme.

Tarayıcıda açmak için:
```bash
# Doğrudan çift tıklayarak veya PowerShell ile:
Start-Process dashboard/index.html
```

---

## 🧪 Birim Testleri (Unit Tests)

Laboratuvardaki tüm modeller otomatik unit testlerle denetlenir:

```bash
python -m unittest discover -s simulations -p "test_*.py" -v
```

Mevcut test paketi:
* `test_ene_model.py` (9 test)
* `test_zerre_model.py` (6 test)
* `test_ihlas_model.py` (6 test)
* `test_entropy_model.py` (5 test)
* `test_teleportation_model.py` (7 test)
* `test_kader_model.py` (7 test)
* `test_hasir_model.py` (6 test)
* `test_hayat_model.py` (7 test)
* `test_mirac_model.py` (6 test)
* **Toplam: 59 test (Tam Başarı)**
