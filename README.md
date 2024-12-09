# EventAPI - Event Management API

EventAPI is a Django-based Event Management API that provides functionalities like user registration, event creation, ticket purchasing, and role-based access control. The application uses MySQL for the database and JWT-based authentication for secure user authorization.

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
EventAPI is a backend system designed to manage events and handle users efficiently. It supports:
- Role-based access control for Admins and Users.
- Event creation and listing.
- Ticket purchases and tracking.

---

## Features
- **User Registration**: Supports roles like Admin and User.
- **Event Management**: Admins can create and manage events.
- **Ticket Purchase**: Users can purchase tickets for events.
- **Role-Based Access Control**: Ensures secure access to features.

---

## Technologies Used
- **Django**: High-level web framework.
- **Django REST Framework (DRF)**: For API handling.
- **MySQL**: Relational database.
- **JWT (JSON Web Token)**: Secure authentication.
- **Postman**: API testing tool.

---

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/EventAPI.git
cd EventAPI
```

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
