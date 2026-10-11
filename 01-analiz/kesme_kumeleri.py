# -*- coding: utf-8 -*-
"""
Uc ariza agacinin minimal kesme kumelerini hesaplar ve aylik formla
karsilastirir.

    python kesme_kumeleri.py

Agaclar asagida ic ice demetlerle yazili: ("VEYA", ...), ("VE", ...).
Yaprak, temel olay kodudur ("B3.11" gibi). Belgelerdeki sayilar bu
betigin ciktisidir; agac degisirse once burasi degisir.
"""
import os
import runpy
from itertools import product

# --- T2: yatak govdesinde titresim Bolge D ---------------------------------
YATAK = ("VEYA", "B2.08", "B2.09", "B2.10", "B2.11", "B2.12")
# --- T3: asiri akim yuklenmesi ---------------------------------------------
ROTOR_KAFES = ("VEYA", "B3.09", "B3.10")
T3 = ("VEYA",
      ("VEYA", "B3.01", "B3.02", "B3.03", "B3.04", "B3.05", "B3.06", "B3.07"),  # A3.1 yuk
      ("VEYA", "B3.08", ROTOR_KAFES),                                           # A3.2 motor ici
      ("VEYA", "B3.11", "B3.12", "B3.13", "B3.14", "B3.15"),                    # A3.3 besleme
      ("VEYA", "B3.16", "B3.17", "B3.18"))                                      # A3.4 kalkis ve frenleme
T2 = ("VEYA",
      ("VEYA", "B2.01", "B2.02", "B2.03", "B2.04"),     # A2.1 dengesizlik
      ("VEYA", "B2.05", "B2.06", "B2.07"),              # A2.2 eksen kacikligi
      YATAK,                                            # A2.3 yatak
      ("VEYA", "B2.13", "B2.14", "B2.15", "B2.16"),     # A2.4 gevseklik
      ("VE", "B2.17", "B2.18"),                         # A2.5 rezonans
      ("VEYA", "B2.19", "B2.20", ROTOR_KAFES))          # A2.6 elektriksel
# --- T1: sargi asiri sicakligi kesilmiyor ----------------------------------
SOGUTMA = ("VEYA", "B2.03", "B1.01", "B1.02", "B1.03", "B1.04", "B1.05")
PTC_YOLU = ("VEYA", "B1.06", "B1.07")
TERMIK_YOLU = ("VEYA", "B1.08", "B1.09", "B1.10")
KONTAKTOR = "B1.11"
T1 = ("VEYA",
      # akimla birlikte gelen isinma: iki koruma yolu da gorur
      ("VE", T3, ("VEYA", KONTAKTOR, ("VE", PTC_YOLU, TERMIK_YOLU))),
      # akim artmadan gelen isinma: yalniz PTC gorur
      ("VE", SOGUTMA, ("VEYA", KONTAKTOR, "B1.06", "B1.07")))

AGACLAR = {"T1": T1, "T2": T2, "T3": T3}
# Formda gecen ama temel olay olmayan kodlar: olcum gecerliligi (Ö), tepe olayin
# kendisi (T2, T3) ve agaclarin kapsami disindaki kontrol (KD)
OLCUM = {"Ö1", "Ö2", "Ö3", "Ö4", "T2", "T3", "KD"}


def kumeler(dugum):
    """Dugumun kesme kumeleri (frozenset listesi), henuz indirgenmemis."""
    if isinstance(dugum, str):
        return [frozenset([dugum])]
    kapi, altlar = dugum[0], [kumeler(a) for a in dugum[1:]]
    if kapi == "VEYA":
        return [k for alt in altlar for k in alt]
    return [frozenset().union(*secim) for secim in product(*altlar)]


def minimal(liste):
    """Yutma kurali: baska bir kumeyi iceren kume atilir."""
    tekil = sorted(set(liste), key=len)
    sonuc = []
    for k in tekil:
        if not any(m <= k for m in sonuc):
            sonuc.append(k)
    return sonuc


def yapraklar(dugum):
    if isinstance(dugum, str):
        return {dugum}
    return set().union(*(yapraklar(a) for a in dugum[1:]))


def form_olaylari():
    yol = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "02-saha-dokumanlari", "aylik-form", "form-uret.py")
    maddeler = runpy.run_path(yol)["MADDELER"]
    return {m[0]: set(m[5].split()) for m in maddeler if len(m) == 6}


if __name__ == "__main__":
    mks = {ad: minimal(kumeler(a)) for ad, a in AGACLAR.items()}
    for ad, liste in mks.items():
        boy = {}
        for k in liste:
            boy[len(k)] = boy.get(len(k), 0) + 1
        print("%s: %3d minimal kesme kumesi  %s" % (
            ad, len(liste), "  ".join("%d elemanli: %d" % b for b in sorted(boy.items()))))

    print("\nT1 de koruma olaylarinin gectigi kume sayisi (toplam %d):" % len(mks["T1"]))
    for kod in ("B1.06", "B1.07", "B1.08", "B1.09", "B1.10", "B1.11"):
        print("  %s: %3d" % (kod, sum(kod in k for k in mks["T1"])))
    ptc = sum(bool(k & {"B1.06", "B1.07"}) for k in mks["T1"])
    print("  PTC yolu (B1.06 veya B1.07): %d" % ptc)

    tum = set().union(*(yapraklar(a) for a in AGACLAR.values()))
    print("\nbenzersiz temel olay: %d" % len(tum))
    print("birden cok tepe olayda gecenler:")
    for kod in sorted(tum):
        gecen = [ad for ad, liste in mks.items() if any(kod in k for k in liste)]
        if len(gecen) > 1:
            print("  %s: %s" % (kod, ", ".join(gecen)))

    # Oz denetim: her olayin formda en az bir kontrolu var, formda tanimsiz kod yok.
    form = form_olaylari()
    formdaki = set().union(*form.values())
    assert not (formdaki - tum - OLCUM), "formda tanimsiz kod: %s" % sorted(formdaki - tum - OLCUM)
    assert not (tum | OLCUM) - formdaki, "kontrolu olmayan olay: %s" % sorted((tum | OLCUM) - formdaki)
    assert not any(len(k) == 1 for k in mks["T1"]), "T1 de tek elemanli kume var"
    print("\nform: %d madde, butun olaylar kapsaniyor" % len(form))
