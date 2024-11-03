ad = input("Adınızı giriniz:")
kilo = int(input("Kilonuzu giriniz (Örn:85):"))
boy = float(input("Boyunuzu girin (Örn:1.75)"))

bki = kilo/(boy**2)

if bki < 18.5:
    sonuc = "Zayıf"

elif bki < 24.9:
    sonuc = "Normal"

elif bki < 29.9:
    sonuc = "Kilolu"

elif bki < 34.9:
    sonuc = "Şişman"

else:
    sonuc = "Obez"

print(f"Sayın {ad}, bki değerinize göre sonuç {sonuc} çıkmıştır.")
    
