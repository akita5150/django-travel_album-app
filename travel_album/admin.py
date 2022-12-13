from django.contrib import admin
from travel_album.models import Prefectures, Diary, Album, Photo
# Register your models here.
admin.site.register(Prefectures)
admin.site.register(Diary)
admin.site.register(Album)
admin.site.register(Photo)
