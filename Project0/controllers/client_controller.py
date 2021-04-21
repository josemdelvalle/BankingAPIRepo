from services.client_service_impl import ClientServiceImpl
from services.account_service_impl import AccountServiceImpl
from models.client import Client
from flask import jsonify, request
import logging


def route(app):
    @app.route("/clients", methods=['POST'])
    def create_client():
        try:
            client_name = request.json['clientName']
            if client_name:
                if type(client_name) == str:
                    ClientServiceImpl.create_client(client_name)
                    logging.info(f"creating client {client_name}")
                    return "Client added", 200
                else:
                    raise ValueError
        except KeyError as e:
            return "Resource not found",400
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request

    @app.route("/clients/", methods=['GET'])
    def get_clients():
        logging.info(f"getting all clients")
        return jsonify(ClientServiceImpl.get_all_clients()), 200

    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            if client_id.isdigit():
                return jsonify(ClientServiceImpl.get_client(client_id=client_id))
            else:
                raise ValueError
        except ValueError as e:
            return "No such client exist", 404

    @app.route("/clients/<client_id>", methods=['PUT'])
    def update_client(client_id):
        logging.info(f"Updating client")
        try:
            if client_id.isdigit():
                client = Client(client_id, Client.json_parse(request.json).name)
                return ClientServiceImpl.update_client(client)
            else:
                raise ValueError
        except ValueError as e:
            return "No such client exist", 404

    @app.route("/clients/<client_id>", methods=['DELETE'])
    def delete_client(client_id):
        logging.info(f"Deleting Client")
        try:
            if client_id.isdigit():
                return ClientServiceImpl.delete_client(client_id)
            else:
                raise ValueError
        except ValueError as e:
            return "No such client exist", 404

    @app.route("/clients/<client_id>/accounts", methods=['POST'])
    def create_client_account(client_id):
        try:
            amount = request.json["amount"]
            if client_id.isdigit():
                client = ClientServiceImpl.get_client(client_id=client_id)
                if client == "Not a valid ID":
                    return "No such client exist", 404
                if amount.isdigit():
                    print("here")
                    logging.info(f"Creating account for client id={client_id}")
                    return AccountServiceImpl.create_account(client_id=client_id, amount=amount)
            else:
                raise ValueError

        except ValueError:
            return "No such client exist", 404

    @app.route("/clients/<client_id>/accounts/", methods=['GET'])
    def get_client_accounts(client_id):
        try:
            amount_greater_than = request.args.get("amountGreaterThan")
            amount_less_than = request.args.get("amountLessThan")
            if amount_less_than and amount_greater_than:

                if amount_less_than.isdigit() and amount_greater_than.isdigit() and client_id.isdigit():
                    return jsonify(
                        AccountServiceImpl.get_all_accounts_in_range(client_id, amount_less_than, amount_greater_than))
                else:
                    raise ValueError
            else:
                ret = AccountServiceImpl.get_all_accounts_for_client(client_id)
                print(ret)
                if ret == []:
                    raise ValueError
                else:
                    return jsonify(ret)
        except ValueError:
            return "no client exists", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['GET'])
    def get_client_account_with_id(client_id, account_id):
        try:
            if client_id.isdigit() and account_id.isdigit():
                client = ClientServiceImpl.get_client(client_id=client_id)
                if client == "Not a valid ID":
                    return "No such client exist", 404
            return jsonify(AccountServiceImpl.get_account_with_id(client_id, account_id))
        except ValueError:
            return "no client exists", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['PUT'])
    def update_account_with_id(client_id, account_id):
        try:
            amount = request.json["amount"]
            if client_id.isdigit() and account_id.isdigit() and amount.isdigit():
                account = AccountServiceImpl.get_account_with_id(client_id, account_id)
                if account == "Not a valid account":
                    return "Not a valid account", 404
                return AccountServiceImpl.update_account_with_id(client_id, account_id, amount)
            else:
                raise ValueError
        except ValueError:
            return "Not a valid ID", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['DELETE'])
    def delete_client_account_with_id(client_id, account_id):
        try:
            if client_id.isdigit() and account_id.isdigit():
                return AccountServiceImpl.delete_account_with_id(client_id, account_id)
            else:
                raise ValueError
        except ValueError:
            return "Not a valid ID", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['PATCH'])
    def withdraw_or_deposit_client_account_with_id(client_id, account_id):
        try:
            deposit = request.get_json().get("deposit")
            withdraw = request.get_json().get('withdraw')
            print(deposit)
            if deposit and isinstance(deposit, int):
                return AccountServiceImpl.deposit_into_account(client_id, account_id, deposit)
            if withdraw and isinstance(withdraw, int):
                return AccountServiceImpl.withdraw_from_account(client_id, account_id, withdraw)
            raise ValueError
        except ValueError:
            return "Not a valid ID", 404

    @app.route("/clients/<client_id>/accounts/<account_id>/transfer/<transfer_id>", methods=['PATCH'])
    def transfer_amount(client_id, account_id, transfer_id):
        amount = request.get_json().get('amount')
        if amount and isinstance(amount, int) and client_id.isdigit() and account_id.isdigit() and transfer_id.isdigit():
            return AccountServiceImpl.transfer_funds(client_id, account_id, transfer_id, amount)
        else:
            return "either client or account exists", 404
