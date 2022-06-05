from django.db import models

# Create your models here.
class Restaurant(models.Model):
    genre = models.IntegerField()
    rating = models.FloatField()
    user_ratings_total = models.IntegerField()
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100, primary_key=True)
    vicinity = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    # add score
    score = models.FloatField(default='0')

    def __str__(self):
        return str(self.genre) + '-' + self.name + '-' + self.place_id


class User(models.Model):
    user_id = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=60)
    def __str__(self):
        return self.user_id



