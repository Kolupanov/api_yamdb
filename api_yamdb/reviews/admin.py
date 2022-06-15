from django.contrib import admin

from .models import Title, Review, Comment, User


admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(User)
