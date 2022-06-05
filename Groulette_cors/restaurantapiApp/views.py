from django.shortcuts import render
from django.http import HttpResponse
import json
# from .models import User
from .models import Restaurant
from django.db.models import Q

def restaurantAPI(request):
    # 前段GET请求给的数据形式应该为
    # genre = [0, 1, 2, ...]
    # mode = 'ONI'
    # userId = '2123dasx'
    if request.method == 'GET':
        genre = []
        genre = request.GET.get('genre')
        mode = request.GET.get('mode')
        if mode == 'oni':
            data = oniMode(genre)
        elif mode == 'kami':
            data = kamiMode(genre)

        else:
            data = normalMode(genre)

        # data 里储存被推荐算法筛选过的数据。每个data 代表一个餐馆。data[0] = [{genre: }{place_id: }{score: }{}]
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
        # [{place_id: 'xsd', name: '', genre : 0}, {place_id: 'xsxsd', name: '1232', genre : 1}, {}, {}]
        json_str = json.dumps(restaurant, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)



# recommend algorithm : oni mode
def oniMode(genreValue):
    data = Restaurant.objects.none()
    for i in genreValue:
        data = data | Restaurant.objects.filter(Q(genre=i))
    data = data.order_by('score')

    if data.count() > 20:
        res = data[:20]
    else:
        res = data

    return res


# recommend algorithm : kami mode
def kamiMode(genreValue):
    data = Restaurant.objects.none()
    for i in genreValue:
        data = data | Restaurant.objects.filter(Q(genre=i))
    data = data.order_by('-score')

    if data.count() > 20:
        res = data[:20]
    else:
        res = data

    return res


# recommend algorithm : normal mode
def normalMode(genreValue):
    data = Restaurant.objects.none()
    for i in genreValue:
        data = data | Restaurant.objects.filter(Q(genre=i))
    data = data.order_by('score')

    num_data = data.count()

    if num_data > 20:
        res = data.order_by('?')[:20]
    else:
        res = data

    return res

# place_id -> google map API -> restaurant link
def getRouteLinkAPI(request):
    if request.method == 'GET':
        place_id = request.GET.get('place_id')

        routeLink = f'https://www.google.com/maps/place/?q=place_id:{place_id}'
        json_str = json.dumps(routeLink, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)