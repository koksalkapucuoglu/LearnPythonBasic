from django.db import models

# Create your models here.
class GameStatistic(models.Model):
    #content uygulamasında kac alan olacaksa bunları girmek gerekiyor.
    id = models.AutoField(primary_key=True)
    #ilk olarak content sahibi, kullanıcı tanımlıyoruz.
    user = models.name = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    #"auth.User" tablosundaki user direk buraya gelecek.
    game_name = models.name = models.CharField(max_length=50) #Oyun ismi
    playing_time = models.name = models.CharField(max_length=50) #OToplam Oynama Süresi(dk/session)
    session_count = models.name = models.CharField(max_length=50)#Oturum Sayısı
    total_step = models.name = models.CharField(max_length=50)#Toplam Adım Sayısı(step)
    total_calori = models.name = models.CharField(max_length=50)# Yakılan Toplam Kalori(cal)