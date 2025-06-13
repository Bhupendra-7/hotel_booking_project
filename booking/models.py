from django.db import models



class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.room_type


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return self.name