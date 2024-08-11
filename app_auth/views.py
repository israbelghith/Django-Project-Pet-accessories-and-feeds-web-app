from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout # django possède la  méthode authenticate qui permet d'auth l'utilis
from django.contrib import messages
from .forms import loginforms,Registerforms
from django.contrib.auth.decorators import login_required
from blog.models import Article
from django.contrib.auth.models import User
from blog.views import home
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    errors = {}
    username = ''
    password = ''

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                #login(request)
                #list_articles=Article.objects.all()
                #request.session['user_is_authenticated'] = user
                request.session['user_is_authenticated'] = True
                request.session['username'] = user.username
                request.session['userid'] = user.id
                return redirect('/')#render(request, '/', {'user_is_authenticated': user, 'list_articles': list_articles})
            else:
                errors['auth'] = "Erreur d'authentification"
        else:
            errors['auth'] = "Erreur d'authentification"

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form, 'errors': errors})
'''errors = {}
    username = ''
    password = ''

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = authenticate(username=username, password=password)
        if not username and  not password:
            errors['userError'] = "Erreur d'authentification"
        elif not username:
                errors['username'] = "Nom d'utilisateur est vide"

        elif not password:
                errors['password'] = "Mot de passe est vide"
                
        #si user  data existe et il fait partie de sys , user sera != null
        if not errors:
            
           if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                # Authentication failed
                errors['auth'] = "Erreur d'authentification"
      #  print(f'le nom: {username}, password:{password} !!! ')
    return render(request,"login.html",  {'username': username,'password': password, 'errors': errors,'user_is_authenticated': request.user.is_authenticated}) 
'''  
       
# Create your views here.
def register(request):
    if request.method=='POST':
        form=Registerforms(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=firstname, last_name=lastname,email=email,username=username,password=password)
            if user is not None:
                return redirect('login')
            else:
                messages.error(request,'création de compte échouée')
                return render(request,'register.html',{'form':form})
        else:
            return render(request,'register.html',{'form':form})
        #return render(request,'register.html',{})
    form =Registerforms()
    return render(request,'register.html',{'form':form})

def logout_User(request):
    logout(request)
    #list_articles=Article.objects.all()
    return redirect('/')#render(request,'index.html',{'list_articles':list_articles}) 

