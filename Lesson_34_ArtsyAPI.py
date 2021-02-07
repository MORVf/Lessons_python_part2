"""Текст задачи.

В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый 
год рождения, выведите их имена в лексикографическом порядке.
В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import os

import requests

FILE_IN = os.path.join('C:\\', 'Documents', 'dataset_24476_4.txt')
FILE_OUT = os.path.join('C:\\', 'Documents', 'out.txt')
BASE_URL = 'https://api.artsy.net/api/artists/{}'
dict_artists_with_years = {}
years = []

headers = {
    'X-XAPP-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOi' \
                    'I2MDIwMDQ1NWNlNzE5MjAwMGVjY2JhYWYiLCJleHAiOjE2MTMzMTU3OTcsImlhdCI6M' \
                    'TYxMjcxMDk5NywiYXVkIjoiNjAyMDA0NTVjZTcxOTIwMDBlY2NiYWFmIiwiaXNzIjoi' \
                    'R3Jhdml0eSIsImp0aSI6IjYwMjAwNDU1YmEyZTQ5MDAxMWNmZTQ0NSJ9.diPwj7EpqA' \
                    'usFuCDl62OpRmND1M4mWmJFS00PVFtIp4'
}

with open(FILE_IN, 'r') as f_in:
    for id_artist in f_in:
        res = requests.get(BASE_URL.format(id_artist.strip()), headers=headers)
        birthday = int(res.json()['birthday'])
        artist_name = res.json()['sortable_name']
        if birthday not in dict_artists_with_years:
            dict_artists_with_years[birthday] = [artist_name]
        else:
            dict_artists_with_years[birthday] += [artist_name]

for year in dict_artists_with_years:
    years += [year]
years.sort()

with open(FILE_OUT, 'w', encoding='UTF-8') as f_out:
    for year in years:
        if len(dict_artists_with_years[year]) == 1:
            f_out.write(dict_artists_with_years[year][0] + '\n')
        else:
            dict_artists_with_years[year].sort()
            for name in dict_artists_with_years[year]:
                f_out.write(name + '\n')
