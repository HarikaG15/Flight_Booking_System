#!C:/Python/python.exe
from db_connect import cursor      # Import database cursor

print("Content-type:text/html\n")  # HTTP header

# Fetch all bookings from database
cursor.execute("SELECT * FROM bookings")

# Loop through each booking and display details
for b in cursor.fetchall():
    print(f"""
    Passenger: {b[0]}               <!-- Passenger name -->
    | Flight: {b[2]}                <!-- Airline / Flight -->
    | Amount: ₹{b[4]}               <!-- Price paid -->
    | Date: {b[5]}                   <!-- Booking date -->
    | PNR: {b[6]}                    <!-- PNR number -->
    <a href='../tickets/{b[6]}.pdf'>Download</a>  <!-- Link to PDF ticket -->
    <hr>
    """)
