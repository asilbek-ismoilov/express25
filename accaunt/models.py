from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number must be provided")
        if not password:
            raise ValueError("Password is not provided")

        email = self.normalize_email(email) if email else None
        user = self.model(
            email=email,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone_number, password, **extra_fields)

    def create_superuser(self, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True, max_length=254, blank=True, null=True)

    phone_number = models.CharField(max_length=15, unique=True)
    is_courier = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1, 
        choices=[('M', 'Male'), ('F', 'Female')], 
        blank=True, 
        null=True
    )
    birth_date = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.phone_number


class Courier(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='courier_profile'
    )
    vehicle_type = models.CharField(
        max_length=50,
        choices=[
            ('bike', 'Bike'),
            ('car', 'Car'),
            ('scooter', 'Scooter'),
        ],
        blank=True,
        null=True
    )
    license_plate = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    availability = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Courier'
        verbose_name_plural = 'Couriers'
        ordering = ['user__phone_number']  # Telefon raqami bo'yicha tartiblash

    def __str__(self) -> str:
        return f'Courier: {self.user.phone_number} ({self.vehicle_type or "No vehicle"})'
