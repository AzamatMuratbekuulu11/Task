# Generated by Django 5.0.6 on 2024-06-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
