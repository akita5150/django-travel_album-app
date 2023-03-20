from django.db import models

from django.contrib.auth.models import User
from travel_album.models import Diary
# Create your models here.
class User_information(models.Model):
    user = models.OneToOneField(User, verbose_name='ユーザー', blank=True, null=True, on_delete=models.CASCADE, related_name='user_information')
    following = models.ManyToManyField(User, verbose_name='フォロー中', blank=True, related_name='following_user')
    like_post = models.ManyToManyField(Diary, verbose_name='いいねした投稿', blank=True, related_name='liked_post')

    def __str__(self):
        return f'{self.user.username}の情報'