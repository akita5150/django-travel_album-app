from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from travel_album.models import Diary, Album, Photo, Prefectures
from travel_album.forms import AlbumAddForms, PhotoAddForms
from django import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
class Diary_listView(LoginRequiredMixin,ListView):
    model = Diary
    template_name = 'travel_album/diary_list.html'
    context_object_name = 'diaries'
    def get_queryset(self):
        diary = Diary.objects.filter(user=self.request.user)
        return diary

class Diary_DeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    template_name = 'travel_album/diary_delete.html'
    success_url = reverse_lazy('diary-list')

class Diary_DetailView(DetailView):
    model = Diary
    template_name = 'travel_album/diary_detail.html'
    context_object_name = 'diary'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album_list = Album.objects.filter(diary_id=self.kwargs['pk'])
        context['album_list'] = album_list
        context['album_add'] = AlbumAddForms
        return context

class Album_addView(CreateView):
    model = Album
    form_class = AlbumAddForms
    def form_valid(self, form):
        # saveしない
        album = form.save(commit=False)
        # diaryが実在するか確認
        diary_pk = self.kwargs['diary_pk']
        diary = get_object_or_404(Diary, pk=diary_pk)
        album.diary = diary
        album.save()
        return redirect('diary-detail', pk=diary_pk)

class Diary_CreateView(CreateView):
    model = Diary
    template_name = 'travel_album/diary_create.html'
    fields = ['title','prefecture', 'start_date', 'end_date', 'memo']
    
    def form_valid(self, form):
        # 変数（object）にcommit=False保存しないでデータ取得
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

class Diary_UpdateView(UpdateView):
    model = Diary
    template_name = 'travel_album/diary_edit.html'
    fields = ['title','prefecture', 'start_date', 'end_date', 'memo']
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



# class Album_CreateView(CreateView):
#     model = Album
#     template_name = 'travel_album/album_create.html'
#     fields = ['location']
#     def form_valid(self, form):
#         object = form.save(commit=False)
#         # urlのpkからdiary抽出 ※リスト型で抽出される
#         diary = Diary.objects.filter(id=self.kwargs['diary_pk'])
#         object.diary = diary[0]
#         # object保存
#         object.save()
#         return super().form_valid(form)
#     success_url = reverse_lazy('diary-list')

class Album_DeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'travel_album/album_delete.html'
    context_object_name = 'album'
    def get_success_url(self):
        return reverse('diary-detail', kwargs={'pk':self.object.diary.pk})

class Photo_listView(ListView):
    model = Photo
    template_name = 'travel_album/photo_list.html'
    context_object_name = 'Photos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Photo_list = Photo.objects.filter(album_id=self.kwargs['album_pk'])
        context["Photos"] = Photo_list
        return context

class Album_DetailView(DetailView):
    model = Album
    template_name = 'travel_album/photo_list.html'
    context_object_name = 'Album'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_list = Photo.objects.filter(album_id=self.kwargs['pk'])
        context['photo_list'] = photo_list
        context['photo_add'] = PhotoAddForms
        return context

class Photo_addView(CreateView):
    model = Photo
    form_class = PhotoAddForms
    def form_valid(self, form):
        # saveしない
        photo = form.save(commit=False)
        # diaryが実在するか確認
        album_pk = self.kwargs['album_pk']
        album = get_object_or_404(Album, pk=album_pk)
        photo.album = album
        photo.save()
        return redirect('diary-detail', pk=album_pk)

class Photo_DeleteView(DeleteView):
    model = Photo
    template_name = "travel_album/photo_delete.html"
    context_object_name = "Photo"
    def get_success_url(self):
        return reverse('photo-list', kwargs={'diary_pk':self.object.album.diary.pk,'pk':self.object.album.pk})
