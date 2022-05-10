import requests
import json

class getRestaurantJSON:
    #def setUp(self):
        #self.key = "AIzaSyCh7xnktNn-nWh_KlNh_VP8rg8DITmqL9Q"
        #self.client = googlemaps.Client(self.key)
        # The location of Kyoto University Yoshidahonmachi
        #self.location = (35.028810, 135.779259)
        #self.language = "ja"
        #self.keyword = "chinese"
        #self.type = "restaurant"
        #self.radius = 1000

    API_KEY = "AIzaSyCh7xnktNn-nWh_KlNh_VP8rg8DITmqL9Q"
    miseName = ["Chinese","Ramen","Fast","Pasta","Italian","Humberger","Gyudon","Syokudo","Teishoku","Family",
                "Udon","Noodles","Franch","Asian","Korean","Pizza","Yakiniku","Pizza","Tempura","cafe","Health",
                "Vegan","Yakitori", "Izakaya","Sushi"]

    nums = []
    for i in miseName:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&" \
          "language=ja&location=35.028810%2C135.779259&" \
          f"radius=1000&keyword={i}&type=restaurant&key={API_KEY}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        f = open(f"/users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend/restaurantData/{i}.txt", mode='a+')
        num = f.write(response.text)
        dictionary = json.loads(response.text)
        nums.append(len(dictionary['results']))


    print(nums)
    f.close()
    # f = open("/users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend_django/.txt", mode='w')
    # num = f.write(response.text)
    # print(num)
    # f.close()
    # send to front end
    # json
    #result:[
    #{name: kahuugenn, location; 19.23445, 110.33333, tel: 070xxxx, rating: 3.8, url},
    #{name: kasyou, location: 8393, tel: 080xxxxx},
    #{name: xxxxx, loca},

    #HTTPS request(POST) header
    #....,

    # ]