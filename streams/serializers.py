from rest_framework import serializers
from models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_id', 'link_or_text', 'title', 'body', 'linkout', 'num_of_replies')


