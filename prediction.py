import joblib
from api_weather import get_weather
import pandas as pd
from location import get_latitude_longitude

model = joblib.load('xgb_model.pkl')


def predict(city,item,pesticides):
   
    lat, lon = get_latitude_longitude(city)
    
    
    avg_temp,avg_rain = get_weather(lat,lon)
    item_hash = {'Cassava': 0,
                'Maize': 1,
                'Plantains and others': 2,
                'Potatoes': 3,
                'Rice, paddy': 4,
                'Sorghum': 5,
                'Soybeans': 6,
                'Sweet potatoes': 7,
                'Wheat': 8,
                'Yams': 9}
    
    item_encoded = item_hash[item]

    data = {
    "Country_Encoded": [42],
    "Item_Encoded": [item_encoded],
    "Pesticides": [pesticides],
    "Avg_Temp": [avg_temp/12],
    "Rainfall": [int(avg_rain/12)]
    }
    df = pd.DataFrame(data)

    predicted_value = model.predict(df)

    return int(predicted_value[0])
