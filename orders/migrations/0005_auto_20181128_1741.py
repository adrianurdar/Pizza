# Generated by Django 2.1.3 on 2018-11-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181128_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Topping', 'Topping'), ('Sub', 'Sub menu'), ('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Dinner Platter', 'Dinner Platter')], max_length=16),
        ),
    ]
