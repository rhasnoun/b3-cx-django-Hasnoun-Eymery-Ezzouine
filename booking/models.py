from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

ECOLE_CHOICES = (
    ("L'ecole d'aviation de Rayan", "L'ecole d'aviation de Rayan"),
     ("L'ecole d'aviation de Maxence", "L'ecole d'aviation de Maxence"),
      ("L'ecole d'aviation de Ezzouine", "L'ecole d'aviation de Ezzouine"),
    )
SERVICE_CHOICES = (
    ("Cours de Pilotage", "Cours de Pilotage"),
    )
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ecole =  models.CharField(max_length=50, choices=SERVICE_CHOICES, default="L'ecole d'aviation de Rayan")
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Cours de Pilotage")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"