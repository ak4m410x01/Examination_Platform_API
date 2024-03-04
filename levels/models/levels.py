from django.db import models


class Level(models.Model):
	level_number = models.IntegerField(unique=True, primary_key=True)

	def __str__(self):
		return f'Level {self.level_number}'
