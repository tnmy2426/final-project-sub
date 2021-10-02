from django.db import models

# For Custom User model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy

# to automatically create One To One Object
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserManager(BaseUserManager):
    """ A custom manager to deal with username as unique identifier """ 
    def create_user(self, username, password=None, **extra_fields):
        """ Creates and saves a user with a given username and password """
        if not username:
            raise ValueError('The Username Must be set !!')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, null=False, max_length=20)
    full_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(
        ugettext_lazy('active'),
        default=True,
        help_text= ugettext_lazy('Designates whether this user should be treated as active. Unselect this if user is not Verified.')
    )
    is_staff = models.BooleanField(
        ugettext_lazy('staff status'), 
        default=False,
        help_text= ugettext_lazy('Designates whether the user can log in this site as Volunteer.')
    )

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username


class ClubAdmin(models.Model):
    Gender_Choices = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("NONE", "None")
    ]

    Designation_Choices = [
        ("PRESIDENT", "President"),
        ("VICE_PRSIDENT", "Vice President"),
        ("GENERAL_SECRETARY", "General Secretary",),
        ("TREASURER", "Treasurer"),
        ("JOIN_SECRETARY", " Join Secretary"),
        ("PC_SECRETARY", "Public & Comunication Secretary"),
        ("NONE", "None")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="club_admin_user")
    designation = models.CharField(max_length=30, choices=Designation_Choices, default="NONE")
    profile_pic = models.ImageField(upload_to="ProfilePics/ClubAdmins", blank=True)
    gender = models.CharField(max_length=50, choices=Gender_Choices, default="NONE")
    phone_no = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    fb_id_link = models.URLField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ClubAdmin.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.club_admin_user.save()
