from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Define roles for the user
    class Role(models.TextChoices):
        RECRUITER = 'recruiter', _('Recruiter')
        CANDIDATE = 'candidate', _('Candidate')
        ADMIN = 'admin', _('Admin')

    # Add a field for user role
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CANDIDATE,
    )

    # Ensure email is unique
    email = models.EmailField(unique=True)

    # Override groups and user_permissions to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Custom related name to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related name to avoid clash
        blank=True
    )

    def __str__(self):
        return self.username

# Optionally, if you need to customize the Group model
class CustomGroup(Group):
    class Meta:
        proxy = True
        verbose_name = "Custom Group"
        verbose_name_plural = "Custom Groups"

    def custom_method(self):
        # Custom method for the group
        return "This is a custom method for the group."
