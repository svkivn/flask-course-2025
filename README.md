# Flask Course 2025 — Lesson: SQLa

This repository contains a Flask web application demonstrating modular architecture using Blueprints. The `lesson5-with-blueprint` branch showcases how to structure a Flask application by organizing related views and other code into reusable components.

## 🔍 Overview

In this lesson, we refactor the Flask application to use Blueprints, which allow for better organization and scalability. The application is divided into multiple modules, each responsible for a specific feature, making the codebase more maintainable.

## 📁 Project Structure
~~~
├── run.py # Application entry point

├── config.py # Configuration settings (SECRET_KEY, DEBUG, etc.)

├── requirements.txt # Python dependencies

├── .flaskenv # Environment variables (FLASK_APP, FLASK_ENV)

├── .gitignore # Files/folders ignored by Git

├── app/ # Main application package

│ 	├── init.py # Flask app creation and blueprint registration

│ 	├── views.py # Main site routes
│
│	├── templates/ # HTML main templates
│
│	├── static/ # static files
│
│	├── tests/ # Unit tests
│
│	├── products/ # Blueprint for products routes
│
│	     ├── init.py # Blueprint initialization
│
│ 	     └── routes.py # Products routes for blueprint
│
│ 	     └── templates # HTML templates
│
│ 			└── products/
│			
│					├── products.html
│ 					└── detail_product.html
~~~
