# flights_booking_System
# Flight Booking System

## Project Overview
This project is a database-driven Flight Booking System developed using
MySQL, basic Python, HTML, CSS, and basic JavaScript. The application
demonstrates core backend and database concepts such as flight search,
dynamic pricing, wallet validation, ticket PDF generation, and booking
history management.

The project was built by a student in the learning stage; therefore,
advanced frameworks and technologies were intentionally avoided while
still ensuring all functional requirements are met.

---

## Features Implemented

### 1. Flight Search Module
- 20 flights are seeded into the database.
- Flights are fetched directly from the database using SQL queries.
- Search is supported using **departure city and arrival city**.
- Each search returns a **minimum of 10 flights**, depending on availability.
- No static JSON, random generation, or external APIs are used.

---

### 2. Dynamic Pricing Engine
- Surge pricing is applied based on booking attempts.
- If the same flight is attempted 3 times within a short time window,
  the price increases by 10%.
- The final price is calculated dynamically during booking.

---

### 3. Wallet System
- Default wallet balance is set to **₹50,000**.
- Wallet balance is checked before booking.
- If the wallet balance is insufficient, a **clear validation error message**
  is displayed.
- On successful booking, the final ticket price is deducted from the wallet.

---

### 4. Ticket PDF Generation
- After every successful booking, a **downloadable PDF ticket** is generated.
- The PDF ticket includes:
  - Passenger Name
  - Airline Name and Flight ID
  - Route (Departure City → Arrival City)
  - Final Price Paid
  - Booking Date and Time
  - Unique PNR Number
- Each ticket is saved with a unique filename and can be re-downloaded later.

---

### 5. Booking History Page
- Complete booking history is stored in the database.
- The booking history page displays:
  - Flight details
  - Amount paid
  - Booking date and time
  - PNR number
  - Button to download the ticket again (PDF)
- Booking history data is fetched directly from the database.

---

### 6. Basic Authentication (Bonus)
- Basic **Login and Register** functionality implemented.
- Frontend created using HTML forms.
- Backend validation performed using Python and MySQL.
- Credentials are verified against the database.

---

## Technologies Used
- **Database:** MySQL  
- **Backend:** Python (basic level)  
- **Frontend:** HTML, CSS, basic JavaScript  
- **PDF Generation:** Python PDF library  
- **Tools:** XAMPP (MySQL), VS Code  

---

