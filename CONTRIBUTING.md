# 🤝 Katkı Rehberi

Tılsım-ı Kâinat'a katkınız için teşekkürler! Bu proje hem bir **tefekkür metni** hem de bir
**modelleme laboratuvarıdır**; her iki alanda da katkıya açıktır.

## Katkı Türleri

| Alan | Örnekler |
|------|----------|
| 📜 **Dokümantasyon** | Yeni risale analizleri, mevcut metinlerin derinleştirilmesi, tefekkür soruları |
| 📖 **Sözlük** | Yeni ıstılahlar, daha isabetli tanımlar, çapraz bağlantılar |
| 🗺️ **Diyagramlar** | Mermaid şemaları, kavram haritaları |
| 🧪 **Simülasyon** | Yeni senaryolar, model iyileştirmeleri, görselleştirmeler, testler |

## İlkeler

1. **Asıl metne sadakat:** Risale-i Nur'dan yapılan iktibaslarda kaynak (Söz/Lem'a/Mektub vb.)
   belirtilmeli; şerh ile asıl metin birbirinden açıkça ayrılmalıdır.
2. **Edep ve itidal:** Kavramsal tartışmalarda kişileri değil fikirleri ele alın.
3. **Sembolik modelleme:** Simülasyonlar birer metafordur; ilmî veya dinî hüküm iddiası taşımamalıdır.
4. **Türkçe öncelikli:** Dokümanlar Türkçe yazılır; kod içi isimlendirmeler mevcut üsluba (Türkçe,
   ASCII uyumlu tanımlayıcılar) uymalıdır.

## İş Akışı

```bash
git checkout -b ozellik/yeni-analiz
# değişikliklerinizi yapın
python -m unittest discover -s simulations -p "test_*.py"
git commit -m "docs: 33. Söz pencereleri analizi eklendi"
git push origin ozellik/yeni-analiz
```

Ardından bir **Pull Request** açın.

### Commit Mesajı Önekleri

- `docs:` dokümantasyon
- `sozluk:` kavramlar sözlüğü
- `sim:` simülasyon kodu
- `diagram:` şemalar
- `ci:` otomasyon
