#!C:/Python/python.exe
import cgi
import cgitb
import os
# Enable CGI error reporting
cgitb.enable()

print("Content-type:text/html\n")

# Get form data
form = cgi.FieldStorage()
pnr = form.getvalue("pnr")

# Path to tickets folder
ticket_path = f"C:/path_to_your_project/tickets/{pnr}.pdf"

# Check if the ticket exists
if os.path.isfile(ticket_path):
    print(f'<h3>Your ticket is ready!</h3>')
    print(f'<a href="/tickets/{pnr}.pdf" download>Click here to download ticket</a>')
else:
    print(f'<h3>No ticket found for PNR: {pnr}</h3>')
    print('<a href="../frontend/download_ticket.html">Try again</a>')
