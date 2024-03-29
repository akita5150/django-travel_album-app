from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from travel_album.models import Diary, Album, Photo
from travel_album.forms import AlbumAddForms, PhotoAddForms, ReplyForms
from accounts.models import User_information
from timeline.models import Reply, Comment
from django import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
class Diary_listView(LoginRequiredMixin,ListView):
    model = Diary
    template_name = 'travel_album/diary_list.html'
    context_object_name = 'diaries'
    paginate_by = 3

    def get_queryset(self):
        diary = Diary.objects.filter(user=self.request.user).order_by('-start_date')
        return diary

class Diary_DeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    template_name = 'travel_album/diary_delete.html'
    success_url = reverse_lazy('diary-list')

class Diary_DetailView(LoginRequiredMixin, DetailView):
    model = Diary
    template_name = 'travel_album/diary_detail.html'
    context_object_name = 'diary'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_diary = Diary.objects.get(id=self.kwargs['pk'])
        album_list = Album.objects.filter(diary_id=this_diary.pk)
        liked_by_user = this_diary.liked_by.all()
        photo_list = []
        for album_name in album_list:
            photo = Photo.objects.filter(album=album_name)
            photo_list.append(photo)
        comment_list = Comment.objects.filter(post_id=self.kwargs['pk'])
        reply_list = Reply.objects.filter(comment__in=comment_list)
        context['album_list'] = album_list
        context['liked_by_user'] = liked_by_user
        context['album_add'] = AlbumAddForms
        context['photo_list'] = photo_list
        context['comment_list'] = comment_list
        context['reply_list'] = reply_list
        return context

class liked_by_user_DetailView(LoginRequiredMixin, DeleteView):
    model = Diary
    template_name = 'travel_album/liked_by_user_list.html'
    context_object_name = 'diary'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_diary = Diary.objects.get(id=self.kwargs['pk'])
        liked_by_user = this_diary.liked_by.all()
        context['liked_by_users'] = liked_by_user
        return context

class Album_addView(LoginRequiredMixin, CreateView):
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

class Diary_CreateView(LoginRequiredMixin, CreateView):
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

class Diary_UpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    template_name = 'travel_album/diary_edit.html'
    fields = ['title','prefecture', 'start_date', 'end_date', 'memo']
    success_url = reverse_lazy('diary-list')
    def get_success_url(self):
        # 新規データのID取得
        id = self.object.id
        return reverse("diary-detail", kwargs={"pk": id})

    
class Album_listView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'travel_album/album_list.html'
    context_object_name = 'Albums'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Album_list = Album.objects.filter(diary_id=self.kwargs['diary_pk']) 
        context["Albums"] = Album_list
        return context

class Album_DeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'travel_album/album_delete.html'
    context_object_name = 'album'
    def get_success_url(self):
        return reverse('diary-detail', kwargs={'pk':self.object.diary.pk})

# class Photo_listView(ListView):
#     model = Photo
#     template_name = 'travel_album/photo_list.html'
#     context_object_name = 'Photos'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         Photo_list = Photo.objects.filter(album_id=self.kwargs['album_pk'])
#         context["Photos"] = Photo_list
#         return context

class Album_DetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'travel_album/photo_list.html'
    context_object_name = 'Album'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_list = Photo.objects.filter(album_id=self.kwargs['pk'])
        context['photo_list'] = photo_list
        context['photo_add'] = PhotoAddForms
        return context

class Photo_addView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoAddForms
    def form_valid(self, form):
        # saveしない
        photo = form.save(commit=False)
        album_pk = self.kwargs['album_pk']
        album = get_object_or_404(Album, pk=album_pk)
        photo.album = album
        photo.save()
        diary_pk = album.diary.pk
        return redirect('diary-detail', pk=diary_pk)

class Photo_DeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = "travel_album/photo_delete.html"
    context_object_name = "Photo"
    def get_success_url(self):
        return reverse('photo-list', kwargs={'diary_pk':self.object.album.diary.pk,'pk':self.object.album.pk})
    
class Reply_CreateView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForms
    template_name = "travel_album/reply_create.html"
    def form_valid(self, form):
        reply = form.save(commit=False)
        comment_pk = self.kwargs['comment_pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = self.request.user
        reply.comment = comment
        reply.user = user
        reply.save()
        comment_post_pk = comment.post.pk
        return redirect('diary-detail', comment_post_pk)

