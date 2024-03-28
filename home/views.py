from django.shortcuts import render, redirect
from django.http import HttpResponse

from home.models import Image, Provements, User, Post, Documents
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Image, Provements, User, Post, Documents
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    # Page from the theme
    return render(request, 'pages/index.html')

# 主页面


def home(request):
    context = {
        'segment': 'home',
    }
    return render(request, 'pages/home.html', context)

# 解决方案生成


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


def myProvements(request):
    context = {
        'segment': 'my-provements',
    }
    return render(request, 'pages/my-provements.html', context)


def lastNews(request):
    context = {
        'segment': 'last-news',
    }
    return render(request, 'pages/last-news.html', context)


# 社区展示
def successfulCases(request, page_id=1):

    context = {
        'segment': 'successful-cases',
        'page_id' : page_id, # 1: 最热 2: 最新 3: 点赞
        'discussion': [
            {
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
            },
            {
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
            },
            {
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
            },
            {
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
            },
            {
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
            },
            {
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
            }
        ],

    }
    return render(request, 'pages/successful-cases.html', context)

# 社区发表文章


def postCase(request):
    context = {
        'segment': 'post',
    }
    return render(request, 'pages/post.html', context)


def myProvements(request):
    context = {
        'segment': 'my-provements',
    }
    return render(request, 'pages/my-provements.html', context)


# 证据上传
@login_required
def provements_upload(request):
    if request.method == 'POST':
        print('证据上传')
        # 获取当前登录用户
        current_user = User.objects.get(username=request.user.username)
        title = request.POST.get('title')
        content = request.POST.get('content')
        img_provements = request.FILES.getlist('img_provements')

        # 如果有图片上传，则处理图片
        img_ids = []
        if img_provements:
            for img in img_provements:
                # 假设 Image 是你的图片模型
                image_id = Image.objects.create(image=img, intro=title).id
                img_ids.append(image_id)

        # 创建 Provements 对象，并将其与当前用户关联
        pro = Provements.objects.create(
            user=current_user, title=title, content=content)
        if img_ids:
            pro.img_provements.add(*img_ids)  # 将上传的图片关联到 Provements 对象中

        # 保存 Provements 对象到数据库中
        pro.save()

        # 收集和处理附加信息
        additional_info = request.POST.get('additional_info')
        # TODO: Process additional_info as needed

        # 重定向到某个页面或者返回一个成功的消息
        return redirect('dispute-list')

    # 如果不是 POST 请求，则返回一个空表单页面或其他适当的响应
    return render(request, 'home.html')


def test(request):
    res = User.objects.first().id
    return HttpResponse(res)
