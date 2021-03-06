'''
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. 
Выведите количество различных объектов в этом списке.
'''

objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]] #список на входе

set_with_elements = set() #множество для уникальных элементов

for obj in objects: #пробегаем все элементы списка 
    set_with_elements.add(id(obj))   #добавляем идентификатор каждого объекта в множество

print(len(set_with_elements))   #считаем длину множества
