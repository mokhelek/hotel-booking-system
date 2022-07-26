
from django.db import models
# Create your models here.
#below is for the admin only
class Rooms(models.Model):
    start_date = models.DateField(blank=True , null=True)  # a date on which the room is booked for
    end_date = models.DateField(blank=True ,  null=True)
    name = models.CharField(max_length=100)
    roomType = models.CharField(max_length= 80)  # single, double or dom ...Maybe I shoud make this to be choice model
    priceRate = models.IntegerField()
    roomDescription = models.CharField(max_length=200)
    room_available = models.BooleanField(default = True)
    thumbanil = models.ImageField(null = False)
    def __str__(self):
        return self.roomType

class BookerDetails(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)  
    valid_Id = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    def __str__(self):
        return self.fullName
    
class RoomPictures(models.Model):
    room = models.ForeignKey(Rooms,on_delete =models.CASCADE)
    picture = models.ImageField(null = True)
    def __str__(self):
        return f'picture for  " {self.room.name} " '
    
class Extras(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    breakfast = models.BooleanField()
    wifi = models.BooleanField()
    cleaning = models.BooleanField() 
    

    
