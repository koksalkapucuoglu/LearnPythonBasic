from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget = forms.PasswordInput)
    email = forms.EmailField(max_length=200, help_text='Required')
    def clean(self):
        username = self.cleaned_data.get("username") #submit edilmeden buradan girişleri alıyoruz.
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor!")

        if User.objects.filter(username = username).exists():
                raise forms.ValidationError('Böyle bir kullanıcı adı zaten var!')
                
        values = {
            "username" : username,
            "password" : password,
            "email" : email,
        } #sözlük biçiminde gönderiyoruz

        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

    