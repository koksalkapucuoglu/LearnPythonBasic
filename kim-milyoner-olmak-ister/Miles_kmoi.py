# -*- coding: utf-8 -*-



"""
-/-/-/-/Kim Milyoner Olmak İster
-/-/-/-/asimkymk
-/-/-/-/ASIMKAYMAK"""
#gerekli kütüphaneler import edidi : sqlite,random ve time
import sqlite3 as sq
import random as rd
import time as tm
#soru sorma fonksiyonu
def Ask(question,correct,other1,other2,other3,level,money):
    
    correctList = [correct,other1,other2,other3] #sırasıyla şıkları sıraladık. ilk index doğru cevap
    mixedList = rd.sample(range(0, 4), 4) # 0,1,2,3 indexlerini karışık sıralar böylece şıklar karıştırılır
    answerList = [] # cevap alındığında buraya cevabı ekler
    print("""
{}. Soru - {}
{}
A-) {}
B-) {}
C-) {}
D-) {}""".format(level,money,question,correctList[mixedList[0]],correctList[mixedList[1]],correctList[mixedList[2]],correctList[mixedList[3]]))
    answer = input("Cevabınız : ")
    #cevapları listeye ilgili şıkka göre ekliyoruz
    if answer.lower() == "a":
        answerList.append(correctList[mixedList[0]])
    elif answer.lower() == "b":
        answerList.append(correctList[mixedList[1]])
    elif answer.lower() == "c":
        answerList.append(correctList[mixedList[2]])
    elif answer.lower() == "d":
        answerList.append(correctList[mixedList[3]])
     #doğruysa  true yanlışsa false döndürüyoruz
    if correct == answerList[0]:
        tm.sleep(level)
        print("Cevap Doğru")
        tm.sleep(2)
        return True
    else:
        tm.sleep(level)
        print("Yanlış")
        tm.sleep(2)
        print("Doğru Cevap : {}".format(correct))
        return False
    
#database oluşturuyoruz
class Server():
    #init fonksiyonumuzu oluturuyoruz direk otomatik çalışır.
    def __init__(self,):
        self.connect = sq.connect("wwtbam.db") #server dosyası oluşturuldu ve bağlanıldı.
        self.cursor = self.connect.cursor() #server işaretçisi seçildi.
        self.Connect() #oluşturulan Connect fonksiyonu çalıştırıldı.
    
    def Connect(self,):#serverımız için gerekli sorgulamalar yapıldı.
        #serverda istediğimiz özellikte table var mı?: Yoksa oluştur:
        self.cursor.execute("create table if not exists allQues (qId INT, level INT,question TEXT, correct TEXT, option1 TEXT, option2 TEXT, option3 TEXT)")
        self.connect.commit()
        print("Server bağlantısı sağlandı.")
    
    def Close(self,):
        tm.sleep(1)
        
        self.connect.close()
        print("Server kapatıldı.")
    
    def addQuestion(self,level,question,correct,option1,option2,option3):
        #Soru ekleme fonksiyonu
        
        while True: #uygun qId'yi bulmak için altta oluşturduğumuz fonksiyonu kullandık
            qId = 1
            while self.qIdQuery(qId) == False: #eğer istenilen id'de soru yoksa o qId soruya atanır yoksa bir yukarı sayı kullanılır.
                qId += 1
            break
        query = "Insert into allQues Values (?,?,?,?,?,?,?)" #yeni veri ekleme sorgusu
        self.cursor.execute(query,(qId,level,question,correct,option1,option2,option3))
        self.connect.commit()
        tm.sleep(1)
        print("Soru başarıyla eklendi.")
        tm.sleep(2)
        self.listShowQues(qId,level,question,correct,option1,option2,option3) #sorunun eklendğine dair soruyu gösteren donksiyon çalıştırılır
    def showQuestion(self,level,money):#soruyu atama fonksiyonu
        query = "Select * from allQues where level = ?"
        self.cursor.execute(query,(level,))
        liste = self.cursor.fetchall() #istenilen leveldan tüm sorular listeye eklendi
        if len(liste) == 0: #istenilen levella alakalı soru yoksa hata döndürdü
            print("Beklenmedik bir hata oldu. Lütfen servera soru eklemeye devam edin. İstenilen levelda herhangi bir soru yok.")
        else:#listede soru varsa:
            levelTotalQuestionsCount = len(liste)
            questionNumber = rd.randint(1,levelTotalQuestionsCount) - 1 #listedeki soru sayısınca karmaşık bir sayı seçilir. o soru kullanıcıya sorulur.
            if Ask(liste[questionNumber][2],liste[questionNumber][3],liste[questionNumber][4],liste[questionNumber][5],liste[questionNumber][6],liste[questionNumber][1],money):
                return True #soruya doğru cevap verilirse true döndürdük
            else:
                return False #yanlış cevap verildiyse false döndürdük
            
    def qIdQuery(self,qId): #qId'ye göre istenilen soru var mı yok mu onu sorguluyoruz
        query = "Select * from allQues where qId = ?"
        self.cursor.execute(query,(qId,))
        qIdList = self.cursor.fetchall()
        if len(qIdList) == 0:
            return True #varsa true döndürdük
        else:
            return False #yoksa false döndürdük
    
    def listShowQues(self,qId,level,question,correct,option1,option2,option3): #kullanıcının belli levela ait soruları görmesi ve qId öğrenebilmesi için kullanılır
        
        print("""
Soru Id    : {}
Soru Level : {}
Soru       : {}
Doğru      : {}
Yanlış1    : {}
Yanlış2    : {}
Yanlış3    : {}
""".format(qId,level,question,correct,option1,option2,option3))
        
        
    def listQuestions(self,level): # listShowQues fonksiyonuna verileri gönderir.
        self.cursor.execute("Select * from allQues where level = ?",(level,))
        listQues = self.cursor.fetchall()
        if len(listQues) == 0:
            tm.sleep(0.5)
            print("Bu levelda gösterilecek herhangi bir soru bulunmuyor.")
        else:
            for soru in listQues:
                tm.sleep(1)
                print("*"*25)
                self.listShowQues(soru[0],soru[1],soru[2],soru[3],soru[4],soru[5],soru[6])
    def updateQuestion(self,qId): #qId sine göre Soru güncellenebilir.
        if self.qIdQuery(qId):
            tm.sleep(0.8)
            print("Serverda bu id numarasında herhangi bir soru bulunmuyor. Lütfen tekrar gözden geçirerek sorgulama yapınız.")
        else:
            question = input("Yeni Soruyu Sonunda ? Olacak Şekilde Yazın : ")
            level = int(input("1 ile 12 arasında (1 ve 12 dahil) soruya uygun level giriniz.(1 EN KOLAY, 12 EN ZOR) : "))
            correct = input("Doğru Şık : ")
            option1 = input("Yanlış Şık1 : ")
            option2 = input("Yanlış Şık2 : ")
            option3 = input("Yanlış Şık3 : ")
            query = "Update allQues set level = ?, question = ?, correct = ?, option1 = ?, option2 = ?, option3 = ? where qId = ?"
            self.cursor.execute(query,(level,question,correct,option1,option2,option3,qId))
            tm.sleep(1)
            self.connect.commit()
            print("Soru başarıyla güncelllendi!")
            tm.sleep(2)
            self.listShowQues(qId,level,question,correct,option1,option2,option3) #güncellenen soruyu tekrar güncellenmiş şekilde kullanıcıya gösterdik
    
    def deleteQuestion(self,qId): #soru silme fonksiyonu
        if self.qIdQuery(qId): #kullanıcıdan alınan qId ye göre soru silinir.
            tm.sleep(0.5)
            print("Serverda zaten bu id numarasında bir soru bulunmuyor.")
        else:
            query = "delete from allQues where qId = ?"
            self.cursor.execute(query,(qId,))
            self.connect.commit()
            tm.sleep(1)
            print("{} id numaralı soru başarıyla silindi.".format(qId))
            
#database ayarları tamamlandı.

    
kmoi = Server() #Server classımıza (Database ' e) bağlanıldı.
garantiKazanc = 0
#sonsuz döngüde program çalıştırıldı.
while True:
    print("""KİM MİLYONER OLMAK İSTER?
      
         -g : Oyunu Başlat
         
         -s : Server Ayarları
         
         -i : Program Hakkında
         
         -q : Çık
""")
    islem = input("İşlem : ")
    if islem.lower() == "q":
        print("Çıkış yapılıyor.")
        tm.sleep(1)
        kmoi.Close()
        print("İşlemler kapandı.")
        break
    elif islem.lower() == "g":
        level =[1,2,3,4,5,6,7,8,9,10,11,12] #toplamda 12 level var
        money = ["₺500","₺1.000","₺2.000","₺3.000","₺5.000","₺7.500","₺15.000","₺30.000","₺60.000","₺125.000","₺250.000","₺1.000.000"] #her bir levela karşılık gelen paralar atandı
        print("Oyun başlatılıyor...")
        tm.sleep(1)
        print("Oyun başlatılıyor..")
        tm.sleep(1)
        print("Oyun başlatılıyor.")
        tm.sleep(1)
        while True:
            garantiKazanc = 0
            for i in range(0,12):
                if kmoi.showQuestion(level[i],money[i]):
                    #eğer son soruyu bildiyse kazandı. eğer 2.soruyu geçtiyse 100 tl garanti parası var
                    #eğer 7. soruyu geçtiyse 7.500 tl garanti parası var
                    if i == 11:
                        print("Tebrikler. 1.000.000 TL Kazandınız!!!")
                        tm.sleep(5)
                        break
                    elif 1 <= i <6:
                        garantiKazanc = "1.000"
                        tm.sleep(2)
                        print("Tebrikler... Diğer soruya geçiliyor...")
                        tm.sleep(1)
                    elif 11> i >= 6:
                        garantiKazanc = "7.500"
                            
                        tm.sleep(2)
                        print("Tebrikler... Diğer soruya geçiliyor...")
                        tm.sleep(1)
                    else:
                        tm.sleep(2)
                        print("Tebrikler... Diğer soruya geçiliyor...")
                        tm.sleep(1)
                    
                else:
                    #yanlış cevaplarsa sorunun doğru cevbı gösterildikten sonra toplam kazanç yazılır ve program ana menüye döner
                    
                    tm.sleep(2)
                    print("İşleniyor....")
                    
                    tm.sleep(1)
                    print("Toplam Kazanç : {} TL ".format(garantiKazanc))
                    tm.sleep(2)
                    kmoi.Close()
                    break
            
            break
    elif islem.lower()== "i":
        #HAKKINDA####
        print("""
        ******************************
        *   ᴠᴇʀꜱɪᴏɴ  : ᴠ1.0          *
        *    ᴀᴜᴛʜᴏʀ   : ᴀꜱɪᴍ ᴋᴀʏᴍᴀᴋ  *
        ******************************
""")
        tm.sleep(2)
       
    elif islem.lower() == "s":
        #yukarıda server classında yapılan tüm ayarlamaları buradan kullanıcıya işleyebiliyoruz.
        #sonsuz döngü
       while True:
           
            print("""Server Ayarları
                  1- Soru Ekle
                  
                  2- Soruları Listele (qId Öğren)
                  
                  3- Soru Güncelle
                  
                  4- Soru Sil
                  
                  5- Ana Menü
                  """)
            islemS = input("İşlem Numarası : ")
            if islemS == "5":
                print("Ana Menü'ye dönülüyor...")
                tm.sleep(1)
                
                break
            elif islemS == "1":
                #soru ekliyoruz:::
                level = int(input("Soru Zorluğu (1-12) : "))
                question = input("Soru : ")
                correct = input("Doğru Şık : ")
                option1 = input("Yanlış Şık1 : ")
                option2 = input("Yanlış Şık2 : ")
                option3 = input("Yanlış Şık3 : ")
                kmoi.addQuestion(level,question,correct,option1,option2,option3) #server soru ekleme fonksiyonu çalıştırıldı
            elif islemS == "2":
                #levela göre qId öğrenebilmek için levela ait tüm sorular gsterilir
                level = int(input("Lütfen hangi leveldan soruları listelemek istediğinizi giriniz (1-12) : "))
                
                print("İstek işleniyor...")
                tm.sleep(3)
                kmoi.listQuestions(level)
                print("*"*25)
    
            elif islemS =="3":
                #qId ye göre soru güncelleniyor.
                qId = int(input("Güncellemek istediğiniz sorunun qId numarası : "))
                print("İşleniyor...")
                tm.sleep(2)
                kmoi.updateQuestion(qId)
                print("*"*25)
            elif islemS == "4":
                #qIdye göre soru siliniyor.
                qId = int(input("Silmek istediğiniz sorunun qId numarası : "))
                print("İşleniyor...")
                tm.sleep(2)
                kmoi.deleteQuestion(qId)
                print("*"*25)
    
#############Miles 