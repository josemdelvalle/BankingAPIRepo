class Client:
    def __init__(self, client_id=None, name="none"):
        self.client_id = client_id
        self.name = name

    def get_client_id(self):
        return self.client_id

    def json(self):
        return {
            'clientId': self.client_id,
            'clientName': self.name
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.name = json["clientName"]
        return client
