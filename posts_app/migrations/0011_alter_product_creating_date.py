# Generated by Django 3.2.5 on 2022-06-09 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0010_auto_20220609_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creating_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 0, 0, 6, 448402, tzinfo=utc)),
        ),
    ]
