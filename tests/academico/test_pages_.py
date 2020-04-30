import pytest

from academico.pages import BoletimPage


class TestBoletimPage:
    @pytest.fixture
    def page(self):
        return BoletimPage(ano=2020, periodo=1)

    def test_get_params(self, page: BoletimPage):
        params = page.get_params({})

        assert params['t'] == '2032'
        assert params['cmbanos'] == 2020
        assert params['cmbperiodos'] == 1
