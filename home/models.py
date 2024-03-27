from django.db import models

# Create your models here.

# 用户model
class User (models.Model):
    id = models.AutoField(primary_key=True)
    username= models.CharField(max_length=100,unique=True)
    password= models.CharField(max_length=100)
    
    avator = models.ImageField(upload_to='static/images/avator',null=True,blank=True)
    email = models.EmailField(max_length=100,unique=True)
    
    # 关联
    my_provements = models.ManyToManyField('provements',related_name='my_provements')
    my_posts= models.ManyToManyField('post',related_name='my_posts')
    def __str__(self):
        return self.user_name
    
    
# 证据model
class Provements(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # provement = models.ImageField(upload_to='static/provements/', null=True, blank=True)
    img_provements = models.ManyToManyField('Image', related_name='img_provements')
    content = models.TextField()
    title = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user_name
    
    
# 社区帖子model 
class Post (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.user_name
    
# 案例库文件model   
class Documents(models.Model):
    id = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='static/files/', null=True, blank=True)
    
# 图片model 
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=100) # 简介
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    