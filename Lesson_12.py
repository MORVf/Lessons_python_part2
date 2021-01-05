'''
В первой строке дано три числа, соответствующие некоторой дате date - год, месяц и день.
Во второй строке дано одно число days - число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Sample Input 1:
2016 4 20
14
Sample Output 1:
2016 5 4

Sample Input 2:
2016 2 20
9
Sample Output 2:
2016 2 29

Sample Input 3:
2015 12 31
1
Sample Output 3:
2016 1 1
'''

import datetime

date = input().split()  # считываем дату(гггг мм дд)
days = int(input())  # считываем сдвиг в днях

d = datetime.date(int(date[0]), int(date[1]), int(date[2])) + datetime.timedelta(days=days)  # вычисляем дату с учетом указанных дней
print(d.year, d.month, d.day)  # выводим атрибуты год, месяц и день из объекта d класса datetime
