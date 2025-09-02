from django.shortcuts import render
from .forms import RatingForm
from core.models import Resturant,Sale,Rating
def index(request):
    # this for parent to child model
    # resturant = Resturant.objects.all()
    #to optimize this we do prefetch releated
    # resturantn = Resturant.objects.prefetch_related('ratings','sales')
    # context= {'resturants':resturant }
    
    # this is for child to parent model
    # ratings = Rating.objects.all()
    # we can optimize this using select_related
    ratings = Rating.objects.select_related('resturant')
    context={'ratings':ratings}
    
    return render(request,'index.html',context)
