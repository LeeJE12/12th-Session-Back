from rest_framework import serializers
from blog.models import Post, LANGUAGE_CHOICES

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'date', 'body', 'language']

    '''
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False, allow_blank = True, max_length = 200)
    date = serializers.DateTimeField('date published')
    body = models.TextField()
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default = 1)
    '''
