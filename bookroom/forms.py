from django.forms import DateInput, ModelForm
from . models import BookerDetails , Extras , Rooms
from django import forms

from bootstrap_datepicker_plus.widgets import DatePickerInput
# my forms will go here

class BookerInfo(ModelForm):
    
    class Meta :
        model = BookerDetails
        fields = ['fullName','valid_Id','phone_number','email']

        
        
class AddExtras(ModelForm):
    class Meta :
        model = Extras
        fields = ['breakfast', 'wifi', 'cleaning']