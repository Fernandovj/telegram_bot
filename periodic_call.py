import time
import bot
import weather

def foo():
    miweather = weather.getWeather()
    bot.sendMessage("Hi William, hour and date are:  "+time.ctime()+". "+miweather)
    print (time.ctime())

cont = 0

while cont < 10:
    foo()
    cont = cont + 1
    time.sleep(3600)