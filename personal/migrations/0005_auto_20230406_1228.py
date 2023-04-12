# Generated by Django 3.2.16 on 2023-04-06 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20230406_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='date',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal.datetype'),
        ),
    ]