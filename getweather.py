# import function from library
import requests,json, datetime, csv
import numpy as np
import pandas as pd
import os

# indentify location by PATH
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TARGET_DIR_PATH = os.path.join(CURR_DIR_PATH + "")

# create function and use API from weather_url
def get_weather(city):
    api_key = "8c28834273d1c5b639e0f53eef0da3a2"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    # use JSON to get data
    response = requests.get(complete_url)
    x = response.json()
    # use datetime to indentify local date
    time = datetime.datetime.now()
    t = time.strftime("%x")
    y = x["main"]
    # get temperature and convert from kelvin to celsius
    temp = y["temp"] - 273.15
    # float must be 2 decimal numbers
    current_temperature = '%.2f' % temp
    # air pressure
    current_pressure = y["pressure"]
    # air humility
    current_humidity = y["humidity"]
    z = x["weather"]
    # weather detail
    weather_description = z[0]["description"]
    # sum up any values
    result = city, str(t), str(current_temperature) , str(current_pressure) , str(current_humidity) , str(weather_description)
    return list(result)

#insert city
city1 = get_weather("Stockholm")

city2 = get_weather("London")

city3 = get_weather("Madrid")

city4 = get_weather("Rom")

city5 = get_weather("Cairo")

# create function to convert rows and columns by numpy and create dataframe
def convert(insert):
    arr = np.array(insert)
    arr = arr.reshape(1,6)
    df = pd.DataFrame(arr, columns=["city", "date", "temperature", "pressure", "humidity", "weather_description"])
    return df

#insert values
get1 = convert(city1)

get2 = convert(city2)

get3 = convert(city3)

get4 = convert(city4)

get5 = convert(city5)

#concate concatenate many dataframes to one dataframe

con = pd.concat([get1, get2, get3, get4, get5], axis=0)
print(con)

#export pandas dataframe to csv file.

con.to_csv(TARGET_DIR_PATH + "/zip/weather.csv")
con.to_csv("weather.csv")

#convert from csv file to json file by creating function

def convert_file(csvfile,jsonfile):
    #data = []
    data = {}
    with open(csvfile, encoding='utf-8') as csvf:
        csvread = csv.DictReader(csvf)
        for rows in csvread:
            #data.append(rows)
            key = rows['city']
            data[key] = rows

    with open(jsonfile, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)

csvfile = r'weather.csv'
jsonfile = r'weather.json'

convert_file(csvfile,jsonfile)









