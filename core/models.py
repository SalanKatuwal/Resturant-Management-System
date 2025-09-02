from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError

def stat_with_a(value):
    if not value.startswith('a'):
        raise ValidationError("The name must begin with a")
    

class Resturant(models.Model):
    name = models.CharField( max_length=100, #validators = [start_with_a]
                            ) 
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
    
    class TypeChoices(models.TextChoices):
        NEPALI = 'NP', 'Nepali'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        FASTFOOD = 'FF' ,'Fast Food'
        OTHER = 'OT', 'Other'
    resturant_type = models.CharField(max_length = 2,
                                      choices = TypeChoices.choices)
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length=50)
    resturatns = models.ManyToManyField(Resturant,through="StaffResturant")
    def __str__(self):
        return self.name

class StaffResturant(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    resturant = models.ForeignKey(Resturant,on_delete=models.CASCADE)
    salary = models.FloatField(null=True)

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    resturant = models.ForeignKey(Resturant,on_delete = models.CASCADE,related_name="ratings")
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(5)
    ])
    
    def __str__(self):
        return f'Rating:{self.rating}'

class Sale(models.Model):
    resturant = models.ForeignKey(Resturant,on_delete=models.SET_NULL,null=True,related_name="sales")
    income = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
    
    

