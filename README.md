# Fast API Project

## Overview
This project is an implementation of a FastAPI application showcasing various features and best practices.

## Features
- **RESTful API**: Build a REST API with CRUD capabilities.
- **Automatic Documentation**: Utilize Swagger UI and ReDoc.
- **Asynchronous Support**: Leverage async capabilities for better performance.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.7+
- pip package manager

## Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Running the Application
To run the application, use the following command:
```bash
uvicorn main:app --reload
```

## MacOS / Linux Support
This application is fully supported on both macOS and Linux platforms. 

## Code Examples
Below are examples of how to use the API endpoints:

### Get All Items
```python
import requests
response = requests.get('http://127.0.0.1:8000/items/')
print(response.json())
```

### Create Item
```python
import requests
response = requests.post('http://127.0.0.1:8000/items/', json={'name': 'Item', 'description': 'A new item.'})
print(response.json())
```

## Data Model
| Field       | Type         | Description               |
|-------------|--------------|---------------------------|
| id          | int          | Unique identifier         |
| name        | string       | Name of the item         |
| description | string       | Description of the item   |

## External Libraries
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

