from django.urls import path
from .views import ProjectCreateView

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name='project_new'),
]
