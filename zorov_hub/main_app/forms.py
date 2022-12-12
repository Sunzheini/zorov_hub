from django import forms


class NameForm(forms.Form):
    grocery_name = forms.CharField(
        max_length=30,
    )
    grocery_count = forms.IntegerField(
    )
