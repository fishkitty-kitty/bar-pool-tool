from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class RatingForm(forms.Form):
    title = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    categories = ['Staff', 'Ambience',	'Patrons',	'Tables Count',	'Table Quality', 'Gear Quality', 'Food', 'Drink', 'Game Cost']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for category in self.categories:
            self.fields[category] = forms.IntegerField(
                label= category,
                validators=[MinValueValidator(0), MaxValueValidator(10)]
            )
