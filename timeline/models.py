from django.db import models

from django.contrib.auth.models import User
from travel_album.models import Diary

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')
    post = models.ForeignKey(Diary, on_delete=models.CASCADE, verbose_name='投稿')
    text = models.TextField(verbose_name='本文', max_length=50)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}{self.post.title}へコメント「{self.text}」'
    
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='コメント')
    text = models.TextField(verbose_name='本文', max_length=50)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}{self.comment}へ返信'