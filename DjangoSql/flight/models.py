from django.db import models

# Create your models here.
class airport (models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64, unique=True)

    def __str__(self) :
        return f" {self.code} {self.city}"

class flight (models.Model):
    origin = models.ForeignKey(airport, on_delete = models.CASCADE, related_name="departers")
    destination = models.ForeignKey(airport, on_delete = models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()


    def __str__(self):
        return f"{self.id} ({self.origin}) ({self.destination})({self.duration})"