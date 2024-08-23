from django.db import models
class Ticket(models.Model):
  date_time=models.DateTimeField()
  Location=models.CharField(max_length=10)
  