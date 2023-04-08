from django.db import models

from django.contrib.auth.models import User
from travel_album.models import Diary

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Diary, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}{self.post.title}へコメント'