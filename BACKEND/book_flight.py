#!C:/Python/python.exe
import cgi
import random
from datetime import datetime, timedelta
from db_connect import cursor, db
from fpdf import FPDF

print("Content-type:text/html\n")  # HTTP header

form = cgi.FieldStorage()          # Read form data
fid = form.getvalue("fid")         # Flight ID
name = form.getvalue("name")       # Passenger name

now = datetime.now()               # Current time

# Get flight details
cursor.execute(
    "SELECT airline, departure_city, arrival_city, base_price FROM flights WHERE flight_id=%s",
    (fid,)
)
airline, dep, arr, base = cursor.fetchone()

# Delete old booking attempts (older than 10 mins)
cursor.execute(
    "DELETE FROM booking_attempts WHERE attempt_time < %s",
    (now - timedelta(minutes=10),)
)

# Insert new booking attempt
cursor.execute(
    "INSERT INTO booking_attempts VALUES(%s, %s)",
    (fid, now)
)

# Count booking attempts in last 5 mins
cursor.execute(
    "SELECT COUNT(*) FROM booking_attempts WHERE flight_id=%s AND attempt_time >= %s",
    (fid, now - timedelta(minutes=5))
)
attempts = cursor.fetchone()[0]

# Calculate price with 10% increase if >=3 attempts in last 5 mins
price = int(base * 1.10) if attempts >= 3 else base

# Check wallet balance
cursor.execute("SELECT balance FROM wallet")
balance = cursor.fetchone()[0]

if balance < price:
    # Not enough money
    print("<h3 style='color:red'>Insufficient Wallet Balance</h3>")
else:
    # Deduct price from wallet
    cursor.execute("UPDATE wallet SET balance=%s", (balance - price,))

    # Generate a random PNR
    pnr = "PNR" + str(random.randint(1000, 9999))

    # Save booking in database
    cursor.execute(
        """INSERT INTO bookings VALUES(%s, %s, %s, %s, %s, %s, %s)""",
        (name, fid, airline, f"{dep} → {arr}", price, now, pnr)
    )

    db.commit()  # Save changes

    # Generate PDF ticket
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Flight Ticket", ln=True)
    pdf.cell(200, 10, f"Passenger: {name}", ln=True)
    pdf.cell(200, 10, f"Flight: {airline} ({fid})", ln=True)
    pdf.cell(200, 10, f"Route: {dep} → {arr}", ln=True)
    pdf.cell(200, 10, f"Price: ₹{price}", ln=True)
    pdf.cell(200, 10, f"PNR: {pnr}", ln=True)
    pdf.output(f"../tickets/{pnr}.pdf")  # Save PDF

    # Success message and link to download ticket
    print("<h3>Booking Successful</h3>")
    print(f"<a href='../tickets/{pnr}.pdf'>Download Ticket</a>")
