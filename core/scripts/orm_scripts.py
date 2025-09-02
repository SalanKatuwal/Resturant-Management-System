from django.contrib.auth.models import User
from core.models import Resturant,Rating,Sale,Staff,StaffResturant
from django.utils import timezone
from django.db.models.functions import Lower 

def run():
    # to add in staff
    Staff.objects.create(name="Salan Katuwal")
    resturant = Resturant.objects.last()
    StaffResturant.objects.create(staff=Staff.objects.first(),resturant=resturant,salary=50000)
    
    # this code is for if we have only done without through model
    # staff ,created = Staff.objects.create(name="Saurav Katuwal")
    # staff.resurants.count()
    # staff.resturants.remove(Resturant.objects.first())
    # this means the single staff works in 5 different resturants
    # staff.resturants.set(Resturant.objects.all()[:5])
    # staff.resturants.add(Resturant.objects.first())
    
    
    
    #fetching user , resturant , and sales data
    # user = User.objects.all()
    # rating = Rating.objects.filter(rating__gte=2)
    # print(rating)
    # resturant = Resturant.objects.count()
    # rating = Rating(user=User.objects.first(),resturant=Resturant.objects.first(),rating=10)
    # rating.full_clean()
    # rating.save()
    # rating.save(update_fields=['rating'])
    
    # to delete all the queryset
    # Resturant.objects.all().delete()
    #to delete single data
    # resturant= Resturant.objects.first()
    # resturants.delete() this will also delete the row in the rating and set null in the sale table
    
    # use look up and multiple where clause
    # resturants = Resturant.objects.filter(resturant_type=Resturant.TypeChoices.ITALIAN,name__startswith='C')
    
    # .earliest and .latest are used for dates returns only single query (record)
    
    #find all the rating associated with the resturant beginning with 'C'
    # ratings = Resturant.objects.filter(resturant__name__startswith='C')
    
    
    #ordering 
    # resturant = Resturant.objects.order_by('-name') it is case sensitive
    # resturant = Resturant.objects.order_by(Lower('name')) it becomes case insensitive
     
    #update mutliple value at once
    # resturant = Resturant.objects.all()
    # resturant.update(date_opened=timezone.now())
    
    # update the database data with .save()
    # rating = Rating.objects.last()
    # rating.resturant= Resturant.objects.all()[1]
    # rating.save()
    
    # performing join operation
    # rating = Rating.objects.all()[3]
    # print(rating.resturant.resturant_type)
    
    # accesing rating(child model) from resturant model(parent model means no foreign key here)
    # resturant = Resturant.objects.first() # this will get us all the rating of the first resturant
    # print(resturant.rating_set.all())
    # another way is to use related_name in model definition
    # resturant = Resturant.objects.last()
    # print(resturant.ratings.all())
    # print(resturant.sales.all())
    
    # next one is get_or_create query
    # Sale.objects.get_or_create(resturant=Resturant.objects.all()[2],income=1150,datetime= timezone.now())
    # or
    # sales , created = Sale.objects.get_or_create(resturant=Resturant.objects.all()[2],income=1150,datetime= timezone.now())
    # this will true if the user has been created and false if the user is present and it will fetch the user
    
    # Create user objects direclty
    # User.objects.create_user(username="salan",password="123")
    # User.objects.create_user(username="Saurav",password="123")
    # User.objects.create_user(username="Sita",password="123")
    # User.objects.create_user(username="Arjun",password="123")
    # User.objects.create_user(username="Padam",password="123")
    
    ## create Resturant data
    # Resturant.objects.create(name="Padmavati Bhojanalaya",date_opened='2014-08-08',latitude=50.3,longitude=55.66,
    #                          resturant_type=Resturant.TypeChoices.FASTFOOD)
    # Resturant.objects.create(name="Hariyali Hotel",date_opened=timezone.now(),latitude=50.3,longitude=55.66,
    #                          resturant_type=Resturant.TypeChoices.GREEK)
    # Resturant.objects.create(name="Taj hotel",date_opened=timezone.now(),latitude=50.3,longitude=55.66,
    #                          resturant_type=Resturant.TypeChoices.OTHER)
    
    # create rating data
    # Rating.objects.create(user=User.objects.first(),resturant=Resturant.objects.last(),rating=4)
    # Rating.objects.create(user=User.objects.all()[3],resturant=Resturant.objects.last(),rating=5)
    # Rating.objects.create(user=User.objects.last(),resturant=Resturant.objects.first(),rating=1)
    # Rating.objects.create(user=User.objects.all()[2],resturant=Resturant.objects.first(),rating=2)
    # Rating.objects.create(user=User.objects.all()[2],resturant=Resturant.objects.all()[3],rating=3)
    
    #create Sales data
    # Sale.objects.create(resturant=Resturant.objects.first(),income=500,datetime=timezone.now())
    # Sale.objects.create(resturant=Resturant.objects.first(),income=1000,datetime=timezone.now())
    # Sale.objects.create(resturant=Resturant.objects.last(),income=200,datetime=timezone.now())
    # Sale.objects.create(resturant=Resturant.objects.last(),income=250,datetime=timezone.now())
    # Sale.objects.create(resturant=Resturant.objects.all()[1],income=500,datetime=timezone.now())
    # Sale.objects.create(resturant=Resturant.objects.all()[1],income=750,datetime=timezone.now())
    # Sale.objects.create(resturant=Resturant.objects.all()[2],income=100,datetime=timezone.now())
    
    