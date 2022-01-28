import requests
import datetime
from config import token
from pprint import pprint

def get_weather(city, token):
    code_to_pic = {
        "Clear": 'weather/static/weather/images/icons/67131.png'
    }

    r= requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={token}&units=metric"
    )
    data = r.json()
    pprint(data)

    gorod = data['name']
    tempVo = data['main']['temp']
    feel = data['main']['feels_like']
    press = data['main']['pressure']
    windS = data['wind']['speed']
    windD = data['wind']['deg']
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    pogoda = data['weather'][0]['main']
    right_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    length_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])


    if pogoda in code_to_pic:
        pg = code_to_pic[pogoda]
    else:
        pg = "ХуйняЯкась"


    print(right_now, pogoda, pg)

def main():
    get_weather("odesa", token)

if __name__ == '__main__':
    main()

