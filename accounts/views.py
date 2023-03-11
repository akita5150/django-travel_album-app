from django.shortcuts import render
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
        
    
    
