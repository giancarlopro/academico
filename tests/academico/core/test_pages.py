import pytest
import requests_mock
import requests

from academico.core.pages import Page
from academico.core.models import Model
from academico.core.fields import StringField


@pytest.fixture
def page():
    class MyModel(Model):
        fields = {
            'nome': StringField('/html/body/div[1]')
        }
    
    class MyPage(Page):
        url = 'http://localhost/'
        models = {
            'mymodel': MyModel
        }

    return MyPage(requests)


class TestPage:
    def test_extract(self, page):
        with requests_mock.Mocker() as m:
            m.get('http://localhost/', text="""
                <html>
                    <body>
                        <div>nome</div>
                        <div>Can't touch this</div>
                    </body>
                </html>
            """)

            with pytest.raises(Exception):
                page.mymodel

            page.extract()

            assert page.mymodel is not None
            assert page.mymodel.nome == 'nome'

            with pytest.raises(AttributeError):
                page.idade
