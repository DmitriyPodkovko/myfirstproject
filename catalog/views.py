from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Category


class CategoryCreateView(UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'category_add.html'
    fields = ['number', 'parent', 'technology']
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser
