'''
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.
В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное целое 
число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое число, число 
добавлялось бы как в стандартный list.
В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
Примечание:
Положительными считаются числа, строго большие нуля.
'''

class NonPositiveError(Exception):  # новый класс с кастомной ошибкой, отнаследованный от класса-предка 
    pass  # ничего не делаем


class PositiveList(list):  # класс, переопределяющий базовую логику встроенного класса list
    def append(self, x):
        if x > 0:  # если число положительное
            super(PositiveList, self).append(x)  # находим в предках нашего класса функцию append и применяем к объекту self
        else:  # иначе
            raise NonPositiveError("The number " + str(x) + " is not positive")  # выбрасываем кастомное исключение

'''
тесты
a = PositiveList()
a.append(8)
print(a)
a.append(5)
print(a)
a.append(-2)
print(a)
'''
