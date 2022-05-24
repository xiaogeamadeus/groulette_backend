from django.db import models

class Restaurant(models.Model):
    genre = models.IntegerField()
    place_id = models.CharField()
    rating = models.FloatField()
    user_ratings_total = models.IntegerField()
    name = models.CharField()
    vicinity = models.CharField()
    geometry_location = models.CharField()


class User(models.Model):
    user_id = models.CharField()
    restaurant_name = models.CharField()