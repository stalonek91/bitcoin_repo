import pandas as pd
import logging

class DataFrameProcessor:

    def __init__(self) -> None:
        raise NotImplementedError
    
    def create_df(self, data: list) -> pd.DataFrame:

        flattened_data = []
        for item in data:
            for symbol, details in item.items():
                details['symbol'] = symbol
                flattened_data.append(details)

        
        return pd.DataFrame(flattened_data)