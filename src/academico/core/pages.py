import requests


class Page:
    url = None
    params = None
    headers = None
    models = {}

    def __init__(self, session=None):
        self.extracted_data = {}
        self.session = session or self.get_session()

    def extract(self):
        url = self.get_url(self.url or '')
        params = self.get_params(self.params or {})
        headers = self.get_headers(self.headers or {})

        response = self.session.get(url, params=params, headers=headers)

        for name, model in self.models.items():
            self.extracted_data[name] = model(response.text)

    def get_session(self):
        return requests.Session()

    def get_url(self, url=None):
        return url

    def get_params(self, params=None):
        return params

    def get_headers(self, headers=None):
        return headers

    def __getattr__(self, name):
        if name in self.extracted_data:
            return self.extracted_data[name]
        elif name in self.models:
            raise Exception('chame extract() antes de utilizar')
        else:
            raise AttributeError()
