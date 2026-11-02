import os
import sqlite3
from flask import Flask, request
import ast

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")  # read from environment variable


def get_user(username):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE users (username TEXT)')
    cur.execute('INSERT INTO users (username) VALUES (?)', ('test',))
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cur.fetchall()
    conn.close()
    return result


@app.route('/user')
def user():
    return str(get_user(request.args.get('username', '')))


@app.route('/calc')
def calc():
    expr = request.args.get('expr', '1')
    try:
        return str(ast.literal_eval(expr))  # safely evaluate expression
    except Exception:
        return 'Error in expression', 400


if __name__ == '__main__':
    app.run(debug=False)
