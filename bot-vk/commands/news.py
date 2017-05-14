import command_system
import urllib.request
import json

#api = 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=a389c8803ac240358459977bfa30389f'


def data_fetch(api):
    url = urllib.request.urlopen(api)
    output = url.read().decode('utf-8')
    api_dict = json.loads(output)
    url.close()
    return api_dict


def data_organizer(api_dict):
    data = dict(
        articles=api_dict.get('articles'),
    )
    return data



def news():
    message = ''
    data = data_organizer(data_fetch('https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=a389c8803ac240358459977bfa30389f'))
    for article in data['articles']:
        message += 'Заголовок: {}. \nОписание: {}. \nСсылка: {}\n---------------\n'.format(article['title'], article['description'], article['url'])
    return message, ''

news_command = command_system.Command()

news_command.keys = ['новости', 'покажи новости', 'news']
news_command.desciption = 'Актуальные новости'
news_command.process = news