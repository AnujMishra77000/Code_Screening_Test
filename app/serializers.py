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
  
### Follow-up Q: 
#- Instead of sorting comments by timestamp, how would you fetch 3 random comments associated to a given post? 
    """ to fetch 3 random comments we can  use random.sample the method is first retrive all 
    comments form all post and the randomly select 3 from them.
    
    def get_comments(self, obj):
    comments = obj.comments.all()
    comments_list = list(comments)
    
    random_comments = random.sample(comments_list, min(3, len(comments_list)))
    return CommentSerializer(random_comments, many=True).data

    """
    

    
