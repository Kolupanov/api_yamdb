from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (CategoryViewSet,
                    CommentViewSet,
                    GenreViewSet,
                    ReviewViewSet,
                    TitleViewSet,
                    UserViewSet, get_jwt_token,
                    register, send_email)


router = DefaultRouter()
router.register('titles', TitleViewSet)
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='title-reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet,
                basename='review-comments')
router.register(r'users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/users/', register, name='register'),
    path('v1/auth/signup/', send_email, name='send_email'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
