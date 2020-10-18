from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Yazar" )#user silindiğinde o user'a ilişkin makalelerde silinecek
    title = models.CharField(max_length = 50 , verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True , verbose_name = "Oluşturulma Tarihi")
    article_image = models.FileField(blank = True, null= True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__ (self):#oluşan makalenin ismi olarak olarak o makalenin başlığı yazıyor. Normalde içerikten 3-5 satır olurdu.
        return  self.title
    class Meta:
        ordering  = ['-created_date'] #tarihe göre sıralama için ekledik.


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete= models.CASCADE, verbose_name = "Makale",related_name="comments")#related_name kısmını bunu detay sayfasında tüm yorumları getirirken kullanıyoruz.
    comment_author = models.CharField(max_length = 50 , verbose_name = "İsim")
    comment_content = models.CharField(max_length = 20 , verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering  = ['-comment_date']