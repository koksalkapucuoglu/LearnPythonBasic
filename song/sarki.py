import sqlite3

import time

class Sarki():
    def __init__(self,isim,sanatci,album,produksiyon,sure):

        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sure = sure


    def __str__(self):

        return "Şarkı İsmi = {}\nSanatçı = {}\nAlbüm = {}\nProdüksiyon Şirketi = {}\nSüre = {}".format(self.isim,self.sanatci,self.album,self.produksiyon,self.sure)

class Sarkilar():

    def __init__(self):

        self.baglanti_olustur()#bu class'a girdiğimizde direkt init fonk. ve init içinde çağırdığımız bağlantı_oluştur
                                #metodu çalışır.

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db") # database'e bağlantı kur.

        self.cursor = self.baglanti.cursor() #database üzerindeki imleci tanımla. Tüm işlemleri bu imleçle yaparız.

        sorgu = " Create Table if not exists sarkilar (isim TEXT, sanatçı TEXT,albüm TEXT,prodüksiyon TEXT, süre INT)"

        self.cursor.execute(sorgu)#sorguyu çalıştır.

        self.baglanti.commit()#database'nin güncellenmesi için bu işlemi metod sonunda tanımlarız.

    def baglantiyi_kes(self):

        self.baglanti.close()

    def sarkilari_goster(self):

        sorgu = "Select * From sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall() #sorgu sonucunda  aldığımız sonucları bir demet olarak alıp kitaplar listesine
                                                #atarız. kaç tane öge aldıysa o kadar demet olur.bu demetlerde tabloda
                                                #kaç sütun varsa o kadar elemana sahiptir.

        if len(sarkilar) == 0:
            print("Kütüphanede şarkı bulunmuyor...")

        else:
            for i in sarkilar:

                sarki = Sarki(i[0],i[1],i[2],i[3],i[4]) #kitap class'ına tüm parametreleri gönderip bilgileri basıyoruz.

                print(sarki)


    def sarki_sorgula(self,isim):

        sorgu = "Select * From sarkilar where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:

            print("Böyle bir şarkı bulunmuyor....")
            cevap = input("Bu şarkıyı eklemek ister misiniz? ")

            if cevap == "E" or cevap == "e":

                isim = input("İsim: ")
                sanatci = input("Sanatçı: ")
                album = input("Albüm: ")
                produksiyon = input("Prodüksiyon: ")
                while True:
                    try:
                        sure = int(input("Süre(sn): "))
                        break
                    except ValueError:
                        print("Lütfen süre değerine sayı girin: ")

                yeni_sarki = Sarki(isim, sanatci, album, produksiyon, sure)

                self.sarki_ekle(yeni_sarki)
                time.sleep(1)
                print("Şarkınız eklendi... İsterseniz işlemler menüsünden '1' işlemini girerek görebilirsiniz...")
            else:
                print("En yakın zamanda bu şarkıyı eklemeye çalışacağız, iyi günler...")
        else:

            sarki = Sarki(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3],sarkilar[0][4])

            print(sarki)

    def sarki_ekle(self,sarki): #sarki burada obje. kitap ekleye bir obje atamak lazım.

        sorgu1 = "Select * From sarkilar where isim = ? and sanatçı = ?"

        self.cursor.execute(sorgu1, (sarki.isim,sarki.sanatci,))

        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:

            sorgu2 = "Insert into sarkilar Values(?,?,?,?,?)"

            self.cursor.execute(sorgu2, (sarki.isim, sarki.sanatci, sarki.album, sarki.produksiyon, sarki.sure))

            self.baglanti.commit()
            print("Şarkı eklendi...")
        else:
            print("Böyle bir şarkı veritabanımızda zaten var!")

            sarkii = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4])

            print(sarkii)

    def sarki_sil(self,isim):

        sorgu1 = "Select * From sarkilar where isim = ?"

        self.cursor.execute(sorgu1, (isim,))

        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:

            print("Böyle bir sarki bulunamadı...")
        else:
            sorgu2 = " Delete from sarkilar where isim = ?"

            self.cursor.execute(sorgu2, (isim,))

            self.baglanti.commit()
            print("Şarkı silindi...")

    def toplam_sure(self):

        sorgu = "Select * From sarkilar "

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        toplam_sure = 0

        for i in sarkilar:

            toplam_sure += i[4]

        print("Toplam şarkı süresi = ",toplam_sure)

    def sanatci_sarkileri_getir(self,sanatci):

        sorgu1 = "Select * From sarkilar where sanatçı = ?"

        self.cursor.execute(sorgu1,(sanatci,))

        sanatci_sarkilar = self.cursor.fetchall()

        print("{}'nın tüm şarkıları\n********************************".format(sanatci))

        for i in sanatci_sarkilar:

            print(i[0])
