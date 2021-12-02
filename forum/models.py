from django.db import models
from django.contrib.auth import get_user_model


class ProjectForum(models.Model):
    project = models.OneToOneField('catalog.Project',
                                   on_delete=models.CASCADE,
                                   related_name='project_forum')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                             null=True, related_name='comments')
    project_forum = models.ForeignKey(ProjectForum, on_delete=models.CASCADE,
                                      related_name='comments')
    comment = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        super().save()
        self.project_forum.project.created_at_comment = self.created_at
        self.project_forum.project.save()

    def __str__(self):
        return self.comment[:50]
