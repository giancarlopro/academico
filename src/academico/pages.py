from academico.core.pages import Page
from academico.models import Boletim


class AcademicoRootPage(Page):
    url = 'https://academico.iff.edu.br/qacademico/index.asp'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }


class BoletimPage(AcademicoRootPage):
    params = {'t': '2032'}
    models = {
        'boletim': Boletim
    }
