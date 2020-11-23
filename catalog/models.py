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

    def __str__(self):
        return self.technology


class Project(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, related_name='projects')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='projects')
    description = models.TextField(max_length=5000, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:50]
