# Generated by Django 3.1.2 on 2021-04-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at_comment',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
