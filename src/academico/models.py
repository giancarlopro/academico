from academico.core.models import Model
from academico.core.fields import IntegerField, StringField, FloatField, ModelField


class Disciplina(Model):
    fields = {
        'componente_curricular': StringField('//td[1]/a'),
        'carga_horaria': IntegerField('//td[2]'),
        'turma': StringField('//td[3]'),
        'total_faltas': IntegerField('//td[4]'),
        'media_final': FloatField('//td[5]'),
        'nota': FloatField('//td[6]'),
        'faltas': IntegerField('//td[7]'),
        'situacao': StringField('//td[8]')
    }


class Boletim(Model):
    fields = {
        'ano': IntegerField('//*[@id="cmbanos"]/option[@selected]'),
        'periodo': IntegerField('//*[@id="cmbperiodos"]/option[@selected]'),
        'media_disciplinas': FloatField('/html/body/table/tr[2]/td/table/tr[2]/td[2]/table[5]/tr[1]/td[2]/div'),
        'rendimento_global': FloatField('/html/body/table/tr[2]/td/table/tr[2]/td[2]/table[5]/tr[1]/td[5]/div'),
        'coeficiente_rendimento': FloatField('/html/body/table/tr[2]/td/table/tr[2]/td[2]/table[5]/tr[1]/td[8]/div'),
        'situacao': StringField('/html/body/table/tr[2]/td/table/tr[2]/td[2]/table[5]/tr[2]/td[2]/div'),
        'disciplinas': ModelField(Disciplina, '/html/body/table/tr[2]/td/table/tr[2]/td[2]/table[4]/tr[@class="conteudoTexto"]')
    }
