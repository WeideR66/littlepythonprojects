"""Простейший шифр Цезаря"""


def coder(text, key):
    result = ''
    key = int(key)
    for i in text:
        if i in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
            if (ord(i) + key) > 1103:
                result += chr(ord(i) - 32 + key)
            else:
                result += chr(ord(i) + key)
        if i in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            if (ord(i) + key) > 1071:
                result += chr(ord(i) - 32 + key)
            else:
                result += chr(ord(i) + key)
        if i in 'abcdefghijklmnopqrstuvwxyz':
            if (ord(i) + key) > 122:
                result += chr(ord(i) - 26 + key)
            else:
                result += chr(ord(i) + key)
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if (ord(i) + key) > 90:
                result += chr(ord(i) - 26 + key)
            else:
                result += chr(ord(i) + key)
        if not i.isalpha():
            result += i
    return result


def decoder(text, key):
    result = ''
    key = int(key)
    for i in text:
        if i in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
            if (ord(i) - key) < 1072:
                result += chr(ord(i) + 32 - key)
            else:
                result += chr(ord(i) - key)
        if i in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            if (ord(i) - key) < 1040:
                result += chr(ord(i) + 32 - key)
            else:
                result += chr(ord(i) - key)
        if i in 'abcdefghijklmnopqrstuvwxyz':
            if (ord(i) - key) < 97:
                result += chr(ord(i) + 26 - key)
            else:
                result += chr(ord(i) - key)
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if (ord(i) - key) < 65:
                result += chr(ord(i) + 26 - key)
            else:
                result += chr(ord(i) - key)
        if not i.isalpha():
            result += i
    return result


while True:
    var = int(input('Выберите необходимую операцию (0 - шифрование, 1 - дешифрование текста)\n'))
    if var == 0:
        print('Введите текст и ключ для шифровки текста\n')
        txt, key = input(), input()
        print(coder(txt, key))
    else:
        print('Введите текст и ключ для расшифровки\n')
        txt, key = input(), input()
        print(decoder(txt, key))
    vyb = int(input('Хотите ли еще выполнить какую либо операцию? (1 - да, 0 - нет)\n'))
    if vyb == 0:
        break
    else:
        continue
