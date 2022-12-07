from django.db import models

# 1 class == 1 table
"""
Groceries.objects.all()             # get all objects // Select
Groceries.objects.create()          # create a new object // Insert
Groceries.objects.filter()          # filter // Select + Where
Groceries.objects.update()          # update // Update
Groceries.objects.raw('SELECT * ')  # directly sql
"""


class Groceries(models.Model):
    grocery_name = models.CharField(
        max_length=30,
    )
    grocery_count = models.IntegerField()


class Tasks(models.Model):
    task_name = models.CharField(
        max_length=30,
    )
    task_responsible = models.CharField(
        max_length=30,
    )
    task_creation_date = models.DateTimeField(
        auto_now=True,
    )
    task_update_date = models.DateTimeField(
        auto_now_add=True,
    )
    task_deadline = models.DateTimeField()
    task_description = models.TextField()
    task_email = models.EmailField()
    task_photo = models.URLField()
    task_attachment = models.FileField()
    task_accepted = models.BooleanField()
