import sqlite3 #sqlite kütüphanesini import ediyoruz.

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():

    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, SayfaSayısı INT)")

    con.commit()

def veri_ekle():

    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    
    con.commit()

def veri_ekle2(isim, yazar, yayınevi, sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
    
    con.commit()#veritabanı üzerinde güncelleme yap.

def verileri_al():
    cursor.execute("SELECT *  FROM kitaplık")

    liste = cursor.fetchall()#cursor üzerindeki tüm verileri bize dönecek.
    print("Kitaplık Tablosunu Bilgileri...")

    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("SELECT İsim, Yazar FROM  kitaplık")
    liste = cursor.fetchall()

    print("Kitaplık Tablosunu Bilgileri...")

    for i in liste:
        print(i)

def verileri_al3(yayınevi):
    cursor.execute("SELECT *FROM  kitaplık WHERE Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()

    print("Kitaplık Tablosunu Bilgileri...")

    for i in liste:
        print(i)
def verileri_güncelle(eski_yayınevi, yeni_yayınevi):
    cursor.execute("UPDATE kitaplık SET Yayınevi = ? WHERE Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def verileri_sil(yazar):
    cursor.execute("DELETE FROM kitaplık WHERE  Yazar = ?",(yazar,))
    con.commit()
    

#isim = input("isim: ")
#yazar = input("Yazar: ")
#yayınevi = input("Yayınevi: ")
#sayfa_sayisi = int(input("Sayfa Sayısı: "))
#veri_ekle2(isim,yazar,yayınevi,sayfa_sayisi)

#verileri_al()
#verileri_al2()

#verileri_al3("Everest")

#verileri_güncelle("Dogan Kitap", "Everest")

verileri_sil("Ahmet Ümit")
con.close()
