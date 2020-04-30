import requests


class Page:
    url = None
    models = {}

    def __init__(self, session=None):
        self.extracted_data = {}
        self.session = session
        self.params = None
        self.headers = None

    def extract(self):
        session = self.get_session(self.session)
        url = self.get_url(self.url or '')
        params = self.get_params(self.params or {})
        headers = self.get_headers(self.headers or {})

        response = session.get(url, params=params, headers=headers)

        for name, model in self.models.items():
            self.extracted_data[name] = model(response.text)

    def get_session(self, session):
        return session

    def get_url(self, url):
        return url

    def get_params(self, params):
        return params

    def get_headers(self, headers):
        return headers

    def __getattr__(self, name):
        if name in self.extracted_data:
            return self.extracted_data[name]
        elif name in self.models:
            raise Exception('chame extract() antes de utilizar')
        else:
            raise AttributeError()
