from django.shortcuts import render
from django.views.generic import ListView, DetailView
from travel_album.models import Diary, Album, Photo, Prefectures


# Create your views here.
class Diary_listView(ListView):
    model = Diary
    template_name = 'travel_album/diary_list.html'
    context_object_name = 'diaries'


class Diary_DetailView(DetailView):
    model = Diary
    template_name = 'travel_album/diary_detail.html'
    context_object_name = 'diary'

class Album_listView(ListView):
    model = Album
    template_name = 'travel_album/album_list.html'
    context_object_name = 'Albums'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Album_list = Album.objects.filter(diary_id=self.kwargs['diary_pk']) 
        context["Albums"] = Album_list
        return context
        

class Photo_listView(ListView):
    model = Photo
    template_name = 'travel_album/Photo_list.html'
    context_object_name = 'Photos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Photo_list = Photo.objects.filter(album_id=self.kwargs['album_pk'])
        context["Photos"] = Photo_list
        return context



