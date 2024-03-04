from accounts.models.user import User
from django.db import models
from levels.models.levels import Level
from levels.models.department import Department


class Student(User):
	department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE)
	level = models.ForeignKey(Level, related_name='students', on_delete=models.CASCADE)
