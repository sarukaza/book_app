from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='検索', max_length=100)