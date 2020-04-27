import os


class RSA:
    """Wrapper object to use javascript RSA encryption using exponent and modulus"""
    def __init__(self, e, n):
        self.e = e
        self.n = n

    def encrypt(self, text):
        """Encrypt text using public key exponent and modulus

        e - Public exponent
        n - Modulus

        It uses node to be compatible with the browser version of QAcademico
        """
        path = os.path.dirname(__file__) + '/encrypt.js'
        stream = os.popen(f'node {path} {self.e} {self.n} {text}')
        return stream.read()[:-1]
