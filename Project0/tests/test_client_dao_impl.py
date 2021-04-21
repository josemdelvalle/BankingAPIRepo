import unittest
from daos.client_dao_impl import ClientDAOImpl
from models.client import Client


class TestClientDAO(unittest.TestCase):

    def test_get_all_clients(self):
        assert ClientDAOImpl.get_all_clients()

    def test_get_client(self):
        assert ClientDAOImpl.get_client(1)

    def test_create_client(self):
        assert ClientDAOImpl.create_client("Daniel")

    def test_update_client(self):
        client = Client(5, "Rose")
        assert ClientDAOImpl.update_client(client)

    def test_delete_client(self):
        assert ClientDAOImpl.delete_client(16)


if __name__ == '__main__':
    unittest.main()
