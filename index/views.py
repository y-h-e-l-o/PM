from django.shortcuts import render
from .models import*
from django.template import loader

def index(request):
	paragraphes = Paragraphe.objects.all()
	alertes = Alerte.objects.all()
	contacts = Contact.objects.all()
	horaires = Horaire.objects.all()
	data = {'paragraphes' : paragraphes, 'alertes' : alertes, 'contacts': contacts, 'horaires': horaires }
	return render(request, 'index/index.html', data)