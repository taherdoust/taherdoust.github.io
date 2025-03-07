from django.shortcuts import render
from .models import Post

# Home Page (Unique Design)
def home(request):
    return render(request, 'index.html')

# Generic function to load weblog pages dynamically
def weblog_page(request, classification, title, heading, description):
    posts = Post.objects.filter(classification=classification, privacy='public').order_by('-datetime')
    return render(request, 'weblog/weblog_page.html', {
        'page_title': title,
        'page_heading': heading,
        'page_description': description,
        'posts': posts
    })

# Define each weblog page using the dynamic function
def professional_weblog(request):
    return weblog_page(request, 'professional', 'Professional Weblog', 'Welcome to the Professional Weblog', 'We discuss digitalization, smart cities, architecture, and more.')

def social_weblog(request):
    return weblog_page(request, 'social', 'Social Weblog', 'Welcome to the Social Weblog', 'Discussing political debates and social issues.')

def portfolio(request):
    return weblog_page(request, 'portfolio', 'My Portfolio', 'Welcome to my Portfolio', 'Here is my portfolio.')

def personal_weblog(request):
    return weblog_page(request, 'personal', 'Personal Weblog', 'Welcome to my Personal Blog', 'Sharing my memories and experiences.')

def coaching(request):
    return weblog_page(request, 'coaching', 'Coaching & Self-Improvement', 'Welcome to the Coaching Page', 'Exploring personal growth and development strategies.')
