import pytest

from academico.security import RSA


class TestRSA:
    def test_encrypt(self):
        key = RSA('c5988dd3f7ea9b92602d0079f41083a1', 'cd6a3683ced2ab919dad4bdc13dfdd4d')

        result = key.encrypt('arbitrarystr')

        assert result == '2ceb706b0e003adc2d889825c792c4ae'
