# Inventory Management System

This project is an Inventory Management System built with Django. It allows managing products, sales orders, suppliers, and stock levels. It also features the ability to create, update, and cancel sales orders, track stock quantity, and manage product details.

## Features

- **Product Management**: Add, update, view, and delete products in the system.
- **Sales Order Management**: Create, view, and cancel sales orders.
- **Stock Management**: Track the stock quantity of products and update it when sales orders are created or cancelled.
- **Supplier Management**: Manage suppliers, including their contact information.

## Requirements

- Python 3.9 or higher
- Django 3.1 or higher
- Database MongoDB
- MongoDB (if using `Decimal128` type for decimals)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone git@github.com:saadshehzad/inventory.git
cd src
python3 -m venv venv
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000