from django.urls import path
from .views import home, professional_weblog, social_weblog, portfolio, personal_weblog, coaching

urlpatterns = [
    path('', home, name='home'),
    path('professional-weblog/', professional_weblog, name='professional'),
    path('social-weblog/', social_weblog, name='social'),
    path('portfolio/', portfolio, name='portfolio'),
    path('personal-weblog/', personal_weblog, name='personal'),
    path('coaching/', coaching, name='coaching'),
]
