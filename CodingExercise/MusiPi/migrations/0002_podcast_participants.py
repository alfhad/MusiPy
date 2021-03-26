# Generated by Django 3.1.5 on 2021-03-26 05:00

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('MusiPi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='participants',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), default='', max_length=1010, size=10),
        ),
    ]