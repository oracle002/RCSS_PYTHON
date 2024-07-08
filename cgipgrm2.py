#!C:\Users\CCL39\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import mysql.connector
import cgitb; cgitb.enable()  # Enable detailed error messages

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    database='example',
    user='root',
    password=''
)
cursor = conn.cursor()

# Retrieve form data
form = cgi.FieldStorage()

# Extract values from the form
name = form.getvalue('name', '')
email = form.getvalue('email', '')
age = form.getvalue('age', '')
action = form.getvalue('action', '')

# Perform CRUD operations based on form action
print("Content-type: text/html\n\n")
print("<html><body>")

try:
    if action == 'insert':
        # Insert operation
        if name and email and age:
            sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, age))
            conn.commit()
            print("<h1>Data inserted successfully!</h1>")
        else:
            print("<h1>Form fields cannot be empty for insert operation!</h1>")

    elif action == 'update':
        # Update operation
        name = form.getvalue('name', '')
        if name and name and email and age:
            sql = "UPDATE users SET name = %s, email = %s, age = %s WHERE name = %s"
            cursor.execute(sql, (name, email, age, name))
            conn.commit()
            print("<h1>Data updated successfully!</h1>")
        else:
            print("<h1>Form fields or user ID cannot be empty for update operation!</h1>")

    elif action == 'delete':
        # Delete operation
        name = form.getvalue('name', '')
        if name:
            sql = "DELETE FROM users WHERE name = %s"
            cursor.execute(sql, (name,))
            conn.commit()
            print("<h1>Data deleted successfully!</h1>")
        else:
            print("<h1>User ID cannot be empty for delete operation!</h1>")

    elif action == 'read':
        # Read operation (Display all users)
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows:
            print("<h1>Users:</h1>")
            print("<ul>")
            for row in rows:
                print(f"<li>{row[0]} - {row[1]}, {row[2]}, {row[3]}</li>")
            print("</ul>")
        else:
            print("<h1>No users found!</h1>")

    else:
        print("<h1>Invalid action!</h1>")

except mysql.connector.Error as e:
    print(f"<h1>Database error: {e}</h1>")

print("</body></html>")

conn.close()
