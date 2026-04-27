# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build RESTful APIs using the FastAPI framework in Python. Learn to create endpoints, handle HTTP requests and responses, and manage data with Pydantic models.

## 📝 Tasks

### 🛠️ Build a REST API for Item Management

#### Description
Create a FastAPI application that provides REST endpoints for managing a collection of items (e.g., a simple to-do list or product catalog). Implement CRUD operations (Create, Read, Update, Delete) with proper data validation.

#### Requirements
Completed API should:

- Set up a FastAPI application with proper imports and app instance
- Define a Pydantic model for the item data structure
- Implement GET endpoint to retrieve all items
- Implement POST endpoint to create new items with validation
- Implement PUT/PATCH endpoint to update existing items
- Implement DELETE endpoint to remove items
- Handle error cases (e.g., item not found) with appropriate HTTP status codes
- Include basic documentation using FastAPI's automatic docs