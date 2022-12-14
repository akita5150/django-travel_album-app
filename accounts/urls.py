from django.urls import include, path
from django.contrib.auth.views import LogoutView
from accounts.views import MyLoginView, SignUpView


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]