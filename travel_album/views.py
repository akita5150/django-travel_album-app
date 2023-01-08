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
    fields = ['prefecture', 'start_date', 'end_date', 'memo']
    
    def form_valid(self, form):
        # 変数（object）にcommit=Falseでsaveメソッドを呼び出して保存する前のデータ取得
        object = form.save(commit=False)
        # userフィールドをログインしているuser
        object.user = self.request.user
        # object保存
        object.save()
        return super().form_valid(form)
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
    fields = ['location']
    def form_valid(self, form):
        object = form.save(commit=False)
        # urlのpkからdiary抽出 ※リスト型で抽出される
        diary = Diary.objects.filter(id=self.kwargs['diary_pk'])
        object.diary = diary[0]
        # object保存
        object.save()
        return super().form_valid(form)
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



