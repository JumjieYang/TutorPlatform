import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def validate_content(content):
    if content is None or content == "":
        raise ValidationError(
            'Content cannot be null',
            code='invalid',
            params={
                'content': content
            }
        )


class Message(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, blank=False, null=False,
                               related_name='author_messages', on_delete=models.CASCADE, to_field='username')
    content = models.TextField(validators=[validate_content])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    room = models.CharField(max_length=100,null=False)
