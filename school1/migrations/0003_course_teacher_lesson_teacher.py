# Generated by Django 5.1.4 on 2024-12-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school1', '0002_alter_lesson_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(max_length=255, null=True),
        ),
    ]