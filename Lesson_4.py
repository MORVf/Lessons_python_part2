'''
'''

n = int(input())

namespaces = {'global': []}

def create(namespace, parent):
    namespaces[parent] += [namespace]
    namespaces[namespace] = []

def add(namespace, var):
    namespaces[namespace] += [var]

def get(namespace, var):
    if var in namespaces[namespace]:
        return print(namespace)
    elif namespace != 'global':
        for key in namespaces.keys():
            for value in namespaces[key]:
                if value == namespace:
                    get(key, var)
    else:
        return print('None')

for i in range(n):
    command = input().split()
    if command[0] == 'create':
        create(command[1], command[2])
    elif command[0] == 'add':
        add(command[1], command[2])
    else:
        get(command[1], command[2])
