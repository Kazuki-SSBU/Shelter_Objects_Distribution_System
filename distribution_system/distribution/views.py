from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .models import RequestData
from .forms import RequestForm
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .models import RequestData
from .forms import RequestForm


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def modeltest(request):
    object_list = RequestData.objects.all()
    return render(request, 'moteltest.html', {'object_list':object_list})

def input_form(request):
    # context = {"sample_var1": "テスト1", "sample_var2":"テスト2"}
    # return render(request, "input_form.html", context)
    print("metho")
    if request.method == 'POST':
        print("iiiii")
        form = RequestForm(request.POST)
        if form.is_valid():
            print("PPP")
            request_data = RequestData()
            request_data.category = form.cleaned_data['category']
            request_data.item_name = form.cleaned_data['item_name']
            request_data.request_num = form.cleaned_data['request_num']
            request_data.stock_num = form.cleaned_data['stock_num']
            request_data.address = form.cleaned_data['address']
            request_data.name = form.cleaned_data['name']
            request_data.distributed_num = 0
            request_data.save()
            return redirect('moteltest')
    else:
        print("llll")
        form = RequestForm()
            
        pass
    return render(request, "input_form.html", {'form':form})
# Create your views here.


# from django.http.response import HttpResponseNotAllowed
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import Reporter, Article
# from .forms import ArticleForm

# def hello(request):
#     hw = 'Hello World!'
#     return render(request, 'base.html', {'object':hw})

# def modeltest(request):
#     object_list = Article.objects.all()
#     return render(request, 'modeltest.html', {'object_list':object_list})

# def formtest(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = Article()
#             article.pub_date = form.cleaned_data['pub_date']
#             article.headline = form.cleaned_data['headline']
#             article.content = form.cleaned_data['content']
#             article.reporter = form.cleaned_data['reporter']
#             article.save()
#             return redirect('modeltest')

#     else:
#         form = ArticleForm()

#     return render(request, 'form.html', {'form': form})  


# from django.http.response import HttpResponseNotAllowed
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .models import Reporter, Article
# from .forms import ArticleForm

# def hello(request):
#     hw = 'Hello World!'
#     return render(request, 'base.html', {'object':hw})

# def modeltest(request):
#     object_list = Article.objects.all()
#     return render(request, 'modeltest.html', {'object_list':object_list})

# def formtest(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = Article()
#             article.pub_date = form.cleaned_data['pub_date']
#             article.headline = form.cleaned_data['headline']
#             article.content = form.cleaned_data['content']
#             article.reporter = form.cleaned_data['reporter']
#             article.save()
#             return redirect('modeltest')

#     else:
#         form = ArticleForm()

#     return render(request, 'form.html', {'form': form})  
