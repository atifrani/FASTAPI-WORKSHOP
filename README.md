# FastAPI  WORKSHOP

This is REST API built with Python and FastAPI, integrating with POSTGRESQL for CRUD operations (Create, Read, Update, Delete) on books. FastAPI is a powerful web framework for building APIs, while POSTGRESQL is a SQL database that provides flexibility and scalability.

## Routes

| HTTP Method | Endpoint              | Description          |
|-------------|-----------------------|----------------------|
| GET         | /books                | Get all books        |
| GET         | /books/{book_id}      | Get a specific book  |
| POST        | /books                | Add a new book       |
| PUT         | /books/{book_id}      | Update a book        |
| DELETE      | /books/{book_id}      | Delete a book        |
| GET         | /user                | Get all users        |
| GET         | /users/{book_id}      | Get a specific user  |
| POST        | /users                | Add a new book       |
| PUT         | /users/{book_id}      | Update a user        |
| DELETE      | /users/{book_id}      | Delete a user        |

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/atifrani/FASTAPI-WORKSHOP
```

Open the project repository using VSCODE.

Open terminal on VSCODE and change into the project directory:

```bash
cd FASTAPI-WORKSHOP
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate # for macos and linux
.\venv\Scripts\activate  # for windows
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the application:  

```bash
uvicorn main:app --reload
```

The application will start and be available at http://localhost:8000.

## API Endpoints for Books

### Add a new book:

```http
POST /books
```
Adds a new book to the system.

### Retrieve a list of books:

```http
GET /books
```
Returns a list of all books in the system


### Retrieve details for a specific book:

```http
GET /books/{book_id}
```
Returns details for a specific book with the given book_id

### Update an existing book:

```http
PUT /books/{book_id}
```
Updates an existing book with the given `book_id`.


### delete an existing book:

```http
DELETE /books/{book_id}
```
Updates an existing book with the given `book_id`.


## API Endpoints for Users

### Add a new user:

```http
POST /users
```
Adds a new user to the system.

### Retrieve a list of user:

```http
GET /users
```
Returns a list of all books in the system


### Retrieve details for a specific user:

```http
GET /users/{user_id}
```
Returns details for a specific book with the given user_id

### Update an existing user:

```http
PUT /users/{user_id}
```
Updates an existing user with the given `user_id`.


### delete an existing user:

```http
DELETE /users/{user_id}
```
Updates an existing user with the given `users_id`.