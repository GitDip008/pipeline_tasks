from django.db import models

# Create your models here.

class Destination(models.Model):
    # DateTime = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Date_Time = models.TextField()
    Log_Category = models.TextField()
    Actual_Message = models.TextField()

    def __str__(self):
        return self.Log_Category