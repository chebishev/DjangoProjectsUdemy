# Generated by Django 4.2.4 on 2023-08-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.treicamile.ro/wp-content/uploads/2021/11/food-placeholder.png', max_length=500),
        ),
    ]
