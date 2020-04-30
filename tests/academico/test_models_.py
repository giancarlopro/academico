import pytest
import os

from academico.models import Boletim


class TestBoletimModel:
    def test_parse_fields(self):
        path = os.path.join(os.path.dirname(__file__), 'boletim.html')

        with open(path) as file:
            content = file.read()

        boletim = Boletim(content)

        assert boletim.ano == 2019
        assert boletim.periodo == 2
        assert boletim.media_disciplinas == 7.4
        assert boletim.rendimento_global == 0.0
        assert boletim.coeficiente_rendimento == 7.76
        assert boletim.situacao == 'Aprovado'

        assert boletim.disciplinas[0].componente_curricular == 'Informática e Sociedade'
        assert boletim.disciplinas[0].carga_horaria == 40
        assert boletim.disciplinas[0].turma == '54 - 20192.120.6N'
        assert boletim.disciplinas[0].total_faltas == 6
        assert boletim.disciplinas[0].media_final == 7.7
        assert boletim.disciplinas[0].nota == 7.7
        assert boletim.disciplinas[0].faltas == 6
        assert boletim.disciplinas[0].situacao == 'Aprovado'

        assert boletim.disciplinas[1].componente_curricular == 'Empreendedorismo'
        assert boletim.disciplinas[1].carga_horaria == 40
        assert boletim.disciplinas[1].turma == '54 - 20192.120.6N'
        assert boletim.disciplinas[1].total_faltas == 0
        assert boletim.disciplinas[1].media_final == 8.1
        assert boletim.disciplinas[1].nota == 8.1
        assert boletim.disciplinas[1].faltas == 0
        assert boletim.disciplinas[1].situacao == 'Aprovado'

        assert boletim.disciplinas[2].componente_curricular == 'Gestão do Conhecimento'
        assert boletim.disciplinas[2].carga_horaria == 60
        assert boletim.disciplinas[2].turma == '54 - 20192.120.6N'
        assert boletim.disciplinas[2].total_faltas == 0
        assert boletim.disciplinas[2].media_final == 7.4
        assert boletim.disciplinas[2].nota == 7.4
        assert boletim.disciplinas[2].faltas == 0
        assert boletim.disciplinas[2].situacao == 'Aprovado'

        assert boletim.disciplinas[3].componente_curricular == 'Gerência de Projetos'
        assert boletim.disciplinas[3].carga_horaria == 80
        assert boletim.disciplinas[3].turma == '54 - 20192.120.6N'
        assert boletim.disciplinas[3].total_faltas == 0
        assert boletim.disciplinas[3].media_final == 6.0
        assert boletim.disciplinas[3].nota == 6.0
        assert boletim.disciplinas[3].faltas == 0
        assert boletim.disciplinas[3].situacao == 'Aprovado'

        assert boletim.disciplinas[4].componente_curricular == 'Qualidade de Software'
        assert boletim.disciplinas[4].carga_horaria == 60
        assert boletim.disciplinas[4].turma == '54 - 20192.120.6N'
        assert boletim.disciplinas[4].total_faltas == 3
        assert boletim.disciplinas[4].media_final == 6.4
        assert boletim.disciplinas[4].nota == 6.4
        assert boletim.disciplinas[4].faltas == 3
        assert boletim.disciplinas[4].situacao == 'Aprovado'

        assert boletim.disciplinas[5].componente_curricular == 'Laboratório de Orientação a Objetos'
        assert boletim.disciplinas[5].carga_horaria == 80
        assert boletim.disciplinas[5].turma == '54 - 20192.120.6N'
        assert boletim.disciplinas[5].total_faltas == 0
        assert boletim.disciplinas[5].media_final == 8.7
        assert boletim.disciplinas[5].nota == 8.7
        assert boletim.disciplinas[5].faltas == 0
        assert boletim.disciplinas[5].situacao == 'Aprovado'
