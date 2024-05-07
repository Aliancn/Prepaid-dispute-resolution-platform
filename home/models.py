from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

# 用户model


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        upload_to='static/images/avatar/', null=True, blank=True, default='static/images/avatar/1.png')


    # 关联
    my_provements = models.ManyToManyField(
        'provements', related_name='my_provements')
    my_posts = models.ManyToManyField('post', related_name='my_posts')

    def __str__(self):
        return self.user.username


# 证据model
class Provements(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # provement = models.ImageField(upload_to='static/provements/', null=True, blank=True)
    file_provements = models.ManyToManyField(
        'File', related_name='file_provements')
    img_provements = models.ManyToManyField(
        'Image', related_name='img_provements')
    content = models.TextField()
    title = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 社区帖子model
class Post (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(
        upload_to='static/images/covers/', null=True, blank=True)
    post_time = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    published_status = models.IntegerField(default=0, blank=True, null=True)


    def __str__(self):
        return self.title


class Documents(models.Model):
    # 案例库文件model
    id = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='static/files/', null=True, blank=True)


class Image(models.Model):
    # 图片model
    id = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=100)  # 简介
    image = models.ImageField(
        upload_to='static/images/', null=True, blank=True)

    def __str__(self):
        return self.intro


class File(models.Model):
    # 文件model
    id = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=100)  # 简介
    file = models.FileField(upload_to='static/files/', null=True, blank=True)

    def __str__(self):
        return self.intro


class ChatItem(models.Model):
    # 单个的聊天记录 包含一问一答
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"


class ChatRecord(models.Model):
    # 用户的聊天记录 包含所有的topic
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = ArrayField(models.CharField(max_length=100),
                       blank=True, default=list)

    def __str__(self):
        return f"{self.user.username}"

class Comments(models.Model):
    # 评论model
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content