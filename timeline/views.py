from django.shortcuts import render
from django.views.generic import ListView, DetailView
from travel_album.models import Diary, Album, Photo
from accounts.models import User_information

# Create your views here.
class PostListView(ListView):
    model = Diary
    template_name = 'timeline/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        login_user = User_information.objects.get(user=self.request.user)
        # login＿user.followingをforループさせてリストにidを格納
        following_user_id = []
        for following_user in login_user.following.all():
            following_user_id.append(following_user.id)
        # user_id__inで複数のuser_idの数値を取得できる
        post = Diary.objects.filter(is_publish=True, user_id__in=following_user_id)
        return post

class PostDetailView(DetailView):
    model = Diary
    template_name = 'timeline/post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album_list = Album.objects.filter(diary_id=self.kwargs['pk'])
        # album＿list内をforループさせて、photo＿listに格納
        photo_list = []
        for album_name in album_list:
            photo = Photo.objects.filter(album=album_name)
            photo_list.append(photo)
        context['album_list'] = album_list
        context['photo_list'] = photo_list
        return context