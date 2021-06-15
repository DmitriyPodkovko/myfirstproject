from django.urls import path
from .views import (
    HomePage,
    CategoryList,
    CategoryCreate,
    ProjectList,
    ProjectCreate,
    RatingCreate
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/add/', CategoryCreate.as_view(), name='category_add'),
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('projects/new/', ProjectCreate.as_view(), name='project_new'),
    path('projects/<int:pk>/rate/new/', RatingCreate.as_view(), name='rating_new'),

]
