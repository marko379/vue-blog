from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    re_path(r'^(?!api|admin|static|media).*$', TemplateView.as_view(template_name='index.html'), name='vue_frontend')
]
