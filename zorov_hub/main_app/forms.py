from django import forms
from zorov_hub.main_app.models import Games
from zorov_hub.main_app.validators import some_validator


# independent form (not modelform)
class NameForm(forms.Form):

    GROCERY_TYPES = (
        (1, 'tomato'),
        (2, 'potato'),
        (3, 'coke'),
    )

    form_grocery_name = forms.CharField(
        max_length=30,
        label='Form grocery namez',
        help_text='help text',

        widget=forms.Textarea,  # default is TextInput and we overwrite with TextArea
    )
    form_grocery_count = forms.IntegerField(
        # required=False,
        label='madafaka count',
        initial=1,
    )

    # types of select widgets - not connected to anything currently
    form_grocery_type_dropdown = forms.ChoiceField(
        choices=GROCERY_TYPES,
    )
    form_grocery_type_radio = forms.ChoiceField(
        choices=GROCERY_TYPES,
        widget=forms.RadioSelect(),
    )
    form_grocery_type_multiple = forms.ChoiceField(
        choices=GROCERY_TYPES,
        widget=forms.SelectMultiple(),
    )
    form_grocery_type_checkbox = forms.BooleanField(
        required=False,
    )

    # example with attrs
    form_attrs_example = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter something',   # grey text in a field
                'class': 'form-control',
            },
        )
    )


# model form - for db driven apps
class GameForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'  # or ('name', 'age')

        widgets = {     # kogato e model form widgetite sa taka
            'game_name': forms.TextInput(
                attrs={
                    'placeholder': 'elden ring',
                }
            )
        }

        labels = {         # drugite defaultni gi promqneme taka
            'game_name': 'game namez',
        }

