from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category1(models.Model):
    parent_name = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category2(models.Model):
    number = models.PositiveIntegerField(default=0)
    technology = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    category1 = models.ForeignKey(Category1, on_delete=models.PROTECT, related_name='projects')
    category2 = models.ForeignKey(Category2, on_delete=models.PROTECT, related_name='projects')
    description = models.TextField(max_length=5000, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:50]


class Rating(models.Model):
    # user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, related_name='ratings')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Project "{}"'.format(self.project)


class Comment(models.Model):
    # user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, related_name='comments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Project "{}"'.format(self.project)
