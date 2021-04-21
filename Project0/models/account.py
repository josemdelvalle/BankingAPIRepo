class Account:
    def __init__(self, account_id=0, client_id=0, amount=0):
        self.account_id = account_id
        self.client_id = client_id
        self.amount = amount

    def get_account_id(self):
        return self.account_id

    def get_client_id(self):
        return self.client_id

    def deposit(self, deposit):
        self.amount = self.amount + deposit

    def withdraw(self, withdraw):
        self.amount = self.amount - withdraw

    def json(self):
        return {
            'accountId': self.account_id,
            'clientId': self.client_id,
            'amount': self.amount
        }

    @staticmethod
    def json_parse(json, client_id):
        account = Account()
        account.client_id = json["clientId"]
        account.amount = json["amount"]
        return account
