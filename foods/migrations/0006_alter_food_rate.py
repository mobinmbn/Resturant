# Generated by Django 3.2.7 on 2021-09-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_alter_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='Rate'),
        ),
    ]
