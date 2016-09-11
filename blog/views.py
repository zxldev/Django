from django.shortcuts import render
from blog.models import Article
from zxldev.service.elasticSearchService import SearchService,SearchIndex,SearchType

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def list(request):
    result = Article.objects.db_manager('blog').raw('select * from blog_article')
    sr = SearchService.getClient()
    for a in result :

        sr.index(index=SearchIndex.blog.value,doc_type=SearchType.entity.value,id=a.id,body={
            "title":a.title,
            'content':a.content,
            "category":a.categroy
        })
    return render(request,'blog/list.html',{'blog_entries':result})