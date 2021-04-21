from services.client_service import ClientService
from daos.client_dao_impl import ClientDAOImpl
import json


class ClientServiceImpl(ClientService):
    # dao = ClientDAOImpl()

    @classmethod
    def get_all_clients(cls):
        clients = [client.json() for client in ClientDAOImpl.get_all_clients()]
        return clients

    @classmethod
    def get_client(cls, client_id):
        client = [client.json() for client in ClientDAOImpl.get_client(client_id)]
        if not client:
            return "Not a valid ID"
        return client

    @classmethod
    def create_client(cls, client_name):
        ClientDAOImpl.create_client(str(client_name))
        return "ok"

    @classmethod
    def update_client(cls, client):
        return ClientDAOImpl.update_client(client)

    @classmethod
    def delete_client(cls, client_id):
        return ClientDAOImpl.delete_client(int(client_id))
