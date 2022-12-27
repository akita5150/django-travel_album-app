from django.urls import include, path
from travel_album.views import Diary_listView, Diary_DetailView, Album_listView, Photo_listView


urlpatterns = [
    path('', Diary_listView.as_view(), name='diary-list'),
    path('diary/<int:pk>', Diary_DetailView.as_view(), name='diary-detail'),
    path('diary/<int:diary_pk>/album', Album_listView.as_view(), name='album-list'),
    path('diary/<int:album_diary_pk>/album/<int:album_pk>/photo', Photo_listView.as_view(), name='photo-list'),
]