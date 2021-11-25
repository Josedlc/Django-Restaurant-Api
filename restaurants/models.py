from django.db import models

class Restaurant_types(models.Model):
    description = models.CharField(max_length=50)



class Direction(models.Model):
    city = models.CharField(max_length=100)
    pc = models.CharField(max_length=20)
    street = models.CharField(max_length=60)
    int_number = models.IntegerField()
    ext_number = models.IntegerField()
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
   
    def __str__(self):
        return self.state+' '+self.city+' '+self.pc+' '+self.street+' '+self.ext_number+' '+self.int_number+' '+self.location


class Restaurant(models.Model):
    name = models.CharField(max_length=130)
    schedule_open = models.TimeField(auto_now=False, auto_now_add=False)
    schedule_close = models.TimeField(auto_now=False, auto_now_add=False)
    direction = models.ForeignKey(Direction, related_name= "restaurant_direction",on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=12)
    restaurant_type = models.ForeignKey(
        Restaurant_types, related_name= "restaurant_type",on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name




