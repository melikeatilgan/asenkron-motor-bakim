# T3: Aşırı akım yüklenmesi

## Tepe olay

> T3: Motor aşırı akımla yükleniyor.

Ölçülebilir tanım, iki durumdan biri:

- Motor rejimdeyken en az bir fazın akımı 31,1 A'i (1,10 × 28,3 A) aşıyor.
- Kalkış akımı (198 A) izin verilenden sık ya da uzun süre çekiliyor, ya da
  motor izin verilmeyen biçimde ters akımla frenleniyor (frenleme akımı kalkış
  akımı mertebesindedir ve sargıyı aynı biçimde ısıtır).

| Büyüklük | Değer | Kaynak |
|---|---|---|
| Anma akımı In | 28,3 A | WEG föyü, 400 V Δ |
| Aşırı akım eşiği | 31,1 A (%110) | Aşağıdaki açıklama |
| Kalkış akımı | 198 A (7,0 × In) | WEG föyü |
| Kilitli rotor dayanımı | 11 s sıcak, 19 s soğuk | WEG föyü |
| Faz akımı dengesizliği | ≤ %10 | Bu çalışmada seçilen tarama eşiği; 100 × en büyük sapma / ortalama |

**Eşik neden %110.** IEC 60947-4-1'e göre termik röle ayar akımının 1,05
katında iki saat açmaz, 1,20 katında iki saat içinde açar. Bu ikisinin arası,
motorun anma değerinin üstünde uzun süre çalışabildiği ve rölenin hemen
tepki vermediği bölgedir. %110 bu bandın içindedir.

**Bu ağaçta koruma neden yok.** T3 bir durumdur: motor fazla akım çekiyor.
Motorun kesilip kesilmediği T1'de modellenir. T1 bu ağacın tamamına transfer
eder ve koruma dalını orada ekler. Koruma burada da yer alsaydı iki kez
sayılmış olurdu.

## Önce ölçüm doğrulanır

"Motor fazla akım çekiyor" şikâyetlerinin bir kısmı ölçüm hatasıdır. Bunlar
tepe olayın sebebi değildir, çünkü akım gerçekte yüksek değildir. Bu yüzden
ağacın içinde değil, ağaçtan önce yapılacak doğrulama adımları olarak
listelendi.

| Kod | Doğrulama | Kabul kriteri | Form |
|---|---|---|---|
| Ö1 | Akım trafosu oranı röle ya da analizöre doğru girilmiş mi | Etiketle aynı | E-04 |
| Ö2 | Pens ampermetre kalibrasyonlu mu, doğru kademede mi | Kalibrasyon geçerli | E-05 |
| Ö3 | Üç faz da ayrı ayrı ölçüldü mü | Üç faz da kayıtlı | E-02 |
| Ö4 | Ölçüm rejimde mi alındı, kalkış akımı mı okundu | Kalkıştan en az 5 dk sonra | E-01 |

## Ağaç

```
T3  Motor aşırı akımla yükleniyor                           ◁ T1 buraya transfer ediyor
│
└─[VEYA]
   ├── A3.1  Mekanik yükün moment talebi anma değerini aşıyor
   │   └─[VEYA]
   │      ├── B3.01  Pompa çalışma noktası kaymış (debi fazla)
   │      ├── B3.02  Pompa çarkı gövdeye ya da aşınma halkasına sürtüyor
   │      ├── B3.03  Salmastra aşırı sıkılmış
   │      ├── B3.04  Akışkan yoğunluğu ya da viskozitesi tasarım değerinin üstünde
   │      ├── B3.05  Pompa tarafında mekanik sıkışma (pompa yatağı, yabancı cisim)
   │      ├── B3.06  Rotor statora sürtüyor
   │      └── B3.07  Motor yatağında ilerlemiş hasar, sürtünme momenti artmış
   │
   ├── A3.2  Motorun kendi iç arızası
   │   └─[VEYA]
   │      ├── B3.08  Sarım arası kısa devre
   │      └── A3.2.1  Rotor kafes arızası                   ◁ T2 buraya transfer ediyor
   │          └─[VEYA]
   │             ├── B3.09  Rotor çubuğu kırık ya da çatlak
   │             └── B3.10  Kısa devre halkası çatlak
   │
   ├── A3.3  Besleme kaynaklı akım artışı
   │   └─[VEYA]
   │      ├── B3.11  Faz kaybı (tek fazlama)
   │      ├── B3.12  Gerilim dengesizliği %1'in üstünde
   │      ├── B3.13  Gerilim düşük
   │      ├── B3.14  Gerilimde yüksek harmonik bozulma
   │      └── B3.15  Klemens ya da bara bağlantısı gevşek
   │
   └── A3.4  Kalkış ve frenleme kaynaklı akım yüklenmesi
       └─[VEYA]
          ├── B3.16  Kalkış sayısı üreticinin izin verdiği sınırın üstünde
          ├── B3.17  Kalkış süresi uzun
          └── B3.18  Ters akımla frenleme yapılıyor
```

Ağaç niteldir. Her temel olay, "tepe olayı doğuracak şiddette gerçekleşmiş"
hâliyle tanımlıdır. Hafif bir gerilim düşüklüğü ya da başlangıç aşamasındaki
tek bir kırık çubuk akımı eşiğin üstüne çıkarmaz; olay, eşiği aştıracak kadar
ilerlediğinde ağaçtaki yerini alır.

## Temel olaylar ve kontrolleri

| Kod | Temel olay | Nasıl kontrol edilir | Kabul kriteri | Form |
|---|---|---|---|---|
| B3.01 | Çalışma noktası kaymış | Basma basıncı ve debi, pompa eğrisiyle | Üreticinin izin verdiği aralıkta; mil gücü ≤ 15 kW | L-01 |
| B3.02 | Çark sürtüyor | Elle çevirme; sökümde gözle | Serbest dönüyor; sürtme izi yok | M-03, L-06 |
| B3.03 | Salmastra aşırı sıkı | Damlatma, salmastra kutusu sıcaklığı | Üretici değerinde damlatma | L-02 |
| B3.04 | Akışkan özelliği değişmiş | Proses verisi | Pompa tasarım değerinde | L-05 |
| B3.05 | Pompa tarafında sıkışma | Elle çevirme (enerji kesik ve kilitli) | Takılma yok | M-03 |
| B3.06 | Rotor statora sürtüyor | Elle çevirme, ses; sökümde gözle | Sürtme sesi ve izi yok | M-03, M-09 |
| B3.07 | Motor yatağında ilerlemiş hasar | Elle çevirme; yatak sıcaklığı ve sesi | Serbest dönüyor; sıcaklıkta artış eğilimi yok | M-03, Y-02 |
| B3.08 | Sarım arası kısa devre | Faz dirençleri; şüphede darbe testi | Direnç dengesizliği ≤ %2 | E-09 |
| B3.09 | Rotor çubuğu kırık | Akım imza analizi | Yan bant ana bileşenin ≥ 45 dB altında | E-10 |
| B3.10 | Kısa devre halkası çatlak | Akım imza analizi | Aynı | E-10 |
| B3.11 | Faz kaybı | Pens ampermetre, üç faz | Üç fazda da akım var; dengesizlik ≤ %10 | E-02 |
| B3.12 | Gerilim dengesizliği | Üç faz-faz gerilimi | ≤ %1 | E-03 |
| B3.13 | Gerilim düşük | Multimetre | 380–420 V | E-03 |
| B3.14 | Harmonik bozulma | Güç kalitesi analizörü | Gerilim THD ≤ %8 (tarama eşiği) | E-07 |
| B3.15 | Bağlantı gevşek | Termal kamera ya da tork | Aynı yükte fazlar arası fark < 4 K | E-06 |
| B3.16 | Sık kalkış | Sayaç ya da operatör kaydı | Üretici sınırı içinde | L-03 |
| B3.17 | Uzun kalkış | Kronometre ve pens ampermetre | Röle kalkışta açmıyor; 4 s'den uzunsa eğriyle karşılaştırılır | L-04 |
| B3.18 | Ters akımla frenleme | Kumanda şeması, gözlem | Yapılmıyor | L-07 |

## Ağaçların kapsamı dışında kalan kontrol

Sargı ile gövde arasındaki yalıtımın zayıflaması üç tepe olaydan birine
doğrudan gitmez. Sonucu toprak arızasıdır; kesilmesi kısa devre ve toprak
kaçağı korumasının işidir ve bu korumalar analizin kapsamı dışındadır. Yalıtım
direnci ölçümü yine de standart bir bakım kontrolü olduğu için formda tutuldu
(E-08) ve Olay sütununda KD koduyla gösterildi.

Ölçüm 500 V DC ile bir dakika yapılır, değer 40 °C'ye düzeltilir ve en az 5 MΩ
aranır (IEEE 43). Test bittikten sonra sargı en az dört dakika topraklanarak
boşaltılır; test gerilimi sargıda yük bırakır.

## Notlar

**Yatak arızası ve akım.** T2'deki yatak olayları (B2.08–B2.12) yüksek
titreşim üretir ama akımı mutlaka artırmaz. Akımın eşiği geçmesi için hasarın
sürtünme momentini belirgin biçimde artıracak kadar ilerlemesi gerekir. Bu
yüzden burada ayrı bir olay olarak yer alır (B3.07): aynı kusurun geç evresi.
Bir yatak olayının T2'de görülmesi T3'ün de gerçekleştiği anlamına gelmez.

**Rotor kafes arızası.** Aynı ayrım rotor çubukları için de geçerlidir. Tek
bir kırık çubuk akım spektrumunda yan bant üretir ama toplam akımı eşiğin
üstüne çıkarmayabilir. B3.09 ve B3.10, kaymayı ve akımı belirgin biçimde
artıracak kadar ilerlemiş arızayı anlatır.

**Düşük gerilim.** Yük değişmezken gerilim düşerse motor aynı gücü daha yüksek
akımla çeker; gerilim %10 düştüğünde anma yükündeki akım kabaca %11 artar ve
eşiği geçer. IEC 60034-1'de anma frekansında gerilimin ±%5'i Bölge A'dır; motor
burada anma momentini sürekli verir. ±%10 Bölge B'nin sınırıdır; motor çalışır
ama sıcaklık artışı büyür ve bu bölgede uzun süre çalışma önerilmez. Form bu
yüzden 380–420 V'u kabul aralığı alır; dışındaki okumalar kaydedilir ve sebebi
araştırılır.

**Gerilim dengesizliği.** Dengesiz gerilim ters bileşen akımı doğurur; bu akım
rotorda yaklaşık iki katı şebeke frekansında dolaşır ve ısıya dönüşür. NEMA
MG-1'e göre %1'e kadar dengesizlikte motor anma yükünde çalışabilir, üstünde
yük düşürülür, %5'in üstünde çalışma önerilmez. Sıcaklık artışındaki ilave
yaklaşık 2 × (dengesizlik yüzdesi)² kadardır: %3 dengesizlik sıcaklık artışını
yaklaşık %18 büyütür.

**Harmonik eşiği.** %8, EN 50160'ın şebeke gerilimi için verdiği sınırdır ve
orada bir haftalık ölçümün %95'i için tanımlıdır. Formdaki tek okuma bu
uygunluğu kanıtlamaz; burada yalnızca tarama eşiği olarak kullanıldı. Aşılırsa
bir haftalık kayıt alınır.

**Faz kaybı.** Bir faz koptuğunda motor kalan iki iletkenden beslenir. Yük
değişmezse hat akımı kabaca 1,7 katına çıkar; bu, gücün ve güç katsayısının
aynı kaldığı varsayımıyla yapılmış bir yaklaşımdır. Yük yüksekse motor devrilir
ve durur.

**Pompa çalışma noktası.** Radyal çarklı santrifüj pompada mil gücü debiyle
birlikte artar. Basma vanası açıldıkça ya da sistem direnci düştükçe motor daha
çok yüklenir. Aynı sebeple çarkın tıkanması debiyi ve gücü düşürür; ağaçta
yalnızca mekanik sürtme yer alır (B3.02). Eksenel ve karışık akışlı pompalarda
eğilim terstir; bu not onlara uygulanmaz.

**Faz dirençleri neyi göstermez.** Faz dirençlerinin birbirine yakın çıkması
sarım arası yalıtımın sağlam olduğunu kanıtlamaz; birkaç sarımlık kısa devre
direnç ölçümünde görünmeyebilir. Bu bir tarama testidir. Şüphe varsa darbe
(surge) testi yapılır.

**Akım imza analizi.** Kırık rotor çubuğu stator akımında şebeke frekansının
iki yanında, 50 ± 2·s·f frekanslarında yan bant üretir. Yan bantların yeri ve
genliği yüke bağlıdır; ölçüm en az %75 yükte alınır ve frekans o andaki gerçek
kaymayla hesaplanır. −45 dB'yi bu çalışmada tarama değeri olarak seçtim; asıl
bakılan zaman içindeki artıştır.

**Kalkış.** Kalkış akımı anma akımının yedi katıdır. Sık kalkış, uzun kalkış ve
ters akımla frenleme bu akımın sargıda bıraktığı ısıyı artırır. Class 10 termik
röle 7,2 × ayar akımında soğuk durumdan en erken 4 saniyede açar; kalkış bundan
uzun sürerse röle normal kalkışta açabilir. Sıcak rölede bu süre daha kısadır.
Formdaki 4 saniye bir uygunluk sınırı değil, eğriye bakmayı gerektiren
eşiktir; kesin değerlendirme ölçülen kalkış akımı ve süresi seçilen rölenin
açma eğrisiyle karşılaştırılarak yapılır.
