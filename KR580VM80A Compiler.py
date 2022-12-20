"""Компилятор это конечно громко сказано, скорее это переводчик с ассемблера
микропроцессора КР580ВМ80А в машинный код. Предыстория: у меня в универе был
предмет 'Микроконтроллеры и однокристальные микро-ЭВМ' и там учились на старом
советском микропроцессоре КР580ВМ80А, на лабах вечно приходилось сначала писать
какую то простую программу на ассемблере, потом заверять код у препода, потом
в ручную переводить ассемблер в машинный код по справочнику, и только потом
машинный код вбивать в эмулятор микропроцессорной системы, и смотреть как она работает.
Меня каждый раз раздражало в ручную искать нужную команду в справочнике и переписывать
байтовые машинные коды в тетрадь и при этом запоминать в какой именно ячейке памяти
должен быть определенный байт команды, поэтому решил тогда и написать такой переводчик.
Это не первая версия переводчика, первая хоть и работала и облегчала работу, но была с изъянами
(кошмарно написанный код, не было отображения адресов и прочие мелкие недочеты).
Недавно вспомнил про нее и решил переписать в ооп стиле и улучшить код.
Конечно, может и этот вариант написан не красиво, но предыдущий вариант был адовым"""


# Массивы с одно, двух, трех байтовыми командами
one_byte_code = ["MOV", "SPHL", "PCHL", "LDAX", "STAX", "PUSH", "POP", "XCHG", "XTHL", "ADD", "ADC", "DAD", "SUB",
                 "SBB", "CMP", "INR", "INX", "DCR", "DCX", "DAA", "RET", "RC", "RNC", "RZ", "RNZ", "RP", "RM", "PRE",
                 "PRO", "RST", "ANA", "ORA", "XRA", "CMA", "RAR", "RAL", "RRC", "RLC", "HLT", "NOP", "EI", "DI",
                 "STC", "CMC"]
two_byte_code = ["MVI", "IN", "OUT", "ADI", "ACI", "SUI", "SBI", "SPI", "ANI", "ORI", "XRI", "CPI"]
three_byte_code = ["LXI", "LDA", "STA", "SHLD", "LHLD", "JMP", "JC", "JNC", "JZ", "JNZ", "JP", "JM", "JPE", "JPO",
                   "CALL", "CC", "CNC", "CZ", "CNZ", "CP", "CM", "CPE", "CPO"]

# Словарь с машинными кодами каждой команды
all_machine_codes = dict(NOP="00", LXI_B="01", STAX_B="02", INX_B="03", INR_B="04", DCR_B="05", MVI_B="06", RLC="07",
                         DAD_B="09", LDAX_B="0A", DCX_B="0B", INR_C="0C", DCR_C="0D", MVI_C="0E", RRC="0F", LXI_D="11",
                         STAX_D="12", INX_D="13", INR_D="14", DCR_D="15", MVI_D="16", RAL="17", DAD_D="19",
                         LDAX_D="1A", DCX_D="1B", INR_E="1C", DCR_E="1D", MVI_E="1E", RAR="1F", LXI_H="21",
                         SHLD="22", INX_H="23", INR_H="24", DCR_H="25", MVI_H="26", DAA="27", DAD_H="29",
                         LHLD="2A", DCX_H="2B", INR_L="2C", DCR_L="2D", MVI_L="2E", CMA="2F", LXI_SP="31",
                         STA="32", INX_SP="33", INR_M="34", DCR_M="35", MVI_M="36", STC="37", DAD_SP="39",
                         LDA="3A", DCX_SP="3B", INR_A="3C", DCR_A="3D", MVI_A="3E", CMC="3F", MOV_B_B="40",
                         MOV_B_C="41", MOV_B_D="42", MOV_B_E="43", MOV_B_H="44", MOV_B_L="45", MOV_B_M="46",
                         MOV_B_A="47", MOV_C_B="48", MOV_C_C="49", MOV_C_D="4A", MOV_C_E="4B", MOV_C_H="4C",
                         MOV_C_L="4D", MOV_C_M="4E", MOV_C_A="4F", MOV_D_B="50", MOV_D_C="51", MOV_D_D="52",
                         MOV_D_E="53", MOV_D_H="54", MOV_D_L="55", MOV_D_M="56", MOV_D_A="57", MOV_E_B="58",
                         MOV_E_C="59", MOV_E_D="5A", MOV_E_E="5B", MOV_E_H="5C", MOV_E_L="5D", MOV_E_M="5E",
                         MOV_E_A="5F", MOV_H_B="60", MOV_H_C="61", MOV_H_D="62", MOV_H_E="63", MOV_H_H="64",
                         MOV_H_L="65", MOV_H_M="66", MOV_H_A="67", MOV_L_B="68", MOV_L_C="69", MOV_L_D="6A",
                         MOV_L_E="6B", MOV_L_H="6C", MOV_L_L="6D", MOV_L_M="6E", MOV_L_A="6F", MOV_M_B="70",
                         MOV_M_C="71", MOV_M_D="72", MOV_M_E="73", MOV_M_H="74", MOV_M_L="75", HLT="76",
                         MOV_M_A="77", MOV_A_B="78", MOV_A_C="79", MOV_A_D="7A", MOV_A_E="7B", MOV_A_H="7C",
                         MOV_A_L="7D", MOV_A_M="7E", MOV_A_A="7F", ADD_B="80", ADD_C="81", ADD_D="82",
                         ADD_E="83", ADD_H="84", ADD_L="85", ADD_M="86", ADD_A="87", ADC_B="88", ADC_C="89",
                         ADC_D="8A", ADC_E="8B", ADC_H="8C", ADC_L="8D", ADC_M="8E", ADC_A="8F", SUB_B="90",
                         SUB_C="91", SUB_D="92", SUB_E="93", SUB_H="94", SUB_L="95", SUB_M="96", SBB_A="97",
                         SBB_B="98", SBB_C="99", SBB_D="9A", SBB_E="9B", SBB_H="9C", SBB_L="9D", SBB_M="9E",
                         SBB_A_="9F", ANA_B="A0", ANA_C="A1", ANA_D="A2", ANA_E="A3", ANA_H="A4", ANA_L="A5",
                         ANA_M="A6", ANA_A="A7", XRA_B="A8", XRA_C="A9", XRA_D="AA", XRA_E="AB", XRA_H="AC",
                         XRA_L="AD", XRA_M="AE", XRA_A="AF", ORA_B="B0", ORA_C="B1", ORA_D="B2", ORA_E="B3",
                         ORA_H="B4", ORA_L="B5", ORA_M="B6", ORA_A="B7", CMP_B="B8", CMP_C="B9", CMP_D="BA",
                         CMP_E="BB", CMP_H="BC", CMP_L="BD", CMP_M="BE", CMP_A="BF", RNZ="C0", POP_B="C1",
                         JNZ="C2", JMP="C3", CNZ="C4", PUSH_B="C5", ADI="C6", RST_0="C7", RZ="C8", RET="C9",
                         JZ="CA", CZ="CC", CALL="CD", ACI="CE", RST_1="CF", RNC="D0", POP_D="D1", JNC="D2",
                         OUT="D3", CNC="D4", PUSH_D="D5", SUI="D6", RST_2="D7", RC="D8", JC="DA", IN="DB",
                         CC="DC", SBI="DE", RST_3="DF", RPO="E0", POP_H="E1", JPO="E2", XTHL="E3", CPO="E4",
                         PUSH_H="E5", ANI="E6", RST_4="E7", RPE="E8", PCHL="E9", JPE="EA", XCHG="EB", CPE="EC",
                         XRI="EE", RST_5="EF", RP="EF", POP_PSW="F1", JP="F2", DI="F3", CP="F4", PUSH_PSW="F5",
                         ORI="F6", RST_6="F7", RM="F8", SPHL="F9", JM="FA", EI="FB", CM="FC", CPI="FE", RST_7="FF")


# Два списка с шестнадцатеричными числами одного и двух байт (от 00 до FF, и от 0000 до FFFF)
# Было важно что бы значения имели формат AD и ADDR
hex_byte = list(map(lambda var: '0' * (2 - len(var)) + var, [hex(i)[2:].upper() for i in range(256)]))
hex_two_byte = list(map(lambda var: '0' * (4 - len(var)) + var, [hex(i)[2:].upper() for i in range(65536)]))


class CodeLine:
    @staticmethod
    def validator(code: str) -> bool:
        """Валидатор вводимых команд"""
        code_parts = code.split('_')
        len_code = len(code_parts)
        all_comands = all_machine_codes.keys()
        if len_code == 1 and code_parts[0] in all_comands:
            return True
        elif len_code == 2 and ((((len(code_parts[-1]) == 4 and code_parts[-1] in hex_two_byte) or
                                  (len(code_parts[-1]) == 2 and code_parts[-1] in hex_byte)) and
                                 code_parts[0] in all_comands) or
                                code in all_comands):
            return True
        elif len_code == 3 and ((((len(code_parts[-1]) == 4 and code_parts[-1] in hex_two_byte) or
                                  (len(code_parts[-1]) == 2) and code_parts[-1] in hex_byte) and
                                 '_'.join(code_parts[:2]) in all_comands) or
                                code in all_comands):
            return True
        else:
            return False

    @staticmethod
    def count_byte(code: str) -> int:
        """Возвращает количество байт введеной команды"""
        code = code.split(' ')[0].upper()
        if code in one_byte_code:
            return 1
        elif code in two_byte_code:
            return 2
        elif code in three_byte_code:
            return 3

    @staticmethod
    def increment_addr(curr_addr: str, byte_count: int) -> str:
        """Увеличивает значение адреса на определенное число.
        Допустим изначально адрес был 0819 и нужно его увеличить на 3,
        функция вернет 081B"""
        res = hex(int(curr_addr, 16) + byte_count)[2:].upper()
        return '0' * (4 - len(res)) + res if len(res) <= 3 else res

    @staticmethod
    def replacer(code: str) -> str:
        """Меняет пробелы и запятые в введенной команде."""
        for char, new_char in ((' ', '_'), (',', '')):
            if char in code:
                code = code.replace(char, new_char)
        return code

    def __init__(self, code: str, hex_addr: str) -> None:
        """Инициализация объекта и проверка на валидность значений.
        Так же идет определение количества байт команды"""
        if self.validator(self.replacer(code.upper())):
            self._code = code
        else:
            raise ValueError('Такой команды не существует, введите правильную команду.')
        if hex_addr in hex_two_byte:
            self._hex_addr = hex_addr
        else:
            raise ValueError('Введите правильный адрес.')
        self._num_of_bytes = self.count_byte(code)

    @property
    def next_free_addr(self) -> str:
        """Возвращает следующий свободный адрес в зависимости от введеной
        команды"""
        return self.increment_addr(self._hex_addr, self._num_of_bytes)

    @property
    def to_mach_code(self) -> list[tuple]:
        """Возвращает список кортежей, в которых пары значений
        (адрес кода, машинный код) """
        code = self.replacer(self._code)
        code_parts = [code[:code.rfind('_')], code[code.rfind('_') + 1:]]
        result_list = list()
        for i in range(self._num_of_bytes):
            if self._num_of_bytes == 1:
                result_list.append((self._hex_addr, all_machine_codes[code]))
            if self._num_of_bytes == 2:
                if i == 0:
                    result_list.append((self.increment_addr(self._hex_addr, i),
                                        all_machine_codes[code_parts[i]]))
                else:
                    result_list.append((self.increment_addr(self._hex_addr, i),
                                        code_parts[i]))
            if self._num_of_bytes == 3:
                drad = (code_parts[-1][2:], code_parts[-1][:2])
                if i == 0:
                    result_list.append((self.increment_addr(self._hex_addr, i),
                                        all_machine_codes[code_parts[i]]))
                else:
                    result_list.append((self.increment_addr(self._hex_addr, i),
                                        drad[i - 1]))
        return result_list


def main(out=True):
    start_addr = input('Введите начальный адрес: ').upper()
    result_code = list()
    used_addr = list()
    while True:
        if start_addr not in hex_two_byte or start_addr in used_addr:
            start_addr = input('Введите правильный адрес (адрес мог уже использоваться): ')
            continue
        line = input(f'{start_addr}: ').upper()
        if line.lower() == 'end':
            break
        if line.lower() == 'subprogramm':
            print('Начало подпрограммы')
            buffer = main(False)
            result_code += buffer[0]
            used_addr += buffer[-1]
            print('Конец подпрограммы')
            continue
        try:
            code = CodeLine(line, start_addr)
            result_code += code.to_mach_code
            start_addr = code.next_free_addr
        except ValueError as err:
            print(err)
            continue
        for tup in result_code:
            if tup[0] not in used_addr:
                used_addr.append(tup[0])
    if out:
        print('Результат')
        for addr, byte in result_code:
            print(f'{addr}: {byte}')
    else:
        return result_code, used_addr


if __name__ == '__main__':
    main()

"""Инструкция"""
"""Первым делом вводите начальный адрес, откуда у вас начинается программа.
Коды можно вводить в любом регистре и в таком синтаксисе (КОМ - команда, X, Y - регистры, 
AD - байтовое число, ADDR - двухбайтовое число) - КОМ; КОМ X; КОМ X, Y; КОМ AD; КОМ X, AD;
КОМ ADDR; КОМ X, ADDR. То есть строго соблюдать пробелы и разделять байтовые числа от регистров и команд.
Если в программе есть подпрограмма, то в строке ввода необходимо ввести 'subprogramm' без кавычек и писать подпрограмму
по нужному адресу. Для выхода из подпрограммы нужно написать 'end' и вы вернетесь к основной программе. Для завершения 
ввода команд напишите 'end' и результат выведется в консоль."""

"""Пример: есть какая то программа
in 05
mvi b, 05
add b
mov c, a
call 0900 #вызов подпрограммы

подпрограмма
lda 1000
ret

Просто вводим ее в консоль:
Введите начальный адрес: 0810
0810: in 05
0812: mvi b, 05
0814: add b
0815: mov c, a
0816: call 0900
0819: subprogramm
Начало подпрограммы
Введите начальный адрес: 0900
0900: lda 10000
Такой команды не существует, введите правильную команду.
0900: lda 1000
0903: ret
0904: end
Конец подпрограммы
0819: end

Как видно, даже простейший валидатор команд есть, так что ошибочные коды не ввести.

И результат будет:

Результат
0810: DB
0811: 05
0812: 06
0813: 05
0814: 80
0815: 4F
0816: CD
0817: 00
0818: 09
0900: 3A
0901: 00
0902: 10
0903: C9

Программа позволяет быстро на лабе ввести написанный код, затем она его переводит в машинный код
и показывает в какой ячейке памяти должен сидеть определенный код."""
