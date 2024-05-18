from flask import Flask, jsonify
import sqlite3
import random

import create_database as db

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('clone_wars_quotes.db')
    conn.row_factory = sqlite3.Row
    return conn

db.create_database()

# all quotes

@app.route('/quotes', methods=['GET'])
def get_quotes():
    conn = get_db_connection()
    quotes = conn.execute('SELECT * FROM CLONE_WARS_QUOTES').fetchall()
    conn.close()
    quotes_list = [dict(quote) for quote in quotes]
    return jsonify(quotes_list)


#create a quotes by language method

@app.route('/quotes/<language>', methods=['GET'])
def get_quotes_by_language(language):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Obtener el id del idioma
    cursor.execute('SELECT id FROM LANGUAGES WHERE language = ?', (language,))
    language_row = cursor.fetchone()
    
    if language_row is None:
        return jsonify({"error": "Language not found"}), 404
    
    language_id = language_row['id']
    
    # Obtener las citas en el idioma especificado
    cursor.execute('SELECT * FROM CLONE_WARS_QUOTES WHERE language_id = ?', (language_id,))
    quotes = cursor.fetchall()
    conn.close()
    
    quotes_list = [dict(quote) for quote in quotes]
    return jsonify(quotes_list)


# quotes by id

@app.route('/quotes/<int:quote_id>', methods=['GET'])
def get_id_quote(quote_id):
    conn = get_db_connection()
    quote = conn.execute('SELECT * FROM CLONE_WARS_QUOTES WHERE id = ?', (quote_id,)).fetchone()
    conn.close()
    if not quote:
        return jsonify({'error': 'No quotes found'}), 404
    return jsonify(dict(quote))


#create random quotes by language method

@app.route('/quotes/random/<language>', methods=['GET'])
def get_random_quotes_by_language(language):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Obtener el id del idioma
    cursor.execute('SELECT id FROM LANGUAGES WHERE language = ?', (language,))
    language_row = cursor.fetchone()
    
    if language_row is None:
        return jsonify({"error": "Language not found"}), 404
    
    language_id = language_row['id']
    
    # Obtener las citas en el idioma especificado
    cursor.execute('SELECT * FROM CLONE_WARS_QUOTES WHERE language_id = ?', (language_id,))
    quotes = cursor.fetchall()
    conn.close()

    random_quote = random.choice(quotes)
    return jsonify(dict(random_quote))


#languages list

@app.route('/languages', methods=['GET'])
def languages_list():
    conn = get_db_connection()
    quotes = conn.execute('SELECT * FROM LANGUAGES').fetchall()
    conn.close()
    quotes_list = [dict(quote) for quote in quotes]
    return jsonify(quotes_list)


if __name__ == '__main__':
    app.run(debug=False)
