from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager, TransactionManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    """ Profile with additional info for User instance (One to one) """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    balance = models.PositiveIntegerField(default=0)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    def __str__(self) -> str:
        return str(self.user)


class Transaction(models.Model):
    """ Each user can make deposit or withdrawal managing account balance"""
    
    DEPOSIT = "DPST"
    WITHDRAWAL = "WDRL"
    SALE = "SALE"
    PAYMENT = "PAYM"
    
    TYPE_CHOICES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
        (SALE, 'Sale'),
        (PAYMENT, 'Payment')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.PositiveIntegerField()
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = TransactionManager()
    
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
    
    def __str__(self) -> str:
        return f"{self.amount} ({self.type})"
