from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from travel_album.models import Diary, Album, Photo, Prefectures
from django.urls import reverse_lazy, reverse


# Create your views here.
class Diary_listView(ListView):
    model = Diary
    template_name = 'travel_album/diary_list.html'
    context_object_name = 'diaries'


class Diary_DetailView(DetailView):
    model = Diary
    template_name = 'travel_album/diary_detail.html'
    context_object_name = 'diary'

class Diary_CreateView(CreateView):
    model = Diary
    template_name = 'travel_album/diary_create.html'
    fields = ['user','prefecture', 'start_date', 'end_date', 'memo']
    # user情報の初期値設定
    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user   
        return initial
    success_url = reverse_lazy('diary-list')
    def get_success_url(self):
        # 新規データのID取得
        id = self.object.id
        return reverse("diary-detail", kwargs={"pk": id})
    

class Album_listView(ListView):
    model = Album
    template_name = 'travel_album/album_list.html'
    context_object_name = 'Albums'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Album_list = Album.objects.filter(diary_id=self.kwargs['diary_pk']) 
        context["Albums"] = Album_list
        return context

class Album_CreateView(CreateView):
    model = Album
    template_name = 'travel_album/album_create.html'
    fields = ['diary', 'location']
    def get_initial(self, **kwargs):
        initial = super().get_initial()
        Album_list = Diary.objects.filter(id=self.kwargs['diary_pk'])
        initial['diary'] = Album_list[0]
        return initial
    success_url = reverse_lazy('diary-list')

class Photo_listView(ListView):
    model = Photo
    template_name = 'travel_album/Photo_list.html'
    context_object_name = 'Photos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Photo_list = Photo.objects.filter(album_id=self.kwargs['album_pk'])
        context["Photos"] = Photo_list
        return context



