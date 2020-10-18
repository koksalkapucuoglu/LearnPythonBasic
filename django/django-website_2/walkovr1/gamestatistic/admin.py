from django.contrib import admin

# Register your models here.
from .models import GameStatistic

#GameStatistic içeriğini burada belirdediğimiz tabloları gösteriyoruz-http://127.0.0.1:8000/admin/content/content/
#yukarıdaki tanım yerine bir decoratör yazıyoruz.
@admin.register(GameStatistic)
class GameStatisticUser(admin.ModelAdmin):    
    #list_display = ["user","playing_time","session_count","total_step","total_walk","total_run","total_calori"]
    list_display = ["user","game_name","playing_time","total_step","total_calori"]
    #link atar
    list_display_links = ["user","game_name"]
    
    class Meta:
        model = GameStatistic