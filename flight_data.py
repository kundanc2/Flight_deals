import requests
from pprint import pprint


GET_ENDPOINT = "https://api.sheety.co/07617da20edaa9539d58ff4962ff184e/flightDeals/prices"

class FlightData:
    #This class is responsible for structuring the flight data.
    def getiing(self,endpoint):
        self.response=requests.get(url=endpoint)
        pprint(self.response.json())

