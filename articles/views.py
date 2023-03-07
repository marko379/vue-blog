from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
# from .forms import Create_User, User_photo_form
from .models import Article, Category,Comments,Rating_star_system,Users_stars
from users.models import User_photo
from .serializers import Article_Serializer, Category_Serializer, Comments_Serializer,Show_User_Stars_Serializer,Show_Article_Stars_Serializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
import json



class LatestProductsList(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        # get all articles with your serializer 
        serializer = Article_Serializer(articles, many=True)
        # when is returned you can accsess those data in vue template
        return Response(serializer.data)


class Articlee(APIView):
    def get(self, request, slug):
        articless = Article.objects.get(slug=slug)
        # comments = Comments.objects.filter(article=articless)
        serializer = Article_Serializer(articless)
        return Response(serializer.data)


class ShowComments(APIView):
    def get(self, request, get_comments):
        articless = Article.objects.get(slug=get_comments)
        comments = Comments.objects.filter(article=articless)
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
                print('pppppppppppppppppppppppppppp')
                return Response('not rated')
            else:
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
        users = User.objects.get(id=userID)
        articless = Article.objects.get(slug=slug)
        username = users.username
        create_new_comment = Comments.objects.create(comment=text,title=title,user=users,article=articless)
        # this is method user_photo() in models articles
        user_photo = create_new_comment.user_photo()

        # data = Comments.objects.filter(id=create_new_comment.id).values()
        
        content = {
            'comment': text,  # `django.contrib.auth.User` instance.
            'user_photo': str(user_photo),
            'title': title,
            'username':username,        
            }

        return Response(content)
        # return JsonResponse(data[0])
    # else:
    #     print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# here you are reciving values from rate_it_stars.html (book_id and num that represents value)
@api_view(['POST'])
def UpdateUserStars(request):
    print(request.data) # <QueryDict: {'num': ['2'], 'slug': ['samsung-s22'], 'userID': ['null']}>
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

    content = {
    'total_stars': star_sytem.total()[1], 
    'star_grade': star_sytem.total()[0],

    }

    return Response(content)




    # return HttpResponse('succsess')
