print("\nTOPLAM FIYAT HESAPLAMA\n")

def toplam_fiyat_hesapla(urunler):
    toplam = 0
    for urun in urunler:
        toplam += urun["fiyat"] * urun["adet"]
    return toplam

def urun_girisi():
    urunler = []
    n = int(input("Kaç ürün gireceksiniz? "))
    for _ in range(n):
        ad = input("Ürün adı: ")
        fiyat = float(input("Fiyatı: "))
        adet = int(input("Adedi: "))
        urunler.append({"ad": ad, "fiyat": fiyat, "adet": adet})
    return urunler

def urunleri_yazdir(urunler):
    for urun in urunler:
        print(f"{urun['ad']} - {urun['adet']} adet - {urun['fiyat']} TL")

urunler = urun_girisi()
urunleri_yazdir(urunler)
print(f"Toplam fiyat: {toplam_fiyat_hesapla(urunler):.2f} TL")