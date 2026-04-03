# FastAPI E-Commerce Backend API

A robust, RESTful backend API for an e-commerce platform built with **FastAPI** and **SQLAlchemy**. This project demonstrates clean architecture, relational database management, and secure user authentication, making it a highly scalable foundation for an online store.

## 🚀 Features

* **User Authentication & Authorization**: Secure JWT-based authentication with Access and Refresh tokens.
* **Product Management**: Authorized users can create, view, and safely delete products.
* **Shopping Cart System**: Users can add products to their cart, update quantities, view their cart, and remove items.
* **Order Processing**: Seamless checkout experience that converts cart items into placed orders and clears the cart automatically using database transactions. Order cancellation and history viewing are also supported.
* **Relational Database**: Managed via SQLAlchemy ORM, handling relationships between Users, Products, Carts, and Orders.
* **Clean Architecture**: Separation of concerns utilizing `routers`, `crud`, `models`, and `schemas` for maintainability.

## 🛠️ Tech Stack

* **Framework**: FastAPI
* **Database ORM**: SQLAlchemy
* **Data Validation**: Pydantic
* **Authentication**: JSON Web Tokens (JWT) via `python-jose`
* **Environment Management**: `python-dotenv`

## 📂 Project Structure

`app/`
`├── auth/          # Authentication dependencies and logic`
`├── core/          # Core configurations (Database setup, JWT tokens)`
`├── crud/          # Database operations (Create, Read, Update, Delete)`
`├── models/        # SQLAlchemy Database Models (User, Product, Cart, Order)`
`├── routers/       # FastAPI route definitions`
`└── schemas/       # Pydantic models for request/response validation`

