from django.shortcuts import render, redirect
from django.http import HttpResponse

from home.models import Image, Provements, UserInfo, Post, Documents, Image, File
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Image, Provements, User, Post, Documents
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def myProvements(request):
    context = {
        'segment': 'my-provements',
    }
    return render(request, 'pages/my-provements.html', context)

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

def myProvements(request):
    context = {
        'segment': 'my-provements',
    }
    return render(request, 'pages/my-provements.html', context)

@login_required
def provements_upload(request):
    if request.method == 'POST':
        print('证据上传')
        current_user = User.objects.get(username=request.user.username)
        title = request.POST.get('title')
        content = request.POST.get('content')
        img_provements = request.FILES.getlist('img_provements')
        file_provements = request.FILES.getlist('file_provements')
        file_info = request.POST.getlist('file_info')
        img_info = request.POST.getlist('img_info')

        img_ids = []
        if img_provements:
            for i, img in enumerate(img_provements):
                # 获取对应的 img_info
                current_img_info = img_info[i] if i < len(img_info) else ''
                # 假设 Image 是你的图片模型
                image = Image.objects.create(image=img, intro=current_img_info)
                img_ids.append(image.id)

        file_ids = []
        if file_provements:
            for i, file in enumerate(file_provements):
                current_file_info = file_info[i] if i < len(file_info) else ''
                file_instance = File.objects.create(file=file, intro=current_file_info)
                file_ids.append(file_instance.id)
            
        pro = Provements.objects.create(user=current_user, title=title, content=content)
        if img_ids:
            pro.img_provements.add(*img_ids) 
        if file_ids:
            pro.file_provements.add(*file_ids) 
        
        pro.save()
        
        additional_info = request.POST.get('additional_info')
        # TODO: Process additional_info as needed
        
        userinfo = UserInfo.objects.filter(user=current_user).first()
        if not userinfo:
            userinfo = UserInfo.objects.create(user=current_user)
        userinfo.my_provements.add(pro)
        
        messages.success(request, '证据上传成功')
        return redirect('my-provements')

    return render(request, 'home.html')


def test(request):
    res = User.objects.first().id
    return HttpResponse(res)