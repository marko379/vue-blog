from django.contrib.auth.models import User
from rest_framework import serializers , validators
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render,redirect
from .models import User_photo,MyUserModel



class RegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )

        extra_kwargs = {
            "password": {"write_only": True},
            "email":{
                "required": False,
                # "allow_blank": False,

            }
        }

    def create(self,validated_data):
        # print(validated_data,'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
        password = validated_data.get('password')
        # print(self.Meta.model) # returns user class
        instance = self.Meta.model(**validated_data)
        if password and instance:
            instance.set_password(password)
            instance.save()
            # print(instance.user_photo.user.username,'0000000000000000000000000000')
        return redirect ('http://localhost:8080/')


class User_photoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User_photo
        fields = (
            "user_img",
            'image_path'
        )


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = (
            "user_profile_photo",
            "user_profile_username",
            "user_profile_email"
        )
