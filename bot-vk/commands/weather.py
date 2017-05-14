import datetime
import json
import urllib.request
import command_system
import vkapi
def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%H:%M')
    return converted_time


def url_builder():
    key = 'a5d0bd00ccd711bc11a24043988bdda0'
    unit = 'metric'  # Имперические или Метрические е.и.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='
    city_id = 703448    # id Kiev
    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + key
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        dt=time_converter(raw_api_dict.get('dt')),
    )
    return data


def weather():
    data = data_organizer(data_fetch(url_builder()))
    if 0 <= int(data['temp']) <= 10:
        comment = 'Сегодня прохладненько, одевайся теплее.'
    elif int(data['temp']) <= 15:
        comment = 'Уже похоже на весну, но кофта лишней не будет.'
    elif int(data['temp']) <= 22:
        comment = 'Настоящий май! Ветровка на футболку и порядок.'
    elif int(data['temp']) >= 23:
        comment = 'Это лето! Одевай футболку и очки'
    else:
        comment = 'Холод собачий! Укутывайся как на север'
    if data['temp_min'] == data['temp_max']:
        message = '{} Сейчас в Киеве {} °C. Погода - {}'.format(comment, data['temp'], data['sky'])
    else:
        message = '{} Сейчас в Киеве {} °C, и температура колеблется от {} до {}. Погода - {}'.format(comment, data['temp'], data['temp_min'],
                                                                    data['temp_max'], data['sky'])
    return message, ''

weather_command = command_system.Command()

weather_command.keys = ['погода', 'покажи погоду']
weather_command.description = 'Покажу погоду'
weather_command.process = weather


def sunset():
    data = data_organizer(data_fetch(url_builder()))
    attachment = ''
    sunset_time = datetime.datetime.strptime(data['sunset'], '%H:%M')

    now_time = datetime.datetime.strptime(datetime.datetime.today().strftime('%H:%M'), '%H:%M')
    if now_time < sunset_time:
        my_sunset = datetime.timedelta(hours=3)
        finaly_sunset = datetime.datetime.strptime((str(sunset_time+my_sunset).split()[1][:-3]), '%H:%M')
        message = 'Сегодня закат в Киеве будет в {}'.format(str(finaly_sunset).split()[1][:-3])
        attachment = vkapi.get_random_wall_picture(-134904756)
    else:
        message = 'Закат уже был. Спроси завтра.'
    return message, attachment

sunset_command = command_system.Command()

sunset_command.keys = ['закат', 'когда закат', 'покажи закат']
sunset_command.description = 'Покажу время заката'
sunset_command.process = sunset
