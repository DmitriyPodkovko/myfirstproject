from django.urls import path
from .views import (
    CommentList, CommentCreate,
    CommentUpdate, CommentDelete
)

urlpatterns = [
    path('<int:pk>/', CommentList.as_view(), name='forum_list'),
    path('<int:pk>/new/', CommentCreate.as_view(), name='comment_new'),
    path('<int:pk>/edit/<int:id_comment>/', CommentUpdate.as_view(), name='comment_edit'),
    path('<int:pk>/delete/<int:id_comment>/', CommentDelete.as_view(), name='comment_delete'),
]
