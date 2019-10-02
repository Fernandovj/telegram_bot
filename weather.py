import requests
import json

token = "51147bd0a70d3c3330cb84b14dc4f786" 
url="http://api.openweathermap.org/data/2.5/weather?q=Campinas,br&APPID=51147bd0a70d3c3330cb84b14dc4f786"

def getWeather():
    #'chat_id': '787248960' Dani
    
    # data = {
    #     'id': '3467865',  
    #     'APPID': token
    # }

    response = requests.get(url)
    r = json.loads(response.text)


    return "The temperature is "+ str(format(r["main"]["temp"]-273.15,'.2f'))+" ºC with "+r["weather"][0]["description"]


#getWeather()