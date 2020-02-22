from django.shortcuts import render
#from core.models import Person

def home(request):
    people = Person.objects.all()
    return render(request, "home.html", {"people": people})