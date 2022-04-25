import requests

class requestToGooglemap:
    #def setUp(self):
        #self.key = "AIzaSyCh7xnktNn-nWh_KlNh_VP8rg8DITmqL9Q"
        #self.client = googlemaps.Client(self.key)
        # The location of Kyoto University Yoshidahonmachi
        #self.location = (35.026416, 135.780920)
        #self.language = "ja"
        #self.keyword = "chinese"
        #self.type = "restaurant"
        #self.radius = 1000

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=fastfood&" \
          "language=ja&location=35.026416%2C135.780920&maxprice=4&minprice=0&opennow=true&" \
          "radius=1000&type=restaurant&key=AIzaSyCh7xnktNn-nWh_KlNh_VP8rg8DITmqL9Q"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    response = requests.request("POST", url, headers=headers, data=payload)

    # send to front end
    # json
    #result:[
    #{name: kahuugenn, location; 19.23445, 110.33333, tel: 070xxxx, rating: 3.8, url},
    #{name: kasyou, location: 8393, tel: 080xxxxx},
    #{name: xxxxx, loca},

    #HTTPS request(POST) header
    #....,

    # ]