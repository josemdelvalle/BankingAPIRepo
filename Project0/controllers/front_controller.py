from controllers import client_controller


def route(app):
    # Calls all other other controllers
    client_controller.route(app)

