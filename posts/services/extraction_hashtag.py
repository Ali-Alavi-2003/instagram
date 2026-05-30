import re

from posts.models.posts import Post
from posts.models.hashtag import Hashtag


class ExtractionHashtag:
    def extract(value: Post):
        hashtags = re.findall(r"#(\w+)", value.caption.lower())
        hashtag_objects = []
        for tag in hashtags:
            hashtag, create = Hashtag.objects.get_or_create(
            body = tag,
            )
            hashtag_objects.append(hashtag)
        value.hashtags.set(hashtag_objects)