from academico.core.utils import parse_xpath, parse_regex


class Field:
    """Base class for all fields"""
    def __init__(self, value_xpath: str = None, expression: str = None):
        if expression is None and value_xpath is None:
            raise Exception('expression e value_xpath não podem ser os dois nulos')

        self.value_xpath = value_xpath
        self.expression = expression

    def parse_value(self, content: str, parse_regex=parse_regex, parse_xpath=parse_xpath):
        value = content

        if self.value_xpath is not None:
            value = parse_xpath(value, self.value_xpath)

        if self.expression is not None:
            value = parse_regex(value, self.expression)

        return self.to_python(value)

    def to_python(self, value):
        return value


class IntegerField(Field):
    def to_python(self, value):
        return int(value)


class StringField(Field):
    def to_python(self, value):
        if isinstance(value, str):
            return value
        return str(value)
