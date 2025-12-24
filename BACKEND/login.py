#!C:/Python/python.exe
import cgi                         # CGI module
from db_connect import cursor      # Database cursor
print("Content-type:text/html\n")  # HTTP header
form = cgi.FieldStorage()          # Read form data
u = form.getvalue("username")      # Get username
p = form.getvalue("password")      # Get password
# Check user in database
cursor.execute(
    "SELECT * FROM users WHERE username=%s AND password=%s",
    (u, p)
)
user = cursor.fetchone()           # Fetch result
if user:                           # If user exists
    print("<h3>Login Successful</h3>")
    print("<a href='../frontend/search.html'>Search Flights</a>")
else:                              # If login fails
    print("<h3 style='color:red'>Invalid Login Try Again!!</h3>")
