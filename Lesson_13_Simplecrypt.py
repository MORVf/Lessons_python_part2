"""Текст задания.

Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять 
какой из паролей ему нужен. Помогите ему решить эту проблему.
Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей 
служит ключом для расшифровки файла с интересной информацией.
Ответом для данной задачи служит расшифрованная интересная информация Алисы.

"""

__all__ = ['ENCRYPTED_FILE', 'PASSWORDS']
__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import os

from simplecrypt import decrypt, DecryptionException

ENCRYPTED_FILE = os.path.join('C:\\', 'Documents', 'encrypted.bin')
PASSWORDS = os.path.join('C:\\', 'Documents', 'passwords.txt')


with open(ENCRYPTED_FILE, 'rb') as enc_f:  # открываем на чтение бинарный файл
    encrypted_text = enc_f.read()  # читаем сразу весь текст из файла

with open(PASSWORDS, 'r') as ps:
    for pwd in ps:
        pwd = pwd.strip()  # забираем по одному каждый пароль
        try:  # пробуем дешифровать текст каждым паролем
            decrypted_text = decrypt(pwd, encrypted_text)
        except DecryptionException:
            pass  # ничего не делаем
        else:
            print(decrypted_text.decode())  # выводим расшифрованный небинарный текст
            break
