from django.db import models

# Create your models here.
# Model for Learning Journey
class LearningJourney(models.Model):
    school_history = models.TextField()
    current_status = models.CharField(max_length=255)

    def __str__(self):
        return "My Learning Journey"
# Model for About Me
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    favorite_song = models.CharField(max_length=100)

    def __str__(self):
        return self.name