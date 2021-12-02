from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .models import Category, Project, Rating


class HomePage(TemplateView):
    template_name = 'home.html'


class CategoryList(UserPassesTestMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    ordering = ['created_at']

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDetail(UserPassesTestMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if Category.objects.filter(id=self.kwargs.get('pk')
                                   )[0].projects.exists():
            messages.error(request,
                           'Unable to delete (you must first '
                           'delete all projects with this category)')
        return self.render_to_response(context)

    def test_func(self):
        return self.request.user.is_superuser


class CategoryCreate(UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'category_add.html'
    fields = ['technology']
    success_url = reverse_lazy('category_list')

    def test_func(self):
        return self.request.user.is_superuser


class CategoryUpdate(UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'category_edit.html'
    fields = ['technology']

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('category_detail',
                            kwargs={'pk': self.kwargs['pk']})


class CategoryDelete(UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            return HttpResponseRedirect(reverse(
                'category_detail', kwargs={'pk': self.kwargs['pk']}))

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


class RatingDeny(TemplateView):
    template_name = 'rating_deny.html'


class RatingCreate(LoginRequiredMixin, CreateView):
    model = Rating
    template_name = 'rating_new.html'
    fields = ['score']
    success_url = reverse_lazy('project_list')

    def is_limit(self):
        return Rating.objects.filter(user=self.request.user,
                                     project=self.kwargs.get('pk')).exists()

    def post(self, request,  *args, **kwargs):
        if self.is_limit():
            return HttpResponseRedirect(reverse('rating_deny'))
        else:
            return super().post(request,  *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = get_object_or_404(Project,
                                                  id=self.kwargs.get('pk'))
        return super().form_valid(form)
