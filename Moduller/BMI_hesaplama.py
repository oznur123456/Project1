print("BMI HESAPLAMA")
print("Merhaba!")

def bmi_hesapla(kilo, boy):
    
    bmi = kilo / (boy ** 2)
    if bmi < 18.5:
        kategori = "Zayıf"
    elif 18.5 <= bmi < 24.9:
        kategori = "Normal"
    elif 25 <= bmi < 29.9:
        kategori = "Fazla Kilolu"
    else:
        kategori = "Obez"
    return bmi, kategori

kilo = float(input("Kilonuzu kilogram cinsinden giriniz (örn: 49.5): "))
boy = float(input("Boyunuzu metre cinsinden giriniz (örn: 1.75): "))

bmi, kategori = bmi_hesapla(kilo, boy)

print(f"Vücut Kitle İndeksiniz: {bmi:.2f}")
print(f"Kategoriniz: {kategori}")

bmi_hesapla(kilo,boy)
