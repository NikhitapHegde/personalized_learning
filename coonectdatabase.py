import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Poornima16@23",
    database="student"
)

uname = input("Enter your username: ")

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

#  Fetch only the age for a given username
table_name = "users"
query_age = f"SELECT age FROM {table_name} WHERE username = '{uname}'"

# Execute the query
cursor.execute(query_age)

# Fetch only one value (age)
age = cursor.fetchone()

if age:
    print(f"The age of user {uname} is: {age[0]}")
else:
    print(f"User {uname} not found or age not available.")

# Fetch all contents from the specified table
table_info_name = "user_" + uname
query_info = f"SELECT * FROM {table_info_name}"
cursor.execute(query_info)
info_result = cursor.fetchall()

if info_result:
    print(f"All information for user {uname}:")
    for row in info_result:
        print(row)
    score_list=info_result[-1]
    print("recent score",score_list[1:7])
else:
    print(f"User {uname} not found or information not available.")
    score_list=("0","0","0","0",0)

# Insert new values into the specified table
from start import start
new_values=start(age,score_list[1:7])



query_insert_values = f"INSERT INTO {table_info_name} (addition, subtraction, multiplication, division, english,progress) VALUES(%s, %s, %s, %s, %s, %s)"
cursor.execute(query_insert_values, new_values)

# Commit the changes to the database
mydb.commit()
print(f"New values {new_values} inserted successfully into {table_info_name} for user {uname}.")

# Close the cursor and database connection
cursor.close()
mydb.close()
