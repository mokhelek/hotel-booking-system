# Generated by Django 4.0.4 on 2022-06-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='end_date',
            field=models.DateTimeField(default='2022-02-02 12:00'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='start_date',
            field=models.DateTimeField(default='2022-02-02 12:00'),
        ),
    ]
