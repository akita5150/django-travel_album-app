from django.shortcuts import render
from django.views.generic import ListView, DetailView
from travel_album.models import Diary, Album, Photo

# Create your views here.
class PostListView(ListView):
    model = Diary
    template_name = 'timeline/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        post = Diary.objects.filter(is_publish=True)
        return post

class PostDetailView(DetailView):
    model = Diary
    template_name = 'timeline/post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album_list = Album.objects.filter(diary_id=self.kwargs['pk'])
        photo_list = []
        for album_name in album_list:
            photo = Photo.objects.filter(album=album_name)
            photo_list.append(photo)
        context['album_list'] = album_list
        context['photo_list'] = photo_list
        print(context['photo_list'])
        return context