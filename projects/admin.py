from django.contrib import admin
from .models import Project, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    verbose_name_plural = 'Ratings'


class ProjectAdmin(admin.ModelAdmin):
    inlines = [RatingInline]
    list_display = ['id', 'project_description']
    list_filter = ['project_description']
    search_fields = ['project_description']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'user', 'stars']
    list_filter = ['project', 'user', 'stars']
    raw_id_fields = ['project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating, RatingAdmin)
