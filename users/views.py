from rest_framework.generics import ListAPIView
from rest_framework import serializers
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerilizer,UserSerializer,UserViewSerializer,User_photoSerilizer
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import User_photo,MyUserModel,Exe
from .forms import Create_User, User_photo_form
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# from articles.models import Users_stars



@api_view(['POST'])
def register_api(request):
    # print(request.data,'sssssssssssssssssssssssssssssss')
    serializer = RegisterSerilizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    print(user)
    return redirect ('http://127.0.0.1:8000/articles/')





@api_view(['POST'])
def register_api_2(request):
    if request.method == 'POST':
        form = Create_User(request.POST)
        if form.is_valid():
            form.save()
        if request.FILES:
            user_photo_form = User_photo_form(request.POST,request.FILES)
            if user_photo_form.is_valid():
                photo_user = user_photo_form.save(commit=False)
                photo_user.user = form.instance
                photo_user.user_img = request.FILES['image']
                photo_user.avatar_photo = request.FILES['avatar']
                photo_user.save()
            token = Token.objects.create(user=form.instance)
            return HttpResponse('succsess')
        else:
            return HttpResponse(form.errors.as_json())


@api_view(['POST'])
def login_api(request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        user_id = Token.objects.get(user__id=user.id)
        login(request, user)
        user_photo = User_photo.objects.get(user__id=user.id).image_path()

        content = {
            'user': str(user.username),  # `django.contrib.auth.User` instance.
            'user_id': str(user_id),  # None
            # i will return photo to my login page so i can accsess that photo anywhere in my app
            'photo': str(user_photo),
            'userID': str(user.id)
        }
        return Response(content)
    else:
        return HttpResponse('UserNone')



# @api_view(['GET'])
class UserView(APIView):
    permission_classes = (IsAuthenticated,)   
    def get(self, request):
        user_id = Token.objects.get(key=request.auth).user.id
        get_user = User.objects.get(id=user_id)
        get_user_photo = User_photo.objects.get(user__id=user_id)
        serializer = UserViewSerializer(get_user)
        serializer_user_photo = User_photoSerilizer(get_user_photo)
        print(serializer,serializer_user_photo,serializer_user_photo)
        content = {
            'user': serializer.data,  # `django.contrib.auth.User` instance.
            'user_photo':serializer_user_photo.data,  # None
        }
        # return Response(serializer.data)
        return Response(content)


@api_view(['POST'])
def ExeView(request):  # use APIview or function based view or any view u want
    # for single file
    if request.method == 'POST':
        file1 = request.FILES["image"]
        text = request.data["text"]
        xxx = Exe.objects.create(text=text,img=file1)
        xxx.save()
        return HttpResponse('UserNone')
    else:
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')



class NewView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

