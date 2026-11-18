"""
🕊️ TILSIM-I KÂİNAT: HAYAT, ŞUUR VE BÜTÜNLEŞİK BİLGİ (IIT Φ) MODELİ
=====================================================================
Kaynak Eserler:
  - 29. Söz (Ruh Risalesi & Vücud-u Haricî Giymiş Kanun-u Emrî)
  - 30. Lem'a (Beşinci Nükte - İsm-i Hayy & Kesrette Vahdet Sırrı)
  - 30. Söz (Ene ve Zerre Risalesi)

Modern Bilim & Felsefe Paralelleri:
  - Giulio Tononi: Integrated Information Theory (IIT & Φ - Phi Metriği)
  - Erwin Schrödinger: Negentropi (What is Life? & Negentropy Pumping)
  - Roger Penrose & Stuart Hameroff: Orch-OR (Kuantum Mikrotübül Bilinci)
  - David Chalmers: Hard Problem of Consciousness & Felsefî Zombi Problemi

Temel Teorem:
  1. Hayat kesrette vahdet rabıtasıdır; koca kâinatın dağınık zerrelerini
     tek bir canlının bünyesinde bir araya toplayıp 'biri' 'hepsi' ile irtibatlandırır.
  2. Ruh, âlem-i emirden gelen zîhayat, zîşuur, nuranî, vücud-u haricî giydirilmiş
     basit (terkipsiz) bir kanun-u emrîdir. Terkipsiz olduğu için parçalanmaz,
     çürümez ve ebediyete namzettir.
  3. Yalnızca mantık kapıları ve algoritmik hesaplama yapan mekanik sistemler
     (veya feedforward yapay zekâ ağları) bağımsız parçalara indirgenebildiği için
     bütünleşik bilgi üretmez (Φ ≈ 0, felsefî zombi). Ruh ise indirgenemez bir
     vahdet tecellisidir (Φ >> 0).
"""

from dataclasses import dataclass
import math
from typing import Dict, List, Optional


@dataclass
class HayatParametreleri:
    """Hayat ve şuur simülasyonu girdi parametreleri."""
    zerre_sayisi: int            # Canlının bünyesindeki zerre/hücre sayısı (N >= 1)
    vahdet_rabitasi: float       # Kesrette vahdet kuvveti [0.0 - 1.0] (İsm-i Hayy tecellisi)
    alem_i_emir_irtibati: float  # Vücud-u haricî giyme ve emrî kanun kuvveti [0.0 - 1.0]
    suur_derecesi: float         # İdrak ve şuur seviyesi [0.0 - 1.0] (0: camid, 0.05: nebat, 0.5: hayvan, 1.0: insan)
    ene_miftahi: float           # Vâhid-i kıyasî / tefekkür aynadarlık kapasitesi [0.0 - 1.0]
    negentropi_pompasi: float    # Termodinamik dağılmaya karşı canlılık düzeni [0.0 - 1.0]


@dataclass
class HayatCiktisi:
    """Hayat ve şuur simülasyonu analitik çıktıları."""
    phi_butunlesik_bilgi: float  # Giulio Tononi Φ (Phi) metriği
    negentropi_orani: float      # Canlılığın ürettiği nizam (dS < 0) [0.0 - 1.0]
    ebediyet_kabiliyeti: float   # Ruhun basitliği ve bekā istidadı [0.0 - 1.0]
    kulliyet_indisi: float       # Bir ferdin koca kâinata muhatap olma seviyesi [0.0 - 1.0]
    durum_etiketi: str           # Ontolojik mertebe tasnifi
    izahat: str                  # Risale-i Nur ve fiziksel şerh


SENARYOLAR: Dict[str, HayatParametreleri] = {
    "insani_ruh": HayatParametreleri(
        zerre_sayisi=100_000_000,
        vahdet_rabitasi=0.98,
        alem_i_emir_irtibati=1.0,
        suur_derecesi=1.0,
        ene_miftahi=1.0,
        negentropi_pompasi=0.95
    ),
    "hayvani_ruh": HayatParametreleri(
        zerre_sayisi=50_000_000,
        vahdet_rabitasi=0.88,
        alem_i_emir_irtibati=0.90,
        suur_derecesi=0.55,
        ene_miftahi=0.0,
        negentropi_pompasi=0.85
    ),
    "nebatat_inbatiye": HayatParametreleri(
        zerre_sayisi=10_000_000,
        vahdet_rabitasi=0.75,
        alem_i_emir_irtibati=0.40,
        suur_derecesi=0.05,
        ene_miftahi=0.0,
        negentropi_pompasi=0.80
    ),
    "camid_madde": HayatParametreleri(
        zerre_sayisi=10_000_000,
        vahdet_rabitasi=0.05,
        alem_i_emir_irtibati=0.05,
        suur_derecesi=0.0,
        ene_miftahi=0.0,
        negentropi_pompasi=0.0
    ),
    "yapay_zeka_zombi": HayatParametreleri(
        zerre_sayisi=1_000_000_000,  # Milyarlarca parametre/transistör
        vahdet_rabitasi=0.15,        # Parçalara ayrılabilir modüler mantık
        alem_i_emir_irtibati=0.0,    # Haricî vücut giymiş emrî ruh yok
        suur_derecesi=0.0,           # Taklidi simülasyon, sübjektif deneyim yok
        ene_miftahi=0.0,
        negentropi_pompasi=0.10
    ),
    "vefat_ve_tecerrud": HayatParametreleri(
        zerre_sayisi=1,              # Beden libası sıyrılmış, basit tekil ruh
        vahdet_rabitasi=1.0,         # Ruh basittir, tecezzi etmez
        alem_i_emir_irtibati=1.0,    # Emr-i Rabbânî asliyeti
        suur_derecesi=1.0,           # Haps-i cesetten kurtulan saf şuur
        ene_miftahi=0.95,
        negentropi_pompasi=1.0       # Beka âleminin ebedî intizamı
    )
}


def dogrula_parametreler(p: HayatParametreleri) -> None:
    """Parametrelerin fiziksel ve ontolojik aralıklarını teftiş eder."""
    if p.zerre_sayisi < 1:
        raise ValueError("Zerre sayısı en az 1 olmalıdır.")
    for isim, deger in [
        ("vahdet_rabitasi", p.vahdet_rabitasi),
        ("alem_i_emir_irtibati", p.alem_i_emir_irtibati),
        ("suur_derecesi", p.suur_derecesi),
        ("ene_miftahi", p.ene_miftahi),
        ("negentropi_pompasi", p.negentropi_pompasi)
    ]:
        if not (0.0 <= deger <= 1.0):
            raise ValueError(f"{isim} [0.0, 1.0] aralığında olmalıdır. Verilen: {deger}")


def hesapla_hayat_durumu(p: HayatParametreleri) -> HayatCiktisi:
    """
    Hayat, şuur ve bütünleşik bilgi göstergelerini formüle eder.
    """
    dogrula_parametreler(p)

    # 1. Bütünleşik Bilgi (IIT Φ - Phi Metriği)
    # Sistem bölündüğünde ortaya çıkan bilgi kaybı.
    # Haricî vücut giymemiş (K_e ~ 0) veya parçaları bağımsız (R_v ~ 0) olan sistemlerde Φ = 0'a çöker.
    if p.vahdet_rabitasi < 0.08 or (p.alem_i_emir_irtibati < 0.05 and p.suur_derecesi < 0.05):
        phi = 0.0
    else:
        log_n = math.log10(max(10, p.zerre_sayisi))
        # Non-lineer vahdet etkisi: R_v^2 ile parçalar üstü sinerji
        vahdet_faktoru = math.pow(p.vahdet_rabitasi, 1.8)
        suur_agirligi = 0.2 * p.suur_derecesi + 0.8 * (p.suur_derecesi ** 2)
        ene_katkisi = 0.5 * p.ene_miftahi
        
        phi = log_n * 8.5 * vahdet_faktoru * (p.alem_i_emir_irtibati ** 1.2) * (suur_agirligi + ene_katkisi)
        phi = round(max(0.0, phi), 2)

    # 2. Canlılığın Negentropi Oranı (Schrödinger Negentropy)
    # Termodinamik dağılmaya karşı hayat iksiri ile intizam kurma derecesi
    negentropi = p.negentropi_pompasi * (0.6 * p.vahdet_rabitasi + 0.4 * p.alem_i_emir_irtibati)
    negentropi = round(min(1.0, max(0.0, negentropi)), 3)

    # 3. Ebediyet Kabiliyeti (Ruhun Basitliği ve Zevalsizliği - 29. Söz)
    # Beden mürekkeptir parçalanır; ruh basittir, haricî vücut giymiş kanun-u emrîdir, ölmez.
    if p.alem_i_emir_irtibati >= 0.70 and p.suur_derecesi >= 0.40:
        ebediyet = min(1.0, p.alem_i_emir_irtibati * (0.7 + 0.3 * p.suur_derecesi))
    elif p.alem_i_emir_irtibati > 0.20:
        # Hayvan veya bitki nev'i misali kod baki kalır, ferdî ebediyet cüz'îdir
        ebediyet = 0.30 * p.alem_i_emir_irtibati
    else:
        ebediyet = 0.0
    ebediyet = round(ebediyet, 3)

    # 4. Külliyet İndisi (Bir ferdin koca kâinata muhatap ve sultan olması)
    # Bir göz ile güneşi, ene ile esmâyı ihata edebilme istidadı
    kulliyet = p.suur_derecesi * p.ene_miftahi * p.vahdet_rabitasi
    kulliyet = round(min(1.0, max(0.0, kulliyet)), 3)

    # 5. Ontolojik Durum ve Tasnif
    if p.zerre_sayisi == 1 and ebediyet >= 0.90:
        durum = "Tecerrüd ve Beka (Berzah Âlemi)"
        izahat = "Beden libası parçalansa da ruhun basitliği zeval bulmaz; hafıza ve bilgi bütünüyle baki kalır."
    elif phi >= 40.0 and ebediyet >= 0.90:
        durum = "İnsanî Ruh & Ene Aynadarlığı (Ahsen-i Takvîm)"
        izahat = "Vücud-u haricî giymiş câmi' kanun-u emrî; kâinatı ihata eden küllî şuur ve ebediyet mazhariyeti."
    elif phi >= 10.0 and ebediyet >= 0.60:
        durum = "Hayvanî Ruh (Hissiyat ve Sevk-i Fıtrî)"
        izahat = "Müstakil can taşıyan, his ve irade sahibi fakat ene miftahı olmayan zîhayat mertebesi."
    elif p.negentropi_pompasi >= 0.50 and p.suur_derecesi <= 0.10:
        durum = "Nebâtî Hayat (Kuvve-i İnbâtiye)"
        izahat = "Şuursuz fakat kudsî sevk ile intizam gösteren, nebatat çekirdeğindeki tekvînî emrî kanun."
    elif p.zerre_sayisi >= 10_000_000 and phi <= 1.0 and p.alem_i_emir_irtibati == 0.0:
        durum = "Yapay Zekâ / Felsefî Zombi (Şuursuz Hesaplama)"
        izahat = "Milyarlarca mantık kapısı çalışsa da emrî ruhtan mahrum; sübjektif deneyim ve vahdeti sıfır (Φ ≈ 0)."
    else:
        durum = "Câmid Madde & Entropik Dağılma"
        izahat = "Hayat iksirinden mahrum, termodinamik dağılmaya açık, şuursuz ve dağınık fiziksel zerreler."

    return HayatCiktisi(
        phi_butunlesik_bilgi=phi,
        negentropi_orani=negentropi,
        ebediyet_kabiliyeti=ebediyet,
        kulliyet_indisi=kulliyet,
        durum_etiketi=durum,
        izahat=izahat
    )


def calistir_senaryo(senaryo_adi: str) -> HayatCiktisi:
    """Belirtilen isimdeki senaryoyu yürütür."""
    if senaryo_adi not in SENARYOLAR:
        raise KeyError(f"Bilinmeyen senaryo: '{senaryo_adi}'. Geçerli olanlar: {list(SENARYOLAR.keys())}")
    return hesapla_hayat_durumu(SENARYOLAR[senaryo_adi])


def tum_senaryolari_karsilastir() -> Dict[str, HayatCiktisi]:
    """Bütün hazır senaryoları çalıştırır ve neticeleri derler."""
    return {ad: hesapla_hayat_durumu(param) for ad, param in SENARYOLAR.items()}


def csv_yaz(dosya_yolu: str) -> None:
    """Senaryo neticelerini CSV dosyasına aktarır."""
    import csv
    sonuclar = tum_senaryolari_karsilastir()
    with open(dosya_yolu, mode="w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f)
        yazici.writerow([
            "Senaryo", "ZerreSayisi", "VahdetRabitasi", "AlemIEmir", "Suur",
            "EneMiftahi", "NegentropiPompasi", "Phi_IIT", "NegentropiOrani",
            "EbediyetKabiliyeti", "KulliyetIndisi", "Durum", "Izahat"
        ])
        for ad, cikti in sonuclar.items():
            p = SENARYOLAR[ad]
            yazici.writerow([
                ad, p.zerre_sayisi, p.vahdet_rabitasi, p.alem_i_emir_irtibati,
                p.suur_derecesi, p.ene_miftahi, p.negentropi_pompasi,
                cikti.phi_butunlesik_bilgi, cikti.negentropi_orani,
                cikti.ebediyet_kabiliyeti, cikti.kulliyet_indisi,
                cikti.durum_etiketi, cikti.izahat
            ])


def tablolastir() -> None:
    """Konsola zengin, biçimlendirilmiş bir tablo basar."""
    print("=" * 88)
    print("  🕊️ HAYAT, ŞUUR VE BÜTÜNLEŞİK BİLGİ (IIT Φ) MODELİ (29. SÖZ & 30. LEM'A)")
    print("=" * 88)
    print(f"{'Senaryo':<20} {'Φ (IIT)':>9} {'Negentropi':>11} {'Ebediyet':>10} {'Külliyet':>9}  Durum")
    print("-" * 88)
    sonuclar = tum_senaryolari_karsilastir()
    for ad, c in sonuclar.items():
        print(f"{ad:<20} {c.phi_butunlesik_bilgi:>9.2f} {c.negentropi_orani:>11.3f} {c.ebediyet_kabiliyeti:>10.3f} {c.kulliyet_indisi:>9.3f}  {c.durum_etiketi}")
    print("=" * 88)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Hayat ve Şuur Simülasyonu (29. Söz & 30. Lem'a)")
    parser.add_argument("--senaryo", type=str, choices=list(SENARYOLAR.keys()), help="Tek bir senaryo çalıştır")
    parser.add_argument("--csv", type=str, help="Sonuçları CSV dosyasına yaz")
    parser.add_argument("--tablo", action="store_true", default=True, help="Özet tabloyu ekrana bas")
    args = parser.parse_args()

    if args.senaryo:
        res = calistir_senaryo(args.senaryo)
        print(f"\nSenaryo: {args.senaryo}")
        print(f"Φ (IIT Bütünleşik Bilgi): {res.phi_butunlesik_bilgi}")
        print(f"Negentropi Oranı:        {res.negentropi_orani}")
        print(f"Ebediyet İstidadı:       {res.ebediyet_kabiliyeti}")
        print(f"Külliyet İndisi:         {res.kulliyet_indisi}")
        print(f"Ontolojik Hüküm:         {res.durum_etiketi}")
        print(f"İzahat:                  {res.izahat}\n")
    else:
        tablolastir()

    if args.csv:
        csv_yaz(args.csv)
        print(f"Sonuçlar CSV dosyasına kaydedildi: {args.csv}")
