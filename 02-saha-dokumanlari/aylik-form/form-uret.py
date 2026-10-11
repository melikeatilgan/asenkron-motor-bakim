# -*- coding: utf-8 -*-
"""
Aylık bakım kontrol formu üreteci.

    python form-uret.py

Çıktı: aylik-bakim-formu.html (tarayıcıdan Ctrl+P, A4, PDF)

Madde eklemek için MADDELER listesi düzenlenir. Her maddenin son alanı,
01-analiz klasöründeki arıza ağaçlarının temel olay kodlarıdır ve formda
"Olay" sütununa basılır. Kodsuz madde eklenmez.
"""
import io

# periyot: A=aylık  3A=üç aylık  Y=yıllık  AR=arıza hâlinde / sökümde
# (kod, madde, yöntem, kabul kriteri, periyot, olaylar)
# olaylar: B kodları temel olay, T2/T3 tepe olayın kendisi, Ö ölçüm geçerliliği
MADDELER = [
 ("KORUMA", "T1'in bütün kesme kümelerinde bu gruptaki olaylardan en az biri yer alır. Bu yüzden form bunlarla başlar."),
 ("P-01","PTC devresi soğuk direnci","Motor soğukken, panoda PTC rölesi klemenslerinde, uçlar ayrılarak; düşük gerilimli ohmmetre (megger **uygulanmaz**)","60–750 Ω ve aynı sıcaklıktaki devreye alma kaydıyla uyumlu. Belirgin düşüş: köprü şüphesi. Sonsuz: kopuk","A","B1.06"),
 ("P-02","PTC rölesi işlev testi","Röle girişine ayarlı direnç bağlanır: açma, açık devre ve varsa kısa devre algılaması denenir","Röle föyündeki dirençlerde açıyor; kontaktör bırakıyor","3A","B1.07"),
 ("P-03","Termik röle akım ayarı","Röle skalası, gözle","Ayar = 28,3 A (In). Üstü kabul edilmez","A","B1.08"),
 ("P-04","Termik röle açma sınıfı","Röle etiketi ve açma eğrisi","Class 10; eğri motorun kalkış süresi ve kilitli rotor dayanımıyla (sıcakta 11 s) karşılaştırılmış","Y","B1.09"),
 ("P-05","Termik röle test düğmesi","Test düğmesi; yardımcı kontak ve kumanda devresi","Kontaktör bırakıyor. Akım-zaman eğrisini sınamaz","A","B1.10"),
 ("P-06","Kontaktör ana kontakları","Bobin enerjisiz, motor uçları ayrılmış; kutup başına süreklilik","Üç kutup da açık (yapışma yok)","3A","B1.11"),

 ("ELEKTRİKSEL", "Akım, gerilim, termal görüntü, harmonik ve spektrum ölçümleri motor rejimdeyken, kalkıştan en az 5 dakika sonra alınır. Tork, yalıtım ve direnç kontrolleri enerji kesik ve kilitliyken yapılır."),
 ("E-01","Ölçüm koşulu","Kalkıştan sonra geçen süre ve yük durumu kaydedilir","≥ 5 dk, normal işletme yükü","A","Ö4"),
 ("E-02","Üç faz akımı","Pens ampermetre, L1 / L2 / L3 ayrı ayrı","Her faz ≤ 28,3 A; dengesizlik (100 × en büyük sapma / ortalama) ≤ %10. > 31,1 A sürekli: iş emri","A","T3 B3.11 Ö3"),
 ("E-03","Faz-faz gerilimleri ve dengesizlik","Multimetre; dengesizlik = 100 × en büyük sapma / ortalama","380–420 V **ve** dengesizlik ≤ %1","A","B3.12 B3.13"),
 ("E-04","Akım ölçü devresi oranı","Röle / analizör ayarı ile akım trafosu etiketi","Aynı","3A","Ö1"),
 ("E-05","Pens ampermetre kalibrasyonu","Kalibrasyon etiketi","Geçerli","Y","Ö2"),
 ("E-06","Klemens bağlantıları","Yük altında termal kamera; ya da enerjisiz ve kilitliyken tork anahtarı","Aynı yükte fazlar arası sıcaklık farkı < 4 K; tork üretici değerinde","3A","B3.15"),
 ("E-07","Gerilim harmonikleri (analizör varsa)","Güç kalitesi analizörü, motor klemensinde","Gerilim THD ≤ %8 (tarama eşiği; aşılırsa bir haftalık kayıt alınır)","Y","B3.14"),
 ("E-08","Yalıtım direnci","Enerji kesik ve kilitli, motor kablosundan ayrılmış. 500 V DC, 1 dk, sargı–gövde. **Test sonrası sargı en az 4 dk topraklanarak boşaltılır**","40 °C'ye düzeltilmiş ≥ 5 MΩ (IEEE 43). Sargı sıcaklığı kaydedilir","Y","KD"),
 ("E-09","Faz dirençleri","Enerji kesik ve kilitli; mikro-ohmmetre, köprüler sökük, üç faz","Dengesizlik (100 × en büyük sapma / ortalama) ≤ %2. Tarama testidir; şüphede darbe (surge) testi","Y","B3.08"),
 ("E-10","Akım imza analizi","Akım spektrumu, yük ≥ %75; 50 Hz ± 2·s·f yan bantları (anma kaymasında 48,3 / 51,7 Hz)","Yan bant ana bileşenin ≥ 45 dB altında; eğilim izlenir","Y","B3.09 B3.10"),

 ("TİTREŞİM", "DE ve NDE yatak gövdelerinde yatay ve düşey ölçülür; karar en yüksek radyal okumaya göre verilir. Eksenel ölçüm eğilim için kaydedilir."),
 ("V-01","Titreşim hızı, RMS (10–1000 Hz)","Titreşim ölçer; 4 radyal, 2 eksenel nokta","≤ 2,8 mm/s. > 2,8 ve ≤ 4,5: iş emri. > 4,5: **durdur**. Önceki ölçüme göre 0,7 mm/s'den büyük değişim incelenir","A","T2"),
 ("V-02","Titreşim spektrumu","FFT, çözünürlük ≤ 0,5 Hz: 1×, 2×, 100 Hz ve yatak frekansları","Aynı yükte önceki kayda göre yeni tepe ya da belirgin artış yok","3A","B2.02 B2.10 B2.19 B2.20"),
 ("V-03","Güç kesme testi (titreşim yüksekse)","Güç kesilir, 100 Hz bileşeni izlenir","Hemen kayboluyorsa elektriksel kaynak şüphesi. Tek başına karar verdirmez","AR","B2.19 B2.20"),
 ("V-04","Rezonans kontrolü","Darbe (bump) testi, motor dururken; doğal frekanslar ve sönüm kaydedilir","En düşük doğal frekans ≥ 30,7 Hz (rijit destek koşulu); 24,6 / 49,2 / 100 Hz'e %10'dan yakın doğal frekans yok; sönüm baz kayda göre belirgin azalmamış","Y","B2.17 B2.18"),

 ("MEKANİK", ""),
 ("M-01","Ayak ve yatak kapağı cıvataları","Tork anahtarı","Üretici torku","3A","B2.13 B2.16"),
 ("M-02","Kaplin elemanı","Gözle: çatlak, aşınma, sertleşme","Hasar yok","A","B2.04"),
 ("M-03","Serbest dönme","Enerji kesik ve kilitli; mil elle çevrilir","Takılma, sürtme sesi yok","3A","B3.02 B3.05 B3.06 B3.07"),
 ("M-04","Ayak altı boşluğu (soft foot)","Cıvata gevşetilirken komparatör ya da sentil","≤ 0,05 mm","Y","B2.14"),
 ("M-05","Eksen hizalaması","Lazer ya da komparatör; ayrıca sıcak duruşta (çalışma sıcaklığında durdurulup kilitlendikten hemen sonra)","Paralel ≤ 0,09 mm; açısal ≤ 0,07 mm/100 mm (kaplin üreticisinin değeri varsa o)","3A","B2.05 B2.07"),
 ("M-06","Boru zorlaması","Pompa izole ve basınçsız; flanş cıvataları gevşetilirken kaplinde komparatör","Mil kayması ≤ 0,05 mm","Y","B2.06"),
 ("M-07","Kaide ve grout","Gözle; çekiçle tıklatma","Çatlak yok, boşluk sesi yok","3A","B2.15"),
 ("M-08","Yatak yuvası ve muylu çapı","Sökümde mikrometre","Üretici toleransı","AR","B2.12"),
 ("M-09","Rotor ve stator yüzeyi","Sökümde gözle","Sürtme izi yok","AR","B3.06"),

 ("YATAK", "Yataklar kapalı tiptir (ZZ) ve ömür boyu yağlıdır; sonradan gres basılmaz."),
 ("Y-01","Yatak çalışma saati","Çalışma saati sayacı, bakım kaydı","Üretici değişim süresi içinde. Süre bilinmiyorsa doğrulanmadı yazılır; yatak durumu Y-02 ve V-02 ile izlenir","A","B2.08"),
 ("Y-02","Yatak sıcaklığı ve sesi","Yatak gövdesinde temaslı termometre; dinleme çubuğu","Aynı yük ve ortamda önceki kayda göre artış eğilimi yok; düzensiz ses yok","A","B2.08 B2.11 B3.07"),
 ("Y-03","Takılan yatağın tipi","Yatak etiketi","DE 6309 ZZ C3, NDE 6209 ZZ C3","AR","B2.09"),
 ("Y-04","Yatak montaj yöntemi","İş kaydı","Isıtarak ya da presle; çakma yok. Kuvvet sıkı geçen bilezikten (mile takarken iç bilezik)","AR","B2.10"),
 ("Y-05","Yatak kapağı ve mil keçesi","Gözle","Keçe yerinde ve hasarsız; su, toz girişi izi yok","3A","B2.11"),

 ("SOĞUTMA", ""),
 ("G-01","Fan kapağı ızgarası","Gözle","Açık; toz, lif birikmesi yok","A","B1.01"),
 ("G-02","Gövde soğutma kanatçıkları","Gözle","Kanat dipleri temiz","A","B1.02"),
 ("G-03","Hava girişi önü","Gözle, şerit metre","Engel yok; üretici kılavuzundaki en az mesafe sağlanıyor","A","B1.03"),
 ("G-04","Fan","Enerji kesik ve kilitli; fan kapağı sökülür","Kanatlar tam, fan milde sıkı, birikinti yok","3A","B2.01 B2.03"),
 ("G-05","Soğutma havası sıcaklığı","Termometre, fan girişinde","≤ 40 °C","A","B1.04"),
 ("G-06","Rakım ve yük düşürme","Tesis rakımı ile motor föyü (bir kez, kayıt)","≤ 1000 m; üstündeyse yük düşürülmüş","Y","B1.05"),

 ("YÜK VE İŞLETME", ""),
 ("L-01","Pompa çalışma noktası","Basma basıncı ve debi; pompa eğrisi","Üreticinin izin verdiği aralıkta; mil gücü ≤ 15 kW","A","B3.01"),
 ("L-02","Salmastra","Damlatma, salmastra kutusu sıcaklığı","Yumuşak salmastra: üretici değerinde damlatma. Mekanik salmastra: sızıntı yok","A","B3.03"),
 ("L-03","Kalkış sayısı ve görev çevrimi","Sayaç ya da operatör kaydı","Üreticinin izin verdiği saatlik kalkış sayısı içinde","A","B3.16"),
 ("L-04","Kalkış süresi","Pens ampermetre ve kronometre","Termik röle kalkışta açmıyor. Süre kaydedilir; 4 s'den uzunsa röle eğrisiyle karşılaştırılır","3A","B3.17"),
 ("L-05","Akışkan yoğunluğu ve viskozitesi","Proses verisi","Pompa tasarım değerinde","3A","B3.04"),
 ("L-06","Pompa çarkı ve aşınma halkaları","Sökümde gözle","Sürtme izi yok","AR","B3.02"),
 ("L-07","Frenleme","Kumanda şeması, gözlem","Ters akımla frenleme yok","Y","B3.18"),
]

MOTOR = {
    "Üretici / tip": "WEG W22 IE3 (12863072)",
    "Anma gücü": "15 kW, S1",
    "Anma akımı In": "28,3 A (400 V Δ)",
    "Anma devri": "1475 d/dk (4 kutup)",
    "Gövde / mil yük.": "160L / 160 mm",
    "Yalıtım / koruma": "F sınıfı / IP55",
    "Yataklar": "DE 6309 ZZ C3 · NDE 6209 ZZ C3",
    "Titreşim sınıfı": "ISO 20816-3 Grup 2, rijit destek",
}

PERIYOT_ACIK = {
    "A":  "Aylık",
    "3A": "Üç aylık",
    "Y":  "Yıllık",
    "AR": "Arıza hâlinde / sökümde",
}

def kacis(m):
    return (m.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("**", "\x00"))

def kalin(m):
    p = kacis(m).split("\x00")
    out = ""
    for i, k in enumerate(p):
        out += ("<b>%s</b>" % k) if i % 2 else k
    return out

def uret():
    satirlar = []
    n = 0
    for m in MADDELER:
        if len(m) == 2:
            baslik, aciklama = m
            ek = ('<div class="gnot">%s</div>' % kacis(aciklama)) if aciklama else ""
            satirlar.append(
                '<tr class="grup"><td colspan="9"><span class="gad">%s</span>%s</td></tr>'
                % (kacis(baslik), ek))
            continue
        kod, madde, yontem, kriter, periyot, olaylar = m
        n += 1
        satirlar.append(
            '<tr>'
            '<td class="no">%d</td>'
            '<td class="kod">%s</td>'
            '<td class="md">%s</td>'
            '<td class="yt">%s</td>'
            '<td class="kr">%s</td>'
            '<td class="pr p-%s">%s</td>'
            '<td class="ev">%s</td>'
            '<td class="ol"></td>'
            '<td class="uy"><span>U</span><span>X</span></td>'
            '</tr>'
            % (n, kacis(kod), kalin(madde), kalin(yontem), kalin(kriter),
               periyot, periyot, "<br>".join(olaylar.split()))
        )
    kimlik = "".join(
        '<div class="kk"><span class="ke">%s</span><span class="kd">%s</span></div>' % (k, v)
        for k, v in MOTOR.items())
    periyotlar = " &nbsp;·&nbsp; ".join(
        "<b>%s</b> %s" % (k, v) for k, v in PERIYOT_ACIK.items())
    return (SABLON.replace("@KIMLIK@", kimlik)
                  .replace("@SATIRLAR@", chr(10).join(satirlar))
                  .replace("@PERIYOTLAR@", periyotlar)
                  .replace("@ADET@", str(n)))

SABLON = """<!DOCTYPE html>
<html lang="tr"><head><meta charset="utf-8">
<title>Aylık Bakım Kontrol Formu</title>
<style>
  @page { size: A4 portrait; margin: 10mm 9mm 9mm 9mm; }
  * { box-sizing: border-box; }
  body { font-family: Arial, "Helvetica Neue", sans-serif; font-size: 7.3pt;
         color: #000; background: #fff; margin: 0; line-height: 1.25; }
  h1 { font-size: 12pt; margin: 0 0 1mm 0; letter-spacing: .2px; }
  .ust { display: flex; justify-content: space-between; align-items: flex-end;
         border-bottom: 1.6pt solid #000; padding-bottom: 1.5mm; margin-bottom: 2mm; }
  .alt1 { font-size: 7pt; color: #333; }
  .rev { font-size: 6.6pt; text-align: right; line-height: 1.5; }

  .kimlik { display: grid; grid-template-columns: repeat(4, 1fr);
            border: .7pt solid #000; margin-bottom: 2mm; }
  .kk { border-right: .4pt solid #999; border-bottom: .4pt solid #999;
        padding: 1mm 1.4mm; }
  .kk:nth-child(4n) { border-right: none; }
  .kk:nth-child(n+5) { border-bottom: none; }
  .ke { display: block; font-size: 6.1pt; color: #555; text-transform: uppercase;
        letter-spacing: .3px; }
  .kd { display: block; font-weight: bold; font-size: 7.4pt; }

  .meta { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2mm;
          margin-bottom: 2.5mm; }
  .mf { border-bottom: .7pt solid #000; padding-bottom: 3.8mm; font-size: 6.4pt;
        color: #555; text-transform: uppercase; letter-spacing: .3px; }

  table { width: 100%; border-collapse: collapse; }
  thead { display: table-header-group; }
  tr { page-break-inside: avoid; }
  th { background: #000; color: #fff; font-size: 6.5pt; text-transform: uppercase;
       letter-spacing: .4px; padding: 1.1mm .8mm; text-align: left;
       border-right: .4pt solid #fff; }
  th:last-child { border-right: none; }
  td { border-bottom: .4pt solid #bbb; padding: .45mm .8mm; vertical-align: top; }
  tr.grup td { background: #e8e8e8; border-top: .9pt solid #000;
               border-bottom: .9pt solid #000; padding: .8mm .8mm; }
  .gad { font-weight: bold; font-size: 7.2pt; letter-spacing: .6px; }
  .gnot { font-size: 6.4pt; color: #444; font-style: italic; margin-top: .3mm; }

  .no { width: 5mm;  text-align: right; color: #888; font-size: 6.4pt; }
  .kod{ width: 9mm;  font-weight: bold; font-family: "Consolas", monospace;
        font-size: 6.9pt; }
  .md { width: 32mm; font-weight: bold; }
  .yt { width: 46mm; color: #333; }
  .kr { width: 47mm; }
  .pr { width: 7mm; text-align: center; font-weight: bold; font-size: 6.3pt; }
  .p-A  { background: #000; color: #fff; }
  .p-3A { background: #777; color: #fff; }
  .p-Y  { background: #ccc; }
  .p-AR { background: #fff; border: .4pt solid #999; }
  .ev { width: 10mm; font-family: "Consolas", monospace; font-size: 6pt;
        color: #444; border-left: .4pt solid #bbb; }
  .ol { width: 14mm; border-left: .4pt solid #bbb; }
  .uy { width: 12mm; border-left: .4pt solid #bbb; text-align: center;
        white-space: nowrap; }
  .uy span { display: inline-block; width: 4mm; height: 4mm; line-height: 3.7mm;
             border: .6pt solid #000; font-size: 6.2pt; margin: 0 .3mm; color: #999; }

  .son { page-break-inside: avoid; }
  .periyot { margin-top: 1.5mm; font-size: 6.5pt; color: #333; }
  .aksiyon { margin-top: 2mm; border: .7pt solid #000; }
  .aksiyon .ab { background: #000; color: #fff; font-size: 6.6pt; padding: 1mm 1.4mm;
                 text-transform: uppercase; letter-spacing: .5px; font-weight: bold; }
  .aksiyon .ar { border-bottom: .4pt solid #999; height: 5.2mm; }
  .aksiyon .ar:last-child { border-bottom: none; }

  .imza { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm;
          margin-top: 4.5mm; }
  .imf { border-top: .7pt solid #000; padding-top: 1mm; font-size: 6.4pt;
         color: #555; text-transform: uppercase; letter-spacing: .3px; }
  .dip { margin-top: 2mm; padding-top: 1mm; border-top: .4pt solid #bbb;
         font-size: 6.2pt; color: #555; }
</style></head><body>

<div class="ust">
  <div>
    <h1>ASENKRON MOTOR AYLIK BAKIM KONTROL FORMU</h1>
    <div class="alt1">Arıza ağacına dayalı kontrol listesi &nbsp;·&nbsp;
      @ADET@ madde &nbsp;·&nbsp; iki sayfa</div>
  </div>
  <div class="rev">Form no: <b>BKM-AM-01</b><br>Rev. 2 &nbsp;·&nbsp; 2026-10</div>
</div>

<div class="kimlik">@KIMLIK@</div>

<div class="meta">
  <div class="mf">Motor etiket no / konum</div>
  <div class="mf">Tarih</div>
  <div class="mf">Kontrol eden</div>
  <div class="mf">Çalışma saati (h)</div>
</div>

<table>
  <thead><tr>
    <th></th><th>Kod</th><th>Kontrol maddesi</th><th>Yöntem / alet</th>
    <th>Kabul kriteri</th><th>P</th><th>Olay</th><th>Ölçülen</th><th>U / X</th>
  </tr></thead>
  <tbody>
@SATIRLAR@
  </tbody>
</table>

<div class="son">
<div class="periyot"><b>P = periyot:</b> @PERIYOTLAR@ &nbsp;&nbsp;|&nbsp;&nbsp;
  <b>U</b> = uygun, <b>X</b> = uygun değil (uygun olmayan her madde için aşağıya iş emri yazılır)</div>

<div class="aksiyon">
  <div class="ab">Uygun olmayan maddeler ve açılan iş emirleri</div>
  <div class="ar"></div><div class="ar"></div><div class="ar"></div>
</div>

<div class="imza">
  <div class="imf">Kontrol eden: ad, imza</div>
  <div class="imf">Onaylayan: ad, imza</div>
  <div class="imf">Bir sonraki kontrol tarihi</div>
</div>

<div class="dip">
  Eşikler referans motorun föyünden, ISO 20816-3, IEC 60034-1, IEC 60947-4-1,
  IEEE 43'ten ve kaynaklar belgesinde listelenen, bu çalışmada seçilen tarama eşiklerinden
  oluşur; başka bir motorda yeniden hesaplanır. Olay sütunu: B kodları
  <b>01-analiz</b> klasöründeki temel olaylar, T2 ve T3 tepe olayın kendisi, Ö ölçümün
  geçerliliği, KD ağaçların kapsamı dışındaki standart kontrol. "Üretici değeri" isteyen
  maddeler, değer forma yazılmadan uygun işaretlenmez. Önceki kayıtla karşılaştırılan
  maddelerde önceki ölçüm yoksa bu ölçüm başlangıç kaydıdır: "Ölçülen" sütununa değerin
  yanına "baz" yazılır. Sayısal sınırı olan kısım o gün de U / X ile işaretlenir; yalnız
  eğilime bakan kısım varsa U / X boş kalır. Durdurma kuralları yine geçerlidir.
  Her müdahaleden önce enerji ayırıcıdan kesilir, ayırıcı açık konumda kilitlenir ve
  etiketlenir, gerilim yokluğu ölçülür.
</div>
</div>

</body></html>
"""

if __name__ == "__main__":
    html = uret()
    with io.open("aylik-bakim-formu.html", "w", encoding="utf-8") as f:
        f.write(html)
    n = sum(1 for m in MADDELER if len(m) == 6)
    g = sum(1 for m in MADDELER if len(m) == 2)
    print("aylik-bakim-formu.html yazildi")
    print("  %d kontrol maddesi, %d grup" % (n, g))
    for p in ("A", "3A", "Y", "AR"):
        print("  %-3s %2d madde" % (p, sum(1 for m in MADDELER
                                            if len(m) == 6 and m[4] == p)))
