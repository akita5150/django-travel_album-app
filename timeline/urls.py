from django.urls import include, path
from timeline.views import PostListView, PostDetailView, Comment_CreateView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:diary_pk>/comment', Comment_CreateView.as_view(), name='comment'),
]