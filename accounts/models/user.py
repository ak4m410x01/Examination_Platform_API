from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER = (
        ("m", "male"),
        ("f", "female"),
    )
    USER_TYPE = (
        (1, "admin"),
        (2, "instructor"),
        (3, "student"),
    )

    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=5000)

    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    third_name = models.CharField(max_length=30, blank=True, null=True)
    fourth_name = models.CharField(max_length=30, blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER)
    birth_date = models.DateField()

    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    user_type = models.IntegerField(choices=USER_TYPE)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = [
        "email",
        "password",
        "first_name",
        "second_name",
        "gender",
        "birth_date",
        "user_type",
    ]

    class Meta:
        swappable = "AUTH_USER_MODEL"

    def __str__(self) -> str:
        return str(self.username)
