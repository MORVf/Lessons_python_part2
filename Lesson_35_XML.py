"""Текст задания.

Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа 
имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под 
нижележащими кубиками, имеют ценность 3. И т. д. Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:
4 3 1

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'
__all__ = ['count_colors', 'colors']

from xml.etree import ElementTree

colors = {'red': 0, 'green': 0, 'blue': 0}


def count_colors(parent, level):
    """Функция подсчета суммы ценностей всех кубиков определенного цвета.

    Атрибуты:
    parent - текущий кубик-родитель
    level - текущий уровень вложенности родителя

    Функция не возвращает значений. Работает с методом ElementTree из модуля xml.etree.

    """
    level += 1
    for child in parent:
        colors[child.attrib['color']] += level
        count_colors(child, level)


if __name__ == '__main__':

    # schema_xml = input()
    schema_xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

    root = ElementTree.fromstring(schema_xml)
    colors[root.attrib['color']] = 1  # записываем ценность самого верхнего кубика

    count_colors(root, 1)

    print(f"{colors['red']} {colors['green']} {colors['blue']}")
