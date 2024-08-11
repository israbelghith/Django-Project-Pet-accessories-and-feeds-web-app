from django import forms


class loginforms(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur",widget=forms.TimeInput(attrs={'class':'form-control form-control-lg'}))
    motdepasse=forms.CharField(label="Mot de Passe",widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
   
class Registerforms(forms.Form):

    firstname=forms.CharField(label="Nom",widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    lastname=forms.CharField(label="Prénom",widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    username=forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    email=forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'}))
    password=forms.CharField(label="Mot de Passe",widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
   