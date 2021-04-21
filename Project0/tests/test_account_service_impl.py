import unittest
from services.account_service_impl import AccountServiceImpl
from models.client import Client


class TestAccountService(unittest.TestCase):

    def test_create_account(self):
        assert AccountServiceImpl.create_account(1, 20)

    def test_get_all_accounts_for_client(self):
        assert AccountServiceImpl.create_account(1, 20)

    def test_get_all_accounts_in_range(self):
        assert AccountServiceImpl.get_all_accounts_in_range(1, 0, 5000)

    def test_get_account_with_id(self):
        assert AccountServiceImpl.get_account_with_id(1, 3)

    def test_update_account_with_id(self):
        assert AccountServiceImpl.update_account_with_id(1, 3, 500)

    def test_delete_account_with_id(self):
        assert AccountServiceImpl.delete_account_with_id(1, 3)

    def test_withdraw_from_account(self):
        assert AccountServiceImpl.withdraw_from_account(1, 15, 3)

    def test_deposit_into_account(self):
        assert AccountServiceImpl.deposit_into_account(1, 15, 300)

    def test_transfer_funds(self):
        assert AccountServiceImpl.transfer_funds(1, 4, 3, 20)


if __name__ == '__main__':
    unittest.main()
