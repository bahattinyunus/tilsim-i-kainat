# 🧪 Tılsım-ı Kâinat Simülasyon Laboratuvarı

> [!CAUTION]
> Bu simülasyonlar **sembolik tefekkür araçlarıdır**. Manevî hakikatler maddî sayılarla ölçülemez;
> parametreler, kavramlar arasındaki dinamik ilişkileri (artırıcı/azaltıcı etkiler, eşikler, geri besleme
> döngüleri, sinerji kanunları) zihne yaklaştırmak için kullanılan modelleme metaforlarıdır.

Laboratuvar bünyesinde dört tamamlayıcı simülasyon motoru yer almaktadır:

1. **`ene-thickening-model.py`** — Ene Kalınlaşma ve Faz Değişimi Modeli (30. Söz, 1. Maksad)
2. **`zerre-simulation.py`** — Tahavvülât-ı Zerrât ve Kudret Kalemi Dinamikleri (30. Söz, 2. Maksad)
3. **`ihlas-synergy-model.py`** — İhlas ve Şahs-ı Manevî Sinerji Modeli (21. Lem'a)
4. **`entropy-information-model.py`** — Kozmik Entropi vs. Negentropik Kudret İntizamı (30. Söz & Wheeler: "It from Bit")

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
* **Toplam: 26 test (Tam Başarı)**
