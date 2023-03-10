from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from accounts.models import User_information
from django.contrib.auth.models import User

# Create your views here.
class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True 

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('diary-list')

class Following_DetailView(DetailView):
    model = User
    template_name = 'accounts/following_list.html'
    context_object_name = 'User'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        information = User_information.objects.get(user_id=self.kwargs['pk'])
        context['information'] = information
        return context
        
    
    
