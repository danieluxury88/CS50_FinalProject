# Generated by Django 3.2.16 on 2023-04-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20230406_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='due_tomorrow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='due_tomorrow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='due_tomorrow',
            field=models.BooleanField(default=False),
        ),
    ]