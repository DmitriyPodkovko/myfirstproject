from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Forum
from catalog.models import Project


class ForumListView(ListView):
    model = Forum
    template_name = 'forum_list.html'

    def get_context_data(self, **kwargs):
        context = super(ForumListView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context

    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        # return Forum.objects.filter(project_id=self.kwargs.get('pk'))
        return project.comments.all()


class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    template_name = 'comment_new.html'
    fields = ['comment']

    def get_context_data(self, **kwargs):
        context = super(ForumCreateView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum_list', kwargs={'pk': self.kwargs['pk']})
