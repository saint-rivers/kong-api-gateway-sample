from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        'userId': "1",
        'username': "tyler",
        'gender': 'male'
    },
    {
        'userId': "37",
        'username': "jameson",
        'gender': 'male'
    },
    {
        'userId': "42",
        'username': "amy",
        'gender': 'female'
    },
]


@app.route('/api/v1/users', methods=["GET"])
def get_users():
    return jsonify({
        'users': users
    })


@app.route('/api/v1/users/<user_id>', methods=["GET"])
def get_user_by_id(user_id):
    for user in users:
        if user['userId'] == user_id:
            return jsonify(user)

    return jsonify({
        'message': 'user not found',
        'request': user_id
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
