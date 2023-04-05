from django.db import models

# Create your models here.

class MenuItem(models.Model):
    # ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.SmallIntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
        

class Booking(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField()
    BookingDate = models.DateTimeField(auto_now=True)
    
    

    