from django.shortcuts import render
from core.models import Tier

def home(request):
    tiers = Tier.objects.all()
    return render(request, "home.html", {"tiers": tiers})