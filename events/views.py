from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views.generic.detail import DetailView


# Create your views here.

def EventView(request):
	events = Event.objects.all()
	return render(request, 'events.html', {'events':events})

def detailview(request, pk):
	events = get_object_or_404(Event,id=pk)
	return render(request,'eventsdetail.html',{'events':events})


def home(request):
	return render(request,'home.html')