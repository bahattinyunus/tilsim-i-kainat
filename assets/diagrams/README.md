# 🗺️ Diyagramlar

Bu klasördeki şemalar [Mermaid](https://mermaid.js.org/) formatındadır; GitHub bunları doğrudan
görselleştirir. Ham `.mmd` dosyaları [Mermaid Live Editor](https://mermaid.live) ile düzenlenebilir
veya `mmdc` (mermaid-cli) ile SVG/PNG'ye dönüştürülebilir:

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i ene-hal-degisimi.mmd -o ene-hal-degisimi.svg
```

| Dosya | İçerik |
|-------|--------|
| [`ene-hal-degisimi.mmd`](ene-hal-degisimi.mmd) | Ene'nin şeffaflıktan yutulmaya hâl değişimleri |
| [`geri-besleme-dongusu.mmd`](geri-besleme-dongusu.mmd) | Kalınlaşmanın kendini besleyen döngüsü ve kırılma noktası |
| [`tilsim-haritasi.mmd`](tilsim-haritasi.mmd) | Projenin tüm kavramlarını bağlayan üst harita |

---

## Ene'nin Hâl Değişimi

```mermaid
stateDiagram-v2
    direction LR
    Hava: Hava gibi şeffaf
    Bulut: Bulutlanma
    Su: Su gibi akışkan
    Toprak: Toprak gibi kesif
    Tas: Taş gibi katı
    Yutulma: Yutulma
    [*] --> Hava: Fıtrat
    Hava --> Bulut: Gaflet
    Bulut --> Su: Malikiyet vehmi
    Su --> Toprak: Esbabperestlik
    Toprak --> Tas: İnkâr ve isyan
    Tas --> Yutulma: Kendine tapma
    Bulut --> Hava: Tefekkür
    Su --> Hava: Şükür
    Toprak --> Hava: Tevbe ve dua
    Tas --> Hava: Tevbe ve dua
```

## Geri Besleme Döngüsü

```mermaid
flowchart LR
    A["Mana-yı ismî nazar"] --> B["Malikiyet vehmi"]
    B --> C["Ene kalınlaşır"]
    C --> D["Nur geçmez"]
    D --> A
    V["Vahiy / Nübüvvet nuru"] -->|"Döngüyü kırar"| A
    V --> T["Tefekkür, şükür, dua, ihlas"]
    T -->|"İnceltir"| C
```

## Tılsım Haritası

```mermaid
flowchart TD
    T(("Tılsım-ı Kâinat"))
    T --> ENE["Ene<br/>(iç tılsım)"]
    T --> ZERRE["Zerre<br/>(dış tılsım)"]
    ENE --> VK["Vâhid-i Kıyasî"]
    ENE --> KAL["Kalınlaşma"]
    ENE --> NAH["Nahnu / İhlas"]
    ZERRE --> TAH["Tahavvülât"]
    ZERRE --> SAH["Acz ve Cümûd"]
    VK --> HARF["Mana-yı Harfî"]
    TAH --> HARF
    KAL --> ISM["Mana-yı İsmî"]
    HARF --> NUB["Nübüvvet"]
    ISM --> FEL["Felsefe"]
    NUB --> MAR["Marifetullah"]
    MAR --> TAA["Taallüm ve Dua"]
    TAA --> HIZ["Sahil-i Selamet Hizmeti"]
```
