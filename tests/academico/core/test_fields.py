import pytest

from academico.core.fields import Field, IntegerField, StringField, FloatField, ModelField
from academico.core.models import Model


@pytest.fixture
def field():
    return Field('/html/body', r'.*')

@pytest.fixture
def integer_field():
    return IntegerField('/html/body', r'\d+')

@pytest.fixture
def string_field():
    return StringField('/html/body', r'.*')

@pytest.fixture
def float_field():
    return FloatField('/html/body', r'^[-+]?\d*\.?\d*$')


class TestField:
    def test_constructor(self, field):
        assert field.value_xpath == '/html/body'
        assert field.expression == r'.*'

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


class TestFloatField:
    def test_to_python_always_return_float(self, float_field):
        assert float_field.to_python(10) == 10.0
        assert float_field.to_python('1.2') == 1.2
        assert float_field.to_python('1,2') == 1.2


@pytest.fixture
def model_field():
    class TestModel(Model):
        fields = {
            'test': StringField('//b')
        }

    return ModelField(TestModel, '//div')


class TestModelField:
    def test_parse_value(self, model_field):
        model_field.parse_value("""
            <html>
                <body>
                    <div>
                        <b>Index 0</b>
                    </div>
                    <div>
                        <b>Index 1</b>
                    </div>
                </body>
            </html>
        """)

        assert model_field[0] is not None
        assert model_field[1] is not None
        assert model_field[0].test == 'Index 0'
        assert model_field[1].test == 'Index 1'

        with pytest.raises(IndexError):
            model_field[3]

        with pytest.raises(TypeError):
            model_field['name']
