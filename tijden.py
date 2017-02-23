import urllib.request
from bs4 import BeautifulSoup
import csv

# Получение html файла по url
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

# Основная функция парсинга
def parce(html):
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find('div', class_='tabs-content')
    news = []
    for ul in section.find_all('ul', class_='news'):
        for li in ul.find_all('li'):
            news.append({
                'title': li.a.text.replace("\t", ""),
                'time': li.span.text,
                'link': li.a.get('href')
            })
    return news

# Функция для сохранения новостей в формате csv
def save(news, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Заголовок', 'Время', 'Ссылка'))

        for new in news:
            writer.writerow((new['title'], new['time'], new['link']))


def main():
    for i in parce(get_html("http://tyzhden.ua/")):
        print(i)
    save(parce(get_html("http://tyzhden.ua/")), 'news.csv')

if __name__ == "__main__":
    main()