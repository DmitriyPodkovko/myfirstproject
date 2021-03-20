from django.urls import path
from .views import ForumListView, ForumCreateView

urlpatterns = [
    path('<int:pk>/', ForumListView.as_view(), name='forum_list'),
    path('<int:pk>/new/', ForumCreateView.as_view(), name='comment_new'),
]
