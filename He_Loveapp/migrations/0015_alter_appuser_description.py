# Generated by Django 3.2.11 on 2022-03-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('He_Loveapp', '0014_alter_dislike_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='description',
            field=models.TextField(default='Hello !', max_length=300),
        ),
    ]
