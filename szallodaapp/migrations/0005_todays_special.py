# Generated by Django 3.1.7 on 2021-06-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szallodaapp', '0004_auto_20210614_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todays_special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=20)),
                ('discount', models.CharField(max_length=20)),
            ],
        ),
    ]
