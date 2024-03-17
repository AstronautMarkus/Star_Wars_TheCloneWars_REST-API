from flask import Flask, jsonify
import sqlite3
import random

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db_connection()
    with app.open_resource('script_database.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

initialize_database()

@app.route('/quotes', methods=['GET'])
def get_quotes():
    conn = get_db_connection()
    quotes = conn.execute('SELECT * FROM CLONE_WARS_QUOTES').fetchall()
    conn.close()
    quotes_list = [dict(quote) for quote in quotes]
    return jsonify(quotes_list)

@app.route('/quotes/random', methods=['GET'])
def get_random_quote():
    conn = get_db_connection()
    quotes = conn.execute('SELECT * FROM CLONE_WARS_QUOTES').fetchall()
    conn.close()
    if not quotes:
        return jsonify({'error': 'No quotes found'}, 404)
    random_quote = random.choice(quotes)
    return jsonify(dict(random_quote))

if __name__ == '__main__':
    app.run(debug=False)
