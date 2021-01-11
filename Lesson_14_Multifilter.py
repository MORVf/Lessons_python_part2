'''
Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента a и f – последовательность 
и функцию, и позволяет проитерироваться только по таким элементам x из последовательности a, что f(x) равно True. Будем говорить, что в этом 
случае функция f допускает элемент x, а элемент x является допущенным.
В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный класс filter, но будет 
использовать не одну функцию, а несколько.
Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько не допускают. Обозначим эти 
количества за pos и neg.
Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает True, если элемент допущен, 
и False иначе.
'''

# функция тестовая, возвращающая True, если цифра делится на 2 без остатка
def mul2(x):
    if x % 2 == 0:
        return True
    else:
        return False


# функция тестовая, возвращающая True, если цифра делится на 3 без остатка
def mul3(x):
    if x % 3 == 0:
        return True
    else:
        return False


# функция тестовая, возвращающая True, если цифра делится на 5 без остатка
def mul5(x):
    if x % 5 == 0:
        return True
    else:
        return False


# класс фильтрации элементов последовательности, удовлетворяющих условиям указанных функций
class MultiFilter:
    def judge_half(pos, neg):  # допускает элемент, если его допускает хотя бы половина фукнций
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):  # допускает элемент, если его допускает хотя бы одна функция
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):  # допускает элемент, если его допускают все функции
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # исходная последовательность
        self.funcs = funcs  # допускающие функции
        self.judge = judge  # решающая функция

    def __iter__(self):  # итерирующая функция
        for itr in self.iterable:  # пробегаем все элементы списка
            pos = 0  # счетчик количества функций, которые допускают элемент
            neg = 0  # счетчик количества функций, которые не допускают элемент
            for func in self.funcs:  # пробегаем все функции
                if func(itr) is True:  # если функция допускает элемент
                    pos += 1  # увеличиваем первый счетчик
                else:  # если не допускает
                    neg += 1  # увеличиваем второй счетчик

            if self.judge(pos, neg) is True:  # вызываем решающую функцию
                yield itr  # генерируем элемент выходной последовательности

# тесты
a = [i for i in range(31)]

print(list(MultiFilter(a, mul2, mul3, mul5)))
print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_any)))
print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_half)))
print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_all)))
