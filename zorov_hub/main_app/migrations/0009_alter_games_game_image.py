# Generated by Django 4.1.3 on 2022-12-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_games_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='game_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
