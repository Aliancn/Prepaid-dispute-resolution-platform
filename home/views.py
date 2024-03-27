from django.shortcuts import render
from django.http import HttpResponse

from home.models import Image, Provements, User, Post, Documents

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')



def home(request):
    context = {
        'segment': 'home',
    }
    return render(request, 'pages/home.html', context)

def smartAnalysis(request):
    context = {
        'segment': 'smart-analysis',
    }
    return render(request, 'pages/smart-analysis.html', context)

def disputeCases(request):
    context = {
        'segment': 'dispute-cases',
    }
    return render(request, 'pages/dispute-list.html', context)

def lastNews(request):
    context = {
        'segment': 'last-news',
    }
    return render(request, 'pages/last-news.html', context)

def successfulCases(request):
    context = {
        'segment': 'successful-cases',
    }
    return render(request, 'pages/successful-cases.html', context)


def provements_upload(request):
    if request.method == 'POST':
        print('证据上传')
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        img_provements = request.FILES.getlist('img_provements')
        
        img_ids = []
        for img in img_provements:
            image_id = Image.objects.create(image=img, intro=title).id
            img_ids.append(image_id)
        # TODO 
        pro = Provements.objects.create(user_id=user_id, title=title, content=content, img_provements=img_ids)
    return HttpResponse('证据上传 成功')

