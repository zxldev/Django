from django.shortcuts import render
from django.http import HttpResponse
from  blog.models import Article
# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def list(request):
    result = Article.objects.db_manager('blog').raw('select * from blog_article')
    for a in result :
        print(a.title,a.content)
    return render(request,'blog/list.html',{'blog_entries':result})