from django.urls import path,include
from articles import views


app_name = 'articles'

urlpatterns = [
    path('comment/', views.PublishComment),
    path('comm/<get_comments>/', views.ShowComments.as_view()),
    path('user-stars/<userID>/<get_slug>/', views.ShowUserStars.as_view()),
    path('article-stars/<slug>/', views.ShowArticleStars.as_view()),
    path('star/',views.UpdateUserStars,name='rating_star'),
    path('', views.LatestProductsList.as_view()),
    path('<slug:slug>/', views.Articlee.as_view()),

    
]