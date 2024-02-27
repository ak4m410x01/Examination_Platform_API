from django.db import models
from accounts.models.user import User


class Instructor(User):
    specialized_in = models.CharField(max_length=50)
