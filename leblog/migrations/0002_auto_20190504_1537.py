# Generated by Django 2.2.1 on 2019-05-04 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2019, 5, 4, 15, 37, 49, 336415)),
        ),
    ]
