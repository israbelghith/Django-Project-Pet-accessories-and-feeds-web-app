from django import forms
from .models import Article, Category, Product
from django.forms import ModelForm

class ArticleForm(ModelForm):    #peut hériter de forms.Form ou forms.ModelForm
    class Meta:
        model=Article
        fields=['title','category','desc','price','image'] #les champs qu'ils seront afficher dans le modèle
        labels={'title':'Titre','category':'catégorie','desc':'Description','price':'Prix','image':'Image'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class CategoryForm(ModelForm):    #peut hériter de forms.Form ou forms.ModelForm
    class Meta:
        model=Category
        fields=['name'] #les champs qu'ils seront afficher dans le modèle
        labels={'name':'Nom'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }     
        
class ProductForm(ModelForm):    #peut hériter de forms.Form ou forms.ModelForm
    class Meta:
        model=Product
        fields=['title','category','desc','price','image'] #les champs qu'ils seront afficher dans le modèle
        labels={'title':'Titre','category':'catégorie','desc':'Description','price':'Prix','image':'Image'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','rows':8}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }           