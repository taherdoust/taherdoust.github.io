from django.shortcuts import render

def home(request):
    return render(request, 'weblog/home.html')

def professional_weblog(request):
    return render(request, 'weblog/professional.html')

def social_weblog(request):
    return render(request, 'weblog/social.html')

def portfolio(request):
    return render(request, 'weblog/portfolio.html')

def personal_weblog(request):
    return render(request, 'weblog/personal.html')

def coaching(request):
    return render(request, 'weblog/coaching.html')