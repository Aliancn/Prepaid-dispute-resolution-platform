import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse

from home.models import Image, Provements, UserInfo, Post, Documents, Image, File, User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

# 社区发表页面


def postCase(request):
    context = {
        'segment': 'post',
    }
    return render(request, 'pages/post.html', context)

# 社区发表提交

@login_required
def post_upload(request):
    if request.method == 'POST':
        print('发表帖子')
        current_user = User.objects.get(username=request.user.username)
        title = request.POST.get('title')
        content = request.POST.get('content')
        cover = request.FILES.get('cover')  # 获取上传的文件

        post = Post.objects.create(
            user=current_user, title=title, content=content)
        if cover:  
            post.cover = cover
        post.save()

        userinfo = UserInfo.objects.filter(user=current_user).first()
        if not userinfo:
            userinfo = UserInfo.objects.create(user=current_user)
        userinfo.my_posts.add(post)

        messages.success(request, '帖子发表成功')
        return redirect('/home')
        #重定向逻辑未写

    return render(request, 'home.html')


# post like


def like(request, post_id=0):

    post = Post.objects.get(id=post_id)
    post.like += 1
    post.save()
    return HttpResponse(post.like)

# 展示详细post


def postCaseDetails(request, post_id=0):
    post_details = Post.objects.get(id=post_id)
    title = post_details.title
    content = post_details.content
    user = post_details.user
    user_info = user.userinfo
    cover = post_details.cover
    post_time = post_details.post_time
    like = post_details.like

    context = {
        'segment': 'post-details',
        'post_id': post_id,
        'title': title,
        'content': content,
        'user_name': user.username,
        'user_avatar': user_info.avatar.url if user_info.avatar else '',
        'cover': cover.url,
        'post_time': post_time,
        'like': like,
    }
    return render(request, 'pages/post-details.html', context)

# 社区展示


def successfulCases(request, page_id=1):

    context = {
        'segment': 'successful-cases',
        'page_id': page_id,  # 1: 最热 2: 最新 3: 点赞
        'discussion': [
            {
                'post_id': 0,
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
                'like': '100'
            },
            {
                'post_id': 2,
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
                'like': '100'
            },
            {
                'post_id': 3,
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
                'like': '100'
            },
            {
                'post_id': 4,
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
                'like': '100'
            },
            {
                'post_id': 5,
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
                'like': '100'
            },
            {
                'post_id': 6,
                'cover': '/static/images/case-test.jpeg',
                'title': '关于某某案件的讨论',
                'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'avatar': '/static/images/avatar/avt.jpg',
                'username': '某某律师',
                'date': '2021-07-01',
                'like': '100'
            }
        ],

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
                file_instance = File.objects.create(
                    file=file, intro=current_file_info)
                file_ids.append(file_instance.id)

        pro = Provements.objects.create(
            user=current_user, title=title, content=content)
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

# 案例库展示
def documents(request):
    documents = Documents.objects.all()
    context = {
        'segment': 'documents',
        'documents': documents,
    }
    return render(request, 'pages/documents.html', context)