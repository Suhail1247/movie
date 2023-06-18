from .models import Movie
from django import forms


class mvform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','imgs']