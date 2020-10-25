from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    project_description = models.TextField(max_length=5000, db_index=True, verbose_name='Project description')

    def number_of_ratings(self):
        ratings = Rating.objects.filter(project=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(project=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.project_description[:50]


class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', verbose_name='Project')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='ratings',
                             verbose_name='User')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)

    def __str__(self):
        return 'Project "{}"'.format(self.project)
