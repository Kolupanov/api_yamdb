from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (CategoryViewSet,
                    CommentViewSet,
                    GenreViewSet,
                    ReviewViewSet,
                    TitleViewSet,
                    UserViewSet, get_jwt_token,
                    signup)


router = DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='title-reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='review-comments'
),
router.register('users', UserViewSet)

urls_auth = [
    path('users/', signup, name='signup'),
    path('signup/', signup, name='signup'),
    path('token/', get_jwt_token, name='token'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(urls_auth)),
]
