import requests

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
# print(coins_data[0])
print(type(coins_data))


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
my_dict = {}

# {'symbol': 'BTC', 'name': 'Bitcoin', 'price': '63005.54907812025', 'change': '-2.33'}

new_key = None
key_to_remove = None

for k, v in filtered_coins[0].copy().items():
    if v == 'BTC':
        new_key = v
        print(f'new_key: {new_key}')
        key_to_remove = k
        print(f'key_to_remove: {key_to_remove}')
        break

if new_key:
    del filtered_coins[0][key_to_remove]

new_dict = {new_key: filtered_coins[0]}

for k,v in new_dict.items():
    print(k, v)
    
    


