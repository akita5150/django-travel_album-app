from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from accounts.models import User_information
from travel_album.models import Diary
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True 

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('diary-list')

class UserPage_View(DetailView):
    model = User
    template_name = 'accounts/userpage.html'
    context_object_name = 'User'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = Diary.objects.filter(user_id=self.kwargs['pk'],is_publish=True)
        login_user = User_information.objects.get(user_id=self.request.user)
        mutual_follow_user = []
        for following_user in login_user.following.all():
            for followed_user in login_user.user.followed_by.all():
                # followed_userはユーザー情報のため「.user」にする
                if following_user == followed_user.user:
                    mutual_follow_user.append(following_user)
        context['posts'] = post_list
        context['login_user'] = login_user
        context['mutual_follow_user'] = mutual_follow_user
        return context

class Following_DetailView(DetailView):
    model = User
    template_name = 'accounts/following_list.html'
    context_object_name = 'User'
    def get_context_data(self, **kwargs):
        a_u = self.request.user
        print(a_u.followed_by.all())
        context = super().get_context_data(**kwargs)
        information = User_information.objects.get(user_id=self.kwargs['pk'])
        context['information'] = information
        return context
    
class Follower_DetailView(DetailView):
    model = User
    template_name = 'accounts/follower_list.html'
    context_object_name = 'User'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.kwargs['pk'])
        follower_list = user.followed_by.all()
        context['follower_list'] = follower_list 
        return context

class Like_postView(ListView):
    model = Diary
    template_name = 'accounts/like_post.html'
    context_object_name = 'posts'
    def get_queryset(self):
        login_user_information = User_information.objects.get(user=self.request.user)
        post = login_user_information.like_post.all()
        return post
    
def Like(request,id):
    post = get_object_or_404(Diary, pk=id)
    login_user_information = User_information.objects.get(user=request.user)
    login_user_information.like_post.add(post)
    login_user_information.save()
    return redirect('post-detail', post.id)

def Like_remove(request,id):
    post =get_object_or_404(Diary, pk=id)
    login_user_information = User_information.objects.get(user=request.user)
    login_user_information.like_post.remove(post)
    login_user_information.save()
    return redirect('post-detail', post.id)
    

def Follow(request,id):
    login_user = request.user
    user = get_object_or_404(User, pk=id)
    login_user_information = User_information.objects.get(user=request.user)   
    # 表示しているユーザーをフォロー
    login_user_information.following.add(user)
    login_user_information.save()
    return redirect('userpage', user.id)

def Follow_remove(request,id):
    user = get_object_or_404(User, pk=id)
    login_user_information = User_information.objects.get(user=request.user)
    login_user_information.following.remove(user)
    login_user_information.save()
    return redirect('userpage', user.id)

class Search_userListView(ListView):
    model = User
    template_name = "accounts/search_user.html"
    context_object_name = "user_list"

    def get_queryset(self):
        self.query = self.request.GET.get('query') or ""
        queryset = super().get_queryset()

        if self.query:
            queryset = queryset.filter(
               Q(username__icontains=self.query) 
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query
        return context