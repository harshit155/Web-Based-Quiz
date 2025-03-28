"""
URL configuration for quiz_techinfini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from quiz_app import views



from quiz_app import views
from quiz_app.views import CustomLoginView
from quiz_app.views import custom_redirect

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("userdashboard/", views.userdashboard, name="userdashboard"),
    path("add_quiz/", views.add_quiz, name="add_quiz"),
    path("take_quiz/", views.take_quiz, name="take_quiz"),
    path("view_score/", views.view_score, name="view_score"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("accounts/profile/", custom_redirect),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]

