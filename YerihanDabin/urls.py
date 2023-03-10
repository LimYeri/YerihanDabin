"""YerihanDabin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # admin 페이지
    path("admin/", admin.site.urls),
    # main 페이지
    path("", include('main.urls')),
    # 소셜로그인
    re_path(r'^accounts/', include('allauth.urls')),
    # 유저 관련
    path("accounts/", include('accounts.urls')),
    # 약 제품 관련
    path("medicine/", include('medicine.urls')),
    # Q&A 게시판 관련
    path("Blog/", include('Blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
