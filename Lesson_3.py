'''
Cочетанием из n элементов по k называется подмножество этих n элементов размера k.
Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

Пример:
Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
Различных сочетаний три, поэтому C(3, 2) = 3.

Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k)

Sample Input:
10 5

Sample Output:
252
'''

n, k = map(int, input().split())  #считываем строку и переводим в числа

def c(n, k):  #объявление функции с аргументами 
    summa = 0   #счетчик числа сочетаний
    if k == 0:  #c(n, 0) = 1, т.к. из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать
        summa += 1
    elif k > n: #если k > n, то c(n, k) = 0, так как невозможно, к примеру, из трех элементов выбрать пять
        summa = 0
    else: #в остальных случаях
        summa += c(n - 1, k) + c(n - 1, k - 1) #пользуемся рекурентной формулой
    return summa  #возвращаем число сочетаний

print(c(n, k))   #выводим число сочетаний
