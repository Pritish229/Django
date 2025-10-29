from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .role import Role

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    contact_no = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?\d{10,15}$', 'Enter a valid contact number.')],
        blank=True,
        null=True
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_no = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^\d{11}$', 'Emergency contact number must be exactly 11 digits.')],
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role.name if self.role else 'No Role'}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"