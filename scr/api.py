import requests
import logging

class APIConnection():


    def __init__(self) -> None:


        self.url = "https://coinranking1.p.rapidapi.com/coins"
        self.querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}
        self.headers = {
	"X-RapidAPI-Key": "1611593e5dmsh2d07beb1089ba76p1c12dfjsnf5da80c87b19",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}
        
    def get_response(self) -> dict:
        """
        Makes a GET request to the specified API URL with headers and query parameters.

        Returns:
            dict: The JSON response from the API converted into a Python dictionary.
        """



        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        json_response = response.json()

        return json_response

        
        
    