import random

print('Добро подаловать в числовую угадайку')


def is_valid(number, gran):
    if gran.isdigit() and number.isdigit():
        return int(number) in range(0, int(gran) + 1)


def get_new_rand(gran):
    return random.randint(0, int(gran))


n, count = input('Введите границу интервала: '), 0
num, flag = get_new_rand(n), True
while flag:
    chislo = input(f'Введите число от 1 до {n}: ')
    if is_valid(chislo, n):
        chislo = int(chislo)
        if chislo < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        if chislo > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        if chislo == num:
            print(f'Вы угадали, поздравляем!\nВаше количество попыток угадать число: {count}')
            ans = input('Может быть еще сыгарем? (да/нет) ')
            while True:
                if ans == 'да':
                    n, count, num = input('Введите новую границу интервала: '), 0, get_new_rand(n)
                    break
                if ans == 'нет':
                    flag = False
                    break
                else:
                    ans = input('Непонел, так да или нет? ')
    else:
        print('А может быть все-таки введем целое число?')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
