# Generated by Django 3.1.7 on 2021-06-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szallodaapp', '0002_auto_20210613_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_customer',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='login_customer',
            name='table_no',
            field=models.IntegerField(),
        ),
    ]
