from django.urls import path
from .views import (
    HomePageView,
    CategoryListView,
    CategoryCreateView,
    ProjectListView,
    ProjectCreateView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/new/', ProjectCreateView.as_view(), name='project_new'),
]
