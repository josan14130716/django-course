# Generated by Django 4.2.1 on 2023-06-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_alter_review_value_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
