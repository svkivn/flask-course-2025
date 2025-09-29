## Code Explanations

This project is a Flask web application with the following structure:

- `run.py`: Entry point. Runs the Flask app.
- `app/`: Main application package.
	- `__init__.py`: Initializes the Flask app and loads configuration.
	- `views.py`: Contains route/view definitions for the main app.
	- `posts/`: Blueprint for post-related functionality.
		- `__init__.py`: Initializes the posts blueprint.
		- `views.py`: Contains routes/views for posts.
		- `templates/posts/`: HTML templates for post pages (`detail_post.html`, `posts.html`).
	- `templates/`: Main HTML templates (`base.html`, `hi.html`, `home.html`).
- `config.py`: Configuration settings for Flask (e.g., secret key, debug mode).
- `requirements.txt`: List of required Python packages.
- `tests/`: Contains unit tests (e.g., `test_user_bp.py`). Uses Python's `unittest` framework. Sets up a test client for the Flask app.

### How it works

1. The app is started via `run.py`, which imports and runs the Flask app from `app`.
2. Routes are defined in `views.py` and `posts/views.py`, handling different URLs and logic.
3. HTML templates render responses for users.
4. Configuration is loaded from `config.py`.
5. Tests are located in the `tests/` folder.
