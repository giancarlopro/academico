from academico.core.pages import Page
from academico.models import Boletim


class AcademicoRootPage(Page):
    url = 'https://academico.iff.edu.br/qacademico/index.asp'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }


class BoletimPage(AcademicoRootPage):
    models = {
        'boletim': Boletim
    }

    def __init__(self, session=None, ano=None, periodo=None):
        super().__init__(session=session)
        self.ano = ano
        self.periodo = periodo

    def get_params(self, params: dict):
        params.update({'t': '2032'})

        if self.ano:
            params.update({'cmbanos': self.ano})
        if self.periodo:
            params.update({'cmbperiodos': self.periodo})

        return params
