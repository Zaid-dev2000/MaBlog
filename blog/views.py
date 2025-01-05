from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogPost, Category, Comment
from .serializers import BlogPostSerializer, CategorySerializer, CommentSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


# Pagination Setup
class BlogPostPagination(PageNumberPagination):
    page_size = 10


# BlogPost Views
class BlogPostListCreateView(generics.ListCreateAPIView):
    """
    View to list all blog posts or create a new post.
    """
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = BlogPostPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['category', 'author']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific blog post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("You can only edit your own posts.")
        serializer.save()


# Category Views
class CategoryListView(generics.ListAPIView):
    """
    View to list all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class PostsByCategoryView(generics.ListAPIView):
    """
    View to list posts by category.
    """
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return BlogPost.objects.filter(category__id=category_id, status='published')


# Comment Views
class CommentListCreateView(generics.ListCreateAPIView):
    """
    View to list or create comments for a blog post.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs.get('post_id'))


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("You can only edit your own comments.")
        serializer.save()

class RegisterView(APIView):
    """
    View to register a new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if not username or not email or not password:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if password != confirm_password:
            return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'message': 'User registered successfully.', 'token': token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    View to log in a user and generate an authentication token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login successful.', 'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    View to log out a user by deleting their authentication token.
    """
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except AttributeError:
            return Response({'error': 'You are not logged in.'}, status=status.HTTP_400_BAD_REQUEST)