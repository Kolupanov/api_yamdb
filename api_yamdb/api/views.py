from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework import filters

from reviews.models import Title, Review, Comment

from .serializers import ReviewSerializer, CommentSerializer
# from .serializers import FollowSerializer
from .permissions import IsOwnerOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsOwnerOrReadOnly, )

    @property
    def current_title(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, pk=title_id)

    def get_queryset(self):
        return self.current_title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.current_title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsOwnerOrReadOnly, )

    @property
    def current_review(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Title, pk=title_id)
        return get_object_or_404(Review, pk=review_id, title=title)

    def get_queryset(self):
        return self.current_review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.current_review)
