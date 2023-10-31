from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PeopleForm
from .models import People
from django.views.generic import ListView, CreateView

# Create your views here.
class ListPeople(ListView):
    model = People
    template_name = 'people.html'
    context_object_name = 'people'
    
class CreatePerson(CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'create_person.html'
    success_url = reverse_lazy('people')