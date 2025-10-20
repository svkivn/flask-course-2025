# Flask Course 2025 — Lesson 4: Cookies and Sessions

This lesson demonstrates how to work with cookies and sessions in Flask to store data between requests.

## 🔐 What are Cookies and Sessions?

- **Cookies** are small pieces of data sent by the server and stored on the client side. Cookie Lifetime: Controlled via max_age or expires. They are used to store information such as user preferences or session identifiers. 

- **Sessions** allow storing data on the server side, preserving user information between requests. Flask uses a cookie to store the session identifier, while the actual session data is stored securely on the server. Sessions are signed but not encrypted; do not store sensitive data in plain cookies.

# Key Concepts

**Session**:

- Use session["key"] = value to store data.

- Use session.pop("key") to remove data.

- Stored client-side in a signed cookie.

**Cookies**:

- Set with response.set_cookie("key", "value", max_age=...).

- Read with request.cookies.get("key").

- Delete with response.delete_cookie("key").



## Cookies ↔ Session Flow

~~~
Client Browser
     │
     │ HTTP Request
     ▼
   Flask Server
     │
     ├─ Read cookie (session ID)
     │
     ├─ If session exists:
     │     └─ Load session data from signed cookie
     │
     ├─ Use session data in views/routes
     │
     └─ Set/update session → Sign data → Send as cookie in response
     ▼
Client Browser stores signed session cookie
~~~




