from sarki import *

print("""
*********************************************************
Kütüphane Programına Hoşgeldiniz.

İşlemler;

1.Şarkıları Göster

2.Şarkı Sorgulama

3.Şarkı Ekle

4.Şarkı  Sil

5.Toplam Şarkı Süresi

6.Sanatçının Tüm Şarkılarını Göster

Çıkmak için 'q'ya basın.

*********************************************************
""")

sarki = Sarkilar() #sarki adlı bir Kutuphane objesi oluşturuyoruz.
while True:

    islem = input("Yapacağınız işlem:")

    if islem == 'q':

        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz...")
        break

    elif islem == "1":

        sarki.sarkilari_goster()

    elif islem == "2":
        isim = input("Hangi şarkıyı sorgulamak istiyorsunuz? ")
        print("Şarkı sorgulanıyor...")
        time.sleep(2)

        sarki.sarki_sorgula(isim)

    elif islem == "3":

        isim = input("İsim: ")
        sanatci = input("Sanatçı: ")
        album = input("Albüm: ")
        produksiyon = input("Prodüksiyon Şirketi: ")
        while True:

            try:
                sure = int(input("Süre(sn):"))
                break
            except ValueError:
                print("Lütfen süre değerine sayı girin: ")



        yeni_sarki= Sarki(isim,sanatci,album,produksiyon,sure)

        print("Şarkı ekleniyor...")
        time.sleep(2)

        sarki.sarki_ekle(yeni_sarki)


    elif islem == "4":
        isim = input("Hangi şarkıyı silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")

        if cevap == "E" or cevap == "e":
            print("Şarkı siliniyor...")
            time.sleep(2)
            sarki.sarki_sil(isim)


    elif islem == "5":
        print("Toplam süre hesaplanıyor..")
        time.sleep(2)

        sarki.toplam_sure()

    elif islem == "6":

        sanatci = input("Sanatçı ismini girin: ")

        print("Şarkılar Aranıyor..")
        time.sleep(2)

        sarki.sanatci_sarkileri_getir(sanatci)


