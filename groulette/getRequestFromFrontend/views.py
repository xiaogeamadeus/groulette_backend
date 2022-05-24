import sqlite3
from sqlite3 import Error
from django.http import HttpResponse
import json
from .models import User


# class UserViewSet():
#     conn = sqlite3.connect('/Users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend/groulette/Groulette.db')
#     cursor = conn.cursor()



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
#


#
def restaurantAPI(request, ):
    conn = sqlite3.connect(
        '/Users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend/groulette/Groulette.db')
    cursor = conn.cursor()

    # restaurant:[{key, value}, {key, value},....]
    # key = restaurant name || value = genre
    # total_number:[the number of restaurant]
    params = {
        'restaurant':,
        'total_number':,
    }

    json_str = json.dumps(params, ensure_ascii=False, indent=2)