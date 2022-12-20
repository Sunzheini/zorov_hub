from django.db import models


# 1 class == 1 table
from zorov_hub.main_app.validators import validate_text, validate_profile_name


class Groceries(models.Model):

    # meta danni za modela
    class Meta:
        ordering = ['-id']   # po kakvo se sortira by default // -id e descending
        verbose_name_plural = 'Groceries'
        # abstract = True   # pozvolqva da se nasledqva napr. kato Mixin

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
        return f"__str__: ID: {self.pk}, " \
               f"grocery_name: {self.grocery_name}, " \
               f"grocery_count: {self.grocery_count}"


class Tasks(models.Model):

    # meta danni za modela
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Tasks'

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
        return f"__str__: ID: {self.pk}, task_name: {self.task_name}, " \
               f"task_responsible: {self.task_responsible}, etc."


class Games(models.Model):

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Games'

    game_name = models.CharField(
        max_length=30,

        validators=(
            validate_text,  # validator na modelform se pravi v modela - raboti!
        ),
    )

    game_description = models.TextField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        # unique=True,
        null=True,
        blank=True,
        verbose_name='SLUG',
    )

    game_image = models.ImageField(
        blank=True, null=True,
        upload_to='images'  # syzdava folder images v MEDIA_ROOT
    )

    # analogichno e s filefield

    def __str__(self):
        return f"{self.game_name} - a game"


class Profile(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Profiles'

    profile_name = models.CharField(
        max_length=30,
        blank=False, null=False,

        validators=(
            validate_profile_name,  # validator na modelform se pravi v modela - raboti!
        ),
    )

    profile_type = models.CharField(
        max_length=30,
        blank=False, null=False,
        choices=(
            ('noob', 'noob'),  # v bazata, v admin
            ('pro', 'pro'),
            ('gigachad', 'gigachad'),
        )
    )

    slug = models.SlugField(
        # unique=True,
        null=True,
        blank=True,
        verbose_name='profile_slug',
    )
