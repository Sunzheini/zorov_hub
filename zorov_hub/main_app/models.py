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
    grocery_count = models.IntegerField(
        default=1,
    )

    @property
    def full_grocery_info(self):
        return f"{self.grocery_count} of {self.grocery_name}"

    # automatically displays like this at admin site
    def __str__(self):
        return f"ID: {self.pk}, " \
               f"grocery_name: {self.grocery_name}, " \
               f"grocery_count: {self.grocery_count}"


class Tasks(models.Model):
    task_name = models.CharField(  # v admin: `task_name` stava `Task name` avtomatichno
        max_length=30,
        unique=True,
        verbose_name='Da Task Name',    # overwrite-va red 33
    )
    task_responsible = models.CharField(
        max_length=30,
        choices=(
            ('DZ', 'Daniel'),       # DZ v bazata, Daniel v admin se vijda
            ('MZ', 'Maxi'),
            ('BA', 'Boryana'),
            ('AZ', 'Adriana'),
        )
    )
    task_creation_date = models.DateTimeField(
        auto_now=True,
    )
    task_update_date = models.DateTimeField(
        auto_now_add=True,
    )
    task_deadline = models.DateTimeField(
        blank=True, null=True,      # 90% of cases they are both used, not separately
    )                               # they are False by default
    task_description = models.TextField(
        blank=True, null=True,
    )
    task_email = models.EmailField(
        blank=True, null=True,
    )
    task_photo = models.URLField(
        blank=True, null=True,
    )
    task_attachment = models.FileField(
        blank=True, null=True,
    )
    task_accepted = models.BooleanField()

    # automatically displays like this at admin site
    def __str__(self):
        return f"ID: {self.pk}, task_name: {self.task_name}, " \
               f"task_responsible: {self.task_responsible}, etc."
