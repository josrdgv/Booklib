from django import forms

from .models import Book,Author


class Authorform(forms.ModelForm):
    class Meta:
        model=Author
        fields=['author_name']  #if we want to specify a particular field we can use like this
class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'  #'all' is used to specify all the field inside the field

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book name'}),
            'Author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the Author'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book price'})

        }






