# Generated by Django 3.1.6 on 2021-06-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog_app', '0002_auto_20210607_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='News', max_length=255, verbose_name='Category'),
        ),
    ]
