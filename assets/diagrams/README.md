# 🗺️ Diyagramlar

Bu klasördeki şemalar [Mermaid](https://mermaid.js.org/) formatındadır; GitHub bunları doğrudan
görselleştirir. Ham `.mmd` dosyaları [Mermaid Live Editor](https://mermaid.live) ile düzenlenebilir
veya `mmdc` (mermaid-cli) ile SVG/PNG'ye dönüştürülebilir:

```bash
npx -p @mermaid-js/mermaid-cli mmdc -i ene-hal-degisimi.mmd -o ene-hal-degisimi.svg
```

| Dosya | Başlık | Eksen Risale & İçerik |
|-------|--------|-----------------------|
| [`tilsim-haritasi.mmd`](tilsim-haritasi.mmd) | Tılsım Haritası | Projenin tüm kavramlarını bağlayan üst sistem haritası |
| [`ene-hal-degisimi.mmd`](ene-hal-degisimi.mmd) | Ene Hâl Değişimi | 30. Söz: Ene'nin şeffaflıktan (hava) yutulmaya (taş) 5 fazı |
| [`geri-besleme-dongusu.mmd`](geri-besleme-dongusu.mmd) | Geri Besleme Döngüsü | Kalınlaşmanın pozitif döngüsü ve nübüvvetle kırılışı |
| [`kainat-sarayi-uc-sual.mmd`](kainat-sarayi-uc-sual.mmd) | Kâinat Sarayı ve 3 Sual | 11. Söz: Necisin? Nereden? Nereye? (Felsefe vs. Kur'an) |
| [`tabiat-risalesi-muhaller.mmd`](tabiat-risalesi-muhaller.mmd) | Tabiat Risalesi Muhalleri | 23. Lem'a: 4 ihtimal, 3 bâtıl yolun muhalleri ve tevhid |
| [`zerre-seyahati-mertebeler.mmd`](zerre-seyahati-mertebeler.mmd) | Zerre Seyahati ve Mertebeler | 30. Söz: Bismillah'tan Elhamdülillah'a kemâlât basamakları |
| [`ihlas-sinerjisi.mmd`](ihlas-sinerjisi.mmd) | İhlas Sinerjisi ve Şahs-ı Manevî | 21. Lem'a: 4 ferdin 4444 kuvvetine çıkması ve kevser havuzu |

---

## 1. Kâinat Sarayı ve Üç Büyük Sual

```mermaid
flowchart TD
    KS["🏛️ KÂİNAT SARAYI"]
    
    subgraph Sorular["İnsanın Yüz Yüze Olduğu Üç Dehşetli Sual"]
        Q1["1. Necisin?"]
        Q2["2. Nereden geliyorsun?"]
        Q3["3. Nereye gidiyorsun?"]
    end
    
    KS --> Sorular
    
    subgraph FelsefeYolu["Felsefenin Karanlık Çıkmazı (Mânâ-yı İsmî)"]
        Q1 -.-> F1["Tesadüf oyuncağı, âciz et-kemik"]
        Q2 -.-> F2["Karanlık ademden / kör maddeden"]
        Q3 -.-> F3["Ebedî yokluğa ve çürümeye"]
        F1 & F2 & F3 --> FN["Netice: Mutlak Yeis ve Dehşet"]
    end
    
    subgraph Kur'anYolu["Kur'ân'ın Müşkilküşâ Cevabı (Mânâ-yı Harfî)"]
        Q1 ==> K1["Sultan-ı Ezelî'nin nazenin memuru ve âyinesi"]
        Q2 ==> K2["Rahmet ve Kudret hazinesinden"]
        Q3 ==> K3["Dâr-ı Saadet-i Ebediyeye ve Cemâlullah'a"]
        K1 & K2 & K3 --> KN["Netice: Ünsiyet, Küllî Şükür ve Ubudiyet"]
    end
```

---

## 2. Tabiat Risalesi Muhalleri ve Tevhid Kolaylığı

```mermaid
flowchart TD
    M["Mevcudatın Vücuda Gelmesindeki Dört Yol"]
    
    M --> Y1["1. Evcedethü'l-Esbâb<br/>(Sebepler yaptı)"]
    M --> Y2["2. Teşekkele Binefsihî<br/>(Kendi kendine oldu)"]
    M --> Y3["3. İktezathü't-Tabiat<br/>(Tabiat iktiza etti)"]
    M --> Y4["4. Tevhid & Vahdaniyet<br/>(Kādir-i Mutlak yarattı)"]
    
    Y1 --> M1["Muhal: Eczahane misali;<br/>câmid sebepler hayat ve şuur veremez"]
    Y2 --> M2["Muhal: Zerreler adedince ilâh gerekir;<br/>her zerre kâinatı bilmelidir"]
    Y3 --> M3["Muhal: Tabiat bir sanattır sâni' olamaz;<br/>kanundur kādir olamaz"]
    
    M1 & M2 & M3 --> BTL["❌ AKIL VE İLİM DIŞI SAFSATA"]
    
    Y4 ==> TRU["✅ SÜHULET-İ MUTLAKA<br/>Kâinatı yaratmak bir ağacı yaratmak kadar kolay"]
```

---

## 3. Zerre Seyahati: Kemâlât Basamakları

```mermaid
flowchart LR
    subgraph Mebde["MEBDE-İ HAREKET"]
        Z0["Havadaki Zerre<br/>Lisan-ı Hâl: 'BİSMİLLÂH'"]
    end
    
    subgraph Mertebeler["KEMÂLÂT BASAMAKLARI"]
        Z1["Toprak ve Suya İntikal<br/>(Hizmet Dairesi)"]
        Z2["Bitkiye / Rızka Giriş<br/>(Hayat Mertebesi)"]
        Z3["Canlı Cismine / Hücreye Sevk<br/>(Nizam-ı Umumî)"]
        Z4["Tevfik'in Gözbebeği / Dimağı<br/>(Şuur ve Marifet Aynası)"]
    end
    
    subgraph Hitam["HİTÂM-I VAZİFE"]
        ZF["Ukûlü Hayrette Bırakan Sanat:<br/>Lisan-ı Hâl: 'ELHAMDÜLİLLÂH'"]
    end
    
    Z0 --> Z1 --> Z2 --> Z3 --> Z4 --> ZF
```

---

## 4. İhlas Sinerjisi ve Şahs-ı Manevî

```mermaid
flowchart TD
    subgraph Ayrı["ENANİYET VE İTTİHADSIZLIK"]
        F1["Fert 1 (Değer: 1)"]
        F2["Fert 2 (Değer: 1)"]
        F3["Fert 3 (Değer: 1)"]
        F4["Fert 4 (Değer: 1)"]
        F1 & F2 & F3 & F4 --> Toplam["Adî Toplam: 1 + 1 + 1 + 1 = 4<br/>(Buzlar erimemiş, benlikler çatışıyor)"]
    end
    
    subgraph Sırr["SIRR-I İHLAS VE İTTİHAD (21. LEM'A)"]
        H1["1"] --- H2["1"] --- H3["1"] --- H4["1"]
        H1 & H2 & H3 & H4 ==> Sinerji["Sırr-ı Adediyet: 4444 Kuvvet-i Maneviyesi!<br/>Kevser Havuzunda Eriyen Buzlar,<br/>Birbirinin Faziletiyle İftihar Eden Ruhlar"]
    end
```
