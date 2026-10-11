# T2: Aşırı titreşim

## Tepe olay

> T2: Yatak gövdesinde ölçülen radyal titreşim hızı Bölge D'ye giriyor.

Ölçülebilir tanım: yatak gövdesinde, radyal yönde ölçülen titreşim hızının RMS
değeri (10–1000 Hz bandı) 4,5 mm/s'yi aşıyor.

Sınırlar ISO 20816-3:2022'den alındı (ISO 10816-3:2009'un yerini aldı). Motor
Grup 2'dedir: elektrik makinelerinde mil yüksekliği 160 mm ≤ H < 315 mm. Destek
rijit kabul edildi.

| Bölge | Rijit destek (mm/s RMS) | Anlamı | Yapılacak |
|---|---|---|---|
| A | ≤ 1,4 | Yeni devreye alınmış makine | Kaydet |
| B | > 1,4 ve ≤ 2,8 | Süre kısıtı olmadan işletilebilir | Kaydet, izle |
| C | > 2,8 ve ≤ 4,5 | Uzun süreli sürekli işletmeye uygun değil | İş emri aç, planlı müdahale |
| D | > 4,5 | Hasar verebilecek seviye | Durdur |

Esnek destekte aynı grubun sınırları 2,3 / 4,5 / 7,1 mm/s'dir.

**Ölçüm.** DE ve NDE yatak gövdelerinde yatay ve düşey olmak üzere dört radyal
nokta ölçülür, karar en yüksek okumaya göre verilir. Tablodaki sınırlar radyal
titreşim içindir. Eksenel titreşim de iki yatakta ölçülür ama tabloyla
değerlendirilmez; eğilimi izlemek için kaydedilir.

**Rijit destek koşulu.** Beton kaide tek başına rijitlik kanıtı değildir.
Standarda göre ölçüm yönündeki en düşük doğal frekans ana uyarım frekansının
en az %25 üstündeyse destek o yönde rijit sayılır. Bu motorda sınır
1,25 × 24,58 = 30,7 Hz'tir ve darbe testiyle doğrulanır (formda V-04). Bu koşul
yalnızca tablonun hangi sütununun kullanılacağını belirler; 2× ya da 100 Hz
yakınındaki bir rezonansı dışlamaz.

**Eğilim.** Sınırın altında kalan ama bir önceki ölçüme göre belirgin değişen
bir okuma da incelenir. Standart, B/C sınırının %25'ini anlamlı değişim olarak
verir; bu motorda 0,7 mm/s. Karşılaştırma aynı noktada ve benzer yükte alınmış
ölçümler arasında yapılır.

## Frekanslar

Genel titreşim seviyesi ayrıntılı incelemenin gerekip gerekmediğini söyler.
Spektrumdaki bileşenler olası nedenleri daraltır, tek başına kesin teşhis
vermez. Bu motor için titreşim spektrumunda bakılacak frekanslar:

| Frekans | Değer | İşaret ettiği dal |
|---|---|---|
| 1× (dönüş) | 24,6 Hz | Dengesizlik (A2.1) |
| 2× | 49,2 Hz | Eksen kaçıklığı (A2.2), gevşeklik (A2.4) |
| 3×, 4× ve üstü | 73,8 Hz, 98,3 Hz… | Gevşeklik (A2.4) |
| 2 × şebeke frekansı | 100 Hz | Elektriksel kaynak (A2.6) |
| 1× ± kutup geçiş frekansı | 22,92 / 26,25 Hz | Rotor kafes arızası (T3 A3.2.1) |
| Yatak kusur frekansları | aşağıda | Yatak arızası (A2.3) |

4× (98,3 Hz) ile 100 Hz birbirine çok yakındır. İkisini ayırabilmek için
spektrum çözünürlüğü 0,5 Hz ya da daha iyi olmalıdır.

Rotor kafes arızası stator akımının spektrumunda da görülür, ama orada farklı
frekanslarda aranır: şebeke frekansının iki yanında, 50 ± 2·s·f. Anma
kaymasında bu 48,33 ve 51,67 Hz'tir. Kayma yüke bağlı olduğundan ölçüm anındaki
gerçek devirle yeniden hesaplanır (formda E-10).

### Yatak kusur frekansları

Dış bilezik sabitken:

```
BPFO (dış bilezik) = (Z / 2) × fr × (1 − (d / D) × cos α)
BPFI (iç bilezik)  = (Z / 2) × fr × (1 + (d / D) × cos α)
```

Z bilya sayısı, d bilya çapı, D bölüm dairesi çapı, α temas açısı, fr dönüş
frekansıdır. Geometri bilinmiyorsa kaba tahmin olarak 0,4 × Z × fr ve
0,6 × Z × fr kullanılır.

| Yatak | Konum | Bilya sayısı (varsayım) | BPFO, kaba | BPFI, kaba |
|---|---|---|---|---|
| 6309 | DE | 8 | ≈ 79 Hz | ≈ 118 Hz |
| 6209 | NDE | 9 ya da 10 | ≈ 88–98 Hz | ≈ 133–148 Hz |

Bilya sayısı ve geometri üreticiye göre değişir. Bu tablo spektrumda nereye
bakılacağını gösterir; teşhis için takılı yatağın üreticisinin verdiği kusur
frekansları kullanılır.

## Ağaç

```
T2  Yatak gövdesinde radyal titreşim > 4,5 mm/s RMS (Bölge D)
│
└─[VEYA]
   ├── A2.1  Dönen kütlede dengesizlik            [1× baskın, radyal]
   │   └─[VEYA]
   │      ├── B2.01  Fan üzerinde asimetrik birikinti
   │      ├── B2.02  Balans ağırlığı düşmüş ya da kaymış
   │      ├── B2.03  Fan kanadı kırık ya da fan milde gevşek   (T1 ile ortak olay)
   │      └── B2.04  Kaplin elemanı asimetrik aşınmış
   │
   ├── A2.2  Eksen kaçıklığı                      [2× baskın, eksenel yüksek]
   │   └─[VEYA]
   │      ├── B2.05  Hizalama tolerans dışında bırakılmış (paralel ya da açısal)
   │      ├── B2.06  Boru zorlaması pompayı hizadan çıkarıyor
   │      └── B2.07  Isıl büyüme hesaba katılmamış (soğukta hizalanmış)
   │
   ├── A2.3  Yatak arızası                        [yatak frekansları, yüksek frekans]
   │   └─[VEYA]
   │      ├── B2.08  Yatak servis ömrünü doldurmuş (kapalı yatakta gres ömrü)
   │      ├── B2.09  Yanlış yatak takılmış (tip ya da boşluk sınıfı)
   │      ├── B2.10  Montaj hatası (çakarak takma, kuvvetin bilyalardan geçmesi)
   │      ├── B2.11  Kirlilik ya da nem girmiş
   │      └── B2.12  Yatak yuvası ya da muylu aşınmış (bilezik dönüyor)
   │
   ├── A2.4  Mekanik gevşeklik                    [2×, 3× ve üstü, yarım harmonikler]
   │   └─[VEYA]
   │      ├── B2.13  Ayak cıvataları gevşek
   │      ├── B2.14  Ayak altı boşluğu (soft foot)
   │      ├── B2.15  Kaide çatlağı ya da grout bozulması
   │      └── B2.16  Yatak kapağı cıvataları gevşek
   │
   ├── A2.5  Rezonans                             [dar bantta büyük genlik]
   │   └─[VE]
   │      ├── B2.17  Destek doğal frekansı bir uyarım frekansına yakın (1×, 2×, 100 Hz)
   │      └── B2.18  Sönüm düşük
   │
   └── A2.6  Elektriksel kaynaklı titreşim        [100 Hz]
       └─[VEYA]
          ├── B2.19  Statik eksantriklik (hava aralığı düzgün değil)
          ├── B2.20  Dinamik eksantriklik (rotor kaçık ya da mil eğik)
          └── ▷ TRANSFER → T3 A3.2.1 (rotor kafes arızası)
```

Ağaç niteldir. Temel olaylar "titreşimi Bölge D'ye taşıyacak şiddette
gerçekleşmiş" kabul edilir. Küçük bir dengesizlik ya da tolerans sınırındaki
bir hizalama tepe olayı doğurmaz.

## Temel olaylar ve kontrolleri

| Kod | Temel olay | Nasıl kontrol edilir | Kabul kriteri | Form |
|---|---|---|---|---|
| B2.01 | Fan üzerinde birikinti | Fan kapağı sökülerek gözle | Birikinti yok | G-04 |
| B2.02 | Balans ağırlığı kaymış | Spektrumda 1× bileşeni | Aynı yükte önceki kayda göre belirgin artış yok | V-02 |
| B2.03 | Fan kanadı kırık ya da fan gevşek | Fan kapağı sökülerek gözle | Kanatlar tam, fan milde sıkı | G-04 |
| B2.04 | Kaplin elemanı aşınmış | Gözle | Çatlak, aşınma, sertleşme yok | M-02 |
| B2.05 | Hizalama tolerans dışında | Lazer ya da komparatör | Paralel ≤ 0,09 mm; açısal ≤ 0,07 mm/100 mm | M-05 |
| B2.06 | Boru zorlaması | Flanş cıvataları gevşetilirken kaplinde komparatör | Mil kayması ≤ 0,05 mm | M-06 |
| B2.07 | Isıl büyüme | Sıcak duruşta hizalama tekrarı | Sıcakta da tolerans içinde | M-05 |
| B2.08 | Yatak servis ömrünü doldurmuş | Çalışma saati kaydı; yatak sıcaklığı ve sesi | Üretici değişim süresi içinde; süre bilinmiyorsa doğrulanmadı yazılır ve durum izlenir | Y-01, Y-02 |
| B2.09 | Yanlış yatak takılmış | Yatak etiketi | 6309 ZZ C3 / 6209 ZZ C3 | Y-03 |
| B2.10 | Montaj hatası | İş kaydı; spektrumda yatak frekansları | Isıtarak ya da presle, kuvvet sıkı geçen bilezikten; yeni tepe yok | Y-04, V-02 |
| B2.11 | Kirlilik ya da nem girmiş | Keçe ve yatak kapağı gözle; yatak sesi | Keçe sağlam; giriş izi yok | Y-05, Y-02 |
| B2.12 | Yatak yuvası ya da muylu aşınmış | Sökümde mikrometre | Üretici toleransı | M-08 |
| B2.13 | Ayak cıvataları gevşek | Tork anahtarı | Üretici torku | M-01 |
| B2.14 | Ayak altı boşluğu | Cıvata gevşetilirken komparatör ya da sentil | ≤ 0,05 mm | M-04 |
| B2.15 | Kaide çatlağı, grout bozulması | Gözle, çekiçle tıklatma | Çatlak yok, boşluk sesi yok | M-07 |
| B2.16 | Yatak kapağı cıvataları gevşek | Tork anahtarı | Üretici torku | M-01 |
| B2.17 | Doğal frekans bir uyarım frekansına yakın | Darbe testi | 24,6 / 49,2 / 100 Hz'e %10'dan yakın doğal frekans yok | V-04 |
| B2.18 | Sönüm düşük | Darbe testinden sönüm oranı | Kaydedilir; kabul sınırı tesisin baz kaydıdır | V-04 |
| B2.19 | Statik eksantriklik | Spektrumda 100 Hz; güç kesme testi | Aynı yükte önceki kayda göre belirgin artış yok | V-02, V-03 |
| B2.20 | Dinamik eksantriklik | Spektrumda 100 Hz çevresinde 1× yan bantları | Yan bant yok | V-02, V-03 |

Hizalama için verilen 0,09 mm ve 0,07 mm/100 mm, 1500 d/dk civarındaki
makineler için bu çalışmada seçilen kabul sınırlarıdır (bkz. kaynaklar). Kaplin
üreticisinin verdiği değer varsa o geçerlidir.

## Notlar

**Yataklar kapalı tiptir.** Föye göre iki yatak da ZZ kapaklıdır ve ömür boyu
yağlıdır; yeniden gresleme aralığı verilmemiştir. Bu yüzden "gres eksik" ya da
"aşırı gres" gibi olaylar bu motorda yoktur. Yağlamayla ilgili tek olay gresin
ömrünü doldurmasıdır (B2.08) ve çaresi yatağın değiştirilmesidir. Yeniden
greslenebilir yataklı büyük gövdelerde bu dal farklı kurulur.

**Rezonans neden VE kapısı.** Doğal frekansın bir uyarım frekansına yakın
olması tek başına büyük genlik üretmez; sönüm yeterliyse genlik sınırlı kalır.
Ağaç rezonansın bu biçimini modeller: yakınlık ve düşük sönüm birlikte.
Ağaçtaki tek VE kapısı budur. Doğal frekansın uyarım frekansına ne kadar yakın
sayılacağı için bir standart değeri kullanılmadı; formda %10 ayrım payı
seçildi. Sönüm için sayısal bir kabul sınırı verilmedi; değer
kaydedilir ve tesisin baz kaydıyla karşılaştırılır.

**Yatak arızasının sonraki evresi.** Yatak olayları burada titreşimi Bölge
D'ye taşıyacak şiddette tanımlıdır. Hasar ilerleyip sürtünme momentini
artırdığında aynı kusur akımı da yükseltir; bu evre T3'te ayrı bir olay olarak
yer alır (B3.07). Yüksek titreşim üreten her yatak kusuru akımı artırmaz.

**Yatak montajı.** Yatak ısıtılarak ya da presle takılır; çakılmaz. Kuvvet
sıkı geçen bilezikten verilir: mile takarken iç bilezikten, yuvaya sıkı geçen
bir yatakta dış bilezikten. Kuvvetin bilyalardan geçmesi yuvarlanma yollarında
iz bırakır.

**Güç kesme testi.** Elektromanyetik kuvvet gerilim kesildiği anda kaybolur.
Motor serbest yavaşlarken 100 Hz bileşeni hemen kayboluyorsa kaynak büyük
olasılıkla elektrikseldir. Bu test destekleyicidir: güç kesilince moment ve
pompanın çalışma koşulu da değişir, elektriksel ve mekanik sebepler bir arada
bulunabilir. Karar spektrum ve diğer ölçümlerle birlikte verilir.

**Boru zorlaması kontrolü.** Flanş cıvataları ancak pompa izole edildikten,
basınç boşaltıldıktan ve akışkan soğuduktan sonra gevşetilir. Motorun
enerjisini kesmek bu iş için yeterli değildir.
