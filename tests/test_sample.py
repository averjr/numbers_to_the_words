import pytest
import GL


class TestClass:
    def test_two(self):
        converter = GL.NumberConverter(12)
        assert converter.currency_string == 'twelve dollars'
