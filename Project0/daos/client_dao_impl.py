from .client_dao import ClientDAO
from models.client import Client
from util.db_connection import connection
from models.client import Client


class ClientDAOImpl(ClientDAO):
    # db = TempDB()

    @classmethod
    def get_all_clients(cls):
        sql = "SELECT * FROM clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        clients = [Client(elem[0], elem[1]) for elem in records]
        return clients

    @classmethod
    def get_client(cls, client_id):
        sql = f" select * from clients where id = {client_id} "
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        client = [Client(elem[0], elem[1]) for elem in records]
        return client

    @classmethod
    def create_client(cls, client_name):
        sql = f"insert into clients values (default, '{client_name}');"
        print(sql)
        cursor = connection.cursor()
        print(cursor.execute(sql))
        connection.commit()

    @classmethod
    def update_client(cls, client):
        sql = f"UPDATE clients SET client_name = '{client.name}'WHERE id = {int(client.client_id)} RETURNING client_name;"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        record = cursor.fetchone()
        if record:
            return "Done!"
        return "no such client exist", 404

    @classmethod
    def delete_client(cls, client_id):

        sql = f"DELETE FROM clients WHERE id ={client_id} RETURNING client_name;"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        record = cursor.fetchone()
        if record:
            return "Success!", 205
        return "no such client exist", 404
