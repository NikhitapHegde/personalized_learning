import logging
from flask import Flask, request, render_template, session

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Function to fetch age of the user from MySQL
def fetch_user_age(username):
    try:
        import mysql.connector

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Poornima16@23",
            database="student"
        )

        cursor = mydb.cursor()
        query = "SELECT age FROM details WHERE username = %s"
        cursor.execute(query, (username,))
        user_age = cursor.fetchone()

        cursor.close()
        mydb.close()

        return user_age[0] if user_age else None
    except mysql.connector.Error as error:
        logging.error("Error fetching data from MySQL: %s", error)
        return None

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/get_age', methods=['POST'])
def get_age():
    if request.method == 'POST':
        username = request.form['uname']
        user_age = fetch_user_age(username)

        if user_age is not None:
            session['current_user'] = username
            print(f"Age fetched successfully for user {username}. Age: {user_age}")
        else:
            print("User not found or age not available.")
    
    return "Age fetched successfully. Check the console for details."

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'  # Change this to a secure secret key for session management
    app.run(debug=True)
