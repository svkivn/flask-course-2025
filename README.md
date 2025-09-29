
# Code Explanations

## app.py

- Imports Flask and related modules for web development.
- Creates a Flask app instance and loads configuration from `config.py`.
Defines several types of routes in Flask:

- **Static routes**: Serve fixed URLs, such as the root (`/`).
- **Dynamic routes**: Use URL parameters to capture values, e.g., `/hi/<string:name>`. [Learn more](https://www.geeksforgeeks.org/python/generating-dynamic-urls-in-flask/)
- **Query parameter routes**: Accept additional data via the URL query string, e.g., `/hi/ivan?age=30`. [Learn more](https://www.geeksforgeeks.org/python/get-request-query-parameters-with-flask/)
- **Redirect routes**: Automatically forward users to another URL, such as `/admin` redirecting to the greetings page. [Learn more](https://www.geeksforgeeks.org/python/redirecting-to-url-in-flask/)
	- `/` is the root route, which handles requests to the main page of the site.
	- `/hi/<string:name>` greets the user by name (converted to uppercase) and optionally shows their age from the query string.
		- This route demonstrates how to use query parameters. For example, `/hi/ivan?age=30` sets `name` to `ivan` and `age` to `30`. The code `age = request.args.get("age", 0, type=int)` retrieves the `age` parameter from the URL, defaulting to `0` if not provided.
		- The return statement `f"Welcome {name=} {age=}"` uses an f-string to display the values of `name` and `age` in the response, and returns an HTTP status code 200 (OK).
	- `/admin` redirects to the greetings page for "administrator".
- The app runs with `app.run()` if executed directly.

## config.py

- Sets `SECRET_KEY` for session security.
- Enables debug mode with `FLASK_DEBUG = 1`.
