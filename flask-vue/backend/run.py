from flask import Flask, render_template, jsonify
from random import randint
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
PORT = 8010

@app.route('/', defaults={'path': ''})


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=int(PORT), debug=True)