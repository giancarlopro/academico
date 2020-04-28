from academico.core.models import Model


class TestModel:
    def test_parameters_creation(self):
        class FieldMock:
            def parse_value(self, contnet):
                return 100

        model = Model('<html><body>100</body></html>')
        model.fields['field'] = FieldMock()

        assert model.field == 100
