from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import RatingForm
from django.forms import formset_factory

from .models import Post
from django.utils import timezone

# def input_name(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         if name:
#             return HttpResponse(f"Hello, {name}! You've successfully entered your name.")
#         else:
#             return HttpResponse("Please enter a valid name.")
#
#     return render(request, 'pooldata/post_list.html')
# def return_data(request):
#     return HttpResponse('')

# def test_view(request):
#     return HttpResponse("This is a test view!")

def formset_view(request):
    RatingFormSet = formset_factory(RatingForm, extra = 5)
    if request.method == 'POST':
        formset = RatingFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
    else:
        formset = RatingFormSet()
    return render(request, "pooldata/home.html", {'formset': formset})
