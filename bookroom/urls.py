from django.urls import path 
from .import views 


app_name = "bookroom"
urlpatterns =[
    path("",views.home, name ="home"),
    path("AvailableRoom/", views.AvailableRoom, name = "AvailableRoom"),
    
    path("booking/<int:booking_id>/", views.booking, name= "booking"),
    path("viewRoom/<int:view_id>/", views.viewRoom, name = "viewRoom"),
   
    
    path("checkout/", views.checkout, name = "checkout"),
    path("searchdate/", views.searchdate, name = "searchdate"),
]