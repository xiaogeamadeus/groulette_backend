# Author: Tianchen Wang
# Backend of groulette app
# Google Maps APIs and Python 3.7

import googlemaps
import responses

class PlaceTest:

    def setUp(self):
        self.key = "mykey"
        self.client = googlemaps.Client(self.key)
        # The location of Kyoto University Yoshidahonmachi
        self.location = (35.026416, 135.780920)
        self.language = "ja"
        self.keyword = "chinese"
        self.type = "restaurant"
        self.radius = 1000

    @responses.activate
    def places_nearby_search(self):
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        responses.add(
            responses.GET,
            url,
            body='{"status": "OK", "results": [], "html_attributions": []}',
            status=200,
            content_type="application/json",
        )

        self.client.places_nearby(
            location=self.location,
            keyword=self.keyword,
            language=self.language,
            min_price=0,
            max_price=4,
            radius=self.radius,
            open_now=True,
            type=self.type,
        )

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            "%s?keyword=chinese&language=ja&location=35.026416%%2C135.780920&"
            "maxprice=4&minprice=0&opennow=true&radius=1000&"
            "type=restaurant&key=%s" % (url, self.key),
            responses.calls[0].request.url,
        )

        # Exception Handling
        with self.assertRaises(ValueError):
            self.client.places_nearby(radius=self.radius)
        with self.assertRaises(ValueError):
            self.client.places_nearby(self.location)

        with self.assertRaises(ValueError):
            self.client.places_nearby(
                location=self.location,
                keyword="restaurant",
                radius=self.radius,
            )
