from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Category, Project


class HomePageView(TemplateView):
    template_name = 'home.html'


class CategoryListView(UserPassesTestMixin, ListView):
    model = Category
    template_name = 'category_list.html'

    def test_func(self):
        return self.request.user.is_superuser


class CategoryCreateView(UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'category_add.html'
    fields = ['technology']
    success_url = reverse_lazy('category_list')

    def test_func(self):
        return self.request.user.is_superuser


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    ordering = ['-created_at_comment']


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_new.html'
    fields = ['category', 'description']
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
