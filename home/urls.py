from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('smart-analysis/',views.smartAnalysis,name='smart-analysis'),
    path('dispute-cases/',views.disputeCases,name='dispute-list'),
    path('last-news/',views.lastNews,name='last-news'),
    path('successful-cases/',views.successfulCases,name='successful-cases'),
    path('my-provements/',views.myProvements,name='my-provements'),
    path('provements_upload/',views.provements_upload,name='provements_upload'),
    path('test/',views.test,name='test'),
]
