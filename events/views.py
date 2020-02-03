from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views.generic.detail import DetailView


# Create your views here.

def EventView(request):
	event = Event.objects.all()
	return HttpResponse(request,event)


#lass EventView(DetailView):

  #  model = Event
#
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
     #   context['now'] = timezone.now()
      #  return context

