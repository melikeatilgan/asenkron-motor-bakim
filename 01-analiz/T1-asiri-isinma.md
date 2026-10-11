# T1: Sargı aşırı sıcaklığı

## Tepe olay

> T1: Stator sargı sıcaklığı F sınıfı sınırını (155 °C) aşıyor ve motor kesilmiyor.

Bu bir eşik aşımı olayıdır, "yalıtım hasarı" değildir. Yalıtımın ne kadar zarar
göreceği sınırın ne kadar aşıldığına ve ne kadar sürdüğüne bağlıdır. Yaygın
kabul, sıcaklıktaki her 10 K artışın yalıtım ömrünü yaklaşık yarıya
indirdiğidir. Ağaç hasarın büyüklüğünü değil, sınırın aşıldığı ve korumanın
motoru kesmediği durumu modeller.

| Büyüklük | Değer | Kaynak |
|---|---|---|
| Yalıtım sınıfı sıcaklığı | 155 °C | F sınıfı (IEC 60085, IEC 60034-1) |
| Anma sıcaklık artışı | 80 K | WEG föyü (B sınıfı artış) |
| Anma yükünde ortalama sargı sıcaklığı | 40 + 80 = 120 °C | 40 °C ortam, direnç yöntemi |
| Sıcak nokta (yaklaşık) | 130 °C | Ortalamaya 10 K sıcak nokta payı |
| Sınıf sınırına kalan pay | 25 K | 155 − 130 |
| PTC algılama sıcaklığı | 155 °C | WEG föyü, faz başına 1 adet |

## Korumanın modellenmesi

Senaryodaki kumandada iki ayrı koruma var. Termik röle akımı izler, PTC rölesi
sargı sıcaklığını. İkisinin açma kontakları kontaktör bobin devresinde seridir;
hangisi açarsa kontaktör bırakır. Ağaç bu yüzden üç ayrımı gözetir:

- Akımın yükseldiği ısınmalarda (aşırı yük, besleme bozukluğu, sargı arızası)
  iki koruma da devreye girebilir. Motorun kesilmemesi için ikisinin birden
  başarısız olması gerekir.
- Akımı termik röleyi açtıracak kadar yükseltmeyen ısınmalarda (soğutma havası
  yolu, ortam sıcaklığı) akıma bakan koruma devreye girmez. Bu durumda temel
  koruma PTC'dir.
- Kontaktör iki yolun ortak elemanıdır. Ana kontakları yapışmışsa hangi röle
  açarsa açsın motor kesilmez.

## Ağaç

```
T1  Sargı sıcaklığı 155 °C'yi aşıyor ve motor kesilmiyor
│
└─[VEYA]
   ├── A1.1  Akımla birlikte gelen ısınma kesilmiyor
   │   └─[VE]
   │      ├── A1.3  Aşırı akım yüklenmesi sargıyı sınıra taşıyacak kadar sürüyor
   │      │   └── ▷ TRANSFER → T3 (ağacın tamamı)
   │      └── A1.4  Ne PTC ne termik röle motoru kestiriyor
   │          └─[VEYA]
   │             ├── B1.11  Kontaktör ana kontakları yapışmış
   │             └─[VE]
   │                ├── A1.5  PTC yolu kestirmiyor
   │                │   └─[VEYA]
   │                │      ├── B1.06  PTC devresi köprülenmiş (röle algılamıyor)
   │                │      └── B1.07  PTC rölesi arızalı ya da çıkışı kumandaya bağlı değil
   │                └── A1.6  Termik yol kestirmiyor
   │                    └─[VEYA]
   │                       ├── B1.08  Termik röle ayarı yüksek (aşırı akımda zamanında açmıyor)
   │                       ├── B1.09  Açma sınıfı motorla uyumsuz (gereğinden yavaş)
   │                       └── B1.10  Termik röle arızalı ya da kontağı kumandaya bağlı değil
   │
   └── A1.2  Akım artmadan gelen ısınma kesilmiyor
       └─[VE]
          ├── A1.7  Isı dışarı atılamıyor
          │   └─[VEYA]
          │      ├── B2.03  Fan kanadı kırık ya da fan milde gevşek   (T2 ile ortak olay)
          │      ├── B1.01  Fan kapağı ızgarası tıkalı
          │      ├── B1.02  Gövde kanatçıkları toz, yağ ya da boyayla kaplı
          │      ├── B1.03  Hava girişinin önü kapalı
          │      ├── B1.04  Soğutma havası 40 °C'nin üstünde
          │      └── B1.05  Rakım 1000 m'nin üstünde, yük düşürülmemiş
          └── A1.8  PTC yolu kestirmiyor
              └─[VEYA]
                 ├── B1.11  Kontaktör ana kontakları yapışmış
                 ├── B1.06  PTC devresi köprülenmiş (röle algılamıyor)
                 └── B1.07  PTC rölesi arızalı ya da çıkışı kumandaya bağlı değil
```

## Modelin sınırları

Ağaç niteldir; olasılık ve şiddet hesabı yapılmamıştır. Aşağıdaki
basitleştirmeler sonuçları okurken akılda tutulmalıdır.

- T3'ün gerçekleşmesi sargının 155 °C'yi aşması demek değildir. Akımın %110'u
  geçmesi sargıyı ancak yeterince uzun sürerse sınıra taşır. A1.3 ara olayı bu
  koşulu taşır: T3'teki olaylar burada "sargıyı sınıra taşıyacak şiddet ve
  sürede" gerçekleşmiş sayılır. Aynı şey A1.7'deki soğutma olayları için de
  geçerlidir; B1.04, soğutma havasının 40 °C'yi bir derece geçmesi değil,
  sargıyı sınıra taşıyacak kadar aşmasıdır.
- PTC ideal bir anahtar değildir. Algılama sıcaklığı toleranslıdır, sensör
  sargının en sıcak noktasında olmayabilir ve ısı sensöre gecikmeyle ulaşır.
  Kilitli rotor gibi hızlı ısınmalarda bu gecikme önem kazanır; o durumda asıl
  koruma termik röledir. Ağaç bu gecikmeyi modellemez, çalışan bir korumanın
  sıcaklığı sınırda tuttuğunu kabul eder.
- Soğutma dalındaki olaylar, akımı termik röleyi açtıracak kadar yükseltmeyen
  soğutma kayıplarıdır. Fan mile sürtüyor ya da sıkışıyorsa bu artık bir yük
  olayıdır ve T3 üzerinden modellenir.
- Koruma olayları da aynı koşulla tanımlıdır. B1.08, ayarın 28,3 A'in biraz
  üstünde olması değil, rölenin o aşırı akımda motor sınıra ulaşmadan
  açmayacağı kadar yüksek olmasıdır. Form ise ayarın anma akımına eşit olmasını
  arar; bu, olayın önleyici kontrolüdür.

## Temel olaylar ve kontrolleri

T3'ten transfer edilen olaylar [T3 belgesinde](T3-asiri-akim.md), B2.03
[T2 belgesinde](T2-titresim.md) listelidir.

| Kod | Temel olay | Nasıl kontrol edilir | Kabul kriteri | Form |
|---|---|---|---|---|
| B1.01 | Fan kapağı ızgarası tıkalı | Gözle | Açık; toz, lif birikmesi yok | G-01 |
| B1.02 | Gövde kanatçıkları kaplı | Gözle | Kanat dipleri temiz | G-02 |
| B1.03 | Hava girişinin önü kapalı | Gözle, şerit metre | Engel yok; üretici kılavuzundaki en az mesafe sağlanıyor | G-03 |
| B1.04 | Soğutma havası 40 °C'nin üstünde | Fan girişinde termometre | ≤ 40 °C | G-05 |
| B1.05 | Rakım 1000 m'nin üstünde, yük düşürülmemiş | Tesis rakımı ile motor föyü | ≤ 1000 m; üstündeyse yük düşürülmüş | G-06 |
| B1.06 | PTC devresi köprülenmiş | Motor soğukken PTC rölesi klemenslerinde direnç ölçümü | 60–750 Ω ve aynı sıcaklıktaki devreye alma kaydıyla uyumlu | P-01 |
| B1.07 | PTC rölesi arızalı ya da çıkışı bağlı değil | Röle girişine ayarlı direnç bağlanarak işlev testi | Röle föyündeki dirençlerde açıyor; kontaktör bırakıyor | P-02 |
| B1.08 | Termik röle ayarı yüksek | Röle skalası | Ayar = 28,3 A | P-03 |
| B1.09 | Açma sınıfı motorla uyumsuz | Röle etiketi ve açma eğrisi | Class 10; eğri motor verisiyle karşılaştırılmış | P-04 |
| B1.10 | Termik röle arızalı ya da kontağı bağlı değil | Test düğmesi | Kontaktör bırakıyor | P-05 |
| B1.11 | Kontaktör ana kontakları yapışmış | Bobin enerjisizken kutup başına süreklilik | Üç kutup da açık | P-06 |

## Notlar

**PTC direnç ölçümü.** PTC termistöre megger uygulanmaz; ölçüm düşük gerilimli
ohmmetreyle ve motor soğukken yapılır. Soğukta eleman başına direnç genellikle
20–250 Ω aralığındadır, üç seri eleman için 60–750 Ω beklenir. Sıfıra yakın
değer devrenin tamamen köprülendiğini, sonsuz değer koptuğunu gösterir. Çalışan
bir PTC rölesi açık devreyi arıza sayar ve motoru durdurur; bu yüzden kopukluk
ağaçta koruma arızası olarak yer almaz, köprü yer alır.

Bu aralık tek başına yeterli değildir. Üç elemandan biri köprülenmişse toplam
direnç yine aralığın içinde kalabilir. Bu yüzden devreye almadaki değer
kaydedilir ve sonraki ölçümler aynı sıcaklık koşulunda onunla karşılaştırılır;
belirgin bir düşüş köprü şüphesidir. Devreye alma kaydı yoksa ilk ölçüm baz
alınır. Ölçüm devrenin sürekli olduğunu gösterir, sıcakta açacağını göstermez.

**PTC rölesi testi.** Rölenin açtığı, girişine ayarlı direnç bağlanarak
sınanır: direnç yükseltildiğinde röle föyündeki değerde açmalı, giriş açık
devre edildiğinde de açmalıdır. Bazı röleler girişin kısa devre edildiğini de
algılar ve tam köprüde açar. Senaryodaki rölede bu özelliğin olup olmadığına
röle föyünden bakılır; B1.06, rölenin algılamadığı köprüyü anlatır. PTC ile
rölenin birlikte çalışma koşulları IEC 60947-8'de tanımlıdır.

**Termik röle sınıfı.** IEC 60947-4-1'e göre Class 10 röle, ayar akımının 7,2
katında soğuk durumdan 4 ile 10 saniye arasında açar; Class 20'de bu 6–20 s,
Class 30'da 9–30 s'dir. Föye göre motorun kilitli rotor dayanımı sıcakta 11 s,
soğukta 19 s'dir. Üç sınıf içinde üst açma sınırı (10 s) motorun sıcak
dayanımının altında kalan tek sınıf Class 10'dur; Class 20 ve Class 30'un üst
sınırları bu dayanımı aşar. Bu, uygunluğun kanıtı değil, başlangıç seçimidir:
sınıf sınırları 7,2 kat için tanımlıdır, motorun kilitli rotor akımı 7,0 kattır
ve rölenin toleransı vardır. Seçilen rölenin soğuk ve sıcak açma eğrileri
motorun kalkış süresi ve kilitli rotor dayanımıyla karşılaştırılarak
doğrulanır (formda P-04).

**Termik röle ayarı.** Röle 1,05 × ayar akımında iki saat açmaz, 1,20 × ayar
akımında iki saat içinde açar. Ayarın anma akımının üstüne çekilmesi bu bandı
yukarı kaydırır ve motorun anma değerinin üstünde uzun süre çalışmasına izin
verir.

**Test düğmesi neyi sınar.** Test düğmesi rölenin açma mekanizmasını ve
yardımcı kontağın kumanda devresini kestiğini gösterir. Bimetalin akım-zaman
davranışını sınamaz; bunun için akım enjeksiyon testi gerekir.

**Soğutma arızalarında PTC.** Fan ızgarası tıkandığında motorun yükü değişmez,
akımı termik röleyi açtıracak kadar artmaz. Sıcaklığı izleyen tek koruma
PTC'dir. PTC yolu çalışmıyorsa bu durumda motoru zamanında kesecek bir şey
kalmaz. Formun PTC kontrolleriyle başlamasının sebebi budur.
