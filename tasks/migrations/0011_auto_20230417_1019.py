# Generated by Django 3.2.16 on 2023-04-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20230416_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestone',
            name='due_today',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='due_tomorrow',
        ),
        migrations.RemoveField(
            model_name='project',
            name='due_today',
        ),
        migrations.RemoveField(
            model_name='project',
            name='due_tomorrow',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_today',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_tomorrow',
        ),
        migrations.AddField(
            model_name='milestone',
            name='due_date',
            field=models.IntegerField(choices=[(1, 'DUE TODAY'), (2, 'DUE TOMORROW'), (3, 'DUE THIS CYCLE'), (4, 'DUE NEXT CYCLE'), (5, 'UNPLANIFIED')], default=5),
        ),
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.IntegerField(choices=[(1, 'DUE TODAY'), (2, 'DUE TOMORROW'), (3, 'DUE THIS CYCLE'), (4, 'DUE NEXT CYCLE'), (5, 'UNPLANIFIED')], default=5),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.IntegerField(choices=[(1, 'DUE TODAY'), (2, 'DUE TOMORROW'), (3, 'DUE THIS CYCLE'), (4, 'DUE NEXT CYCLE'), (5, 'UNPLANIFIED')], default=5),
        ),
    ]
