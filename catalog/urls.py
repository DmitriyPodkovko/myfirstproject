from django.urls import path
from .views import CategoryListView, CategoryCreateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('add/', CategoryCreateView.as_view(), name='category_add'),
]
