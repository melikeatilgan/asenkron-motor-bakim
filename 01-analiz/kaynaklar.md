# Kaynaklar

## Motor verisi

WEG veri föyü, ürün kodu 12863072, W22 IE3, 15 kW, 4 kutup, 160L gövde.
15.04.2025 tarihli. Akım, devir, moment, verim, güç katsayısı, kilitli rotor
dayanımı, yatak tipleri ve PTC sıcaklığı bu föyün 400 V / 50 Hz sütunundan
alındı.

## Standartlar

| Standart | Nerede kullanıldı | Alınan değer |
|---|---|---|
| ISO 20816-3:2022 | T2 titreşim sınırları | Grup 2, rijit destek: 1,4 / 2,8 / 4,5 mm/s RMS; rijit destek koşulu (%25); anlamlı değişim, B/C sınırının %25'i (0,7 mm/s) |
| IEC 60034-1 | Sıcaklık artışı, gerilim bölgeleri | B sınıfı artış 80 K; Bölge A ±%5, Bölge B ±%10 |
| IEC 60085 | Yalıtım sınıfı sıcaklığı | F sınıfı 155 °C |
| IEC 60947-4-1 | Termik röle açma sınıfları | Soğukta 7,2 × Ie'de Class 10: 4–10 s, Class 20: 6–20 s, Class 30: 9–30 s; 1,05 × Ie'de 2 saat açmaz, 1,20 × Ie'de 2 saat içinde açar |
| IEC 60947-8 | PTC termistör rölesi | PTC ve rölenin birlikte çalışma koşulları |
| IEC 60034-12 | Kalkış performansı | N tasarım |
| IEEE 43-2013 | Yalıtım direnci | 1 kV altı sargılar için 40 °C'de en az 5 MΩ; 500 V DC, 1 dk; test sonrası en az test süresinin dört katı boşaltma |
| NEMA MG-1 | Gerilim dengesizliği | %1'e kadar anma yükü, üstünde yük düşürme, %5'in üstünde çalışma önerilmez |
| EN 50160 | Şebeke gerilim kalitesi | Gerilim THD %8 (bir haftalık ölçümün %95'i için); formda yalnızca tarama eşiği |
| AB 2019/1781 | Asgari verim sınıfı | IE3, 1 Temmuz 2021 |

ISO 20816-3:2022, ISO 10816-3:2009'un yerini almıştır. Grup 2 için bölge
sınırları iki sürümde aynıdır.

## Standart dışı değerler

Aşağıdaki değerler bir standarttan alınmadı. Bu çalışma için seçtiğim tarama
eşikleri; bir kaynağa karşı doğrulanmadılar. Üretici ya da tesis kendi değerini
veriyorsa o geçerlidir.

| Değer | Kullanıldığı yer |
|---|---|
| Faz akımı dengesizliği ≤ %10 | E-02 |
| Faz direnci dengesizliği ≤ %2 | E-09 |
| Akım spektrumunda yan bant ≥ 45 dB altta | E-10 |
| Termal kamerada aynı yükte fazlar arası fark < 4 K | E-06 |
| Paralel kaçıklık ≤ 0,09 mm, açısal ≤ 0,07 mm/100 mm (1500 d/dk, kısa esnek kaplin) | M-05 |
| Ayak altı boşluğu ve boru zorlamasında mil kayması ≤ 0,05 mm | M-04, M-06 |
| Doğal frekans ile uyarım frekansı arasında en az %10 ayrım | V-04 |
| PTC soğuk direnci, eleman başına 20–250 Ω | P-01 |
| Yatak kusur frekansı kaba tahmini 0,4 × Z × fr ve 0,6 × Z × fr | T2 |
| Sıcaklık artışındaki ilave ≈ 2 × (dengesizlik yüzdesi)² | T3 notları |
| Her 10 K artış yalıtım ömrünü yaklaşık yarıya indirir | T1 |

Dengesizlik her yerde aynı biçimde hesaplanır: 100 × ortalamadan en büyük
sapma / ortalama.

## Doğrulanmayanlar

- Standart metinlerinin kendisini satın almadım; değerleri standartları aktaran
  üretici kataloglarından ve uygulama notlarından aldım. Gerçek bir uygulamada
  standardın güncel sürümünden doğrulanması gerekir.
- PTC soğuk direnç aralığı genel bir aralıktır. Bu motordaki sensörün kendi
  kabul aralığı föyde yazmıyor.
- Class 10 rölenin bu motora uygunluğu, belirli bir rölenin açma eğrisiyle
  karşılaştırılarak doğrulanmadı. Belgelerde başlangıç seçimi olarak geçer.
- 6309 ve 6209 yataklarının bilya sayısı ve geometrisi üreticiye göre değişir.
  T2'deki yatak frekansları kaba tahmindir.
- Üretici bakım kılavuzundaki değerler (cıvata torkları, saatlik kalkış sınırı,
  hava girişi önündeki en az mesafe) buraya yazılmadı; formda "üretici değeri"
  olarak geçer ve değer forma yazılmadan madde uygun işaretlenmez. Kapalı
  yatağın değişim süresi bilinmiyorsa Y-01'e "doğrulanmadı" yazılır; yatağın
  durumu ayrıca Y-02 ve V-02 ile izlenir.
- Eğilime bakan kriterlerde (PTC direnci, spektrum tepeleri, yatak sıcaklığı,
  sönüm) sayısal eşik verilmedi; tesisin baz kaydına göre değerlendirilir. Baz
  kayıt yoksa ilk ölçüm baz olarak yazılır, karşılaştırma bir sonraki kontrolde
  yapılır. Satırda sayısal sınırı olan bir kısım varsa o gün yalnız ona göre
  U / X işaretlenir; yalnız eğilime bakan satırda U / X boş kalır.
- Kalkış süresi için formdaki 4 saniye bir uygunluk sınırı değildir; aşıldığında
  röle eğrisine bakılması gerektiğini gösteren eşiktir.
- Formun iki sayfaya, kartın A6'ya sığdığı Chrome ile, %100 ölçekte, üstbilgi
  ve altbilgi kapalı yazdırılarak denetlendi. Başka tarayıcıda taşabilir;
  yazdırılmış PDF'ler depodadır.
- Saha ölçümü yapılmadı. Eşikler föy ve standart değerleridir.
