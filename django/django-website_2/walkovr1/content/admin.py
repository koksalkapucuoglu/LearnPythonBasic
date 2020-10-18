from django.contrib import admin

from .models import Content

# Register your models here.
#admin.site.register(Content)
#content içeriğini burada belirdediğimiz tabloları gösteriyoruz-http://127.0.0.1:8000/admin/content/content/
#yukarıdaki tanım yerine bir decoratör yazıyoruz.
@admin.register(Content)
class ContentUser(admin.ModelAdmin):    
    #list_display = ["user","playing_time","session_count","total_step","total_walk","total_run","total_calori"]
    list_display = ["user","playing_time","total_step","total_calori"]
    #link atar
    list_display_links = ["user","total_calori"]
    
    class Meta:
        model = Content