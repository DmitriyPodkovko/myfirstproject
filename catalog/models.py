from django.db import models
from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from forum.models import ProjectForum


class Category(models.Model):
    # PARENT = [
    #     (1, 'Projects'),
    #     (2, 'Mentors'),
    # ]
    # number = models.PositiveIntegerField(unique=True, default=0)
    # parent = models.IntegerField(choices=PARENT)
    technology = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def category_projects_all(self):
        if self.projects.all():
            return True
        else:
            return False

    def __str__(self):
        return self.technology


class Project(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='projects')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='projects')
    description = models.TextField(max_length=5000, db_index=True)
    stars = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at_comment = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        super().save()
        if not ProjectForum.objects.filter(project=self).exists():
            ProjectForum.objects.create(project=self)

    def __str__(self):
        return self.description[:50]


class Rating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='ratings')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        super().save()
        scores = self.project.ratings.aggregate(Avg('score'))
        star = scores['score__avg']
        if star is not None:
            self.project.stars = round(star)
            self.project.save()

    def __str__(self):
        return self.score
