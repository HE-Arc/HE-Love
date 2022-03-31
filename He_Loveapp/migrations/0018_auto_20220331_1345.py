# Generated by Django 3.2.11 on 2022-03-31 11:45

import He_Loveapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('He_Loveapp', '0017_merge_20220330_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to=He_Loveapp.models.event_upload),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='profilePicture',
            field=models.ImageField(upload_to=He_Loveapp.models.user_Image_Files_directory_path),
        ),
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
