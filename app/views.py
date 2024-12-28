from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer
from app.pagination  import InfiniteLOPagination



class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-timestamp')  # Order posts by latest timestamp
    serializer_class = PostSerializer
    pagination_class = InfiniteLOPagination

    


