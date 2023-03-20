from django.urls import include, path
from django.contrib.auth.views import LogoutView
from accounts.views import MyLoginView, SignUpView, Following_DetailView, UserPage_View, Like_postView, Follow, UnFollow


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/userpage/', UserPage_View.as_view(), name='userpage'),
    path('<int:pk>/following/', Following_DetailView.as_view(), name='following-list'),
    path('<int:pk>/like_post/', Like_postView.as_view(), name='like-post'),
    path('<int:id>/follow/', Follow, name='follow'),
    path('<int:id>/un_follow/', UnFollow, name='un_follow'),
]