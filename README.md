# Invoice Management System

This is a simple invoice management system built using FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- Create, read, update, and delete invoices.
- FastAPI for building APIs quickly and efficiently.
- PostgreSQL for storing invoice data.
- SQLAlchemy for ORM.

## Prerequisites

- Python 3.7+
- PostgreSQL
- Git

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/invoice-system.git
   cd invoice-system

## Create a virtual environment & Activate the virtual environment  

python -m venv env
.\env\Scripts\activate

## Set up PostgreSQL database

Make sure PostgreSQL is installed and running on your system.

Create a new PostgreSQL database and user:

CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

## Configure environment variables

Create a .env file in the root directory of the project and add the following:

DATABASE_URL=postgresql://myuser:mypassword@localhost/mydatabase

## Running the Application

Start the FastAPI server

uvicorn app.main:app --reload

## Access the API documentation

Open your web browser and go to http://127.0.0.1:8000/docs to view and interact with the API documentation.

## To run these tests, execute the following command in your terminal: 

pytest

## Requirements 

fastapi==0.95.1
uvicorn==0.22.0
sqlalchemy==2.0.15
psycopg2-binary==2.9.6
python-dotenv==1.0.0
pydantic==2.1.1
pytest==7.1.2
httpx==0.23.0
pytest-asyncio 

## Explanation:

app/: This directory contains all the core application files.

__init__.py: Indicates that app is a Python package.
main.py: Contains the FastAPI application instance and the route definitions.
models.py: Defines the database models using SQLAlchemy.
schemas.py: Defines the data validation schemas using Pydantic.
crud.py: Contains functions that perform CRUD operations on the database.
db.py: Sets up the database connection, including the SQLAlchemy engine and session.
config.py: Holds configuration settings, such as database connection details.

tests/: This directory contains the unit tests for the application.

__init__.py: Indicates that tests is a Python package.
test_main.py: Contains unit tests for the API endpoints defined in main.py.

README.md: Provides an overview of the project, setup instructions, usage examples, and other relevant information.

.env: Contains environment variables used for configuration, such as database connection strings and other sensitive information.

This structure ensures a clear separation of concerns, making the application easier to understand, maintain, and extend.
