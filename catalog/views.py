from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Category, Project, Rating


class HomePage(TemplateView):
    template_name = 'home.html'


class CategoryList(UserPassesTestMixin, ListView):
    model = Category
    template_name = 'category_list.html'

    def test_func(self):
        return self.request.user.is_superuser


class CategoryCreate(UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'category_add.html'
    fields = ['technology']
    success_url = reverse_lazy('category_list')

    def test_func(self):
        return self.request.user.is_superuser


class ProjectList(ListView):
    model = Project
    template_name = 'project_list.html'
    ordering = ['-created_at_comment']


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_new.html'
    fields = ['category', 'description']
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RatingCreate(LoginRequiredMixin, CreateView):
    model = Rating
    template_name = 'rating_new.html'
    fields = ['score']
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        return super().form_valid(form)
