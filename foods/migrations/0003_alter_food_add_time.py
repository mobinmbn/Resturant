# Generated by Django 3.2.7 on 2021-09-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_rename_foods_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Add time'),
        ),
    ]
