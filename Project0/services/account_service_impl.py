from services.account_service import AccountService
from daos.account_dao_impl import AccountDAOImpl
from models.account import Account


class AccountServiceImpl(AccountService):

    @classmethod
    def create_account(cls, client_id, amount):
        return AccountDAOImpl.create_account(int(client_id), int(amount))

    @classmethod
    def get_all_accounts_for_client(cls, client_id):
        accounts = [account.json() for account in AccountDAOImpl.get_all_accounts_for_client(int(client_id))]
        return accounts

    @classmethod
    def get_all_accounts_in_range(cls, client_id, range1, range2):
        accounts = [account.json() for account in
                    AccountDAOImpl.get_all_accounts_in_range(int(client_id), int(range1), int(range2))]
        return accounts

    @classmethod
    def get_account_with_id(cls, client_id, account_id):
        ret = [account.json() for account in AccountDAOImpl.get_account_with_id(int(client_id), int(account_id))]
        if not ret:
            return "Not a valid account"
        return ret

    @classmethod
    def update_account_with_id(cls, client_id, account_id, amount):
        ret = AccountDAOImpl.update_account_with_id(int(client_id), int(account_id), int(amount))
        if not ret:
            return "Not a valid account"
        return ret

    @classmethod
    def delete_account_with_id(cls, client_id, account_id):

        return AccountDAOImpl.delete_account_with_id(int(client_id), int(account_id))

    @classmethod
    def withdraw_from_account(cls, client_id, account_id, amount):
        return AccountDAOImpl.withdraw_from_account(int(client_id), int(account_id), int(amount))

    @classmethod
    def deposit_into_account(cls, client_id, account_id, amount):
        return AccountDAOImpl.deposit_into_account(int(client_id), int(account_id), int(amount))

    @classmethod
    def transfer_funds(cls, client_id, account_idw, account_idd, amount):
        return AccountDAOImpl.transfer_funds(int(client_id), int(account_idw), int(account_idd), int(amount))
