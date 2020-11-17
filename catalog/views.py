from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Category


class CategoryListView(UserPassesTestMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class CategoryCreateView(UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'category_add.html'
    fields = ['number', 'technology']
    login_url = 'login'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        return self.request.user.is_superuser
