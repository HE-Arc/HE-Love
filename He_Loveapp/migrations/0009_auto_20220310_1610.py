# Generated by Django 3.2.11 on 2022-03-10 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('He_Loveapp', '0008_auto_20220310_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_gender_interest',
            name='gender_id',
        ),
        migrations.RemoveField(
            model_name='user_gender_interest',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user_interest',
            name='interest_id',
        ),
        migrations.RemoveField(
            model_name='user_interest',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user_gender_interest',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_gender_interest_gender', to='He_Loveapp.gender'),
        ),
        migrations.AddField(
            model_name='user_gender_interest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_gender_interest_user', to='He_Loveapp.appuser'),
        ),
        migrations.AddField(
            model_name='user_interest',
            name='interest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_interest_interest', to='He_Loveapp.interest'),
        ),
        migrations.AddField(
            model_name='user_interest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_interest_user', to='He_Loveapp.appuser'),
        ),
    ]