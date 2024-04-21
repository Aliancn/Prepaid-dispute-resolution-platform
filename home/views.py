import datetime
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

from home.models import ChatItem, ChatRecord, Image, Provements, UserInfo, Post, Documents, Image, File, User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator

from utils.qianfanmodle import qianfan_Yi_34B_Chat, qianfan_pre_Yi_34B_Chat, qianfan_withHistory_Yi_34B_Chat

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


@login_required
def disputeCases(request):
    try:
        documents = Documents.objects.all()
    except Documents.DoesNotExist:
        documents = []
    context = {
        'segment': 'dispute-cases',
        'documents': documents,
    }
    return render(request, 'pages/dispute-list.html', context)


def lastNews(request):
    context = {
        'segment': 'last-news',
    }
    return render(request, 'pages/last-news.html', context)


# 社区发表页面

@login_required
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
        # 重定向逻辑未写

    return render(request, 'home.html')


# post like


def like(request, post_id=0):

    post = Post.objects.get(id=post_id)
    post.like += 1
    post.save()
    return HttpResponse(post.like)


def postCaseDetails(request, post_id=0):
    # 展示详细post
    try:
        post_details = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post_details = Post.objects.first()
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
        'comments': [
            {
                'comment_id': 0,
                'user_avatar': '/media/static/images/avatar/1.png',
                'user_name': '张三',
                'post_time': '2023-07-01',
                'content': '评论内容, elitrat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.',
            },
            {
                'comment_id': 0,
                'user_avatar': '/media/static/images/avatar/1.png',
                'user_name': '张三',
                'post_time': '2023-07-01',
                'content': '评论内容, elitrat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.',
            }
        ]
    }
    return render(request, 'pages/post-details.html', context)


def successfulCases(request, page_id=1):
    # 社区展示

    discussion_sample = [
        {
            'post_id': 0,
            'cover': '/media/static/images/covers/1.png',
            'title': '一口价黄金套路多',
            'content': '多名消费者向消费者报道反映称一口价黄金存在销售套路，涉及的品牌包括老凤祥、周六福、中国黄金等。他们普遍提及，购买一口价黄金时导购并未如实告知产品克重，而且导购有意回避消费者追询重量和称重的环节。后续消费者称重后才发现每克黄金的单价在800元至1200元，远超克重计价金饰的单价。',
            'avatar': '/media/static/images/avatar/1.png',
            'username': '黄先生',
            'date': '2022-03-04',
            'like': '100'
        },
        {
            'post_id': 2,
            'cover': '/media/static/images/covers/2.png',
            'title': '手机租赁价格高',
            'content': '多名消费者在投诉平台发起投诉称，手机租赁平台租机价格过高，涉及的平台包括俏租机、八戒租、爱租机、优品租等。根据他们的反馈，租赁平台主要提供“租完归还（随时买断）”和“租完即送”两种租赁方案。但两个方案的租机费用均远高于手机的新品发售价。以爱租机上的全新iPhone 15（128G）为例，在租完即送模式下的总花费为7319元。',
            'avatar': '/media/static/images/avatar/2.png',
            'username': '陈先生',
            'date': '2023-06-09',
            'like': '100'
        },
        {
            'post_id': 3,
            'cover': '/media/static/images/covers/3.png',
            'title': '智能家电配套App停止维护，消费者日常使用受影响',
            'content': '多名消费者不满小狗扫地机器人无法连接配套App正常使用。在断连状态下，机器人失去地图规划功能，无法执行自定义避障设定，清扫路线杂乱无章。而小狗客服没有明确回复App的修复时间。据客服介绍，目前小狗已不再经营扫地机器人品类。这或是小狗机器人App停止维护的原因。多名消费者投诉称阿里智能App下架以后，公牛智能插座变成了“摆设”，无法执行远程控制和耗电量统计的功能。',
            'avatar': '/media/static/images/avatar/3.png',
            'username': '李先生',
            'date': '2023-07-01',
            'like': '100'
        },
        {
            'post_id': 4,
            'cover': '/media/static/images/covers/4.png',
            'title': '套路贷屡禁不止',
            'content': '用户张女士在信用飞平台申请了16000元的贷款。贷款期限为1年（十二期），还款方式为等额本息。但她查看账单才发现每期还款除了本金和利息以外，还有担保费。从还款记录来看，她每期还款额（含担保费）大致在1606.93元，换算下来的利率超过了35.9%。她认为担保费比利息还要高，算上担保费后，实际利率已经超过相关规定，与宣称的低利率并不相符。',
            'avatar': '/media/static/images/avatar/4.png',
            'username': '张女士',
            'date': '2021-07-01',
            'like': '100'
        },
        {
            'post_id': 5,
            'cover': '/media/static/images/covers/IMG_C95ABA542BE4-1.jpeg',
            'title': '关于某某案件的讨论',
            'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'avatar': '/media/static/images/covers/IMG_C95ABA542BE4-1.jpeg',
            'username': '某某律师',
            'date': '2021-07-01',
            'like': '100'
        },
        {
            'post_id': 6,
            'cover': '',
            'title': '关于某某案件的讨论(无cover)',
            'content': 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'avatar': '/media/static/images/avatar/avt.jpg',
            'username': '某某律师',
            'date': '2021-07-01',
            'like': '100'
        }
    ]
    # 读取post
    discussion = []
    postall = Post.objects.all()
    for post in postall:
        userinfo = UserInfo.objects.filter(user=post.user.id).first()
        discussion.append({
            'post_id': post.id,
            'cover': post.cover.url if post.cover else '',
            'title': post.title,
            'content':  post.content,
            'avatar': userinfo.avatar.url if userinfo.avatar else '',
            'username': userinfo.user.username,
            'date': post.post_time,
            'like': post.like
        })

    discussion_sample = discussion_sample + discussion

    context = {
        'segment': 'successful-cases',
        'page_id': page_id,
        'discussion': discussion_sample,

    }
    return render(request, 'pages/successful-cases.html', context)


@login_required
def myProvements(request):
    current_user = User.objects.get(username=request.user.username)
    userInfo = UserInfo.objects.filter(user=current_user).first()
    if not userInfo:
        print("Creating new UserInfo for user:", current_user.username)
        userInfo = UserInfo.objects.create(user=current_user)
    else:
        print("User already has UserInfo:", current_user.username)

    my_provements = userInfo.my_provements.all()

    context = {
        'segment': 'my_provements',
        'my_provements': my_provements,
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
        selectedDocument_id = request.POST.get('selected_document')

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

        document = Documents.objects.filter(id=selectedDocument_id).first()

        pro = Provements.objects.create(
            user=current_user, title=title, content=content, document=document)
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


# ai 智能分析
class smartAnalysis(View):
    def getHistory(self, topic):
        if not self.request.user.is_authenticated:
            return []
        if topic:
            topic_history = ChatItem.objects.filter(
                user=self.request.user, topic=topic).order_by('-created_at')
        else:
            topic_history = []
        return topic_history

    # @method_decorator(login_required)
    def get(self, request):
        # history = self.getHistory()
        topic = request.GET.get('topic')
        user = request.user
        topics = []
        if not user.is_authenticated:
            topic_history = [
                {
                    'user': '未登陆',
                    'topic': 'topic',
                    'message': 'message',
                    'response': 'response',
                    'created_at': 'time',
                },
                {
                    'user': '未登陆',
                    'topic': 'topic2',
                    'message': 'message2',
                    'response': 'response2',
                    'created_at': 'time2',
                },
            ]
        else:
            topic_history = self.getHistory(topic)
            try:
                topics = ChatRecord.objects.get(user=user.id).topic
            except ChatRecord.DoesNotExist:
                topics = []

        context = {
            'segment': 'smart-analysis',
            'history': topic_history,
            'topics': topics,
            'topic_now': topic if topic else '未选择',
        }
        return render(request, 'pages/smart-analysis.html', context)
# @method_decorator(login_required)

    def post(self, request):
        # 登陆会保存历史信息，不登陆不会保存历史信息
        message = request.POST.get("message")
        topic = request.POST.get("topic")
        history = self.getHistory(topic)
        if self.request.user.is_authenticated:
            # TODO : 上下文传输
            # response = qianfan_Yi_34B_Chat(message)
            historylist = []
            for h in history:
                historylist.append({
                    'role': 'user',
                    'content': h.message
                })
                historylist.append({
                    'role': 'assistant',
                    'content': h.response
                })
            if historylist == []:
                print("无历史信息")
                if "案例" in message:
                    print("案例")
                    response = qianfan_pre_Yi_34B_Chat(message)
                else:
                    response = qianfan_withHistory_Yi_34B_Chat(
                        message, historylist)
            else:
                print("有历史信息")
                if "案例" in message:
                    print("案例")
                    response = qianfan_pre_Yi_34B_Chat(message)
                else:
                    print("有历史信息")
                    response = qianfan_withHistory_Yi_34B_Chat(
                        message, historylist)
            if topic:
                chat_message = ChatItem(user=request.user, topic=topic,
                                        message=message, response=response.body['result'],
                                        created_at=datetime.datetime.now())
                chat_message.save()
        else:
            print("未登录询问")
            historylist = []
            response = qianfan_withHistory_Yi_34B_Chat(message, historylist)
        response = response.body['result']
        return JsonResponse({"message": message, "response": response})


def smartAnalysisTopic(request):
    # 新建topic
    topic = request.POST.get('topic')
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"message": "未登录"})
    if not topic:
        return JsonResponse({"message": "未输入topic"})
    # 检查是否存在相同topic
    try:
        topicSet = ChatRecord.objects.get(user=user.id)
    except ChatRecord.DoesNotExist:
        topicSet = ChatRecord.objects.create(user=user)

    for item in topicSet.topic:
        if item == topic:
            return JsonResponse({"message": "topic已存在"})
    # 创建新topic
    topicSet.topic.append(topic)
    topicSet.save()
    return JsonResponse({"message": "创建成功"})


def test(request):
    res = User.objects.first().id
    return HttpResponse(res)

# 案例库展示


@login_required
def documents(request):
    # 创建五个 Documents 实例并保存到数据库
    # documents = []
    # for i in range(1, 6):
    #     document = Documents.objects.create(
    #         user=request.user,
    #         title=f'Document {i}',
    #         content=f'This is document {i} content.',
    #         file=f'static/files/document_{i}.pdf'
    #     )
    #     documents.append(document)
    try:
        documents = Documents.objects.all()
    except Documents.DoesNotExist:
        documents = []
    context = {
        'segment': 'documents',
        'documents': documents,
    }
    return render(request, 'pages/documents.html', context)
