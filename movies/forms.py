from django import forms 
from .models import Movie ,Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title','released_year','number_in_stoke','daily_rate','genre']
