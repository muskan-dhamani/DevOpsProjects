from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="testdb",
        user="user",
        password="password"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_table;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return f"Data from DB: {rows}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

