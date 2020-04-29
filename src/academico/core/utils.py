from lxml import etree
import re
import requests

from academico.security import RSA

def parse_xpath(content: str, xpath: str) -> str:
    tree = etree.HTML(content)

    return tree.xpath(xpath)[0].text.strip()

def parse_regex(content: str, regex: str) -> str:
    return re.search(regex, content).group(0)

def create_session():
    s = requests.Session()
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    })
    return s

def create_rsa_key(session):
    url = 'https://academico.iff.edu.br/qacademico/lib/rsa/gerador_chaves_rsa.asp'
    keyrx = r'RSAKeyPair\(\s+\"(\w+).*\s+.*\s+\"(\w+)\"\s+\)'

    r = session.get(url)
    match = re.search(keyrx, r.text)
    return RSA(match.group(1), match.group(2))

def create_logged_session(login, senha):
    session = create_session()

    url = 'https://academico.iff.edu.br/qacademico/lib/validalogin.asp'

    clean_data = {
        'LOGIN': login,
        'SENHA': senha,
        'TIPO_USU': '1',
        'Submit': 'OK'
    }

    key = create_rsa_key(session)

    data = {k: key.encrypt(v) for k,v in clean_data.items()}

    r = session.post(url, data=data)

    if r.status_code != 200:
        raise Exception('Não foi possível realizar o login')

    return session
