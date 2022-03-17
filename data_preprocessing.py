import pandas as pd

class Preprocessing:
    def prepare_data(file_name):
        file_name = 'weather.xls'
        data = pd.read_excel(file_name, skiprows=6)
        data = data[data['T'].notna()]
        data['date'] = pd.to_datetime(data['Местное время в Москве (ВДНХ)'], dayfirst=True)
        data_short = data[data['date'].between('2016-10-01', '2017-03-01')]

        data['dayofyear'] = data['date'].dt.dayofyear
        
        return data

# print(data.head())