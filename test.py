import logging
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

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
    try:
        if request.method == 'POST':
            username = request.form['uname']
            user_age = fetch_user_age(username)

            if user_age is not None:
                print(f"Age fetched successfully for user {username}. Age: {user_age}")
                return f"Age fetched successfully for user {username}. Age: {user_age}"
            else:
                return "User not found or age not available."
    except Exception as e:
        logging.error("An error occurred: %s", e)
        return "An error occurred."

if __name__ == '__main__':
    app.run(debug=True)
