# Generated by Django 3.2.5 on 2022-06-09 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0011_alter_product_creating_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='creating_date',
        ),
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 0, 0, 34, 798445, tzinfo=utc)),
        ),
    ]
