"""Текст задания.

Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
Антон написал код, который выглядит следующим образом:
try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как 
ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите 
ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений 
можно удалить из кода. Типы исключений не созданы, создавать классы исключений также не требуется.
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы 
уже ранее где-то поймали их предка.

Формат входных данных:
В первой строке входных данных содержится целое число n - число классов исключений.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется 
i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется 
сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных:
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом 
поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

dict_classes = {}
temp_lst_exceptions = []  # список для хранения исключений, которые необходимо проверить на нужность 
lst_with_fail_exceptions = []  # список исключений, которые были выброшены из-за ненужности


def is_useless_exception(error):
    """Функция проверки нужности исключения.
    
    Аргумент:
    error - исключение, которое необходимо проверить
    
    Функция возвращает None.
    
    """
    global is_root_exception
    global lst_with_fail_exceptions
    for parent in dict_classes:
        if error in dict_classes[parent]:  # если нашли такой ключ, у которого значение == исключению
            if parent in temp_lst_exceptions:  # если ключ-исключение присутствует в списке на проверку
                # если индекс предка меньше индекса исключения
                if temp_lst_exceptions.index(parent) < temp_lst_exceptions.index(is_root_exception):
                    if is_root_exception not in lst_with_fail_exceptions:  # если исключение ещё не помечено как ненужное
                        lst_with_fail_exceptions += [is_root_exception]  # то добавляем его в список ненужных
                        print(is_root_exception)
            else:
                is_useless_exception(parent)  # вызываем рекурсивно функцию проверки нужности исключения по саб-классу


def add_subclass_in_parent():
    """Функция добавления исключений.
    
    Аргументы отсутствуют, возвращает None.
    
    """
    for ind_cls in range(2, len(lst_cls)):  # пробегаем все элементы входящего списка после ":"
        if lst_cls[ind_cls] not in dict_classes:
            dict_classes[lst_cls[ind_cls]] = []
        for key in dict_classes.keys():
            if key == lst_cls[ind_cls]:  # при совпадении ключа-родителя с элементом списка
                dict_classes[key] += [lst_cls[0]]  # добавляем к родителю нового наследника

 
n = int(input())
      
for i in range(n):
    lst_cls = input().split()
    if lst_cls[0] not in dict_classes:
        dict_classes[lst_cls[0]] = []

    if ':' in lst_cls:
        add_subclass_in_parent()

m = int(input())

for j in range(m):
    str_exception = input()
    if str_exception not in lst_with_fail_exceptions:  # если исключения ещё нет в списке ненужных
        # если исключения нет в словаре наследований или исключение уже использовалось
        if str_exception not in dict_classes or str_exception in temp_lst_exceptions:
            lst_with_fail_exceptions += [str_exception]
            print(str_exception)
        else:
            temp_lst_exceptions += [str_exception]  # добавляем его в список, требующий проверки на нужность
            if len(temp_lst_exceptions) > 1:
                is_root_exception = str_exception  # запоминаем первичное входящее исключение
                is_useless_exception(str_exception)  # вызываем функцию проверки
