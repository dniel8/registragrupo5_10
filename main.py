import json
from flask import Flask
from flask_cors import CORS
from waitress import serve

from blueprints.party_blueprints import party_blueprints

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(party_blueprints)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to the senate elections administration software"}
    return response


# --------Config and execution code----------#
def load_config_file():
    with open("config.json", "r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_config_file()
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
