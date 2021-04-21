from abc import abstractmethod, ABC


class AccountDAO(ABC):

    @abstractmethod
    def create_account(self, client_id, amount):
        pass

    @abstractmethod
    def get_all_accounts_for_client(self, client_id):
        pass

    @abstractmethod
    def get_all_accounts_in_range(self, client_id, range1, range2):
        pass

    @abstractmethod
    def get_account_with_id(self, client_id, account_id):
        pass

    @abstractmethod
    def update_account_with_id(self, client_id, account_id, amount):
        pass

    @abstractmethod
    def delete_account_with_id(self, client_id, account_id):
        pass

    @abstractmethod
    def withdraw_from_account(self, client_id, account_id, amount):
        pass

    @abstractmethod
    def deposit_into_account(self, client_id, account_id, amount):
        pass

    @abstractmethod
    def transfer_funds(self, client_id, account_idw, account_idd, amount):
        pass
