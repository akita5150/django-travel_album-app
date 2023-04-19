from django.urls import include, path
from travel_album.views import Diary_listView, Diary_DetailView, liked_by_user_DetailView, Diary_DeleteView, Album_listView, Photo_listView, Album_DetailView, Diary_CreateView, Diary_UpdateView, Album_addView, Album_DeleteView, Photo_addView, Photo_DeleteView, Reply_CreateView


urlpatterns = [
    path('', Diary_listView.as_view(), name='diary-list'),
    path('diary/<int:pk>', Diary_DetailView.as_view(), name='diary-detail'),
    path('diary/<int:pk>/liked_by', liked_by_user_DetailView.as_view(), name='liked-by'),
    path('diary/create', Diary_CreateView.as_view(), name='diary-create'),
    path('diary/<int:pk>/delete', Diary_DeleteView.as_view(), name='diary-delete'),
    path('diary/<int:pk>/edit', Diary_UpdateView.as_view(), name='diary-edit'),
    path('diary/<int:diary_pk>/album_add', Album_addView.as_view(), name='album-add'),
    path('diary/<int:diary_pk>/album', Album_listView.as_view(), name='album-list'),
    path('diary/<int:diary_pk>/album/<int:pk>/delete', Album_DeleteView.as_view(), name='album-delete'),
    path('diary/<int:diary_pk>/album/<int:pk>/photo', Album_DetailView.as_view(), name='photo-list'),
    path('diary/<int:album_diary_pk>/album/<int:album_pk>/photo_add', Photo_addView.as_view(), name='photo-add'),
    path('diary/<int:album_diary_pk>/album/<int:album_pk>/photo/<int:pk>/photo_delete', Photo_DeleteView.as_view(), name='photo-delete'),
    path('diary/<int:comment_post_pk>/<int:comment_pk>/reply', Reply_CreateView.as_view(), name='reply-create'),
]