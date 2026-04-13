from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ✅ Signup (your custom view)
    path('signup/', views.signup, name='signup'),

    # ✅ Django built-in login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]