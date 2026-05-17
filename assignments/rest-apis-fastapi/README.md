# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a production-ready REST API using FastAPI. In this assignment, you will set up routing, handle request and response data, and implement CRUD operations—essential skills for backend development.

## 📝 Tasks

### 🛠️ Set Up Your FastAPI Application

#### Description
Initialize a FastAPI application with basic routes and run it on a local server. Understand the fundamentals of how FastAPI structures endpoints and handles HTTP requests.

#### Requirements
Completed program should:

- Import and instantiate a FastAPI application.
- Define a root endpoint (`GET /`) that returns a welcome message.
- Define a health check endpoint (`GET /health`) that returns a status object.
- Run the server using `uvicorn` and verify it responds to requests.

### 🛠️ Create CRUD Endpoints for a Todo Resource

#### Description
Build endpoints to Create, Read, Update, and Delete todo items. Each todo should have an id, title, and completion status.

#### Requirements
Completed program should:

- Define a `POST /todos` endpoint to create a new todo and return it with a generated id.
- Define a `GET /todos` endpoint to retrieve all todos.
- Define a `GET /todos/{id}` endpoint to retrieve a specific todo by id.
- Define an `PUT /todos/{id}` endpoint to update a todo's title or status.
- Define a `DELETE /todos/{id}` endpoint to remove a todo by id.

### 🛠️ Handle Request Validation and Error Responses

#### Description
Implement input validation using Pydantic models and return appropriate HTTP status codes for success and error cases.

#### Requirements
Completed program should:

- Use Pydantic models to define the structure of todo items and validate incoming data.
- Return `201 Created` for successful todo creation.
- Return `200 OK` for successful reads and updates.
- Return `204 No Content` for successful deletions.
- Return `404 Not Found` when a todo id does not exist.
- Return `422 Unprocessable Entity` for invalid input data.
