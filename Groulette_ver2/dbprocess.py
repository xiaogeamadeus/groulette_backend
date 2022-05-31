from restaurantapiApp.models import Restaurant
import pickle


with open('restaurant.pkl', 'rb') as f:
    l = pickle.load(f)

# insert new record into the db
'''
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
'''

with open('score.pkl', 'rb') as f2:
    score = pickle.load(f2)

# update score data of the restaurant
for id, s in score.items():
    mise = Restaurant.objects.get(pk = id)
    mise.score = s
    mise.save()

# execute the following command in terminal
# manage.py shell
# >>> exec(open('myscript.py').read())

