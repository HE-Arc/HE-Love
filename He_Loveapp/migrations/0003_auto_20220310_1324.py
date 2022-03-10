# Generated by Django 3.2.11 on 2022-03-10 12:24

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('He_Loveapp', '0002_auto_20220224_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('birth_date', models.DateField()),
                ('description', models.TextField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_gender', to='He_Loveapp.gender')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='chat',
            name='user_receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='user_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_user_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='user_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='user_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_user_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_gender_interest',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_gender_interest_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_interest',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_interest_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
