"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from web import views
from web.views import ArichiveView, AddCommentView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('web.urls')),
    path('index/', views.Blog, name='home'),
    path('article/<article_id>', views.article),
    path('type/<cate_id>', views.blogs_with_type, name='blogs_with_type'),
    url(r'^archive/$', ArichiveView.as_view(), name='archive'),
    url(r'', include('ckeditor_uploader.urls')),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
