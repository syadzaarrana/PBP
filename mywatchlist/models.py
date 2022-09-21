from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=11)
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.CharField(max_length=17)
    review = models.TextField()

    # Ratings & review from rottentomatoes.com (audience score & critics consensus)
