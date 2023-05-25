from django.contrib import admin

from .models import Article , Comments,Category, Rating_star_system,Users_stars,Books_in_Basket


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Rating_star_system)
admin.site.register(Users_stars)
admin.site.register(Books_in_Basket)



