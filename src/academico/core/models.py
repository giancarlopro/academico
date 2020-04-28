class Model:
    """Base class for all models

    Usage:
    >>> class AgeModel(Model):
    >>>     fields = {
    >>>         'age': IntegerField('/html/body/div')
    >>>     }

    >>> model = AgeModel('<html><body><div>15</div></body></html>')
    >>> model.age
    15
    """
    fields = {}
    _cached_fields = {}

    def __init__(self, content):
        self.content = content

    def __getattr__(self, name):
        if name in self._cached_fields:
            return self._cached_fields[name]
        elif name in self.fields:
            x = self._cached_fields[name] = self.fields[name].parse_value(self.content)
            return x
        raise AttributeError()
