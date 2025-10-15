from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import RatingForm
from django.forms import formset_factory

def formset_view(request):
    RatingFormSet = formset_factory(RatingForm)
    if request.method == 'POST':
        formset = RatingFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
    else:
        formset = RatingFormSet()

    return render(request, "pooldata/home.html", {'formset': formset})
