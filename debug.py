import json
import os, glob, pickle

# with open('groulette_backend/restaurantDB/restaurant.pkl', 'rb') as f:
#     l = pickle.load(f)

# print(l[0][0])
                

l = [
    {'name':'a', 'id':1, 'score':2.0},
    {'name':'b', 'id':2, 'score':10.0}
]

for record in l:
    print(record['name'])
    print(record['score'])
    print('================')