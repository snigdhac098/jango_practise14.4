from django import forms 
import datetime
from django.core import validators
from django.forms.widgets import NumberInput


class PractiseForm(forms.Form):
    BIRTH_YEAR_CHOICES = ['2023', '2002', '2005']
    name=forms.CharField(label="Full Name",
                         widget=forms.Textarea(attrs={'placeholder':'Enter Your Name','rows':3}))
    first_name = forms.CharField(initial='Your first name')
    last_name = forms.CharField(initial='Your last name')
    email=forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput()) 
    Agree=forms.BooleanField()
    value = forms.DecimalField()
    Today_date = forms.DateField()
    Birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    day = forms.DateField(initial=datetime.date.today)
    message = forms.CharField(
	max_length = 10,
)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    

    FAVORITE_OUTFIT_CHOICES = [
    ('sari', 'Sari'),
    ('kurti', 'Kurti'),
    ('Causal', 'causual'),
]
    
    favorite_outfit= forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_OUTFIT_CHOICES)
    


    FAVORITE_PLACE_CHOICES = [
    ('moheskhali', 'Moheskhali'),
    ('cox bazar', 'Cox bazar'),
    ('sentmartin', 'Sentmartin'),
]
    
    favorite_place = forms.MultipleChoiceField(choices=FAVORITE_PLACE_CHOICES)

    FAVORITE_Blog_CHOICES = [
    ('science', 'Science'),
    ('horor', 'Horor'),
    ('regular', 'Regular'),
]


    favorite_blog = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_Blog_CHOICES,)