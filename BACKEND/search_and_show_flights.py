#!C:/Python/python.exe
import cgi
from db_connect import cursor

print("Content-type:text/html\n")  # HTTP header

form = cgi.FieldStorage()          # Read form data
src = form.getvalue("source")      # Optional source
dst = form.getvalue("destination") # Optional destination
date = form.getvalue("date")       # Optional date

# If search parameters exist, filter flights
if src and dst and date:
    cursor.execute(
        "SELECT * FROM flights WHERE source=%s AND destination=%s AND date=%s",
        (src, dst, date)
    )
else:
    # Otherwise, show first 10 flights
    cursor.execute("SELECT * FROM flights LIMIT 10")

flights = cursor.fetchall()       # Fetch flight records

# Search form
print("""
<h2>Search Flights</h2>
<form method='get'>
    Source: <input name='source'>
    Destination: <input name='destination'>
    Date: <input type='date' name='date'>
    <button>Search</button>
</form>
<hr>
""")

# Display flights with booking form
if flights:
    print("<h2>Available Flights</h2>")
    for f in flights:
        print(f"""
        Flight ID: {f[0]} | {f[1]} | {f[2]} → {f[3]} | ₹{f[4]}
        <form action='book_flight.py' method='post'>
            <input type='hidden' name='fid' value='{f[0]}'>
            Passenger Name: <input name='name' required>
            <button>Book</button>
        </form><hr>
        """)
else:
    print("<h3>No flights found</h3>")
