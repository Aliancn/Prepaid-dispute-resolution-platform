from django.shortcuts import redirect
from django.urls import include, path
from django.conf.urls.static import static

from core import settings
from . import views

urlpatterns = [
    path('', views.home, name='/'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('smart-analysis/', views.smartAnalysis.as_view(), name='smart-analysis'),
    path('smart-analysis/topic/', views.smartAnalysisTopic, name='add-topic'),
    path('dispute-cases/', views.disputeCases, name='dispute-list'),
    path('last-news/', views.lastNews, name='last-news'),
    path('successful-cases/<int:page_id>/',
         views.successfulCases, name='successful-cases'),
    path('post-case/', views.postCase, name='post-case'),
    path('post-case-details/<int:post_id>/',
         views.postCaseDetails, name='post-details'),
    path('like/<int:post_id>/', views.like, name='like'),
    path('my-provements/', views.myProvements, name='my-provements'),
    path('provements_upload/', views.provements_upload, name='provements_upload'),
    path('post_upload/', views.post_upload, name='post_upload'),
    path('test/', views.test, name='test'),
    path('documents/', views.documents, name='documents'),
    path('my-posts/', views.myPosts, name='my-posts'),
    path('documents_create/', views.documents_create, name='documents_create'),
    path('comments_upload/', views.comments_upload, name='comments_upload'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
