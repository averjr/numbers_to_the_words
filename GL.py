import locale
import math
from decimal import *

from lang.eng import English
from lang.ua import Ukrainian


class NumberConverter():
    def get_verbal(self):
        return self.locale.get()

    def __init__(self, n, locale):
        getcontext().prec = 2
        self.number = Decimal(n)
        self.whole_and_remainder = []
        self.get_whole_and_remainder()

        self.ranked = []
        self.get_ranks()

        self.locale = locale(self.ranked, self.whole_and_remainder[1])

    def get_whole_and_remainder(self):
        f, w = math.modf(self.number)
        whole = int(w)
        frac = int(Decimal(f)*100)
        self.whole_and_remainder = [whole, frac]

    # TODO: find better way to split by triplets
    def get_ranks(self):
        n = self.whole_and_remainder[0]
        result = []
        ns = str(n)
        for k in range(3, 15, 3):
            r = ns[-k:]
            q = len(ns) - k

            if q < -2:
                break
            else:
                if q >= 0:
                    result.append(int(r[:3]))
                elif q >= -1:
                    result.append(int(r[:2]))
                elif q >= -2:
                    result.append(int(r[:1]))
        self.ranked = result


def set_lang_from_promt(prompt):
    try:
        value = int(input(prompt))
        if value == 1:
            lang = 'en'
        elif value == 2:
            lang = 'ua'
            locale.setlocale(locale.LC_NUMERIC, 'uk_UA.KOI8-U')
        return lang
    except ValueError:
        print("Sorry, I didn't understand that.")
        return get_non_negative_int(prompt)

    if value not in [1, 2]:
        print("Sorry, please use [1] for English and [2] for Ukrainian")
        return set_lang_from_promt(prompt)


def convert_from_promt(prompt):
    try:
        value = locale.atof(input(prompt))
        return value
    except ValueError:
        print("Sorry, I didn't understand that.")
        return convert_from_promt(prompt)

    if 0 >= value <= 2147483647:
        print("Sorry, only numbers between 0 and 2147483647 are allowed.")
        return convert_from_promt(prompt)


if __name__ == "__main__":
    lang = set_lang_from_promt(
        "Please select language [1] for English [2] for Ukrainian:"
    )
    if lang == 'en':
        loc = English
    if lang == 'ua':
        loc = Ukrainian

    num = convert_from_promt("Enter number between 0 and 2147483647:")
    nc = NumberConverter(num, loc)
    print(nc.get_verbal())
