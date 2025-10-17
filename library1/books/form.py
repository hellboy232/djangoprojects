from django import forms

# class Books(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     page=forms.IntegerField()
#     price=forms.IntegerField()
#     language=forms.CharField()


from books.models import Book

class Books(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

