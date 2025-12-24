CREATE DATABASE flightdb;
USE flightdb;

-- USERS (LOGIN / REGISTER)
CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

-- FLIGHTS
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,
    airline VARCHAR(50),
    departure_city VARCHAR(50),
    arrival_city VARCHAR(50),
    base_price INT
);

-- SEED 10+ FLIGHTS
INSERT INTO flights VALUES
(101,'IndiGo','Delhi','Mumbai',2500),
(102,'Air India','Chennai','Delhi',2700),
(103,'Vistara','Hyderabad','Bangalore',2300),
(104,'SpiceJet','Mumbai','Pune',2000),
(105,'IndiGo','Bangalore','Kolkata',2900),
(106,'Air India','Delhi','Jaipur',2100),
(107,'Vistara','Chennai','Hyderabad',2400),
(108,'SpiceJet','Mumbai','Delhi',2800),
(109,'IndiGo','Pune','Goa',2200),
(110,'Air India','Kolkata','Delhi',3000),
(111,'IndiGo','Delhi','Chandigarh',1900),
(112,'SpiceJet','Ahmedabad','Mumbai',2600),
(113,'Vistara','Bangalore','Delhi',3100),
(114,'Air India','Lucknow','Delhi',2000),
(115,'IndiGo','Jaipur','Mumbai',2400),
(116,'SpiceJet','Goa','Bangalore',2300),
(117,'Vistara','Delhi','Hyderabad',2800),
(118,'Air India','Indore','Delhi',2100),
(119,'IndiGo','Nagpur','Mumbai',2200),
(120,'SpiceJet','Patna','Delhi',2700);
-- WALLET
CREATE TABLE wallet (
    balance INT
);
INSERT INTO wallet VALUES (50000);

-- BOOKING ATTEMPTS (SURGE PRICING)
CREATE TABLE booking_attempts (
    flight_id INT,
    attempt_time DATETIME
);

-- BOOKINGS
CREATE TABLE bookings (
    passenger VARCHAR(50),
    flight_id INT,
    airline VARCHAR(50),
    route VARCHAR(100),
    amount INT,
    booking_time DATETIME,
    pnr VARCHAR(20)
);
