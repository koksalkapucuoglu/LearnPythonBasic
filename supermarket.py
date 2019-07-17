import sqlite3

import time

class Urun():
    def __init__(self,isim,kategori,paket_agirligi,fiyat,stok):

        self.isim = isim
        self.kategori = kategori
        self.paket_agirligi = paket_agirligi
        self.fiyat = fiyat
        self.stok = stok



    def __str__(self):


        return "Ürün İsmi = {}\nKategori = {}\nPaket Ağırlığı = {}\nAdet Fiyatı  = {}\nStok: {}".format(self.isim,self.kategori,self.paket_agirligi,self.fiyat,self.stok)

class Supermarket():

    def __init__(self,):

        self.baglanti_olustur()#bu class'a girdiğimizde direkt init fonk. ve init içinde çağırdığımız bağlantı_oluştur
                                #metodu çalışır.
        self.count = 0

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db") # database'e bağlantı kur.

        self.cursor = self.baglanti.cursor() #database üzerindeki imleci tanımla. Tüm işlemleri bu imleçle yaparız.

        sorgu = " Create Table if not exists urunler (isim TEXT, kategori TEXT,paket_ağırlığı TEXT,fiyat INT,stok INT)"

        self.cursor.execute(sorgu)#sorguyu çalıştır.

        self.baglanti.commit()#database'nin güncellenmesi için bu işlemi metod sonunda tanımlarız.

    def baglantiyi_kes(self):

        self.baglanti.close()

    def urunleri_goster(self):

        sorgu = "Select * From urunler"

        self.cursor.execute(sorgu)

        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Şu an süpermarkette ürün yok...")

        else:
            for i in urunler:

                urun = Urun(i[0],i[1],i[2],i[3],i[4]) #ürün class'ına tüm parametreleri gönderip bilgileri basıyoruz.

                print(urun)


    def urun_sorgula(self,isim):

        sorgu = "Select * From urunler where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        urunler = self.cursor.fetchall()

        if len(urunler) == 0:

            print("Böyle bir ürün kaydı bulunmamaktadır....")

        else:

            urun = Urun(urunler[0][0],urunler[0][1],urunler[0][2],urunler[0][3],urunler[0][4])

            print(urun)

    def urun_ekle(self,urun): #urun burada obje. kitap ekleye bir obje atamak lazım.

        sorgu1 = "Select * From urunler where isim = ?"

        self.cursor.execute(sorgu1, (urun.isim,))

        urunler = self.cursor.fetchall()

        if len(urunler) == 0:

            sorgu2 = "Insert into urunler Values(?,?,?,?,?)"

            self.cursor.execute(sorgu2, (urun.isim, urun.kategori, urun.paket_agirligi, urun.fiyat, urun.stok))

            self.baglanti.commit()
            print("Ürün eklendi...")
        else:
            print("Böyle bir ürün veritabanımızda zaten var!")

            urunn = Urun(urunler[0][0], urunler[0][1], urunler[0][2], urunler[0][3], urunler[0][4])

            print(urunn)

    def urun_sil(self,isim):

        sorgu1 = "Select * From urunler where isim = ?"

        self.cursor.execute(sorgu1, (isim,))

        urunler = self.cursor.fetchall()

        if len(urunler) == 0:

            print("Böyle bir ürün bulunamadı...")
        else:
            sorgu2 = " Delete from urunler where isim = ?"

            self.cursor.execute(sorgu2, (isim,))

            self.baglanti.commit()
            print("Ürün silindi...")




    def urun_al(self,alinan_urunler,n):

        print(alinan_urunler)

        sorgu1 = "Select * From urunler "

        self.cursor.execute(sorgu1)

        urunler = self.cursor.fetchall()

        self.urun_stok_kontrol(alinan_urunler,n)

        if self.count == n:

            print("Ödemeniz gereken toplam ücret hesaplanıyor...")

            time.sleep(2)

            fiyat = 0
            print("Alınan ürünler ve adetleri\n*************************************************")
            for i in alinan_urunler:
                print(i)
            print("\n*************************************************")
            for i in range(0, n):
                for j in range(len(urunler)):
                    if alinan_urunler[i][0] == urunler[j][0]:
                        fiyat += int(urunler[j][3]) * int(alinan_urunler[i][1])

            print("Toplam Tutar: ", fiyat)

            cevap = input("Devam etmek istermisiniz?(E/H)")

            if cevap == "E" or cevap == "e":
                print("Ödeme sayfasına aktarılıyorsunuz...")
                time.sleep(0.3)
                print("Ödeme Yapıldı. İyi günler dileriz.")

                for i in range(0, n):
                    for j in range(len(urunler)):
                        if alinan_urunler[i][0] == urunler[j][0]:
                            list1 = list(urunler[j])

                            list1[4] -= int(alinan_urunler[i][1])

                            sorgu2 = "Update urunler set stok = ? where isim = ?"

                            self.cursor.execute(sorgu2, (list1[4], urunler[j][0]))

                            self.baglanti.commit()


            else:
                print("Ana menüye aktarılıyorsunuz...")
                time.sleep(0.3)


        else:

            print("Stok yok....")
            print("Almak istediğiniz ürünlerin stok bilgileri\n*********************************************")

            for i in range(0, n):
                for j in range(len(urunler)):
                    if alinan_urunler[i][0] == urunler[j][0]:
                        print(urunler[j])




    def urun_stok_kontrol(self,alinan_urunler,n):

        sorgu = "Select * From urunler"

        self.cursor.execute(sorgu)

        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Şu an süpermarkette ürün yok...")

        else:
            self.count = 0
            for i in range(0, n):
                for j in range(len(urunler)):
                    if alinan_urunler[i][0] == urunler[j][0] and int(urunler[j][4]) >= int(alinan_urunler[i][1]):
                        self.count += 1

            return self.count

    def kategori_urunleri_getir(self, kategori):

        sorgu = "Select * From urunler"

        self.cursor.execute(sorgu)

        urunler = self.cursor.fetchall()

        if len(urunler) == 0:
            print("Şu an süpermarkette ürün yok...")

        else:
            print("{} kategorindeki ürünler\n********************************".format(kategori))
            sayac = 0
            for i in urunler:

                if kategori == i[1]:
                    print(i)

                    sayac += 1
            if sayac == 0:

                print("Böyle bir kategori bulunamamıştır.")

