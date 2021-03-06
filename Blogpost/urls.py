from django.urls import path
from Blogpost.views import PostList, PostDetail, likeView

app_name = 'Blogpost'
urlpatterns = [
    path('', PostList.as_view(), name = 'post-list'),
    path('detail/<int:pk>/', PostDetail.as_view(),name = 'post-detail'),
    path('ajax/likes/',likeView, name = 'like'),
    ]