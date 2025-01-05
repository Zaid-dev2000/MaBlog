from django.urls import path
from .views import BlogPostListCreateAPIView, home

urlpatterns = [
    path('posts/', BlogPostListCreateAPIView.as_view(), name='blogpost-list-create'),
    path('', home, name='home'),
]
