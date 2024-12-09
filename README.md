# EventAPI - Event Management API

EventAPI is a Django-based API for managing events, user roles, and ticket sales. It provides secure role-based access control using JWT authentication and utilizes MySQL as the database.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation Guide](#installation-guide)
5. [Environment Setup](#environment-setup)
6. [Configuration](#configuration)
7. [Running the Application](#running-the-application)
8. [API Endpoints](#api-endpoints)
9. [Database Structure](#database-structure)
10. [License](#license)

---

## Overview
EventAPI simplifies event management by supporting user registration, event creation, and ticket purchasing, with features tailored for both admin and regular user roles.

---

## Features
- **User Registration**: Admins and users can register with designated roles.
- **Event Management**: Admins can create and manage events.
- **Ticket Purchasing**: Users can purchase tickets for available events.
- **Role-Based Access Control**: Only admins can create events, while authenticated users can purchase tickets.

---

## Technologies Used
- **Django**: A high-level Python web framework.
- **Django REST Framework (DRF)**: For creating RESTful APIs.
- **MySQL**: A relational database for storing data.
- **JWT (JSON Web Token)**: For secure user authentication.
- **Postman**: For testing API endpoints.

---

## Installation Guide

### Clone the Repository
```bash
git clone https://github.com/your-username/EventAPI.git
cd EventAPI

2. Set Up a Virtual Environment
bash
Copy code
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
Environment Setup
Install MySQL
For Ubuntu:
bash
Copy code
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
For macOS:
bash
Copy code
brew install mysql
For Windows: Download and install MySQL from MySQL Downloads.
Start MySQL Service
Linux/macOS:
bash
Copy code
sudo service mysql start
Windows: Start the MySQL service from the Services app.
Create a Database
Log in to MySQL and create a new database:

bash
Copy code
mysql -u root -p
In the MySQL shell:

sql
Copy code
CREATE DATABASE eventdb;
CREATE USER 'event_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON eventdb.* TO 'event_user'@'localhost';
FLUSH PRIVILEGES;
Configuration
Update MySQL Database Settings
In EventAPI/settings.py, configure the database:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eventdb',
        'USER': 'event_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser
bash
Copy code
python manage.py createsuperuser
Running the Application
To start the server:

bash
Copy code
python manage.py runserver
The application will be accessible at: http://127.0.0.1:8000/

API Endpoints
1. User Registration (POST)
Endpoint: /api/register/
Request Body:

json
Copy code
{
    "username": "john_doe",
    "password": "password123",
    "role": "User"  // or "Admin"
}
Response:

json
Copy code
{
    "message": "User registered successfully"
}
2. Login and Get JWT Token (POST)
Endpoint: /api/token/
Request Body:

json
Copy code
{
    "username": "john_doe",
    "password": "password123"
}
Response:

json
Copy code
{
    "access": "jwt-access-token",
    "refresh": "jwt-refresh-token"
}
3. Create Event (Admin Only) (POST)
Endpoint: /api/events/
Request Body:

json
Copy code
{
    "name": "Tech Conference 2025",
    "date": "2025-05-15",
    "total_tickets": 500
}
Response:

json
Copy code
{
    "id": 1,
    "name": "Tech Conference 2025",
    "date": "2025-05-15",
    "total_tickets": 500,
    "tickets_sold": 0
}
4. View All Events (GET)
Endpoint: /api/events/
Response:

json
Copy code
[
    {
        "id": 1,
        "name": "Tech Conference 2025",
        "date": "2025-05-15",
        "total_tickets": 500,
        "tickets_sold": 0
    }
]
5. Purchase Tickets (User Only) (POST)
Endpoint: /api/events/{id}/purchase/
Request Body:

json
Copy code
{
    "quantity": 3
}
Response:

json
Copy code
{
    "message": "Tickets purchased successfully!"
}
Database Structure
User (Extended from Django's default User model):
id: Primary Key
username: CharField (Unique)
password: CharField (Hashed)
role: Choices (Admin/User)
Event:
id: Primary Key
name: CharField (Max 255 characters)
date: DateField
total_tickets: IntegerField
tickets_sold: IntegerField (default 0)
Ticket:
id: Primary Key
user: ForeignKey to User
event: ForeignKey to Event
quantity: IntegerField (Number of tickets purchased)
purchase_date: DateTimeField (auto_now_add=True)
