from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
# from .models import User
from .models import Restaurant



def restaurantAPI(request):
    # solve the error


    # 前段GET请求给的数据形式应该为
    # genre = [yakitori, fastfood, ...]
    # mode = 'ONI'
    # userId = '2123dasx'
    if request.method == 'GET':
        genre = []
        genre = request.GET.get('genre')
        mode = request.GET.get('mode')
    restaurantWeNeed = selectDB(genre, mode)
    data = restaurantWeNeed.object.all()
    # data 里储存被推荐算法筛选过的数据。data[0] = [{genre: }{place_id}{}{}]
    # restaurant:[{key, value}, {key, value},....]
    # {palceId : [name, genre]}
    # total_number:[the number of restaurant]
    # results: xxxx request.result

    restaurant = []

    for i in data:
        params = {
            'place_id': i.place_id,
            'name': i.name,
            'genre': i.genre,
        }
        restaurant.append(params)
        if len(restaurant) == 20:
            break

    json_str = json.dumps(restaurant, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

# Choose right tables of restaurant.db
def selectDB(genre, mode):
    data = Restaurant.object.all()