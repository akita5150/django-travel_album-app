from django.urls import include, path
from timeline.views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail')
]