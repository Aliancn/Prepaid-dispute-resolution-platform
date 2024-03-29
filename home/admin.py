from django.contrib import admin
from .models import Provements, Post, UserInfo, Documents, Image, File

# Register your models here.


admin.site.register(UserInfo)
admin.site.register(Post)

admin.site.register(Provements)
admin.site.register(Documents)
admin.site.register(Image)
admin.site.register(File)
