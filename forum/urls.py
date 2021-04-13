from django.urls import path
from .views import CommentList, CommentCreate

urlpatterns = [
    path('<int:pk>/', CommentList.as_view(), name='forum_list'),
    path('<int:pk>/new/', CommentCreate.as_view(), name='comment_new'),
]
