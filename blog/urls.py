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
    # path('', views.index, name='home'),

    # Catch-all route for Vue frontend
    # re_path(r'^(?!admin|static).*$', views.index, name='vue_frontend'),
    re_path(r'^(?!api|admin|static|media).*$', TemplateView.as_view(template_name='index.html'), name='vue_frontend')
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)