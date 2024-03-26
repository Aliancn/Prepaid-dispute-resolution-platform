from django.shortcuts import render
from django.http import HttpResponse

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
