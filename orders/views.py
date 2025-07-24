from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def place_order(request):
    current_user = request.user

    # if the cart count is less than or equal to 0, then redirect back to shop 
    