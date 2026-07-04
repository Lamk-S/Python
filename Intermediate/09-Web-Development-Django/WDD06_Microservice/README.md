# Product Microservice

A RESTful microservice built with **Django** and **Django REST Framework** for managing products. This project demonstrates how to build a simple CRUD API and generate interactive API documentation using **drf-spectacular**, **Swagger UI**, and **ReDoc**.

## Features

* RESTful API for product management
* Full CRUD operations
* Django Admin integration
* Automatic OpenAPI schema generation
* Interactive Swagger UI documentation
* ReDoc API documentation
* Environment variable support using `.env`

## Technologies

* Python 3
* Django
* Django REST Framework
* drf-spectacular
* drf-spectacular-sidecar
* SQLite

## Project Structure

```text
WDD06_Microservice/
│
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── microservice/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── requirements.txt
├── .env.example
├── manage.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd WDD06_Microservice
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
```

## Database

Apply the migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

## Running the Project

Start the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

## API Endpoints

### Products

| Method | Endpoint               | Description                |
| ------ | ---------------------- | -------------------------- |
| GET    | `/api/productos/`      | Retrieve all products      |
| GET    | `/api/productos/{id}/` | Retrieve a product         |
| POST   | `/api/productos/`      | Create a product           |
| PUT    | `/api/productos/{id}/` | Update a product           |
| PATCH  | `/api/productos/{id}/` | Partially update a product |
| DELETE | `/api/productos/{id}/` | Delete a product           |

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/swagger/
```

ReDoc

```
http://127.0.0.1:8000/redoc/
```

OpenAPI Schema

```
http://127.0.0.1:8000/swagger.json
```

## Django Admin

```
http://127.0.0.1:8000/admin/
```

## Development Commands

Generate migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Create an administrator:

```bash
python manage.py createsuperuser
```

## License

This project is licensed under the MIT License.