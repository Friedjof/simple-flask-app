import peewee
from flask import Flask, request, jsonify
from random import randint
import os

app = Flask(__name__)

DATABASE_PATH = "data/users.db"

db = peewee.SqliteDatabase(DATABASE_PATH)

class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()


@app.route('/user', methods=['GET'])
def get_user():
    data = request.args
    
    if 'username' in data and 'password' in data:
        User.create(username=data['username'], password=data['password'])
        return jsonify({'success': 'User created'}), 201
    else:
        users = User.select()
        return jsonify({'users': [user.username for user in users]})

@app.route('/login', methods=['GET'])
def login():
    data = request.args
    user = User.get_or_none(username=data['username'], password=data['password'])
    if user:
        return jsonify({'success': 'User logged in'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


if not os.path.exists(DATABASE_PATH) or not os.path.isfile(DATABASE_PATH):
    db.create_tables([User])


if os.path.exists(DATABASE_PATH) and os.path.isfile(DATABASE_PATH):
    os.remove(DATABASE_PATH)
    db.create_tables([User])
    print("Database removed and created again")


if not User.get_or_none(username='admin'):
    admin = User.get_or_create(
        username='admin', password=''.join([str(randint(0, 9)) for _ in range(10)]))[0]
print(f"Admin is {admin.username} and password is {admin.password}")
