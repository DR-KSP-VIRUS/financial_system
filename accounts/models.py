from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False, is_customer=False):
        if not email:
            raise ValueError("User must have email")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters")
        
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.customer = is_customer
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email, password=password,
            is_admin=True,
            is_staff=True,
            is_customer=True
        )

        return user
    def create_customeruser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_customer=True
        )
        return user

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)
    customer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_customer(self):
        return self.customer
