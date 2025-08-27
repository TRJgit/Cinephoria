from django import forms

class NewMovie(forms.Form):
    name = forms.CharField(label="Movie Name ", max_length=200)

  