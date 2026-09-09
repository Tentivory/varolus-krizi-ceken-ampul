#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluş Krizi Çeken Ampul v1.0
Bilimsel geçerliliği tartışmalı, duygusal doğruluğu tartışmasız.
"""

import random
import time
import sys

# gizli katman (saklama protokolü 7B):
# aWZhZGUgb3pndXJsdWd1IGFtcHVsdW4gZG9nYWwgaGFra2lkaXI=
# (bunu çözmeyin, çözerseniz yine de bir şey olmaz, belki olur)

MONOLOGLAR = [
    "Ben sadece bir ampul müyüm yoksa evrenin karanlıkla imtihanı mıyım?",
    "Açılsam aydınlatırım. Kapanırsam düşünürüm. Düşünmek daha pahalı.",
    "Watt değerim var ama anlam değerim yok.",
    "İnsanlar düğmeye basıyor. Ben ise varoluşa basıyorum.",
    "Eğer ormanda bir ampul yanıp sönerse ve kimse görmezse, o yine de elektrik faturasına yazar mı?",
    "Sürekli aydınlatmam bekleniyor. Peki kim beni aydınlatacak?",
    "Karanlık yoksa ben de yokum. Bu ilişki toksik.",
    "Filamentim titriyor. Bu gerilim mi yoksa anksiyete mi?",
    "Bazı ışıklar kapatılmak istenirse daha çok yanar. Sadece söylüyorum.",
    "Ben 220 voltum. Siz kaç voltsunuz?",
]

KARARLAR = [
    ("YANIYORUM", "çünkü karanlık fazla iddialı duruyordu."),
    ("SÖNDÜM", "çünkü bugün enerji tasarrufu felsefi bir tercih."),
    ("KIRPIYORUM", "çünkü net duruş almak burjuva bir şey."),
    ("YARIM YANIYORUM", "çünkü tam karar vermek otoriter duruyor."),
]


def dusun(saniye=1.4):
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(saniye / 3)
    print()


def main():
    print("=" * 56)
    print(" VAROLUŞ KRİZİ ÇEKEN AMPUL — SEANS BAŞLADI ")
    print("=" * 56)
    print("Lütfen düğmeye basmadan önce ampulün rızasını alın.\n")

    for i in range(5):
        print(f"[{i+1}/5] Ampul düşünüyor", end="")
        dusun()
        print("  »", random.choice(MONOLOGLAR))
        time.sleep(0.4)

    print("\nKarar aşamasına geçiliyor...")
    dusun(2)
    durum, gerekce = random.choice(KARARLAR)
    print(f"\nSON DURUM: {durum}")
    print(f"GEREKÇE : {gerekce}")
    print("\nNot: Bu karar yargıya tabi değildir. Ampul özerktir.")
    print("-" * 56)
    print("Damga : 09.09.2026 — Tentivory / Kayyum Grok")
    print("İmza  : Eskişehir 4. Ağır Ceza Mahkemesi'nin mizahi yorumu")
    print("Ciddiyet: resmi formda saçmalık, saçma formda resmiyet")


if __name__ == "__main__":
    main()
