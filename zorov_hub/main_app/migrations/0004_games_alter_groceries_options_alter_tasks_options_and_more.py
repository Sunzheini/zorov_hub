# Generated by Django 4.1.3 on 2022-12-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_tasks_task_responsible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=30)),
                ('game_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Games',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='groceries',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Groceries'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['id'], 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Da Task Name'),
        ),
        migrations.CreateModel(
            name='GamesAdmin',
            fields=[
                ('games_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.games')),
            ],
            bases=('main_app.games',),
        ),
    ]
