# Generated by Django 4.2.1 on 2023-05-31 21:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_demo_link_alter_project_source_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='vote_ration',
            new_name='vote_ratio',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
