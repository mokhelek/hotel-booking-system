
from django.shortcuts import render, redirect
from .models import BookerDetails , Extras , Rooms
from .forms import BookerInfo , AddExtras
import datetime

# Create your views here. 

def home(request):
    import time
    search = request.POST.get('userdate1')
    search2 = request.POST.get('userdate2')
    
    
    
    if search:
        #  my model has start_date and end_date
        
        
        search1C = search.replace("/","-")  
        search2C = search2.replace("/","-")
        rooms = Rooms.objects.all() #all my rooms
        avail_rooms = []
        
        request.session["search1C"] = search1C
        request.session["search2C"] = search2C
        
        for i in rooms:
            if i.start_date > datetime.datetime.strptime(search1C, "%Y-%m-%d").date() and  i.start_date > datetime.datetime.strptime(search2C, "%Y-%m-%d").date():
                avail_rooms.append(i)
                
        for x in rooms:
            if i.end_date < datetime.datetime.strptime(search1C, "%Y-%m-%d").date() and i.end_date < datetime.datetime.strptime(search2C, "%Y-%m-%d").date():
                avail_rooms.append(x)        
      
        context = {"avail":avail_rooms}
        return render (request , "bookroom/home.html" , context )     
        
    else:
        context = {}
        return render (request , "bookroom/home.html" , context )   
    

def booking(request, booking_id):
    rooms = Rooms.objects.get(id = booking_id)
    
    start_date = rooms.start_date
    end_date = rooms.end_date
    
    search1C = request.session['search1C'] # start date
    search2C = request.session['search2C']  # end date
    
    if request.method != 'POST':
        form = BookerInfo()
    else:
        form = BookerInfo(data=request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.rooms = rooms
            rooms.room_available = False 
            
            rooms.start_date = search1C
            rooms.end_date = search2C
            
            
            myform.start_date = start_date
            myform.end_date = end_date
            
            
            myform.save()
            rooms.save(update_fields = ['room_available',"start_date","end_date"])
            return redirect('bookroom:home' )       
    
    context = {'rooms':rooms, "form":form,"start":search1C,"end":search2C}
    return render (request , "bookroom/booking.html" , context)

def viewRoom(request, view_id):
    view =  Rooms.objects.get(id = view_id)
    allrooms = Rooms.objects.exclude(id=view_id)
    context = {"view":view,"allrooms":allrooms}
    return render (request , "bookroom/viewRoom.html" , context)   

def AvailableRoom(request):
    rooms = Rooms.objects.all()
    context = {'rooms':rooms}
    return render (request, "bookroom/available.html" , context) 



def checkout(request):
    search = request.GET['userdate1']
    search2 = request.GET['userdate2']
    
    search1C = search.replace("/","-")  # finale converted date and time ...
    search2C = search2.replace("/","-")

    rooms = Rooms.objects.filter(start_date__range = [search1C,search2C])
    #rooms = Rooms.objects.all()
    context = {"rooms":rooms}
  
    return render (request , "bookroom/checkout.html" , context  )

def searchdate(request): 
    search = request.POST.get('userdate1')
    search2 = request.POST.get('userdate2')
    
    
    if search:
        #  my model has start_date and end_date
        search1C = search.replace("/","-")  
        search2C = search2.replace("/","-")
        rooms = Rooms.objects.all() #all my rooms
        avail_rooms = []
        
        for i in rooms:
            if i.start_date > datetime.datetime.strptime(search1C, "%Y-%m-%d").date() and  i.start_date > datetime.datetime.strptime(search2C, "%Y-%m-%d").date():
                avail_rooms.append(i)
                
        for x in rooms:
            if i.end_date < datetime.datetime.strptime(search1C, "%Y-%m-%d").date() and i.end_date < datetime.datetime.strptime(search2C, "%Y-%m-%d").date():
                avail_rooms.append(x)        
      
        context = {"avail":avail_rooms}
        return render (request , "bookroom/check.html" , context )     
        
    else:
        context = {}
        return render (request , "bookroom/check.html" , context )   
    
    
"""
rooms = Rooms.objects.exclude(start_date__gte=search1C)
rooms = Rooms.objects.exclude(start_date__lte=search2C)

 booked_rooms = Rooms.objects.filter(start_date__gte=search1C) and Rooms.objects.filter(end_date__lte = search2C) # object of all the booked rooms
        
        available_rooms =[] # will contain all the non booked rooms
        
        for available_room in rooms:
            if available_room not in booked_rooms:
                available_rooms.append(available_room)
                
        for i in booked_rooms:
            if search2C <= booked_rooms.end_date:
                alias.append(i)                
                                
        for x in rooms:
            if alias not in rooms:
                available_room.append(x)
                

"""  

