# Generated by Django 3.2.11 on 2022-03-30 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('He_Loveapp', '0020_merge_0017_merge_20220329_1942_0019_alter_chat_match'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='profilePicture',
            new_name='profile_picture',
        ),
    ]
