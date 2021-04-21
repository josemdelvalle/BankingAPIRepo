from .account_dao import AccountDAO
from models.client import Client
from models.account import Account
from util.db_connection import connection


class AccountDAOImpl(AccountDAO):
    @classmethod
    def create_account(cls, client_id, amount):
        sql = f"insert into accounts values (default, {client_id}, {amount} );"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Account created", 201

    @classmethod
    def get_all_accounts_for_client(cls, client_id):
        sql = f"select * from accounts  where client_id ={client_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        accounts = [Account(elem[0], elem[1], elem[2]) for elem in records]
        return accounts

    @classmethod
    def get_all_accounts_in_range(cls, client_id, range1, range2):
        sql = f"SELECT * FROM accounts  where client_id ={client_id} AND amount BETWEEN {range1} AND {range2};"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        accounts = [Account(elem[0], elem[1], elem[2]) for elem in records]
        return accounts

    @classmethod
    def get_account_with_id(cls, client_id, account_id):
        sql = f"SELECT * FROM(SELECT * FROM accounts  where client_id = {client_id}) m WHERE id ={account_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        accounts = [Account(elem[0], elem[1], elem[2]) for elem in records]
        return accounts

    @classmethod
    def update_account_with_id(cls, client_id, account_id, amount):
        sql = f"UPDATE accounts SET amount ={amount} WHERE id = {account_id} AND client_id={client_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Account updated", 200

    @classmethod
    def delete_account_with_id(cls, client_id, account_id):
        account = cls.get_account_with_id(client_id, account_id)
        if not account:
            return "no account or client exists", 404
        sql = f"DELETE FROM accounts WHERE id = {account_id} AND client_id={client_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Deleted account"

    @classmethod
    def withdraw_from_account(cls, client_id, account_id, amount):
        account = cls.get_account_with_id(client_id, account_id)
        if not account:
            return "no account or client exists", 404
        elif account[0].amount - amount < 0:
            return "insufficient funds", 422
        else:
            sql = f"UPDATE accounts SET amount ={account[0].amount - amount} WHERE id = {account_id} AND client_id={client_id};"
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()

        return "withdraw complete", 200

    @classmethod
    def deposit_into_account(cls, client_id, account_id, amount):
        account = cls.get_account_with_id(client_id, account_id)
        if not account:
            return "no account or client exists", 404
        else:
            sql = f"UPDATE accounts SET amount ={amount + account[0].amount} WHERE id = {account_id} AND client_id={client_id};"
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()

        return "deposit complete", 200

    @classmethod
    def transfer_funds(cls, client_id, account_idw, account_idd, amount):
        account = cls.get_account_with_id(client_id, account_id=account_idw)
        if not account:
            return "no account or client exists", 404
        elif account[0].amount - amount < 0:
            return "insufficient funds", 422
        else:
            sql = f"UPDATE accounts SET amount ={account[0].amount - amount} WHERE id = {account_idw} AND client_id={client_id};" \
                  f"UPDATE accounts SET amount ={amount + account[0].amount} WHERE id = {account_idd} AND client_id={client_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "transfer complete", 200
