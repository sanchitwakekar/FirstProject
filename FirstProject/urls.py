"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from Firstapp import views
from rest_framework_swagger.views import get_swagger_view
from django.urls import path
from Firstapp.views import ArticleView
from rest_framework_simplejwt import views as jwt_views

swag = get_swagger_view(title='Polls API')

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('', views.index, name="index"),
    path('swagger-docs/', swag),
    path('articles/', ArticleView.as_view()),
    path('hello/', views.JWTDemo.as_view(), name='hello'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('form/', views.form_name_view, name='form_name'),
]
