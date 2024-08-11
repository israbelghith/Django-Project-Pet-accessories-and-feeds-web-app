from django.shortcuts import render
from .models import Article, Category, Product

def home(request):
   lisprod=Product.objects.all()
   list_articles=Article.objects.all()
   list_categories=Category.objects.all()
   context={"lisprod":lisprod, "list_categories":list_categories}
   return  render(request,"index.html",context)
# Create your views here.

def consulter(request,id_article):
   article=Article.objects.get(id=id_article)
   print('id est ',id_article)
   category=article.category
   list_articles=Article.objects.filter(category=category)[:5]
   #list_articles=Article.objects.all()
  # context={"list_articles":list_articles}
   return render(request,'consulter.html',{'article':article,'list_articles':list_articles})


def search(request):
    list_categories=Category.objects.all()
    query = request.GET.get("article", "")
    if query:
        liste_articles = Article.objects.filter(title__icontains=query)
    else:
        liste_articles = []
    return render(request, "search.html", {"liste_articles": liste_articles,"list_categories":list_categories})
'''def search(request):
   query=request.GET["article"]
   liste_articles=Article.objects.filter(title__icontains=query) '''   #title__icontains : i: s'il contient accents

def listeArticles(request,pk):
   list_categories=Category.objects.all()
   list_artCateg = Article.objects.filter(category_id=pk)
   return  render(request,"listeArticles.html",{"list_artCateg":list_artCateg, "list_categories":list_categories})

#Products
def consulterProd(request,id_product):
   list_categories=Category.objects.all()
   prod=Product.objects.get(id=id_product)
   print('id est ',id_product)
   category=prod.category
   list_produits=Product.objects.filter(category=category)[:4]
   #list_articles=Article.objects.all()
  # context={"list_articles":list_articles}
   return render(request,'consulter.html',{'article':prod,'list_articles':list_produits,'list_categories':list_categories})

def searchProd(request):
    list_categories=Category.objects.all()
    query = request.GET.get("product", "")
    if query:
        liste_Products = Product.objects.filter(title__icontains=query)
    else:
        liste_Products = []
    return render(request, "search.html", {"liste_Products": liste_Products,"list_categories":list_categories})
 
def listeProducts(request,pk):
   list_categories=Category.objects.all()
   list_prodCateg = Product.objects.filter(category_id=pk)
   return  render(request,"listeArticles.html",{"list_prodCateg":list_prodCateg, "list_categories":list_categories})



