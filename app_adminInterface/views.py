from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, View
from blog.models import Article, Category, Product
from blog.forms import ArticleForm, CategoryForm, ProductForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def dashboard(request):
    return render(request,'partials/dashboard.html')

def user_products(request):
    if request.session.get('user_is_authenticated'):
        username = request.session.get('username')  # Retrieve username from session
        list_Products = Product.objects.filter(user__username=username)
        if not list_Products:
            list_Products = []  
        return render(request,'partials/my_articles.html', {'list_Products':list_Products})        
    else:
       return redirect('home')   
    #return render(request,'partials/my_articles.html', {'list_articles':list_articles})

class AddArticle(CreateView):
    model=Article
    form_class=ArticleForm
    template_name="partials/add-article.html"
    success_url=reverse_lazy('my_articles')
    
    def form_valid(self,form):
         user_id = self.request.session.get('userid')
         if user_id:
            # If user ID is found in the session, retrieve the user object
            user = User.objects.get(pk=user_id)
            # Set the user of the article
            form.instance.user = user
        # Call the form_valid method of the parent class
         return super().form_valid(form)

class UpdateArticle(UpdateView):
    model=Article
    form_class=ArticleForm
    template_name="app_adminInterface/article_form.html"
    success_url=reverse_lazy('my_articles')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_name = self.object.image.name if self.object.image else None
        context['image_name'] = image_name.split('/')[-1] if image_name else None
        return context

'''
class DeleteArticle(DeleteView):
    model = Article
    success_url = reverse_lazy('my_articles')

    def post(self, request, *args, **kwargs):
        # Get the instance of the article
        self.object = self.get_object()

        # Delete the article
        self.object.delete()

        # Redirect to the success URL
        return HttpResponseRedirect(self.get_success_url())
'''    

class DeleteArticle(View):
    def get(self, request, pk):
        # Retrieve the article object
        article = get_object_or_404(Article, pk=pk)
        # Delete the article
        article.delete()
        # Redirect to the desired URL after deletion
        return redirect('my_articles')
    
#categories
def user_categories(request):
    if request.session.get('user_is_authenticated'):
        username = request.session.get('username')  # Retrieve username from session
        list_Categorys = Category.objects.all()
        if not list_Categorys:
            list_Categorys = []  
        return render(request,'partials/my_categories.html', {'list_Categorys':list_Categorys})        
    else:
       return redirect('home')   
    #return render(request,'partials/my_articles.html', {'list_articles':list_articles})


class AddCategory(CreateView):
    model=Category
    form_class=CategoryForm
    template_name="partials/add-category.html"
    success_url=reverse_lazy('my_categories')
    
class UpdateCategory(UpdateView):
    model=Category
    form_class=CategoryForm
    template_name="app_adminInterface/categorie_form.html"
    success_url=reverse_lazy('my_categories')
     
class DeleteCategory(View):
    def get(self,request, pk):
        # Retrieve the article object
        category = get_object_or_404(Category, pk=pk)
        # Delete the article
        category.delete()
        # Redirect to the desired URL after deletion
        return redirect('my_categories')     
#
class AddProduct(CreateView):
    model=Product
    form_class=ProductForm
    template_name="partials/add-product.html"
    success_url=reverse_lazy('my_products')
    
    def form_valid(self,form):
         user_id = self.request.session.get('userid')
         if user_id:
            # If user ID is found in the session, retrieve the user object
            user = User.objects.get(pk=user_id)
            # Set the user of the article
            form.instance.user = user
        # Call the form_valid method of the parent class
         return super().form_valid(form)
    
class UpdateProduct(UpdateView):
    model=Product
    form_class=ProductForm
    template_name="app_adminInterface/product_form.html"
    success_url=reverse_lazy('my_products')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_name = self.object.image.name if self.object.image else None
        context['image_name'] = image_name.split('/')[-1] if image_name else None
        return context   

class DeleteProduct(View):
    def get(self, request, pk):
        # Retrieve the article object
        product = get_object_or_404(Product, pk=pk)
        # Delete the article
        product.delete()
        # Redirect to the desired URL after deletion
        return redirect('my_products')    

class ReadProduct(UpdateProduct):
    model=Product
    form_class=ProductForm
    template_name="app_adminInterface/read_product.html"
    success_url=reverse_lazy('my_products')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_name = self.object.image.name if self.object.image else None
        context['image_name'] = image_name.split('/')[-1] if image_name else None
        return context   
