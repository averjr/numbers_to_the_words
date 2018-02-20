import pytest
from GL import NumberConverter


class TestNumberConverterEn:
    def test_singular(self):
        nc = NumberConverter(1.00, 'en').get_verbal()
        assert nc == 'one dollar'

    def test_singular_cent(self):
        nc = NumberConverter(0.01, 'en').get_verbal()
        assert nc == 'one cent'

    def test_million_and_cents(self):
        nc = NumberConverter(1234567.89, 'en').get_verbal()
        assert nc == (
            'one million two hundred thirty-four thousand five hundred '
            'sixty-seven dollars and eighty-nine cents'
        )

    def test_thousand_and_cents(self):
        nc = NumberConverter(1234.12, 'en').get_verbal()
        assert nc == (
            'one thousand two hundred thirty-four dollars '
            'and twelve cents'
        )


class TestNumberConverterUa:
    def test_singular(self):
        nc = NumberConverter(1.00, 'ua').get_verbal()
        assert nc == 'одна гривня'

    def test_singular_cent(self):
        nc = NumberConverter(0.01, 'ua').get_verbal()
        assert nc == 'одна копійка'

    def test_million_and_cents(self):
        nc = NumberConverter(1234567.89, 'ua').get_verbal()
        assert nc == (
            'один мільйон двісті тридцять чотири тисячі п\'ятсот шістдесят сім '
            'гривень вісімдесят дев\'ять копійок'
        )

    def test_thousand_and_cents(self):
        nc = NumberConverter(1234.12, 'ua').get_verbal()
        assert nc == (
            'одна тисяча двісті тридцять чотири гривні '
            'дванадцять копійок'
        )
