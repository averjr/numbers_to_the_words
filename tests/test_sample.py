import pytest
from GL import NumberConverter
from lang.eng import English
from lang.ua import Ukrainian


class BaseTestEng():
    loc = English


class BaseTestUkr():
    loc = Ukrainian


class TestNumberConverterEn(BaseTestEng):
    def test_singular(self):
        nc = NumberConverter(1.00, self.loc).get_verbal()
        assert nc == 'one dollar'

    def test_singular_cent(self):
        nc = NumberConverter(0.01, self.loc).get_verbal()
        assert nc == 'one cent'

    def test_million_and_cents(self):
        nc = NumberConverter(1234567.89, self.loc).get_verbal()
        assert nc == (
            'one million two hundred thirty-four thousand five hundred '
            'sixty-seven dollars and eighty-nine cents'
        )

    def test_thousand_and_cents(self):
        nc = NumberConverter(1234.12, self.loc).get_verbal()
        assert nc == (
            'one thousand two hundred thirty-four dollars '
            'and twelve cents'
        )


class TestNumberConverterUa(BaseTestUkr):
    def test_singular(self):
        nc = NumberConverter(1.00, self.loc).get_verbal()
        assert nc == 'одна гривня'

    def test_singular_cent(self):
        nc = NumberConverter(0.01, self.loc).get_verbal()
        assert nc == 'одна копійка'

    def test_million_and_cents(self):
        nc = NumberConverter(1234567.89, self.loc).get_verbal()
        assert nc == (
            'один мільйон двісті тридцять чотири тисячі п\'ятсот шістдесят сім '
            'гривень вісімдесят дев\'ять копійок'
        )

    def test_thousand_and_cents(self):
        nc = NumberConverter(1234.12, self.loc).get_verbal()
        assert nc == (
            'одна тисяча двісті тридцять чотири гривні '
            'дванадцять копійок'
        )
