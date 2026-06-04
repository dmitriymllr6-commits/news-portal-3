from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'summary',
            'content',
            'author',
            'author_name',
            'date_created'
        ]
        read_only_fields = ['author', 'date_created']