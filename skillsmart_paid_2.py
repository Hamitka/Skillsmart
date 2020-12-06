"""5. Задания
1. Проверьте по коду результата, что отправка данных с помощью POST на сервер httpbin.org пройдёт корректно.
2. Выберите для эксперимента произвольный сайт и распарсьте из него интересующие вас значения. """

import requests
from bs4 import BeautifulSoup

some_post = requests.post('http://httpbin.org/post', data={'UserId': '12345', 'Status': 'On'})
if some_post.status_code == 200:
    print('OK')
else:
    print('Some error %s' % (some_post.status_code,))



some_response = requests.get('https://yandex.ru/pogoda/ufa')
if some_response.status_code == 200:
    # print(some_response.text)
    # soup = BeautifulSoup(some_response.text, features="html5lib")
    soup = BeautifulSoup(some_response.text, features='html.parser')
    forecast_day_list = soup.find_all('div', {'class': 'forecast-briefly__name'})
    forecast_date_list = soup.find_all('time', {'class': 'forecast-briefly__date'})
    forecast_temp_day_list = soup.find_all('div', {'class': 'forecast-briefly__temp_day'})
    forecast_temp_nigth_list = soup.find_all('div', {'class': 'forecast-briefly__temp_night'})

forecast_list = zip(forecast_day_list,
                    forecast_date_list,
                    forecast_temp_day_list,
                    forecast_temp_nigth_list)
for forecast in forecast_list:
    for item in forecast:
        print(item.text, end=' ')
    print()
