from django.urls import include, path
from travel_album.views import Diary_listView, Diary_DetailView, Album_listView, Photo_listView, Diary_CreateView, Album_addView


urlpatterns = [
    path('', Diary_listView.as_view(), name='diary-list'),
    path('diary/<int:pk>', Diary_DetailView.as_view(), name='diary-detail'),
    path('diary/create', Diary_CreateView.as_view(), name='diary-create'),
    path('diary/<int:diary_pk>/album_add', Album_addView.as_view(), name='album-add'),
    path('diary/<int:diary_pk>/album', Album_listView.as_view(), name='album-list'),
    path('diary/<int:album_diary_pk>/album/<int:album_pk>/photo', Photo_listView.as_view(), name='photo-list'),
    path('diary/<int:album_diary_pk>/album/<int:album_pk>/photo/upload', Photo_listView.as_view(), name='photo-upload'),

]