# Generated by Django 2.0.13 on 2019-10-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0010_auto_20191016_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuetracker',
            name='availability',
            field=models.IntegerField(default=0),
        ),
    ]
