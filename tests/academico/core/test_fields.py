import pytest

from academico.core.fields import Field, IntegerField, StringField


@pytest.fixture
def field():
    return Field('/html/body', r'\d+')

@pytest.fixture
def integer_field():
    return IntegerField('/html/body', r'\d+')

@pytest.fixture
def string_field():
    return StringField('/html/body', r'\d+')


class TestField:
    def test_constructor(self, field):
        assert field.value_xpath == '/html/body'
        assert field.expression == r'\d+'

    def test_parse_value(self, field):
        value = field.parse_value('<html><body>100</body></html>')
        assert value == '100'

    def test_to_python(self, field):
        assert field.to_python(10) == 10
        assert field.to_python('10') == '10'


class TestIntegerField:
    def test_to_python_always_return_integer(self, integer_field):
        assert integer_field.to_python('10') == 10
        assert integer_field.to_python(10) == 10


class TestStringField:
    def test_to_python_always_return_string(self, string_field):
        assert string_field.to_python(10) == '10'
        assert string_field.to_python('10') == '10'
