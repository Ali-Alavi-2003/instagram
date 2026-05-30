from rest_framework import serializers
from posts.models.hashtag import Hashtag
from posts.models.posts import Post


class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtag
        fields = [
            "id",
            "body",
        ]