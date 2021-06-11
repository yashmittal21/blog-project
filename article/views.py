from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from . import forms
# Create your views here.
 
def home(request):
	article = Article.objects.all().order_by('date')
	return render(request,'index.html',{
		"article":article
		})

def detail(request,slug):
	article = Article.objects.get(slug=slug)
	return render(request,"detail.html",{
		"article":article
		})

def create_article(request): 
	if(request.method=='POST'):
		form = forms.CreateArticle(request.POST)
		if(form.is_valid()):
			objct = form.save(commit=False)
			objct.author = request.user
			objct.save()
			return redirect('/article')
	#making an object of class CreateArticle
	form = forms.CreateArticle()
	return render(request,'create.html',{
		'form':form
		})