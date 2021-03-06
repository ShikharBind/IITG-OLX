# Generated by Django 3.2.5 on 2022-06-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0014_alter_product_created_date'),
        ('user_profile', '0003_alter_userprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='wishlist_products',
            field=models.ManyToManyField(blank=True, null=True, to='posts_app.Product'),
        ),
    ]
