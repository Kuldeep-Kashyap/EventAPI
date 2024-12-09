
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

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/EventAPI.git
cd EventAPI
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate your project dependencies:
```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scriptsctivate`
```

### 3. Install Dependencies
Install the required Python dependencies by running:
```bash
pip install -r requirements.txt
```

---

## Environment Setup

### 1. Install MySQL

#### For Ubuntu:
```bash
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

#### For macOS:
```bash
brew install mysql
```

#### For Windows:
Download and install MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/installer/).

### 2. Start MySQL Service

#### For Linux/macOS:
```bash
sudo service mysql start
```

#### For Windows:
Start the MySQL service from the Services app.

### 3. Create a Database
Log in to MySQL and create a new database:
```bash
mysql -u root -p
```

In the MySQL shell:
```sql
CREATE DATABASE eventdb;
CREATE USER 'event_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON eventdb.* TO 'event_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## Configuration

### 1. Update MySQL Database Settings
In `EventAPI/settings.py`, configure the database:
```python
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
```

### 2. Apply Migrations
Run migrations to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a Superuser
Create a superuser account for accessing the Django admin panel:
```bash
python manage.py createsuperuser
```

---

## Running the Application

To start the server, run:
```bash
python manage.py runserver
```

The application will be accessible at: `http://127.0.0.1:8000/`.

---

## API Endpoints

1. **User Registration (POST)**  
   Endpoint: `/api/register/`  
   Request Body:
   ```json
   {
       "username": "john_doe",
       "password": "password123",
       "role": "User"  // or "Admin"
   }
   ```
   Response:
   ```json
   {
       "message": "User registered successfully"
   }
   ```

2. **Login and Get JWT Token (POST)**  
   Endpoint: `/api/token/`  
   Request Body:
   ```json
   {
       "username": "john_doe",
       "password": "password123"
   }
   ```
   Response:
   ```json
   {
       "access": "jwt-access-token",
       "refresh": "jwt-refresh-token"
   }
   ```

3. **Create Event (Admin Only) (POST)**  
   Endpoint: `/api/events/`  
   Request Body:
   ```json
   {
       "name": "Tech Conference 2025",
       "date": "2025-05-15",
       "total_tickets": 500
   }
   ```
   Response:
   ```json
   {
       "id": 1,
       "name": "Tech Conference 2025",
       "date": "2025-05-15",
       "total_tickets": 500,
       "tickets_sold": 0
   }
   ```

4. **View All Events (GET)**  
   Endpoint: `/api/events/`  
   Response:
   ```json
   [
       {
           "id": 1,
           "name": "Tech Conference 2025",
           "date": "2025-05-15",
           "total_tickets": 500,
           "tickets_sold": 0
       }
   ]
   ```

5. **Purchase Tickets (User Only) (POST)**  
   Endpoint: `/api/events/{id}/purchase/`  
   Request Body:
   ```json
   {
       "quantity": 3
   }
   ```
   Response:
   ```json
   {
       "message": "Tickets purchased successfully!"
   }
   ```

---

## Database Structure

### 1. User Table (Extended from Django's default User model)
- `id`: Primary Key
- `username`: CharField (Unique)
- `password`: CharField (Hashed)
- `role`: Choices (Admin/User)

### 2. Event Table
- `id`: Primary Key
- `name`: CharField (Max 255 characters)
- `date`: DateField
- `total_tickets`: IntegerField
- `tickets_sold`: IntegerField (default 0)

### 3. Ticket Table
- `id`: Primary Key
- `user`: ForeignKey to User
- `event`: ForeignKey to Event
- `quantity`: IntegerField (Number of tickets purchased)
- `purchase_date`: DateTimeField (auto_now_add=True)

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.
