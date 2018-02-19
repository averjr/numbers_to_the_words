# - *- coding: utf- 8 - *-
class Ukrainian():
    def __init__(self, ranked_whole, cents):
        self.prepare_whole = self.name_all(ranked_whole)
        self.prepare_remainder = self.name_all([cents])

        self.verbal = self.get_currency()

    def get(self):
        return self.verbal

    def gender_corection(self):
        pass

    def numbers_to_text(self):
        pass

    def get_units(self):
        pass

    def get_cents(self):
        pass

    # def add_currency(self):
    #
    #     # return special form for ukrainian
    #     if unit_words.split()[-1] in [numerators[2], numerators[3], numerators[4]]:
    #         return currency_unit[2]
    #
    #     # use to check correction_list for right value
    #     if cent_words.split()[-1] == correction_list[0]:
    #         return currency_cent[1]
    #
    #     # return special form for ukrainian
    #     if cent_words.split()[-1] in [numerators[2], numerators[3], numerators[4]]:
    #         return currency_cent[2]

    def name_all(self, arr):
        r = []
        for i, el in enumerate(arr):
            named = self.name_hundreds(el)
            ranged = ranges[i]
            if int(str(el)[-1]) == 1:
                ranged = ranges_single[i]
            if 1 < int(str(el)[-1]) <= 4:
                ranged = ranges_multiple[i]

            # for the unitary form of million
            if int(str(el)[-1]) == 1 and i > 1:
                splited = named.split()
                splited[-1] = correction_list[0]
                named = " ".join(splited)

            # for the unitary form of million
            if int(str(el)[-1]) == 2 and i > 1:
                splited = named.split()
                splited[-1] = correction_list[1]
                named = " ".join(splited)

            r.append([named, ranged])

        return self._convert_to_string(r[::-1])

    def _convert_to_string(self, l):
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

    def get_currency_unit(self, unit_words):
        # return unitary form
        if unit_words.split()[-1] == numerators[1]:
            return currency_unit[1]

        # return special form for ukrainian
        if unit_words.split()[-1] in [numerators[2], numerators[3], numerators[4]]:
            return currency_unit[2]

        # return plural form
        return currency_unit[0]

    def get_currency_cent(self, cent_words):
        # return unitary form
        if cent_words.split()[-1] == numerators[1]:
            return currency_cent[1]

        # use to check correction_list for right value
        if cent_words.split()[-1] == correction_list[0]:
            return currency_cent[1]

        # return special form for ukrainian
        if cent_words.split()[-1] in [numerators[2], numerators[3], numerators[4]]:
            return currency_cent[2]


        # return plural form
        return currency_cent[0]

    def get_currency(self):
        units = ""
        cents = ""

        if self.prepare_whole.strip():
            right_currency_unit = self.get_currency_unit(self.prepare_whole)
            units = "{}{}".format(self.prepare_whole, right_currency_unit)

        if self.prepare_remainder.strip():
            right_currency_cent = self.get_currency_cent(self.prepare_remainder)
            cents = "{}{}".format(self.prepare_remainder, right_currency_cent)

        if units and cents:
            return "{}{}{}".format(units, currency_delimiter, cents)
        elif units:
            return units
        elif cents:
            return cents

        return ""


delimiter = " "
currency_delimiter = " "
currency_unit = ['гривень', 'гривня', 'гривні']
currency_cent = ['копійок', 'копійка', 'копійки']
numerators = [
 '',
 'одна',
 'дві',
 'три',
 'чотири',
 'п\'ять',
 'шість',
 'сім',
 'вісім',
 'дев\'ять',
 'десять',
 'одинадцять',
 'дванадцять',
 'тринадцять',
 'чотирнадцять',
 'п\'ятнадцять',
 'шістнадцять',
 'сімнадцять',
 'вісімнадцять',
 'дев\'ятнадцять'
 ]
tens = [
 '',
 'десять',
 'двадцять',
 'тридцять',
 'сорок',
 'п\'ятдесят',
 'шістдесят',
 'сімдесят',
 'вісімдесят',
 'дев\'яносто'
 ]
hundreds = [
 '',
 'сто',
 'двісті',
 'триста',
 'чотириста',
 'п\'ятсот',
 'шістсот',
 'сімсот',
 'вісімсот',
 'дев\'ятсот'
 ]
ranges = [
 '',
 'тисяч',
 'мільйонів',
 'мільярдів',
]
ranges_single = [
 '',
 'тисяча',
 'мільйон',
 'мільярд',
]
ranges_multiple = [
 '',
 'тисячі',
 'мільйони',
 'мільярди',
]
correction_list = [
 'один',
 'два'
]
