import requests

city = 'Moscow,RU'
appid = 'fb800fc292600e3463ff0a5af2a3cdd1'


res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print('Скорость ветра: ', data['wind']['speed'])
print('Видимость: ', data['visibility'])
print('__________________________________________________')

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <",
          i['wind']['speed'], "> \r\nВидимость <",
          i['visibility'], ">")
    print("____________________________")


