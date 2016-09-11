from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Activity(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='activities')
	name = models.CharField(max_length=128)
	description = models.TextField()
	created_datetime = models.DateTimeField(default=timezone.now)
	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField(null=True)

	def __str__(self):
		return '{s.user.username}: {s.name} on {s.start_datetime:%Y-%m-%d}'.format(s=self)


