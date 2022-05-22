import json
import os, glob, pickle


with open('groulette_backend/restaurantDB/restaurant.pkl', 'rb') as f:
    l = pickle.load(f)

print(l[0][0])
                

