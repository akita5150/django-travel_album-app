from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class User_information(models.Model):
    user = models.OneToOneField(User, verbose_name='ユーザー', blank=True, null=True, on_delete=models.CASCADE, related_name='user_information')
    following = models.ManyToManyField(User, verbose_name='フォロー中', blank=True, related_name='following_user')

    def __str__(self):
        return f'{self.user.username}の情報'