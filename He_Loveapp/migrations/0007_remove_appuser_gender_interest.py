# Generated by Django 3.2.11 on 2022-03-10 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('He_Loveapp', '0006_auto_20220310_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='gender_interest',
        ),
    ]