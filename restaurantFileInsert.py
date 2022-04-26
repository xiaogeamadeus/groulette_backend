import json
import requests

class restaurantFileInsert:

    miseName = ["Chinese"]
    API_KEY = "AIzaSyCh7xnktNn-nWh_KlNh_VP8rg8DITmqL9Q"

    miseNum = []

    for i in miseName :
        f = open(f"/users/xiaogeamadeus/mypy/Practice_of_Information_System/groulette_backend/restaurantData/{i}.txt", mode='a+')
        payload = {}
        headers = {}
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&" \
              "language=ja&location=35.028810%2C135.779259&" \
              f"radius=1000&keyword={i}&type=restaurant&key={API_KEY}"

        response = requests.request("GET", url, headers=headers, data=payload)
        num = f.write(response.text)
        dictionary = json.loads(response.text)
        pageToken = dictionary['next_page_token']



        url1 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&" \
              "language=ja&location=35.028810%2C135.779259&" \
              f"radius=1000&keyword={i}&pagetoken={pageToken}&key={API_KEY}"

        response1 = requests.request("GET", url1, headers=headers, data=payload)
        num2 = f.write(response1.text)
        dictionary1 = json.loads(response1.text)
        misenum = len(dictionary['results']) + len(dictionary1['results'])
        miseNum.append(misenum)


        #jhhh222
    print(miseNum)
    f.close()