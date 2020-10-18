from django import forms
from .models import GameStatistic
from django.contrib.auth.models import User
class GameStatisticForm(forms.ModelForm):
    class Meta:
        model = GameStatistic
        fields =["game_name","playing_time","session_count","total_step","total_calori"]


"""class AddGroupForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["username"]
    def clean(self):
        username = self.cleaned_data.get("username") #submit edilmeden buradan girişleri alıyoruz.
        if User.objects.filter(username = username).exists() is False:
            raise forms.ValidationError('Böyle bir kullanıcı adı yok!')
        
        values = {
            "username" : username,
        } #sözlük biçiminde gönderiyoruz
        return values
            
class RemoveGroupForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["username"]
    def clean(self):
        username = self.cleaned_data.get("username") #submit edilmeden buradan girişleri alıyoruz.
        if User.objects.filter(username = username).exists() is False:
            raise forms.ValidationError('Böyle bir kullanıcı adı yok!')
        
        values = {
            "username" : username,
        } #sözlük biçiminde gönderiyoruz
        return values"""