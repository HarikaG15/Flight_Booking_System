import cgi                      # CGI module
from db_connect import cursor, db  # DB connection

print("Content-type:text/html\n")  # HTTP header

form = cgi.FieldStorage()       # Get form data

u = form.getvalue("username")   # Username
p = form.getvalue("password")   # Password

# Insert data into table
cursor.execute(
    "INSERT INTO users VALUES(%s,%s)", (u, p)
)

db.commit()                     # Save changes

print("<h3>Registration Successful</h3>")  # Success message
print("<a href='../frontend/login.html'>Login</a>")  # Login link
