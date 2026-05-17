from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI application
app = FastAPI(title="Todo API", version="1.0")

# Pydantic model for todo items
class TodoItem(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False

# In-memory storage for todos (for this assignment)
todos_db: dict[int, TodoItem] = {}
next_id = 1

# TODO: Implement the endpoints below

# Root endpoint - GET /
@app.get("/")
async def root():
    """Welcome endpoint"""
    pass

# Health check endpoint - GET /health
@app.get("/health")
async def health():
    """Health check endpoint"""
    pass

# Create a todo - POST /todos
@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoItem):
    """Create a new todo item"""
    pass

# Get all todos - GET /todos
@app.get("/todos")
async def get_todos():
    """Retrieve all todo items"""
    pass

# Get a specific todo - GET /todos/{id}
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    """Retrieve a specific todo by id"""
    pass

# Update a todo - PUT /todos/{id}
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: TodoItem):
    """Update a todo item"""
    pass

# Delete a todo - DELETE /todos/{id}
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    """Delete a todo item"""
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
