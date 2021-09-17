from django.urls import path
from .views import (
    HomePage,
    CategoryList,
    CategoryDetail,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
    ProjectList,
    ProjectCreate,
    RatingDeny,
    RatingCreate
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('categories/add/', CategoryCreate.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', CategoryUpdate.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view(), name='category_delete'),
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('projects/new/', ProjectCreate.as_view(), name='project_new'),
    path('projects/rate/deny/', RatingDeny.as_view(), name='rating_deny'),
    path('projects/<int:pk>/rate/new/', RatingCreate.as_view(), name='rating_new'),
]
