import random


def get_random_word():
    word_list = ['университет', 'собака', 'кот', 'ручка', 'лист', 'петля', 'фонарик',
                 'мышь', 'компьютер', 'лестница', 'кольцо', 'точилка', 'плата', 'пиво',
                 'генератор', 'синусоида', 'график', 'интеграл', 'машина', 'подъезд',
                 'никотин', 'вода', 'пища', 'космос', 'объект', 'светодиод', 'телефон', 
                 'разработка', 'страница']
    return random.choice(word_list)


def draw_gallows(stage):
    if stage == 0:
        print('*************\n'
              '*           *\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '***********************', end='\n')
    if stage == 1:
        print('*************\n'
              '*           *\n'
              '*          ***\n'
              '*          ***\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '*\n'
              '***********************', end='\n')
    if stage == 2:
        print('*************\n'
              '*           *\n'
              '*          ***\n'
              '*          ***\n'
              '*           *\n'
              '*           *\n'
              '*           *\n'
              '*           *\n'
              '*           *\n'
              '*\n'
              '*\n'
              '*\n'
              '***********************', end='\n')
    if stage == 3:
        print('*************\n'
              '*           *\n'
              '*          ***\n'
              '*          ***\n'
              '*           *\n'
              '*         * *\n'
              '*        *  *\n'
              '*       *   *\n'
              '*           *\n'
              '*\n'
              '*\n'
              '*\n'
              '***********************', end='\n')
    if stage == 4:
        print('*************\n'
              '*           *\n'
              '*          ***\n'
              '*          ***\n'
              '*           *\n'
              '*         * * *\n'
              '*        *  *  *\n'
              '*       *   *   * \n'
              '*           *\n'
              '*\n'
              '*\n'
              '*\n'
              '***********************', end='\n')
    if stage == 5:
        print('*************\n'
              '*           *\n'
              '*          ***\n'
              '*          ***\n'
              '*           *\n'
              '*         * * *\n'
              '*        *  *  *\n'
              '*       *   *   *\n'
              '*           *\n'
              '*          *\n'
              '*         *\n'
              '*\n'
              '***********************', end='\n')
    if stage == 6:
        print('*************\n'
              '*           *\n'
              '*          ***\n'
              '*          ***\n'
              '*           *\n'
              '*         * * *\n'
              '*        *  *  *\n'
              '*       *   *   *\n'
              '*           *\n'
              '*          * *\n'
              '*         *   *\n'
              '*\n'
              '***********************', end='\n')


def is_valid(char):
    return char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def word_handler(stroka, char, trig):
    if trig:
        string = list(slovo)
        for i in range(len(string)):
            if slovo[0] == string[i] or slovo[len(slovo) - 1] == string[i]:
                continue
            else:
                string[i] = '_'
        return ''.join(string)
    else:
        if char in slovo:
            prom = list(stroka)
            for i in range(len(prom)):
                if slovo[i] == char:
                    prom[i] = char
            return ''.join(prom)
        else:
            return 0


def game():
    game_flag, stage = True, 0
    slovo = get_random_word()
    global slovo
    ugad = word_handler('', '', True)
    while game_flag:
        print()
        draw_gallows(stage)
        print(ugad)
        symb = input('Введите букву: ').lower()
        if is_valid(symb):
            if word_handler(ugad, symb, False) == 0:
                stage += 1
            else:
                ugad = word_handler(ugad, symb, False)
        else:
            print('Нужны русские буквы!!!')
        if stage == 6:
            draw_gallows(stage)
            res1 = input('Игра окончена, вы проиграли. Хотите начать заново? (да/нет)')
            while True:
                if res1 == 'да':
                    slovo = get_random_word()
                    ugad = word_handler('', '', True)
                    stage = 0
                    break
                elif res1 == 'нет':
                    print('Было приятно поиграть с вами!')
                    game_flag = False
                    break
                else:
                    res1 = input('Я не понел, так да или нет? (да/нет)')
                    continue
        if ugad == slovo:
            res2 = input('Поздравляем! Вы выиграли! Хотите продолжить? (да/нет)')
            while True:
                if res2 == 'да':
                    slovo = get_random_word()
                    ugad = word_handler('', '', True)
                    stage = 0
                    break
                elif res2 == 'нет':
                    print('Было приятно поиграть с вами!')
                    game_flag = False
                    break
                else:
                    res2 = input('Я не понел, так да ли нет? (да/нет)')

game()