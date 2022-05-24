# Author: Tianchen Wang
# Database of Restaurant.
# SQLite & Python 3.7

import json
import urllib.request
import sqlite3
from os import path

stocks = ['AAPL', "MSFT"]

restaurant = sqlite3.connect('Restaurant.db')
c = restaurant.cursor()
print("Database Open Successful")

for stock in stocks:

    url = "https://financialmodelingprep.com/api/v3/historical-price-full/" + stock
    data = urllib.request.urlopen(url).read().decode()

    obj = json.loads(data)

    for child in obj['historical']:
        print(child)

        c.execute("Insert into StockPrices values (?, ?, ?, ?, ?, ?, ?)",
                       (child['date'], child['close'], child['high'], child['low'],
                       child['open'], child['volume'], stock))
        restaurant.commit()

## A case of json from the google map API
# "business_status" : "OPERATIONAL",
#          "geometry" : {
#             "location" : {
#                "lat" : 35.0289888,
#                "lng" : 135.7785215
#             },
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 35.03038317989272,
#                   "lng" : 135.7798834798927
#                },
#                "southwest" : {
#                   "lat" : 35.02768352010728,
#                   "lng" : 135.7771838201072
#                }
#             }
#          },
#          "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
#          "icon_background_color" : "#FF9E67",
#          "icon_mask_base_uri" : "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
#          "name" : "マクドナルド 百万遍店",
#          "opening_hours" : {
#             "open_now" : true
#          },
#          "photos" : [
#             {
#                "height" : 3464,
#                "html_attributions" : [
#                   "\u003ca href=\"https://maps.google.com/maps/contrib/117294368366339487001\"\u003eA Google User\u003c/a\u003e"
#                ],
#                "photo_reference" : "Aap_uEC_IrQAy_Tpx3PlE21xhVtG3DqntXNdCMmt2tOb7iIPktCx4NAFAoMvOD66tNp3JdxAvd7EyC-24WPsjfH9YBNcgV5ZU9i8ewoyPlVZ25U8osYXCBQyIS1Po2ANm0btJVRPYy87BrIYNAePzWXNdNLJFGCsAwMeOIMepP7YS0821KTL",
#                "width" : 4618
#             }
#          ],
#          "place_id" : "ChIJBQ7HhlkIAWARfaBSnTD5oCA",
#          "plus_code" : {
#             "compound_code" : "2QHH+HC 京都市、京都府",
#             "global_code" : "8Q7Q2QHH+HC"
#          },
#          "price_level" : 2,
#          "rating" : 3.5,
#          "reference" : "ChIJBQ7HhlkIAWARfaBSnTD5oCA",
#          "scope" : "GOOGLE",
#          "types" : [
#             "cafe",
#             "restaurant",
#             "food",
#             "point_of_interest",
#             "store",
#             "establishment"
#          ],
#          "user_ratings_total" : 509,
#          "vicinity" : "京都市左京区吉田泉殿町１"
#       },