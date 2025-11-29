from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-RRA9HP9;"
        "DATABASE=students;"
        "Trusted_Connection=yes;"
    )
    return conn

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    
    users = []
    for row in rows:
        users.append({
            "Id": row.Id,
            "Name": row.Name,
            "Age": row.Age
        })
    
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
