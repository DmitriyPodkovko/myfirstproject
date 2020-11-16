from django.urls import path
from .views import CategoryCreateView

urlpatterns = [
    path('add/', CategoryCreateView.as_view(), name='category_add'),
]
