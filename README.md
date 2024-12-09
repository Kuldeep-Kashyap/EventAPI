# Creating the content for the README.md file
readme_content = """
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
