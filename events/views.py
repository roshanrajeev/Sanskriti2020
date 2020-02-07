from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views.generic.detail import DetailView
from django.views import generic


# Create your views here.

a = '''class detailview(generic.DetailView):
	events=Event.objects.all()
	model = Event
	template_name='./templates/eventsdetail.html'
	context_object_name= 'events'
	local_context={'events':events}
	
	def get_queryset(self):
		qs = super(detailview, self).get_queryset()
		return qs.filter(pk=self.kwargs['pk'])'''


def EventView(request):
	events = Event.objects.all()
	return render(request, 'events.html', {'events':events})

def detailview(request, pk):
	events = get_object_or_404(Event,id=pk)
	return render(request,'eventsdetail.html',{'events':events})


def home(request):
	return render(request,'home.html')

def aranguview(request):
	return render(request,'arangu.html')

def interview(request):
	return render(request, 'inter.html')

def filmfestview(request):
	return render(request, 'filmfest.html')