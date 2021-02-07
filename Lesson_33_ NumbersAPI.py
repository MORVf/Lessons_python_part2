"""Текст задания.

В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный 
математический факт об этом числе.
Для каждого числа выведите Interesting, если для числа существует интересный факт, и 
Boring иначе. Выводите информацию об интересности чисел в таком же порядке, в каком следуют 
числа во входном файле.

Пример входного файла:
31
999
1024
502
Пример выходного файла:
Interesting
Boring
Interesting
Boring

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import os

import requests

FILE_IN = os.path.join('C:\\', 'Documents', 'dataset_24476_3.txt')
BASE_URL = 'http://numbersapi.com/{}/math'

params = {
    'json': True
}

with open(FILE_IN, 'r') as f_in:
    for number in f_in:
        number = int(number.strip())
        res = requests.get(BASE_URL.format(number), params=params)
        if res.json()['found']:
            print('Interesting')
        else:
            print('Boring')
