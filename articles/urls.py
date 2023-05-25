from django.urls import path,include
from articles import views


app_name = 'articles'

urlpatterns = [
    path('comment/', views.PublishComment),
    path('like-dislike-comment/', views.comment_like_dislike_system),
    path('book-to-basket/', views.AddBookBasket),
    path('get-books-from-basket/', views.ReturnBasket),
    path('delete-book-from-basket/', views.DeleteBookBasket),
    path('delete-comment/', views.delete_comment),
    path('comm/<get_comments>/', views.ShowComments.as_view()),
    path('books-by-genres/<genre>/', views.BookByGenres.as_view()),
    path('carousel-books/', views.BookForCarousel),
    path('search_books/<value>/', views.search_book.as_view()),
    path('user-stars/<userID>/<get_slug>/', views.ShowUserStars.as_view()),
    path('article-stars/<slug>/', views.ShowArticleStars.as_view()),
    path('star/',views.UpdateUserStars,name='rating_star'),
    path('', views.LatestProductsList.as_view()),
    path('<slug:slug>/', views.Articlee.as_view()),

    
]