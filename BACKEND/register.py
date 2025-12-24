import cgi
import cgitb
import mysql.connector
cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="your_mysql_password", database="flight_booking")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        print("<h3>Username already exists. Please choose another.</h3>")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("<h3>Registration successful!</h3>")
except mysql.connector.Error as err:
    print(f"<h3>Database Error: {err}</h3>")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
