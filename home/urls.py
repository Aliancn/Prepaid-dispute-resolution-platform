from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('smart-analysis/',views.smartAnalysis,name='smart-analysis'),
    path('dispute-cases/',views.disputeCases,name='dispute-list'),
    path('last-news/',views.lastNews,name='last-news'),
    path('successful-cases/',views.successfulCases,name='successful-cases'),
]
