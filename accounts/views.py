from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from accounts.models import User_information
from travel_album.models import Diary
from django.contrib.auth.models import User

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
        # user_information = User_information.objects.get(user_id=self.kwargs['pk'])
        login_user_information = User_information.objects.get(user_id=self.request.user)
        context['posts'] = post_list
        # context['user_information'] = user_information
        context['login_user_information'] = login_user_information
        return context

class Following_DetailView(DetailView):
    model = User
    template_name = 'accounts/following_list.html'
    context_object_name = 'User'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        information = User_information.objects.get(user_id=self.kwargs['pk'])
        context['information'] = information
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

