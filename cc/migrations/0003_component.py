# Generated by Django 2.0.13 on 2019-09-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0002_auto_20190916_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Component', models.CharField(choices=[('M&A', 'Merger and Acquisition'), ('Inv', 'Investment'), ('Financial', 'Financials'), ('JD', 'Jobs')], default='M&A', max_length=20)),
            ],
        ),
    ]