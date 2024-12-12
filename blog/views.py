from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import BlogPostSerializer

# Class-Based View for Blog Posts
class BlogPostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get(self, request):
        # Retrieve all blog posts
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Add a new blog post
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Function-Based View for a Secure Endpoint
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Restrict access to authenticated users
def secure_endpoint(request):
    return Response({"message": "This is a secure endpoint!"})
