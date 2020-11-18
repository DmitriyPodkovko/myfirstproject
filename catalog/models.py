from django.db import models


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
