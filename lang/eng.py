from Locale import Locale


class English(Locale):
    def __init__(self, ranked_whole, cents):
        self.prepare_whole = self.name_all(ranked_whole)
        self.prepare_remainder = self.name_all([cents])

        self.verbal = self.get_currency()

    def get(self):
        return self.verbal

    def name_all(self, arr):
        r = []
        for i, el in enumerate(arr):
            named = self.name_hundreds(el)
            ranged = ranges[i]

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

        # return plural form
        return currency_unit[0]

    def get_currency_cent(self, cent_words):
        # return unitary form
        if cent_words.split()[-1] == numerators[1]:
            return currency_cent[1]

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


delimiter = "-"
currency_delimiter = " and "
currency_unit = ['dollars', 'dollar']
currency_cent = ['cents', 'cent']
numerators = [
 "",
 "one",
 "two",
 "three",
 "four",
 "five",
 "six",
 "seven",
 "eight",
 "nine",
 "ten",
 "eleven",
 "twelve",
 "thirteen",
 "fourteen",
 "fifteen",
 "sixteen",
 "seventeen",
 "eighteen",
 "nineteen"
]
tens = [
 "",
 "ten",
 "twenty",
 "thirty",
 "forty",
 "fifty",
 "sixty",
 "seventy",
 "eighty",
 "ninety"
]
hundreds = [
 "",
 "one hundred",
 "two hundred",
 "three hundred",
 "four hundred",
 "five hundred",
 "six hundred",
 "seven hundred",
 "eight hundred",
 "nine hundred"
]
ranges = [
 '',
 'thousand',
 'million',
 'billion'
]
ranges_single = []
ranges_multiple = []
correction_list = []
