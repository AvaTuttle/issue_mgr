# Generated by Django 5.1.5 on 2025-01-18 16:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')], default='to_do', max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=20)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_issues', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_issues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
