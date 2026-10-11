# Referans motor

## Kapsam

Bu çalışma belirli bir tesisteki motorun incelemesi değildir. Üretici föyündeki
değerler ve standartlardaki sınırlar kullanılarak bir motor tipi için kurulmuş
nitel bir arıza ağacı ve bakım planıdır. Saha ölçümü yapılmamıştır.

Başka bir motora uygulanırken eşikler o motorun plaka değerleriyle yeniden
hesaplanır; koruma düzeni ya da işletme koşulları farklıysa ağaçların da
gözden geçirilmesi gerekir.

## Neden bu motor

| Seçim | Gerekçe |
|---|---|
| 15 kW, 4 kutup | Pompa, fan ve konveyör tahriklerinde yaygın bir güç ve devir. |
| 160L gövde | Mil yüksekliği 160 mm. ISO 20816-3 elektrik makinelerini mil yüksekliğine göre de sınıflar: 160 mm ≤ H < 315 mm Grup 2'dir. Standardın güç ölçütü "15 kW'ın üstü" olduğundan sınıflandırma güce göre değil mil yüksekliğine göre yapıldı. |
| IE3 | AB 2019/1781 ile 1 Temmuz 2021'den beri bu güçteki yeni motorlar için asgari verim sınıfı. |
| PTC termistörlü | Termal koruma dalının gerçek bir karşılığı var. |
| Kapalı (ZZ) yataklı | Föydeki standart donanım. Yeniden gresleme yok; yatak dalı buna göre kuruldu. |

## Föy değerleri

Kaynak: WEG veri föyü, ürün kodu 12863072, W22 IE3 serisi, 15.04.2025 tarihli.
Aşağıdaki değerler 400 V, 50 Hz sütunundan alındı.

| Büyüklük | Değer | Not |
|---|---|---|
| Anma gücü | 15 kW | S1 sürekli görev, servis faktörü 1,00 |
| Gerilim | 400 V Δ / 690 V Y, 50 Hz | Senaryoda 400 V üçgen |
| Anma akımı In | 28,3 A (400 V Δ) | 690 V Y'de 16,4 A |
| Yüksüz akım | 13,0 A | |
| Kalkış akımı | 198 A | Ia/In = 7,0 |
| Anma devri | 1475 d/dk | Kayma %1,67 |
| Anma momenti | 97,2 Nm | Kalkış momenti %270, devrilme momenti %300 |
| Verim (%50 / %75 / %100 yük) | %92,0 / %92,5 / %92,3 | IE3 |
| Güç katsayısı (%50 / %75 / %100 yük) | 0,66 / 0,77 / 0,83 | |
| Yalıtım sınıfı | F | Sıcaklık artışı 80 K (B sınıfı artış) |
| Kilitli rotor dayanımı | 19 s soğuk, 11 s sıcak | Termik röle sınıfı seçiminde kullanıldı |
| Termal koruma | Sargıda PTC, faz başına 1 adet | Algılama sıcaklığı 155 °C |
| Yataklar | DE 6309 ZZ C3, NDE 6209 ZZ C3 | Kapalı tip, yeniden gresleme aralığı yok |
| Koruma sınıfı, soğutma | IP55, IC411 (TEFC) | Mil ucundaki fan motorla aynı devirde |
| Ortam, rakım | −20…+40 °C, 1000 m | Üstünde yük düşürme gerekir |
| Montaj | B3 (ayaklı) | |
| Eylemsizlik momenti | 0,1534 kgm² | |
| Ağırlık | 147 kg | |
| Tasarım | N (IEC 60034-12) | |

## Türetilen değerler

| Büyüklük | Hesap | Sonuç |
|---|---|---|
| Senkron devir | 120 × 50 / 4 | 1500 d/dk |
| Kayma s | (1500 − 1475) / 1500 | %1,67 |
| Dönüş frekansı (1×) | 1475 / 60 | 24,58 Hz |
| Kayma frekansı | s × f | 0,83 Hz |
| Kutup geçiş frekansı | 2 × s × f | 1,67 Hz |
| Görünür güç | √3 × 400 V × 28,3 A | 19,6 kVA |
| Şebekeden çekilen güç | 15 kW / 0,923 | 16,3 kW |
| Aşırı akım eşiği | 1,10 × 28,3 A | 31,1 A |
| Anma yükünde ortalama sargı sıcaklığı | 40 °C + 80 K | 120 °C |

## Varsayılan işletme senaryosu

Eşikler ve ağaçlardaki dallar bu senaryoya göre kuruldu. Senaryo değişirse
ağaçlar da değişir.

- Tahrik: radyal çarklı santrifüj pompa, esnek kaplinle doğrudan akuple.
- Montaj: beton kaide üzerine ayaklı (B3), rijit destek. ISO 20816-3'e göre
  desteğin rijit sayılması için ölçüm yönündeki en düşük doğal frekans ana
  uyarım frekansının en az %25 üstünde olmalıdır. Bu motorda sınır 30,7 Hz'tir
  ve formdaki V-04 kontrolüyle doğrulanır.
- Çalışma: sürekli (S1), günde yaklaşık 16 saat.
- Yol verme: doğrudan (DOL), günde birkaç kalkış.
- Besleme: doğrudan şebeke, sürücü yok.
- Ortam: kapalı pompa dairesi, tozlu, 25–38 °C.
- Koruma ve kumanda: termik aşırı akım rölesi (Class 10, ayar 28,3 A) ve PTC
  termistör rölesi. İkisinin açma kontakları kontaktör bobin devresinde seri
  bağlıdır; hangisi açarsa kontaktör bırakır.

Kısa devre koruması (sigorta ya da motor koruma şalteri) ve toprak kaçağı
koruması bu analizin kapsamında değildir.
