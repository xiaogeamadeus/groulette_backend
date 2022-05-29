from restaurantapiApp.models import Restaurant
import pickle


with open('restaurant.pkl', 'rb') as f:
    l = pickle.load(f)

for genre in l:
    for record in genre:
        new_mise = Restaurant(
            genre=record['genre'], 
            rating=record['rating'], user_ratings_total=record['user_ratings_total'], 
            name=record['name'], 
            place_id=record['place_id'],
            vicinity=record['vicinity'], 
            location=record['location'])
        new_mise.save()

