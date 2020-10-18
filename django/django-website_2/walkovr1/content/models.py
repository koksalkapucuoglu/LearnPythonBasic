from django.db import models,migrations

# Create your models here.
class Content(models.Model):
    #content uygulamasında kac alan olacaksa bunları girmek gerekiyor.
    id = models.AutoField(primary_key=True)
    #ilk olarak content sahibi, kullanıcı tanımlıyoruz.
    user = models.ForeignKey("auth.User",blank=True, null=True, on_delete=models.CASCADE)#foreignkey-auth.user tablosuna bağlıyor. 
    #"auth.User" tablosundaki user direk buraya gelecek.
    playing_time = models.CharField(max_length=50) #Oturum Başına Ortalama Oynama Süresi(dk/session)
    session_count  = models.CharField(max_length=50)#Toplam Oynama Süresi(dk)
    total_step  = models.CharField(max_length=50)#Toplam Adım Sayısı(step)
    total_walk  = models.CharField(max_length=50)#Toplam Yürüme Mesafesi(m)
    total_run = models.CharField(max_length=50)#Toplam Koşu Mesafesi(m)
    total_calori  = models.CharField(max_length=50)# Yakılan Toplam Kalori(cal)
    

    def __str__(self):
        return "Statistics of " + str(self.user)
   