from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views.generic.detail import DetailView


# Create your views here.

def EventView(request):
	events = Event.objects.all()
	return render(request, 'home.html', {'events':events})

def detailview(request):
	events = get_object_or_404(Event,id=event_id)
	return render(request,'eventsdetail.html',{'events':events})