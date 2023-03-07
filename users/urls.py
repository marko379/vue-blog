from django.urls import path,include
from users import views


app_name = 'users'

urlpatterns = [
    path('register/', views.register_api_2),
    # path('u/', views.register_api),
    path('login/', views.login_api),
    path('profile-user/', views.UserView.as_view()),
    path('exe/', views.ExeView),
    path('new/', views.NewView.as_view()),
]