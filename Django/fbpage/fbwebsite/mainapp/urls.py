from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('pricing/', views.pricing, name="pricing"),
    path('privacypolicy/', views.privacy, name="privacy"),
    path('about/', views.about, name="about"),
]