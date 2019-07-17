import sqlite3

import time

class Kitap(): #kitap parametrelerini bir class'da tanımlıyoruz. Böylece bir kitabın tüm bilgilerini yazdırmak istediğimizde
                #kitap classı ile bunu yapıyoruz.
    def __init__(self,isim,yazar,yayinevi,tur,baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski


    def __str__(self):

        return "Kitap İsmi = {}\nYazaar = {}\nYayın Evi = {}\nTür = {}\nBaskı = {}".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)

    #print(Kitap) direkt __str__ 'yi çalıştırır.



class Kutuphane():

    def __init__(self):

        self.baglanti_olustur()#bu class'a girdiğimizde direkt init fonk. ve init içinde çağırdığımız bağlantı_oluştur
                                #metodu çalışır.

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db") # database'e bağlantı kur.

        self.cursor = self.baglanti.cursor() #database üzerindeki imleci tanımla. Tüm işlemleri bu imleçle yaparız.

        sorgu = " Create Table if not exists kitaplar (isim TEXT, yazar TEXT,yayınevi TEXT,tür TEXT, baskı INT)"

        self.cursor.execute(sorgu)#sorguyu çalıştır.

        self.baglanti.commit()#database'nin güncellenmesi için bu işlemi metod sonunda tanımlarız.

    def baglantiyi_kes(self):

        self.baglanti.close()

    def kitaplari_goster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall() #sorgu sonucunda  aldığımız sonucları bir demet olarak alıp kitaplar listesine
                                                #atarız. kaç tane öge aldıysa o kadar demet olur.bu demetlerde tabloda
                                                #kaç sütun varsa o kadar elemana sahiptir.

        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunmuyor...")

        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4]) #kitap class'ına tüm parametreleri gönderip bilgileri basıyoruz.

                print(kitap)


    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))#burada soru işareti ile olan kısmı demet olarak tanımlıyoruz.
                                        # eger 1 eleman varsa sonuna ',' koyarız.

        kitaplar = self.cursor.fetchall()#eğer söylenen kitap varsa bu kitap bilgileri, kitaplar listesine tek demet
                                            #olarak gelir.

        if len(kitaplar) == 0:

            print("Böyle bir kitap bulunmuyor....")
            cevap = input("Bu kitabı eklemek ister misiniz? ")

            if cevap == "E" or cevap == "e":

                isim = input("İsim: ")
                yazar = input("Yazar: ")
                yayinevi = input("Yayınevi: ")
                tur = input("Tür: ")
                while True:

                    try:
                        baski = int(input("Baskı"))
                        break
                    except ValueError:
                        print("Lütfen baskı değerine sayı girin: ")

                yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)  # yeni_kitap adlı bir Kitap objesi oluşturuyoruz.

                self.kitap_ekle(yeni_kitap)
                time.sleep(1)
                print("Kitabınız eklendi... İsterseniz işlemler menüsünden '1' işlemini girerek görebilirsiniz...")
            else:
                print("En yakın zamanda bu kitabı eklemeye çalışacağız, iyi günler...")
        else:

            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])

            print(kitap)

    def kitap_ekle(self,kitap): #kitap burada obje. kitap ekleye bir obje atamak lazım.

        sorgu1 = "Select * From kitaplar where isim = ? and yazar = ?"

        self.cursor.execute(sorgu1, (kitap.isim,kitap.yazar,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:

            sorgu2 = "Insert into kitaplar Values(?,?,?,?,?)"

            self.cursor.execute(sorgu2, (kitap.isim, kitap.yazar, kitap.yayinevi, kitap.tur, kitap.baski))

            self.baglanti.commit()
            print("Kitap eklendi...")
        else:
            print("Böyle bir kitap veritabanımızda zaten var!")

            kitapp = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4])

            print(kitapp)

    def kitap_sil(self,isim):

        sorgu1 = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu1, (isim,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:

            print("Böyle bir kitap bulunamadı...")
        else:
            sorgu2 = " Delete from kitaplar where isim = ?"

            self.cursor.execute(sorgu2, (isim,))

            self.baglanti.commit()
            print("Kitap silindi...")



    def baski_yukselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:

            print("Böyle bir kitap bulunmuyor....")
        else:

            baski = kitaplar[0][4]

            baski += 1


            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"


            self.cursor.execute(sorgu2,(baski,isim))

            self.baglanti.commit()
            print("Baskı yükseltildi.")











