from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import ProjectForum, Comment


class CommentList(ListView):
    model = Comment
    template_name = 'forum_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        project_forum = get_object_or_404(ProjectForum, project=self.kwargs.get('pk'))
        context['num_forum'] = project_forum.pk
        return context

    def get_queryset(self):
        project_forum = get_object_or_404(ProjectForum, project=self.kwargs.get('pk'))
        return project_forum.comments.all()


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ['comment']

    def get_context_data(self):
        context = super().get_context_data()
        project_forum = get_object_or_404(ProjectForum, project=self.kwargs.get('pk'))
        context['num_forum'] = project_forum.pk
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project_forum = get_object_or_404(ProjectForum, project=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum_list', kwargs={'pk': self.kwargs['pk']})
