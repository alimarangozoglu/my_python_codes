print("Adınız nedir?")
ad = str(input())
print("Merhaba " , ad)

print("Kaçıncı sınıfsınız?")
sinif = int(input())
print(sinif , ". sınıfa gidiyorsunuz!")


print("Notunuzu giriniz!")
sinav_notu = int(input())
if 0 <= sinav_notu <= 44:
    print("Daha çok çalışmalısın! 1 aldınız")
elif  45 <= sinav_notu <= 54:
    print("Çok iyi çalışmalısın. 2 aldınız!")
elif 55 <= sinav_notu <=69:
    print("Çalışmalısın. 3 aldınız!")
elif 70 <= sinav_notu <=84:
    print("Biraz daha gayret. 4 aldınız!")
elif 85 <= sinav_notu <= 100:
    print("Aferin! 5 aldınız! Böyle devam!")
    