import unittest
from services.client_service_impl import ClientServiceImpl
from models.client import Client


class TestClientService(unittest.TestCase):

    def test_get_all_clients(self):
        assert ClientServiceImpl.get_all_clients()

    def test_get_client(self):
        assert ClientServiceImpl.get_client(1)

    def test_create_client(self):
        assert ClientServiceImpl.create_client(client_name="jose")

    def test_update_client(self):
        client = Client(1, "jose")
        assert ClientServiceImpl.update_client(client)

    def test_delete_client(self):
        assert ClientServiceImpl.delete_client(12)


if __name__ == '__main__':
    unittest.main()
