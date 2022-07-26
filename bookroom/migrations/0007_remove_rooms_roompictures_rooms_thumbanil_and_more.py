# Generated by Django 4.0.4 on 2022-07-24 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookroom', '0006_remove_bookerdetails_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='roomPictures',
        ),
        migrations.AddField(
            model_name='rooms',
            name='thumbanil',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RoomPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookroom.rooms')),
            ],
        ),
    ]