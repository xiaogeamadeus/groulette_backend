# Author: Tianchen Wang
# Get the details of restaurant.
# SQLite & Python 3.7

import json
import requests

def txt2list(filename):
    """txt2list _summary_
    txtファイル内のplace_idをlistとして読み込み
    Args:
        filename (String): ファイル名
    Returns:
        List: place_idのlist
    """
    with open(filename, 'r') as f:
        data = f.read()
        data2list = data.split('\n')
        return data2list

class getRestaurantDetail:
    miseName = ["Chinese1","Chinese2","Ramen","Fast","Pasta","Italian","Humberger","Gyudon","Syokudo","Teishoku","Family",
                "Udon","Noodles","Franch","Asian","Korean","Pizza","Yakiniku","Pizza","Tempura","cafe","Health",
                "Vegan","Yakitori", "Izakaya","Sushi"]
    API_KEY = "AIzaSyCh7xnktNn-nWh_KlNh_VP8rg8DITmqL9Q"
    payload = {}
    headers = {}

    for i in miseName:
      placeIds = txt2list(f"/users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend/restaurantPlaceid/{i}.txt")

      for id in placeIds:
          url = "https://maps.googleapis.com/maps/api/place/details/json?" \
              f"place_id={id}&language=ja&" \
              f"key={API_KEY}"

          response = requests.request("GET", url, headers=headers, data=payload)
          f = open(f"/users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend/restaurantPlaceDetail/{i}.json",
             mode='a+')
          num = f.write(response.text)

    f.close()
