from rest_framework.generics import ListAPIView
from rest_framework import serializers
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerilizer,UserSerializer,UserViewSerializer,User_photoSerilizer
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import User_photo,MyUserModel,Exe
from .forms import Create_User, User_photo_form
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session
from PIL import Image
from io import BytesIO
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from rest_framework import status



@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerilizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return redirect ('https://vue-blog-production.up.railway.app/articles/')


@api_view(['POST'])
def register_api_2(request):
    if request.method == 'POST':
        form = Create_User(request.POST)
        if form.is_valid():
            form.save()
            token = Token.objects.create(user=form.instance)
            username = form.instance.username
            if request.FILES:
                user_photo_form = User_photo_form(request.POST,request.FILES)
                if user_photo_form.is_valid():
                    photo_user = user_photo_form.save(commit=False)

                    if request.FILES['image']:
                        photo_user.user_img = request.FILES['image']
                    filepath = request.FILES.get('filepath', False)
                    photo_user.user = form.instance # aditonal added
                    photo_user.save() # aditonal added
            else:
                default_user_img = ''   # this is the **public_id**
                default_avatar = '123456789'

                user_photo = User_photo.objects.create(
                    user=form.instance,
                    user_img=default_user_img,
                    avatar_photo=default_avatar
                ) # 
                              
            return Response({'success': 'user created' , 'name_of_user': username})
        else:
            return HttpResponse(form.errors.as_json())


@api_view(['POST'])
def login_api(request):
    username = request.data["username"].strip()
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        user_id = Token.objects.get(user__id=user.id)
        login(request, user)
        # user_photo = User_photo.objects.get(user__id=user.id).image_avatar_path()
        user_photo = User_photo.objects.get(user__id=user.id).image_path()



        content = {
            'user': str(user.username),
            'user_id': str(user_id),
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
        content = {
            'user': serializer.data,  # `django.contrib.auth.User` instance.
            'user_photo':serializer_user_photo.data,  # None
        }
        return Response(content)

# @api_view(['POST'])
# def delete_user(request):
#     if request.method == 'POST':
#         user_id = request.data["userID"]
#         user_photo = User_photo.objects.get(user__id=user_id).delete()
#         user = User.objects.get(id=user_id).delete()
#         return Response('succsess')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    try:
        request.user.delete()
        return Response({
        'status': 'ok',
        'message': 'Your account has been deleted'
        }, status = status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"status": "error", "message": "Deletion failed. Please try again!"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )





@api_view(['POST'])
def ExeView(request):  # use APIview or function based view or any view u want
    # for single file
    if request.method == 'POST':
        file1 = request.FILES["image"]
        text = request.data["text"]
        xxx = Exe.objects.create(text=text,img=file1)
        xxx.save()
        return Response('UserNone')
    else:
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')



class NewView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

# DJANGO ALWAYS CHECK IF USER IS LOGGED IN OR NOT, ON EVERY REQUEST, DOSE NOT MATTER IF FUNCTION 
# HAS ANYTHING TO DO USERS OR NOT, IF U PASS TOKEN OR USER_ID OR USERNAME U CAN ACCSES USER,
# BEST PRACTICE IS WITH TOKEN , HOW IT WORKS? ONCE USER CREATE PROFILE TOKEN IS ASSINGED TO USER, 
# THAT TOKEN U NEED TO STORE IN COOKIES OR LOCAL STORAGE, SO U NEED TO USE ONE OF THOSE 3(cokkies or 
# local storage or seesion storage, ), 
# when cookies are stored in broswer, if u interact  let say with facebook
# every time u do different HTTP requests on facebpook, all cookies will be included in those requests
# so tahts how u can accses request user if user is logged in, every time u do something on page ,
# cookies will be sent 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_photo(request):
    if 'image' not in request.FILES:
        return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

    uploaded_file = request.FILES['image']

    # if file is bigger then 5 mb
    if uploaded_file.size > 5 * 1024 * 1024: 
        return Response({"error": "Image too large (max 5MB)"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_photo = User_photo.objects.get(user=request.user)
        user_photo.user_img = uploaded_file
        user_photo.save()

        return Response({
            "message": "Photo updated successfully",
            "photo_url": user_photo.image_path()
        }, status=status.HTTP_200_OK)

    except User_photo.DoesNotExist:
        return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)




