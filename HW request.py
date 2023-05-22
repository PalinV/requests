import requests
import os
from pprint import pprint
import json

url_heroes = 'https://akabab.github.io/superhero-api/api//all.json'
response = requests.get(url_heroes)
data_json = response.json()
heroes_intelligence = {}
heroes_name = ['Hulk', 'Captain America', 'Thanos']
for name_hero in data_json:
    if name_hero['name'] in  heroes_name:
       heroes_intelligence[name_hero['name']] = name_hero['powerstats']['intelligence']
best_mind = 0
for name, mind in heroes_intelligence.items():
    if mind > best_mind:
        cleverest = name
        best_mind = mind
print(f'Самый умный супергерой - это {cleverest}!!! Его IQ {best_mind} )))!!!')


#===========================================================================================
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path" : file_path, "overwrite" : "true"}
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)
        }
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()
        href = response_data['href']
        response = requests.put(href, data=open(path_to_file, 'rb'))
        
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Укажите путь в исходному файлу')
    token = input('Укажите свой токен')
    uploader = YaUploader(token)
    result = uploader.upload("test.txt", path_to_file)
