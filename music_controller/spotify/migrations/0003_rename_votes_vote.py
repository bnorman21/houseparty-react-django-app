# Generated by Django 3.2.13 on 2022-06-11 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_room_current_song'),
        ('spotify', '0002_votes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]