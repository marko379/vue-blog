from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Article, Category,Comments,Rating_star_system,Users_stars,Books_in_Basket
from users.models import User_photo
from .serializers import Article_Serializer, Category_Serializer, Comments_Serializer,Show_User_Stars_Serializer,Show_Article_Stars_Serializer,Book_in_Basket_Serializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count, Min, Sum


class LatestProductsList(APIView):

    def get(self, request, format=None):
        try:
            articles = Article.objects.all()
            # get all articles with your serializer 
            serializer = Article_Serializer(articles, many=True)
            # when is returned you can accsess those data in vue template
            return Response(serializer.data)
        except Exception as e:
            print("Error in articles_list:", str(e))  # log to Railway logs
            return Response({"error": str(e)}, status=500)

class Articlee(APIView):
    def get(self, request, slug):
        articless = Article.objects.get(slug=slug)
        # comments = Comments.objects.filter(article=articless)
        serializer = Article_Serializer(articless)
        return Response(serializer.data)

class ShowComments(APIView):
    def get(self, request, get_comments):
        articless = Article.objects.get(slug=get_comments)
        comments = Comments.objects.filter(article=articless).annotate(num_authors=Count('comment_likes')).order_by('-num_authors')
        serializer = Comments_Serializer(comments, many=True)
        return Response(serializer.data)

class ShowUserStars(APIView):
    def get(self, request, userID,get_slug):
        if userID != 'null':
            articless = Article.objects.get(slug=get_slug)
            user = User.objects.get(id=userID)
            stars = Users_stars.objects.filter(article=articless,user=user)
            serializer = Show_User_Stars_Serializer(stars, many=True)
            if not serializer.data:
                return Response('not rated')
            else:
                return Response(serializer.data)

class BookByGenres(APIView):
    def get(self, request, genre):
        articless = Article.objects.filter(category__name=genre)
        serializer = Article_Serializer(articless,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def BookForCarousel(request):  # use APIview or function based view or any view u want
    if request.method == 'POST':

        answers_list = list(request.POST)
        num = 0
        while len(answers_list) <= 3:
            add_value = answers_list[num]
            answers_list.append(add_value)
            num = num + 1 
        

        queryset = Article.objects.filter(
            Q(category__name__icontains=answers_list[0]) |
            Q(category__name__icontains=answers_list[1]) |
            Q(category__name__icontains=answers_list[2]) 
        ).distinct()[:9]

        serializer = Article_Serializer(queryset, many=True)

        return Response(serializer.data)


class ShowArticleStars(APIView):
    def get(self, request,slug):
        articless = Article.objects.get(slug=slug)
        rating_star_system = Rating_star_system.objects.get(star=articless)
        serializer = Show_Article_Stars_Serializer(rating_star_system)
        return Response(serializer.data)

@api_view(['POST'])
def PublishComment(request):  # use APIview or function based view or any view u want
    if request.method == 'POST':
        text = request.data["comment"]
        title = request.data["title"]
        slug = request.data["slug"]
        userID = request.data['userID']
        articless = Article.objects.get(slug=slug)

        if userID != 'null':
            users = User.objects.get(id=userID)
            username = users.username
            create_new_comment = Comments.objects.create(comment=text,title=title,user=users,article=articless)
            # get photo of the user
            user_photo = create_new_comment.user_photo()
        else:
            username = 'unknown'
            create_new_comment = Comments.objects.create(comment=text,title=title,article=articless)
            user_photo = create_new_comment.user_photo()

        content = {
            'comment': create_new_comment.comment,  # `django.contrib.auth.User` instance.
            'user_photo': str(user_photo),
            'title': create_new_comment.title,
            'username': create_new_comment.username(),
            'user_stars': create_new_comment.user_stars(),
            'datepublished': create_new_comment.datepublished(),
            'user_like_comment': create_new_comment.user_like_comment(),
            'user_dislike_comment': create_new_comment.user_dislike_comment(),
            'id': create_new_comment.id,
            'userID': create_new_comment.userID(),
            'comment_1st_part' : create_new_comment.comment_1st_part(),
            'comment_2nd_part' : create_new_comment.comment_2nd_part(),
            }

        return Response(content)

# here you are reciving values from rate_it_stars.html (book_id and num that represents value)
@api_view(['POST'])
def UpdateUserStars(request):
    # print(request.data) # <QueryDict: {'num': ['2'], 'slug': ['samsung-s22'], 'userID': ['null']}>
    # check forum 4 with coments to see explanation if u forget how code below works 
    if request.method == 'POST':
        stars = request.data['num']
        stars = int(stars)
        user = User.objects.get(id=request.data['userID'])
        article = Article.objects.get(slug=request.data['slug'])
        star_sytem = Rating_star_system.objects.get(star=article)
        user_stars = Users_stars.objects.filter(user=user,article=article)
 

    if stars == 1: 
        if not star_sytem.star_1.filter(id=user.id).exists():
            star_sytem.star_1.add(user)
            if star_sytem.star_2.filter(id=user.id).exists():
                star_sytem.star_2.remove(user)
            if star_sytem.star_3.filter(id=user.id).exists():
                star_sytem.star_3.remove(user)
            if star_sytem.star_4.filter(id=user.id).exists():
                star_sytem.star_4.remove(user)
            if star_sytem.star_5.filter(id=user.id).exists():
                star_sytem.star_5.remove(user)
        else:
            star_sytem.star_1.remove(user)
            user_stars.delete()



    elif stars == 2: 
        if not star_sytem.star_2.filter(id=user.id).exists():
            star_sytem.star_2.add(user)
            if star_sytem.star_1.filter(id=user.id).exists():
                star_sytem.star_1.remove(user)
            if star_sytem.star_3.filter(id=user.id).exists():
                star_sytem.star_3.remove(user)
            if star_sytem.star_4.filter(id=user.id).exists():
                star_sytem.star_4.remove(user)
            if star_sytem.star_5.filter(id=user.id).exists():
                star_sytem.star_5.remove(user)
        else:
            star_sytem.star_2.remove(user)
            user_stars.delete()

    elif stars == 3: 
        if not star_sytem.star_3.filter(id=user.id).exists():
            star_sytem.star_3.add(user)
            if star_sytem.star_1.filter(id=user.id).exists():
                star_sytem.star_1.remove(user)
            if star_sytem.star_2.filter(id=user.id).exists():
                star_sytem.star_2.remove(user)
            if star_sytem.star_4.filter(id=user.id).exists():
                star_sytem.star_4.remove(user)
            if star_sytem.star_5.filter(id=user.id).exists():
                star_sytem.star_5.remove(user)
        else:
            star_sytem.star_3.remove(user)
            user_stars.delete()


    elif stars == 4: 
        if not star_sytem.star_4.filter(id=user.id).exists():
            star_sytem.star_4.add(user)
            if star_sytem.star_1.filter(id=user.id).exists():
                star_sytem.star_1.remove(user)
            if star_sytem.star_2.filter(id=user.id).exists():
                star_sytem.star_2.remove(user)
            if star_sytem.star_3.filter(id=user.id).exists():
                star_sytem.star_3.remove(user)
            if star_sytem.star_5.filter(id=user.id).exists():
                star_sytem.star_5.remove(user)
        else:
            star_sytem.star_4.remove(user)
            user_stars.delete()

    elif stars == 5: 
        if not star_sytem.star_5.filter(id=user.id).exists():
            star_sytem.star_5.add(user)
            if star_sytem.star_1.filter(id=user.id).exists():
                star_sytem.star_1.remove(user)
            if star_sytem.star_2.filter(id=user.id).exists():
                star_sytem.star_2.remove(user)
            if star_sytem.star_3.filter(id=user.id).exists():
                star_sytem.star_3.remove(user)
            if star_sytem.star_4.filter(id=user.id).exists():
                star_sytem.star_4.remove(user)
        else:
            star_sytem.star_5.remove(user)
            user_stars.delete()

    try:
        grade_of_user = Users_stars.objects.get(user=user,article=article).stars
    except ObjectDoesNotExist:
        grade_of_user = 'not exists'

    content = {

    'total_stars': star_sytem.total()[1], # calculation of  avarge grade
    'star_grade': star_sytem.total()[0], # total nuber of all users 
    'user_grade': grade_of_user # 

    }

    return Response(content)

class search_book(APIView):
    def get(self, request,value):
        titles = value.split()  # ['aa', 'bb', 'cc']
        num = 0
        while len(titles) <= 8:
            add_value = titles[num]
            titles.append(add_value)
            num = num + 1 
            
        queryset = Article.objects.filter(
            Q(name__icontains=titles[0]) &
            Q(name__icontains=titles[1]) &
            Q(name__icontains=titles[2]) &
            Q(name__icontains=titles[3]) &
            Q(name__icontains=titles[4]) &
            Q(name__icontains=titles[5]) &
            Q(name__icontains=titles[6]) &
            Q(name__icontains=titles[7]) 
        )
        serializer = Article_Serializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def comment_like_dislike_system(request):
    if request.method == 'POST':
        like_dislike = request.POST.get('like_dislike')        
        user_id = request.POST.get('user_id')
        slug = request.POST.get('slug')
        comment_id = request.POST.get('comment_id')
        comment = Comments.objects.get(id=comment_id)
        user = User.objects.get(id=user_id)

        if like_dislike == 'like' and  comment.comment_likes.filter(id=user_id).exists():
            comment.comment_likes.remove(user)
            user_like = 'false'
            user_dislike = 'false'

        elif like_dislike == 'like' and not comment.comment_likes.filter(id=user_id).exists():
            comment.comment_likes.add(user)
            user_like = 'true'
            user_dislike = 'false'

            if comment.comment_dislikes.filter(id=user_id).exists():
                comment.comment_dislikes.remove(user)
                user_dislike = 'false'

        elif like_dislike == 'dislike' and comment.comment_dislikes.filter(id=user_id).exists():
            comment.comment_dislikes.remove(user)
            user_dislike = 'false'
            user_like = 'false'

        elif like_dislike == 'dislike' and not comment.comment_dislikes.filter(id=user_id).exists():
            comment.comment_dislikes.add(user)
            user_dislike = 'true'
            user_like = 'false'

            if comment.comment_likes.filter(id=user_id).exists():
                comment.comment_likes.remove(user)
                user_like = 'false'

        comment_liskes_count = comment.user_like_comment_count()
        comment_disliskes_count = comment.user_dislike_comment_count()

        content = { 'user_like_comment' : comment.comment_likes.filter(id=user_id).exists(),
                    'user_dislike_comment' : comment.comment_dislikes.filter(id=user_id).exists(),
                    'comment_id' : comment.id,
                    'user_id' : user_id,
                    'comment_disliskes_count' : comment_disliskes_count,
                    'comment_liskes_count' : comment_liskes_count
                  }
        
        return Response(content)

@api_view(['POST'])
def AddBookBasket(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')        
        user_id = request.POST.get('user_id')
        article = Article.objects.get(slug=slug)
        user = User.objects.get(id=user_id)
        b = Books_in_Basket.objects.create(user=user,basket=article)

        return Response('kkkkkkkkkkkkkkkkk')

@api_view(['POST'])
def ReturnBasket(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')

        user = User.objects.get(id=user_id)
        b = Books_in_Basket.objects.filter(user=user)

        serializer = Book_in_Basket_Serializer(b, many=True)

        return Response(serializer.data)


@api_view(['POST'])
def DeleteBookBasket(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        slug = request.POST.get('slug')
        articless = Article.objects.get(slug=slug)
        user = User.objects.get(id=user_id)
        b = Books_in_Basket.objects.filter(user=user,basket=articless)[0].delete()

        return Response('succsess')



@api_view(['POST'])
def delete_comment(request):  # use APIview or function based view or any view u want
    if request.method == 'POST':
        comment_id = request.data["comment_id"]
        slug = request.data["slug"]
        userID = request.data['user_id']
        articless = Article.objects.get(slug=slug)
        comments = Comments.objects.filter(article__slug=slug).get(id=comment_id).delete()

        return Response('succsess')

