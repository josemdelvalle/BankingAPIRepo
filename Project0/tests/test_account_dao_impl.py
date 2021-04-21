import unittest
from daos.account_dao_impl import AccountDAOImpl
from models.client import Client


class TestAccountDAO(unittest.TestCase):

    def test_create_account(self):
        assert AccountDAOImpl.create_account(1, 100)

    def test_get_all_accounts_for_client(self):
        assert AccountDAOImpl.get_account_with_id(1, 2)

    def test_get_all_accounts_in_range(self):
        assert AccountDAOImpl.get_all_accounts_in_range(1, 0, 5000)

    def test_get_account_with_id(self):
        assert AccountDAOImpl.get_account_with_id(1, 13)

    def test_update_account_with_id(self):
        assert AccountDAOImpl.update_account_with_id(1, 13, 900)

    def test_delete_account_with_id(self):
        assert AccountDAOImpl.delete_account_with_id(1, 15)

    def test_withdraw_from_account(self):
        assert AccountDAOImpl.withdraw_from_account(1, 5, 10)

    def test_deposit_into_account(self):
        assert AccountDAOImpl.deposit_into_account(1, 3, 40)

    def test_transfer_funds(self):
        assert AccountDAOImpl.transfer_funds(1,4,16)


if __name__ == '__main__':
    unittest.main()
