from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'reservation_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
    
