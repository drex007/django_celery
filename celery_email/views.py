from django.shortcuts import render
from time import sleep
from .tasks import birthday_message
from django.http import HttpResponse
# Create your views here.
def index(request):
    # birthday_message.delay()
    return HttpResponse('<h1>EMAIL IS SENT AGAIN<h1/>')