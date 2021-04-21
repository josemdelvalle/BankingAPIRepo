from flask import Flask, jsonify
from controllers import front_controller as fc
import logging

app = Flask(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info('Started')
fc.route(app)

if __name__ == '__main__':
    app.run(debug=True)
