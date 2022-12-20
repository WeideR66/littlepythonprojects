from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

terms = {'num_enable': True, 'RandReg_enable': True, 'symb_enable': False, 'unusual_enable': False}


class PassGenerator:
    @staticmethod
    def __add_num(string: str) -> str:
        return string + digits

    @staticmethod
    def __add_uppercase(string: str) -> str:
        return string + ascii_uppercase

    @staticmethod
    def __add_punctuation(string: str) -> str:
        return string + punctuation

    @staticmethod
    def __remove_ambigious(string: str) -> str:
        for letter in 'iI1Lo0O':
            string.replace(letter, '')
        return string

    @staticmethod
    def generate_passwords(terms: dict, pass_len: int, pass_count: int) -> tuple:
        functions = {'num_enable': PassGenerator.__add_num,
                     'RandReg_enable': PassGenerator.__add_uppercase,
                     'symb_enable': PassGenerator.__add_punctuation,
                     'unusual_enable': PassGenerator.__remove_ambigious}
        symbols = ascii_lowercase
        for term, value in terms.items():
            if value:
                symbols = functions[term](symbols)

        result = tuple(''.join(choices(symbols, k=pass_len)) for _ in range(pass_count))
        return result


print(PassGenerator.generate_passwords(terms, 10, 10))