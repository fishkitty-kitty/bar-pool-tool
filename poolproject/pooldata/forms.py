from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class RatingForm(forms.Form):
    title = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])


# class RatingForm(models.Model):
#     overs = models.IntegerField(default=0, choices=((i,i) for i in range(0,11)))
