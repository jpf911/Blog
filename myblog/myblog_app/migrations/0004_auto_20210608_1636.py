# Generated by Django 3.1.6 on 2021-06-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog_app', '0003_auto_20210608_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255, verbose_name='Category'),
        ),
    ]