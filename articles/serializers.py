from rest_framework import serializers

from .models import Category, Article, Comments,Users_stars , Rating_star_system,Books_in_Basket


# this willl be returned in views as """"return Response(serializer.data)""""
class ArticleSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)
    image_path = serializers.SerializerMethodField()  # new
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
            "image_path",
            "writer"
        )
    
    def get_image_path(self, obj): # new
        return obj.image_path()

class BookInBasketSerializer(serializers.ModelSerializer):
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

class UserStarsSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Users_stars
        fields = (
            'user',
            'stars',
            'article'
        )

class ShowArticleStarsSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Rating_star_system
        fields = (
            'star',
            'total',
            'each_star_procentage'
        )


class  CommentsSerializer(serializers.ModelSerializer):
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

class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            # "get_absolute_url",
            # "products",
        )