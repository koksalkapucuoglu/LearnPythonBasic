from django import forms
from .models import Content
from django.contrib.auth.models import Group,User

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields =["playing_time","session_count","total_step","total_walk","total_run","total_calori"]
        
class AddGroupForm(forms.ModelForm):
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
        return values
                
        