# 🧪 Simülasyonlar (Deneysel)

> [!CAUTION]
> Bu simülasyonlar **sembolik tefekkür araçlarıdır**. Manevî hakikatler sayılarla ölçülemez;
> parametreler, kavramlar arasındaki ilişkileri (artırıcı/azaltıcı etkiler, eşikler, geri besleme
> döngüleri) görünür kılmak için kullanılan metaforlardır.

## `ene-thickening-model.py` — Ene Kalınlaşma Modeli

30. Söz'deki *"Ene zâtında hava gibi şeffaftır; gaflet, inkâr ve isyanla kalınlaşır, sahibini yutar"*
sürecini iki değişkenli bir dinamik sistem olarak modeller.

### Değişkenler

| Sembol | Anlam | Aralık |
|--------|-------|--------|
| `K` | **Kalınlık** (kesafet): 0 = hava gibi şeffaf, 1 = taş gibi katı | [0, 1] |
| `S = 1 − K` | **Şeffafiyet**: marifet nurunun geçirgenliği | [0, 1] |
| `H` | **Harfî nazar** oranı: eşyaya mana-yı harfî ile bakma meyli | [0, 1] |

### Parametreler

| Tekâsüf (kalınlaştırıcı) | Tasfiye (inceltici) |
|---|---|
| `--gaflet` | `--tefekkur` (esbabperest nazarla zayıflar) |
| `--inkar` (esbabperestlik) | `--sukur` |
| `--isyan` | `--dua` |
| `--malikiyet` (temellük vehmi) | `--ihlas` |

### Denklemler

$$
\begin{aligned}
\text{tekâsüf} &= \tfrac{1}{4}(\text{gaflet} + \text{inkâr} + \text{isyan} + \text{malikiyet}) \\
\text{tasfiye} &= \tfrac{1}{4}\big(\text{tefekkür}\cdot(1-\text{inkâr}) + \text{şükür} + \text{dua} + \text{ihlas}\big) \\
\frac{dK}{dt} &= a\cdot\text{tekâsüf}\cdot(1 - H + e)(K + e)(1 - K) \;-\; b\cdot\text{tasfiye}\cdot H\cdot K \\
\frac{dH}{dt} &= c\cdot\text{tasfiye}\cdot(1 - H) \;-\; d\cdot\text{tekâsüf}\cdot K\cdot H
\end{aligned}
$$

- **Pozitif geri besleme:** `K` arttıkça `H` düşer, `H` düştükçe `K`'nin artışı hızlanır → *"sahibini yutma"*.
- **Esbabperest tefekkür:** `tefekkur × (1 − inkar)` — akıl keskin olsa da harfî nazar olmadan inceltmez.
- **`e` (vehmî çizgi):** En şeffaf enede bile farazî hat tamamen kaybolmaz.

### Hazır Senaryolar

| Senaryo | Açıklama | Beklenen Netice |
|---------|----------|-----------------|
| `fitrat` | Dengeli hâl | Şeffaf |
| `firavun` | Gaflet, inkâr, isyan, temellük zirvede | Hızlı yutulma |
| `gafil` | Derin gaflet, düşük tasfiye | Yavaş yutulma |
| `tevbe` | Kalınlaşmış ene + güçlü tasfiye | Şeffaflaşma |
| `salik` | Yüksek tefekkür, şükür, dua, ihlas | Şeffaf kalır |
| `filozof` | Yüksek tefekkür ama esbabperest nazar | Yutulma |

### Kullanım

```bash
python simulations/ene-thickening-model.py --listele
python simulations/ene-thickening-model.py --senaryo firavun
python simulations/ene-thickening-model.py --karsilastir
python simulations/ene-thickening-model.py --senaryo gafil --dua 0.9 --sukur 0.9
python simulations/ene-thickening-model.py --senaryo tevbe --csv tevbe.csv
python simulations/ene-thickening-model.py --karsilastir --kaydet karsilastirma.png   # matplotlib gerekir
```

Yalnızca Python ≥ 3.8 standart kütüphanesi gerekir. `--grafik` / `--kaydet` için opsiyonel olarak
`pip install matplotlib`.

### Örnek Çıktı

```text
Senaryo     Tekâsüf  Tasfiye  Nihai K  Yutulma t  Mertebe
------------------------------------------------------------------------
fitrat         0.38     0.37    0.000          —  Hava gibi şeffaf
firavun        0.91     0.01    1.000       5.10  Yutulma
gafil          0.54     0.16    0.925      20.60  Yutulma
tevbe          0.15     0.80    0.000          —  Hava gibi şeffaf
salik          0.06     0.90    0.000          —  Hava gibi şeffaf
filozof        0.59     0.11    0.970      11.85  Yutulma
```

### Testler

```bash
python -m unittest discover -s simulations -p "test_*.py" -v
```
