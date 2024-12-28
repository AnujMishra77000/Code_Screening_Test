from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'author_username']
     

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='user.username', read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    comments = serializers.SerializerMethodField()

    
    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'author_username', 'comment_count', 'comments']


    def get_comments(self, obj):
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data    
  
    
    
    
