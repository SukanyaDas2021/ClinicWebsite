from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Clinic API!"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

import sqlite3

def init_db():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            appointment_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    # Logic to save appointment (sample code)
    pass

init_db()
