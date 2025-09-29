# `.gitignore` and `.flaskenv`

These files help manage your Flask project's environment and version control.

## `.gitignore`

This file tells Git which files or directories to ignore. Example contents:

```gitignore
__pycache__/
*.pyc
.env
instance/
*.db
```

## `.flaskenv`

This file sets environment variables for Flask. Example contents:

```env
FLASK_APP=app.py
FLASK_ENV=development
```

## Usage

- Place `.gitignore` in your project root to avoid committing unwanted files.
- Use `.flaskenv` to configure Flask settings automatically when running the app.

## Next Steps

- Customize `.gitignore` for your needs.
- Add more environment variables to `.flaskenv` as your app grows.

## Understanding `app.py`

The `app.py` file contains the main code for your Flask application. Typically, it creates a Flask app instance, defines routes, and handles requests.

## Running the Server

You can start your Flask server in two common ways:

- Using the Flask CLI:
    ```
    flask run
    ```
    This command runs the app using the settings in `.flaskenv`.

- Directly with Python:
    ```
    python app.py
    ```
    This runs the `app.py` file directly. Make sure it includes the following block:
    ```python
    if __name__ == "__main__":
            app.run()
    ```

## Managing Dependencies

To view installed Python packages, run:

```
pip list
```

To install a specific package, use:

```
pip install package_name
```

To save your project's dependencies, run:

```
pip freeze > requirements.txt
```

To install dependencies from `requirements.txt`, use:

```
pip install -r requirements.txt
```