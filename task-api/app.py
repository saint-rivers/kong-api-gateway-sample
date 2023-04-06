import datetime
from flask import Flask, jsonify
import requests
import os

user_api_url = "http://localhost:5002"


def env_setup():
    if os.environ["USER_API"] != None:
        user_api_url = os.environ["USER_API"]

    return user_api_url


user_api_url = env_setup()

app = Flask(__name__)


@app.route('/hello/', methods=['GET'])
def welcome():
    return jsonify({
        'message': 'hello world',
        'timestamp': datetime.datetime.now()
    })


@app.route('/api/v1/tasks', methods=['GET'])
def get_task():
    return jsonify({
        'tasks': [
            {
                "name": "do reactjs homework",
                "isCompleted": True,
                "user": requests.get(f'{user_api_url}/api/v1/users/{1}').json()
            },
            {
                "name": "buy groceries",
                "isCompleted": False,
                "user": requests.get(f'{user_api_url}/api/v1/users/{1}').json()
            },
            {
                "name": "take out trash",
                "isCompleted": False,
                "user": requests.get(f'{user_api_url}/api/v1/users/{42}').json()
            },
            {
                "name": "do spring boot homework",
                "isCompleted": True,
                "user": requests.get(f'{user_api_url}/api/v1/users/{37}').json()
            },
        ]
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
