from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, role='sender'):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        if role not in ['sender', 'rider', 'admin']:
            raise ValueError('Invalid role')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password, role='admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('sender', 'Sender'),
        ('rider', 'Rider'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    def __str__(self):
        return self.name
    

    
# Separate models for Sender and Rider to store additional information specific to each role    
class Sender(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    pickup_latitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        null=True, blank=True
    )
    pickup_longitude = models.DecimalField(
        max_digits=9, decimal_places=6,
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
    

class Rider(models.Model):
    VEHICLE_CHOICES = [
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('van', 'Van'),
    ]
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('offline', 'Offline'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES, null=True, blank=True)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='offline')
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.vehicle_type}"