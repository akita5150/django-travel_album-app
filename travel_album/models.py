from datetime import date
from random import choices
from secrets import choice
from sre_parse import Verbose
from tabnanny import verbose
from turtle import title
from django.db import models
from config.settings import PREFECTURES

from django.contrib.auth.models import User

# Create your models here.
class Prefectures(models.Model):
    prefecture = models.CharField(verbose_name='都道府県名', choices=PREFECTURES, max_length=4)

class Diary(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    prefecture = models.CharField(verbose_name='都道府県名', choices=PREFECTURES, max_length=4)
    start_date = models.DateField(verbose_name='旅行開始日', null=True, blank=True)
    end_date = models.DateField(verbose_name='終了日', null=True, blank=True)
    memo = models.TextField(verbose_name='メモ', max_length=10000, null=True, blank=True)
    
    def __str__(self):
        return self.prefecture

class Album(models.Model):
    diary = models.ForeignKey(Diary, verbose_name='旅行県', on_delete=models.CASCADE)
    location = models.CharField(verbose_name='場所', max_length=50)

    def __str__(self):
        return f'{self.diary} {self.location}'

class Photo(models.Model):
    album = models.ForeignKey(Album, verbose_name='場所', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='写真', upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f'{self.album}の写真'
