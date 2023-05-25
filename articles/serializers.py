from rest_framework import serializers

from .models import Category, Article, Comments,Users_stars , Rating_star_system,Books_in_Basket


# this willl be returned in views as """"return Response(serializer.data)""""
class Article_Serializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "date_added",
            "description",
            "image",
            'slug',
            'tracks',
            'description_1st_part',
            'description_2nd_part',
            'price',
            'num_of_comments',
            'category',
            'categories',
            # "get_absolute_url",
            "image_path",
            # "get_thumbnail"
        )

class Book_in_Basket_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Books_in_Basket
        fields = (
            "id",
            "basket",
            "slug",
            "book",
            "user",
            "book_price",
            "image_path"
        )

class Show_User_Stars_Serializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Users_stars
        fields = (
            'user',
            'stars',
            'article'
        )

class Show_Article_Stars_Serializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Rating_star_system
        fields = (
            'star',
            'total',
            'each_star_procentage'
        )


class  Comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            "id",
            "comment",
            "userID",
            "comment_1st_part",
            "comment_2nd_part",
            "user_like_comment_count",
            "user_dislike_comment_count",
            "user_like_comment",
            "user_dislike_comment",
            "id",
            "date_added",
            "title",
            "user",
            "username",
            "user_photo",
            "datepublished",
            "user_stars"
        )

class Category_Serializer(serializers.ModelSerializer):
    articles = Article_Serializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            # "get_absolute_url",
            # "products",
        )