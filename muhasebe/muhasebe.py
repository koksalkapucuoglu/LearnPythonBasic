import time
import datetime
import sqlite3
import sys
with sqlite3.connect("LKS.db") as con:
    cursor=con.cursor()
zaman = time.time()
tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%d-%m-%y %H:%M:%S '))

def tablo_ekle():
    cursor.execute("CREATE TABLE IF NOT EXISTS yetkili (kullanici_adi TEXT, parola TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS musteriler (ad TEXT, soyad TEXT, borc INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS satislar (ad TEXT, soyad TEXT, urun TEXT, birim_fiyat TEXT, adet INT, toplam INT, tarih TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS urunler (id INT PRIMARY KEY, ad TEXT, adet INT, birim_fiyat INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS alislar (ad TEXT, soyad TEXT, urun TEXT, adet INT, birim_fiyat INT, toplam INT, tarih TEXT)")


def kullanici_kaydi():
    cursor.execute("SELECT * FROM yetkili")
    data=cursor.fetchall()
    if data==[]:
        kullanici_adi=input("Lütfen kullanıcı adınızı belirleyin: ")
        parola=input("Lütfen şifrenizi belirleyin: ")
        parola2=input("Lütfen şifrenizi tekrar yazın: ")
        while parola!= parola2:
            print("Şifreler uyuşmuyor. Lütfen tekrar deneyin.")
            parola=input("Lütfen şifrenizi belirleyin: ")
            parola2=input("Lütfen şifrenizi tekrar yazın: ")
        cursor.execute("INSERT INTO yetkili VALUES (?,?)", (kullanici_adi,parola))


def menu():
    while True:
        print("""    **************************************************
            ***               [1] Müşteri Ekle             ***
            ***               [2] Ürün Ekle                ***
            ***               [3] Satış Yap                ***
            ***               [4] Alış Yap                 ***
            ***               [5] Tahsilat Yap             ***
            ***               [6] Borç Ver                 ***
            **************************************************""")
        secim = input("Lütfen işlem kodu giriniz: ")
        if secim == "1":
            musteri_ekle()
            altmenu()
        elif secim == "2":
            urun_ekle()
            altmenu()
        elif secim == "3":
            satis_yap()
            altmenu()
        elif secim == "4":
            alis_yap()
            altmenu()
        elif secim == "5":
            tahsilat()
            altmenu()
        elif secim == "6":
            borc_ver()
            altmenu()
        else:
            print("Lütfen geçerli bir işlem kodu giriniz.")



def altmenu():
    alt_menu_secim = input("Ana menüye dönmek için 0 - Çıkış için 1 \n"
                           "İşlem kodu:")
    if alt_menu_secim == "0":
        menu()
    elif alt_menu_secim == "1":
        exit()
    else:
        print("Lütfen geçerli bir işlem kodu giriniz.")



def musteri_ekle():
    ad=input("Müşterinin adı: ")
    soyad=input("Müşterinin soyadı: ")
    borc=0
    cursor.execute("INSERT INTO musteriler VALUES (?,?,?)",(ad.lower(),soyad.lower(),borc))
    con.commit()
    print("İşlem başarılı.")


def musteri_bul():
    global musteri_adi, musteri_soyadi,data
    musteri_adi = input("Lütfen müşteri adını giriniz: ")
    musteri_soyadi = input("Lütfen müşteri soyadını giriniz: ")
    cursor.execute("SELECT * FROM musteriler WHERE ad==? AND soyad==?", (musteri_adi.lower(), musteri_soyadi.lower()))
    data = cursor.fetchall()
    if data == []:
        print("Böyle bir müşteri bulunamadı. Lütfen Doğru yazdığınızda emin olun.")
        musteri_bul()
    print(data)


def urun_bul():
    global urun_adi, urundata
    urun_adi = input("Lütfen Ürünün adını giriniz: ")
    while len(urun_adi) == 0:
        print("Lütfen bir ürün adı giriniz ve gelen listeden Ürün ID kısmına dikkat ediniz.")
    cursor.execute("SELECT * FROM urunler WHERE ad LIKE ?", ('%' + urun_adi + '%',))
    urundata = cursor.fetchall()
    i = 0
    while len(urundata) > i:
        print("""Ürün Adı:{} Ürün Id:{}""".format(urundata[i][1], urundata[i][0]))
        i += 1


def urun_ekle():
    cursor.execute("SELECT * FROM urunler")
    urundata=cursor.fetchall()
    urun_id=urundata[len(urundata)-1][0]+1 #int(input("Ürün için id giriniz: "))
    urun_adi=input("Ürünün adını giriniz: ")
    urun_miktari=input("Ürünün miktarını giriniz: ")
    birim_fiyat=input("Ürünün birim fiyatını giriniz: ")
    cursor.execute("INSERT INTO urunler VALUES (?,?,?,?)", (urun_id,urun_adi.lower(),urun_miktari,birim_fiyat))
    con.commit()
    print("İşlem başarılı.")


def satis_yap():
    musteri_bul()
    urun_bul()
    while True:
        try:
            urun_id=int(input("Lütfen ürünün ID'ını doğru bir şekilde giriniz: "))
            cursor.execute("SELECT * FROM urunler WHERE id==?",(urun_id,))
            urundata=cursor.fetchall()
            miktar=int(input("Satış miktarını giriniz: "))
            birim_fiyat=int(input("Birim fiyatı giriniz(Varsayılan Birim fiyat:{}): ".format(urundata[0][3])))
            borc=data[0][2]
            borc-=(miktar*birim_fiyat)
            print(borc)
            kalan_urun=urundata[0][2]-miktar
            toplam=miktar*birim_fiyat
            cursor.execute("UPDATE musteriler SET borc=? WHERE ad==? AND soyad==?",(borc,musteri_adi,musteri_soyadi))
            cursor.execute("UPDATE urunler SET adet=? WHERE id==?", (kalan_urun,urun_id))
            cursor.execute("INSERT INTO satislar VALUES (?,?,?,?,?,?,?)",
                           (musteri_adi,musteri_soyadi,urun_adi,birim_fiyat,miktar,toplam,tarih))
            ##satislar() Sonra bakılacak.
            con.commit()
            print("İşlem başarılı.")
            break
        except ValueError:
            print("Lütfen geçerli bir değer giriniz")


def alis_yap():
    musteri_bul()
    print("Daha önce var olan bir ürün için alış bilgisi girmek istiyorsanız 1\n"
          "Yeni bir ürün eklemek için 2 yazınız.")
    secim=input("İşlem kodu: ")
    if secim=="2":
        urun_ekle()
    elif secim=="1":
        urun_bul()
        try:
            urun_id=int(input("Lütfen ürünün ID'ını doğru bir şekilde giriniz: "))
            urun_miktarı=int(input("Satın alınan miktarı giriniz: "))
            while urun_miktarı<=0:
                print("Lütfen miktarı doğru bir şekilde giriniz.")
                urun_miktarı = int(input("Satın alınan miktarı giriniz: "))
            birim_fiyat=int(input("Alış birim fiyatını giriniz: "))
            while birim_fiyat<=0:
                print("Lütfen geçerli bir alış fiyatı giriniz.")
                birim_fiyat=int(input("Alış birim fiyatını giriniz: "))
        except ValueError:
            print ("Lütfen geçerli bir değer giriniz.")
        urun_adi=urundata[0][1]
        toplam_urun_miktarı=urun_miktarı+urundata[0][2]
        toplam=(urun_miktarı*birim_fiyat)
        borc=data[0][2]
        borc+=(urun_miktarı*birim_fiyat)
        cursor.execute("UPDATE urunler SET adet=? WHERE id==?",(toplam_urun_miktarı,urun_id))
        cursor.execute("INSERT INTO alislar VALUES (?,?,?,?,?,?,?)",(musteri_adi,musteri_soyadi, urun_adi, urun_miktarı, birim_fiyat, toplam,tarih))
        cursor.execute("UPDATE musteriler set borc=? WHERE ad==? AND soyad==?",(borc, musteri_adi.lower(),musteri_soyadi.lower()))
        con.commit()
        print("İşlem başarılı.")
    else:
        print("Lütfen geçerli bir işlem kodu giriniz: ")


def tahsilat():
    musteri_bul()
    tahsil_edilen=int(input("Lütfen tahsil edilen para miktarını giriniz: "))
    toplam_borc=data[0][2]+tahsil_edilen
    cursor.execute("UPDATE musteriler SET borc=? WHERE ad==? AND soyad==?",(toplam_borc,musteri_adi,musteri_soyadi))
    con.commit()
    print("İşlem başarılı.")


def borc_ver():
    musteri_bul()
    borc_miktarı=int(input("Lütfen verilen borç miktarını giriniz: "))
    toplam_borc=data[0][2]-borc_miktarı
    cursor.execute("UPDATE musteriler SET borc=? WHERE ad==? AND soyad==?",(toplam_borc,musteri_adi,musteri_soyadi))
    con.commit()
    print("İşlem başarılı.")


def satislar():
    pass
def tarih_siralaması():
    pass
def hesap_siralaması():
    pass

tablo_ekle()
kullanici_kaydi()
menu()