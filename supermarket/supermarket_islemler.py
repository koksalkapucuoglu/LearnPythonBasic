from supermarket import *

print("""
*********************************************************
Kütüphane Programına Hoşgeldiniz.

İşlemler;

1.Ürünleri Göster

2.Ürün Sorgulama

3.Ürün Ekle

4.Ürün  Sil

5.Ürün Alma

6.Kategorideki Ürünlere Bakma


Çıkmak için 'q'ya basın.

*********************************************************
""")

urun = Supermarket()
while True:

    islem = input("Yapacağınız işlem:")

    if islem == 'q':

        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz...")
        break

    elif islem == "1":

        urun.urunleri_goster()

    elif islem == "2":
        isim = input("Hangi ürünü sorgulamak istiyorsunuz? ")
        print("Ürün sorgulanıyor...")
        time.sleep(2)

        urun.urun_sorgula(isim)

    elif islem == "3":

        isim = input("İsim: ")
        kategori = input("Kategori: ")
        paket_agirligi = input("Paket Ağırlığı : ")
        while True:
            try:
                fiyat = int(input("Adet Fiyatı(TL): "))
                break
            except ValueError:
                print("Lütfen sayı biçiminde girin: ")
        while True:
            try:
                stok = int(input("Stok(Adet): "))
                break
            except ValueError:
                print("Lütfen sayı biçiminde girin: ")

        yeni_urun = Urun(isim, kategori, paket_agirligi, fiyat, stok)


        print("Ürün Ekleniyor...")
        time.sleep(2)

        urun.urun_ekle(yeni_urun)


    elif islem == "4":
        isim = input("Hangi ürünü silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")

        if cevap == "E" or cevap == "e":
            print("Ürün siliniyor...")
            time.sleep(2)
            urun.urun_sil(isim)

    elif islem == "5":

        alinan_urunler = list()


        print("Ürün satın almaya hoşgeldiniz...")

        n = int(input("Kaç adet ürün almak istersiniz? "))

        for i in range(0,n):

            uruns = input("Almak istediğiniz {}. ürünü ve adetini arada boşluk bırakarak giriniz : ".format(i+1)).split(" ")
            alinan_urunler.append(uruns)

        urun.urun_al(alinan_urunler,n)



    elif islem == "6":

        kategori = input("Lütfen aramak istediğiniz kategoriyi girin: ")

        urun.kategori_urunleri_getir(kategori)
