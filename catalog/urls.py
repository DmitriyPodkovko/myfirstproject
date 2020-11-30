from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    ProjectCreateView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('projects/new/', ProjectCreateView.as_view(), name='project_new'),
]
