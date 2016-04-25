from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def permit_sys1(request):
    return render(request, 'main2.1.html')