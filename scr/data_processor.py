from prettytable import PrettyTable
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DataProcessor:

    def __init__(self) -> None:

        self.needed_keys = ['symbol', 'name', 'price', 'change']
        logging.debug(f"DataProcessor initialized with keys: {self.needed_keys}")

    def iter_dict(self, response: dict, looked_key: str) -> dict:

        """Formateddata coming from json request response

        Args:
            response (dict): json formatted dict with all coins
            looked_key (str): value that can be passed in function to find coins

        Returns:
            dict: dictionaries with coins
        """
        logging.debug(f"Searching for key: {looked_key} in response")
        for key, value in response.items():
            if key == looked_key and isinstance(value, list):
                logging.debug(f"Found key {looked_key}, returning value")
                return value
            elif isinstance(value, dict):
                result = self.iter_dict(value, looked_key)
                if result is not None:
                    # print(f' Found result, returning result with type: {type(result)}')
                    return result
                
        logging.debug(f"Key {looked_key} not found in response")
        return None
                

    def get_values(self, coins_list: list) -> list:
        """_summary_

        Args:
            coins_list (list): list of coins that have been previously gathered from json file
            list_of_keys (list): keys that will be used to create andother dict with key values like price name etc

        Returns:
            list: list of dictionaires with all coins but with only key data
        """

        logging.debug("Filtering coins list with specified keys")
        coins_output = []
        for coin in coins_list:

            filtered_coin = {k: v for k, v in coin.items() if k in self.needed_keys}
            coins_output.append(filtered_coin)

        return coins_output
    
    def new_dict_creation(self, filtered_coins) -> list:

        """create new dictionary where coin is a main key

        Returns:
            _type_: list with dictionaries
        """
        logging.debug("Creating new dictionary where coin symbol is the key")
        new_list_with_dict = []
        
        for coin in filtered_coins:
            new_key = coin.pop('symbol', None)
            
            if new_key:
                my_dict = {}
                my_dict[new_key] = coin
                new_list_with_dict.append(my_dict)
        
        return new_list_with_dict
    
    def display_table(self, data: list) -> None:

        """
        this is a function that uses external library to display list of dictionaries
        in ascii format
        """

        logging.debug("Displaying data in a formatted table")
        table = PrettyTable()
        columns = ["Coin", "Name", "Value", "Change"]
        table.field_names = columns

        for entry in data:
            for key, sub_dict in entry.items():
                row = [key]
                row.extend(sub_dict.values())
                table.add_row(row)
        
        print(table)