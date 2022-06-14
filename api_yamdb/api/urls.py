from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ReviewViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='title-reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewSet,
                basename='review-comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
