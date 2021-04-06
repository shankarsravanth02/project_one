from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc= "most flooded"
    dest1.img = 'destination_1.jpg'
    dest1.price = 720
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'delhi'
    dest2.desc= "non polluted"
    dest2.img = 'destination_2.jpg'
    dest2.price = 700
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'chennai'
    dest3.desc= "filmy"
    dest3.img = 'destination_3.jpg'
    dest3.price = 650
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'hyderabad'
    dest4.desc= "biriyani"
    dest4.img = 'destination_4.jpg'
    dest4.price = 690
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'Banglore'
    dest5.desc= "green"
    dest5.img = 'destination_5.jpg'
    dest5.price = 730
    dest5.offer = False

    dest6 = Destination()
    dest6.name = 'pune'
    dest6.desc= "spacious"
    dest6.img = 'destination_6.jpg'
    dest6.price = 720
    dest6.offer = True

    dests =[dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request,'index.html',{'dests':dests})