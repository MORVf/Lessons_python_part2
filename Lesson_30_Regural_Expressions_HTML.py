"""Текст задания.

Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и 
вывести список сайтов, на которые есть ссылка.
Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это 
последовательность символов, которая следует сразу после символов протокола, если он есть, до 
символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.
Сайты следует выводить в алфавитном порядке.

Пример HTML файла:
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import re

import requests

SUB_STRING = r'\ba\b.*\bhref=["\'](\.*)(\w+://)?([\w\d\.-]*)'
set_unique_urls = set()
list_urls_out = []

url = input().rstrip()
res = requests.get(url)
all_matches = re.findall(SUB_STRING, res.text)  # находим все совпадения с регулярным выражением

try:
    for index, elem in enumerate(all_matches):
        url_temp = all_matches[index][2]  # собираем все ссылки из 3-ей группы
        set_unique_urls.add(url_temp)
except IndexError:
    pass

for link in set_unique_urls:
    if link != '':
        list_urls_out += [link]

for url_out in sorted(list_urls_out):
    print(url_out)
