# Minimal kesme kümeleri

## Tanımlar

**Kesme kümesi:** birlikte gerçekleştiğinde tepe olayı doğuran temel olay grubu.

**Minimal kesme kümesi:** içinden bir olay çıkarıldığında artık tepe olayı
doğurmayan kesme kümesi.

**Tek elemanlı kesme kümesi:** tek başına tepe olayı doğuran olay.

Ağaç hangi olayların tepe olaya gidebileceğini gösterir. Kesme kümeleri bunların
hangi birleşimlerle gittiğini gösterir.

## Yöntem

1. VEYA kapısının altındaki her dal ayrı bir küme verir.
2. VE kapısının altındaki dallar aynı kümede birleşir.
3. Transferler yerine konur. Döngü yoktur: T1 yalnızca T3'e, T2 yalnızca
   T3'ün rotor kafes dalına gider; T3'ten başka ağaca transfer yoktur.
4. Bir kümeyi içeren daha büyük kümeler atılır (yutma kuralı).
5. İki ağaçta geçen aynı olay tek kodla yazılır: B2.03 (fan) T1 ve T2'de,
   rotor kafes olayları (B3.09, B3.10) T3 ve T2'de aynı kodla geçer.

Sayılar elle sayılmadı. Ağaçlar [`kesme_kumeleri.py`](kesme_kumeleri.py)
içinde tanımlı; betik minimal kesme kümelerini hesaplar ve formdaki her
maddenin tanımlı bir koda, her olayın da formda en az bir maddeye bağlı
olduğunu denetler.

```
python kesme_kumeleri.py
```

## Sonuçlar

| Tepe olay | Minimal kesme kümesi | Tek elemanlı | İki elemanlı | Üç elemanlı |
|---|---|---|---|---|
| T1 Sargı aşırı sıcaklığı kesilmiyor | 144 | 0 | 36 | 108 |
| T2 Titreşim Bölge D | 21 | 20 | 1 | 0 |
| T3 Aşırı akım yüklenmesi | 18 | 18 | 0 | 0 |

Üç ağaçta toplam 49 benzersiz temel olay var.

### T1

T1'in kümeleri üç gruptan oluşur:

| Grup | Küme yapısı | Sayı |
|---|---|---|
| Herhangi bir ısınma sebebi + kontaktör yapışması | {ısınma, B1.11} | 18 + 6 = 24 |
| Soğutma arızası + PTC yolu arızası | {soğutma, PTC} | 6 × 2 = 12 |
| Akımla gelen ısınma + PTC yolu arızası + termik yol arızası | {akım, PTC, termik} | 18 × 2 × 3 = 108 |

Bu modelde tek elemanlı küme yoktur. Bunun sebebi tepe olayın tanımıdır: T1,
sıcaklığın sınırı aşmasını değil, aşıp da kesilmemesini modeller; her ısınma
sebebinin yanında en az bir koruma arızası yer alır.

İki elemanlı 36 küme en kısa yollardır ve iki şeyi gösterir:

- Kontaktör iki koruma yolunun ortak elemanıdır. Yapışmış bir kontaktör, 24
  ısınma sebebinden herhangi biriyle birlikte tepe olaya gider.
- Soğutma arızalarında akıma bakan koruma devreye girmez. PTC yolu
  çalışmıyorsa tıkalı bir fan ızgarası tek bir koruma arızasıyla tepe olaya
  gider.

### T2 ve T3

T2'de 20 olay tek başına tepe olaya gider; tek istisna rezonanstır
({B2.17, B2.18}). T3'te 18 olayın hepsi tek elemanlıdır.

Bu iki ağaçta tepe olay bir durumdur (titreşim yüksek, akım yüksek) ve koruma
modele dâhil değildir. Bu yüzden T1'in küme sayılarıyla karşılaştırılmazlar.
T3'ün kesilip kesilmediği zaten T1'in içinde modellenmiştir.

## Koruma olayları

T1'in 144 kümesinin her birinde koruma grubundan en az bir olay vardır.

| Kod | Olay | Geçtiği küme sayısı | Kontrol |
|---|---|---|---|
| B1.06 | PTC devresi köprülenmiş | 60 | P-01 |
| B1.07 | PTC rölesi arızalı ya da çıkışı bağlı değil | 60 | P-02 |
| B1.08 | Termik röle ayarı yüksek | 36 | P-03 |
| B1.09 | Açma sınıfı motorla uyumsuz | 36 | P-04 |
| B1.10 | Termik röle arızalı ya da kontağı bağlı değil | 36 | P-05 |
| B1.11 | Kontaktör ana kontakları yapışmış | 24 | P-06 |

PTC yolundaki iki olay birlikte 144 kümenin 120'sinde geçer. Kontaktör daha az
kümede geçer ama geçtiği kümelerin hepsi iki elemanlıdır.

Form bu altı kontrolle başlar. Gerekçesi sayıların büyüklüğü değil, yapıdır:
koruma grubu bütün ısınma senaryolarının ortak yoludur ve buradaki bir arıza
çalışan motorda kendini göstermez; ancak bakılırsa bulunur.

## Birden çok tepe olayda geçen olaylar

| Olaylar | Geçtiği ağaçlar | Açıklama |
|---|---|---|
| B3.09, B3.10 (rotor kafesi) | T1, T2, T3 | Titreşim, akım artışı ve akım üzerinden ısınma |
| B2.03 (fan) | T1, T2 | Soğutmayı bozar, dengesizlik yaratır |
| T3'ün diğer olayları | T1, T3 | Transfer yoluyla |

Yatak olayları (B2.08–B2.12) yalnızca T2'dedir. Hasar ilerleyip sürtünme
momentini artırdığında T3'te ayrı bir olay olarak yer alır (B3.07) ve oradan
T1'e gider. Bu bir Boolean transfer değil, aynı kusurun zaman içindeki
ilerlemesidir.

## Bu sonuçlar nasıl okunmalı

Analiz niteldir. Olayların olasılığı ve sonuçlarının şiddeti hesaplanmamıştır.

Küme sayıları bu Boolean modelin yapısal özellikleridir ve olayların nasıl
bölündüğüne bağlıdır: bir sebebi iki ayrı kodla yazmak sayıyı artırır. Bir
olayın çok kümede geçmesi riskinin büyük olduğu anlamına gelmez. Gerçek bir
önceliklendirme ve kontrol periyotlarının seçimi için arıza sıklığı, arızanın
gelişme süresi ve üretici önerileri gerekir; formdaki periyotları bu analizden
türetmedim, başlangıç değeri olarak seçtim.

Senaryodaki koruma kapsamı için şu söylenebilir. Sıcaklık ve akım için otomatik
kesme vardır (PTC ve termik röle). Titreşim için otomatik bir izleme ya da kesme
tanımlı değildir; titreşim ancak aylık ölçümle (V-01) fark edilir ve iki ölçüm
arasında gelişen bir arıza görülmez. Yatak sıcaklığı için de durum aynıdır.

## Sürekli izlemeyle kapatılabilecek boşluk

Aşağıdaki büyüklükler aylık kontrollerin arasında da değişebilir; sürekli
izlenirse bu boşluk daralır:

| Ölçülen | İlgili olaylar |
|---|---|
| Yatak gövdesinde titreşim hızı (DE, NDE) | T2'nin tamamı |
| Yatak sıcaklığı (DE, NDE) | B2.08–B2.12, B3.07 |
| Üç faz akımı | T3; faz kaybı ve dengesizlik (B3.11, B3.12) |
| PTC devresinin direnci | B1.06 (köprü) |

Bir izleme cihazının göremeyeceği şeyler formda kalır: termik röle ayarı ve
sınıfı, kontaktör kontaklarının durumu, ölçüm cihazlarının doğruluğu.
