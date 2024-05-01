import requests
from prettytable import PrettyTable
import pandas as pd


url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}
headers = {
	"X-RapidAPI-Key": "1611593e5dmsh2d07beb1089ba76p1c12dfjsnf5da80c87b19",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
json_response = response.json()

def iter_dict(response: dict, looked_key: str) -> dict:
    """Formateddata coming from json request response

    Args:
        response (dict): json formatted dict with all coins
        looked_key (str): value that can be passed in function to find coins

    Returns:
        dict: dictionaries with coins
    """
    for key, value in response.items():
        # print(f'Current key: {key}')
        if key == looked_key and isinstance(value, list):
            # print(f' Found key, returning value')
            return value
        
        elif isinstance(value, dict):
            result = iter_dict(value, looked_key)
            if result is not None:
                # print(f' Found result, returning result with type: {type(result)}')
                return result
            

coins_data = iter_dict(json_response, 'coins')
needed_keys = ['symbol', 'name', 'price', 'change']


def get_values(coins_list: list, list_of_keys: list) -> list:
    """_summary_

    Args:
        coins_list (list): list of coins that have been previously gathered from json file
        list_of_keys (list): keys that will be used to create andother dict with key values like price name etc

    Returns:
        list: list of dictionaires with all coins but with only key data
    """
    coins_output = []

    for coin in coins_list:

        filtered_coin = {k: v for k, v in coin.items() if k in list_of_keys}
        coins_output.append(filtered_coin)

    return coins_output


filtered_coins = get_values(coins_data, needed_keys)
list_of_my_coins = ['BTC', 'DOGE', 'PEPE']


def new_dict_creation() -> list:

    """create new dictionary where coin is a main key

    Returns:
        _type_: list with dictionaries
    """

    new_list_with_dict = []
    
    for coin in filtered_coins:
        new_key = coin.pop('symbol', None)
        
        if new_key:
            my_dict = {}
            my_dict[new_key] = coin
            new_list_with_dict.append(my_dict)
    
    return new_list_with_dict


def display_table(data: list) -> None:

    """
    this is a function that uses external library to display list of dictionaries
    in ascii format
    """

    
    table = PrettyTable()
    columns = ["Coin", "Name", "Value", "Change"]
    table.field_names = columns

    for entry in data:
        for key, sub_dict in entry.items():
            row = [key]
            row.extend(sub_dict.values())
            table.add_row(row)
    
    print(table)



content_to_display = new_dict_creation()
display_table(content_to_display)




    


