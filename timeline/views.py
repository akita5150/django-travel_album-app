from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from timeline.models import Comment
from timeline.forms import CommentForms
from travel_album.models import Diary, Album, Photo
from accounts.models import User_information
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
class PostListView(ListView):
    model = Diary
    template_name = 'timeline/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        login_user = User_information.objects.get(user=self.request.user)
        # login＿user.followingとlogin_user.user.followed_by(逆抽出)をforループさせてリストにidを格納
        mutual_follow_user_id = []
        for following_user in login_user.following.all():
            for followed_user in login_user.user.followed_by.all():
                # followed_userはユーザー情報のため「.user」にする
                if following_user == followed_user.user:
                    mutual_follow_user_id.append(following_user.id)
        # user_id__inで複数のuser_idの数値を取得できる
        post = Diary.objects.filter(is_publish=True, user_id__in=mutual_follow_user_id)
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
        login_user_information = User_information.objects.get(user=self.request.user)
        comment_list = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['album_list'] = album_list
        context['photo_list'] = photo_list
        context['login_user_information'] = login_user_information
        context['comment_form'] = CommentForms
        context['comment_list'] = comment_list
        return context
    
class Comment_CreateView(CreateView):
    model = Comment
    form_class = CommentForms
    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['diary_pk']
        post = get_object_or_404(Diary, pk=post_pk, is_publish=True)
        user = self.request.user
        comment.post = post
        comment.user = user
        comment.save()
        return redirect('post-detail', pk=post_pk)