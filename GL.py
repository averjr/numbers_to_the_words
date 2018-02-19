import locale
import math
from decimal import *

from eng import correction_list,currency_cent,currency_delimiter,currency_unit,delimiter,hundreds,numerators,ranges,ranges_multiple,ranges_single,tens,ranges_single,ranges_multiple,correction_list
LANG = 'eng'
global correction_list,currency_cent,currency_delimiter,currency_unit,delimiter,hundreds,numerators,ranges,ranges_multiple,ranges_single,tens,ranges_single,ranges_multiple,correction_list


class NumberConverter():
    def __init__(self, n):
        getcontext().prec = 2
        self.number = Decimal(n)

        whole = self.get_whole()
        self.prepare_whole = ''
        if(whole):
            self.prepare_whole = self.prepare(whole)

        remainder = self.get_remainder()

        self.prepare_remainder = ''
        if(remainder):
            self.prepare_remainder = self.prepare(remainder)
        self.currency_string = self.get_currency()

    def get_currency_unit(self, unit_words):
        # return unitary form
        if unit_words.split()[-1] == numerators[1]:
            return currency_unit[1]

        # return special form for ukrainian
        if unit_words.split()[-1] in [numerators[2], numerators[3], numerators[4]] and LANG == 'ua':
            return currency_unit[2]

        # return plural form
        return currency_unit[0]

    def get_currency_cent(self, cent_words):
        # return unitary form
        if cent_words.split()[-1] == numerators[1]:
            return currency_cent[1]
        # use to check correction_list for right value
        elif LANG == 'ua' and cent_words.split()[-1] == correction_list[0]:
            return currency_cent[1]

        # return special form for ukrainian
        if cent_words.split()[-1] in [numerators[2], numerators[3], numerators[4]] and LANG == 'ua':
            return currency_cent[2]
        # return plural form
        return currency_cent[0]

    def get_currency(self):
        units = ""
        cents = ""

        if self.prepare_whole:
            right_currency_unit = self.get_currency_unit(self.prepare_whole)
            units = "{}{}".format(self.prepare_whole, right_currency_unit)

        if self.prepare_remainder:
            right_currency_cent = self.get_currency_cent(self.prepare_remainder)
            cents = "{}{}".format(self.prepare_remainder, right_currency_cent)

        if units and cents:
            return "{}{}{}".format(units, currency_delimiter, cents)
        elif units:
            return units
        elif cents:
            return cents

        return ""

    def prepare(self, num):
        ranks = self.get_ranks(num)
        return self.name_all(ranks)

    def get_whole(self):
        return int(math.modf(self.number)[1])

    def get_remainder(self):
        frac = math.modf(self.number)[0]
        return int(Decimal(frac)*100)

    def get_ranks(self, n):
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
        return result

    # TODO: improve grammar check
    def name_all(self, arr):
        r = []
        for i, el in enumerate(arr):
            named = self.name_hundreds(el)
            ranged = ranges[i]
            if int(str(el)[-1]) == 1 and LANG == 'ua':
                ranged = ranges_single[i]
            if 1 < int(str(el)[-1]) <= 4 and LANG == 'ua':
                ranged = ranges_multiple[i]

            # for the unitary form of million
            if int(str(el)[-1]) == 1 and LANG == 'ua' and i > 1:
                splited = named.split()
                splited[-1] = correction_list[0]
                named = " ".join(splited)

            # for the unitary form of million
            if int(str(el)[-1]) == 2 and LANG == 'ua' and i > 1:
                splited = named.split()
                splited[-1] = correction_list[1]
                named = " ".join(splited)

            r.append([named, ranged])

        return self.convert_to_string(r[::-1])

    def convert_to_string(self, l):
        results = []
        for el in l:
            as_string = " ".join(el)
            results.append(as_string)

        return " ".join(results)

    def name_hundreds(self, n):
        results = ''
        if n < 20:
            return numerators[n]
        if n <= 99:
            t, remainder = divmod(n, 10)
            if remainder:
                return "{}{}{}".format(tens[t], delimiter, numerators[remainder])
            else:
                return "{}".format(tens[t])
        if n >= 100:
            t, remainder = divmod(n, 100)
            if remainder:
                return "{} {}".format(hundreds[t], self.name_hundreds(remainder))
            else:
                return "{}".format(hundreds[t])


def set_lang_from_promt(prompt):
    try:
        value = int(input(prompt))
        if value == 1:
            global LANG
            global correction_list,currency_cent,currency_delimiter,currency_unit,delimiter,hundreds,numerators,ranges,ranges_multiple,ranges_single,tens,ranges_single,ranges_multiple,correction_list
            from eng import correction_list,currency_cent,currency_delimiter,currency_unit,delimiter,hundreds,numerators,ranges,ranges_multiple,ranges_single,tens,ranges_single,ranges_multiple,correction_list
            LANG = 'eng'
        elif value == 2:
            global correction_list,currency_cent,currency_delimiter,currency_unit,delimiter,hundreds,numerators,ranges,ranges_multiple,ranges_single,tens,ranges_single,ranges_multiple,correction_list
            from ua import correction_list,currency_cent,currency_delimiter,currency_unit,delimiter,hundreds,numerators,ranges,ranges_multiple,ranges_single,tens,ranges_single,ranges_multiple,correction_list
            LANG = 'ua'
            locale.setlocale(locale.LC_NUMERIC, 'uk_UA.KOI8-U')
    except ValueError:
        print("Sorry, I didn't understand that.")
        return get_non_negative_int(prompt)

    if value not in [1, 2]:
        print("Sorry, please use [1] for English and [2] for Ukrainian")
        return set_lang_from_promt(prompt)


def conver_from_promt(prompt):
    try:
        value = locale.atof(input(prompt))
        print(NumberConverter(value).currency_string)
    except ValueError:
        print("Sorry, I didn't understand that.")
        return conver_from_promt(prompt)

    if 0 >= value <= 2147483647:
        print("Sorry, only numbers between 0 and 2147483647 are allowed.")
        return conver_from_promt(prompt)


set_lang_from_promt("Please select language [1] for English [2] for Ukrainian:")
conver_from_promt("Enter number between 0 and 2147483647:")
