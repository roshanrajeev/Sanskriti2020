from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views.generic.detail import DetailView
from django.views import generic


# Create your views here.



def EventView(request):
	events = Event.objects.all()
	return render(request, 'events.html', {'events':events})

def detailview(request, slug):
	events = get_object_or_404(Event,slug=slug)
	return render(request,'eventsdetail.html',{'events':events})


def home(request):
	return render(request,'home/index.html')

def aranguview(request):
	events = Event.objects.filter(event_type='Arangu')
	return render(request,'arangu.html', {'events':events})

def interview(request):
	events = Event.objects.filter(event_type='Inter')
	return render(request,'inter.html', {'events':events})

def filmfestview(request):
	return render(request, 'filmfest.html')