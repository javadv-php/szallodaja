# Generated by Django 3.1.7 on 2021-07-01 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szallodaapp', '0005_todays_special'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_customer',
            name='phone',
        ),
    ]
