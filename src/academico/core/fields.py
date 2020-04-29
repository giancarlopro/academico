from academico.core.utils import parse_xpath, parse_regex, parse_multi_xpath


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


class FloatField(Field):
    def to_python(self, value):
        if isinstance(value, str):
            value = value.replace(',', '.')

        return float(value)


class ModelField:
    model = None
    elements_xpath = None

    def __init__(self, model=None, elements_xpath=None):
        self._elements = []
        self.model = model or self.model
        self.elements_xpath = elements_xpath or self.elements_xpath

    def parse_value(self, content: str, parse_multi_xpath=parse_multi_xpath):
        for element_content in parse_multi_xpath(content, self.elements_xpath):
            self._elements.append(self.model(element_content))

        return self

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError()

        return self._elements[key]
