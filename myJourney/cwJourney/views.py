from django.shortcuts import render
from .models import LearningJourney, AboutMe
# Create your views here.
# Home page view
def index(request):
    journey = LearningJourney.objects.first()  # get the first entry
    return render(request, 'index.html', {'journey': journey})

# About Me page view
def about_me(request):
    about = AboutMe.objects.first()  # get the first entry
    return render(request, 'aboutMe.html', {'about': about})