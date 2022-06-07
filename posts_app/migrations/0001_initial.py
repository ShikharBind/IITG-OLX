# Generated by Django 3.2.5 on 2022-06-07 11:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('product_details', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('current_age', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 6, 7, 11, 10, 17, 357750, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]