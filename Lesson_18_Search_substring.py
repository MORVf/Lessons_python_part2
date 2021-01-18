'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.

Sample Input 1:
abababa
aba
Sample Output 1:
3

Sample Input 2:
abababa
abc
Sample Output 2:
0

Sample Input 3:
abc
abc
Sample Output 3:
1

Sample Input 4:
aaaaa
a
Sample Output 4:
5
'''

s = input()
t = input()
count = 0

if t not in s:  # если подстроки не найдено, то сразу возвращаем 0
    print(count)
else:
    for i in range(len(s) + 1 - len(t)):  # пробегаем всю строку до тех пор, пока хватает символов в конце
        if s[i:len(t) + i:].find(t) != -1:  # и считываем все совпадения с подстрокой в исходной строке, сдвигая индекс вправо
            count += 1
    print(count)
