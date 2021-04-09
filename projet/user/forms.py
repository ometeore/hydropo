from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import MyUser


class Connexion(forms.Form):
    identifiant = forms.CharField(label="identifiant", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class Creation(forms.Form):
    last_name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Nom"}))
    first_name = forms.CharField(label="Prénom", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Prenom"}))
    Username = forms.CharField(label="Pseudo", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Pseudo"}))
    email = forms.EmailField(label="email", widget=forms.TextInput(attrs={'placeholder':"email"}))
    confirm_password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'placeholder':"Mot de passe"}))
    password = forms.CharField(label="Confirmation mot de passe", widget=forms.PasswordInput(attrs={'placeholder':"Confirmation mot de passe"}))

class CreationRpi(forms.Form):
    name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Nom"}))


class Update(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('rpi',)