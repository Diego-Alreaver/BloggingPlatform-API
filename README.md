# Personal Blogging Platform API

This project is a simple RESTful API designed to manage a personal blogging platform. The API provides basic CRUD operations (Create, Read, Update, Delete) for blog posts. It allows users to create, update, delete, and retrieve blog posts, as well as search for posts using a term. 

## Features
- Create, update, and delete blog posts
- Retrieve individual or all blog posts
- Search for posts by title, content, or category
- Follows RESTful API best practices and conventions

## Goals
This project aims to:
- Teach RESTful API development and best practices
- Introduce common HTTP methods (GET, POST, PUT, DELETE)
- Implement CRUD operations and error handling
- Work with databases to store and retrieve data

## API Endpoints
- `POST /posts` - Create a new blog post
- `PUT /posts/{id}` - Update an existing blog post
- `DELETE /posts/{id}` - Delete a blog post
- `GET /posts/{id}` - Retrieve a single blog post
- `GET /posts` - Retrieve all blog posts
- `GET /posts?term={search}` - Search posts by term in title, content, or category

## Tech Stack
- **Backend Framework**: Django (Python)
- **Database**: SQLite 
- **API Documentation**: Swagger UI

## How to Run
1. Install dependencies via Pipenv or your package manager.
2. Run the Django server: `python manage.py runserver`
3. Access the API documentation at `/swagger/`.

Feel free to explore and extend this API to fit your needs!
