# Generated by Django 2.1.7 on 2019-04-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]