# MaBlog

MaBlog is a blogging platform API designed to provide a seamless experience for managing blog posts and user profiles. Built using Django and Django REST Framework (DRF), this project serves as the capstone for the Backend Web Development program in ALX Academy.

---

## Features

### Core Functionality
- **CRUD Operations:**
  - Users: Create, read, update, and delete user profiles.
  - Blog Posts: Create, read, update, and delete blog posts.
- **Categorized Views:**
  - View blog posts grouped by category.
- **Author-Specific Views:**
  - Fetch blog posts authored by a specific user.
- **Authentication and Authorization:**
  - Secure endpoints with user authentication.
  - Restrict actions like editing and deleting posts to their respective authors.

### Deployment
- Hosted on **Heroku** or **PythonAnywhere**.

---

## Project Structure

```
Mablog/
├── blog/                      # Main blogging app
│   ├── admin.py               # Admin configurations
│   ├── apps.py                # App configuration
│   ├── migrations/            # Database migrations
│   ├── models.py              # Database models
│   ├── serializers.py         # Data serialization/deserialization
│   ├── tests.py               # Unit tests
│   ├── urls.py                # App-specific routes
│   ├── views.py               # Business logic and request handling
│   └── __init__.py            # Module initialization
├── blogging_platform/         # Project configuration
│   ├── asgi.py                # ASGI configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project-wide routes
│   ├── wsgi.py                # WSGI configuration
│   └── __init__.py            # Module initialization
├── db.sqlite3                 # SQLite database (for development)
├── manage.py                  # Django management script
├── README.md                  # Project documentation
└── venv/                      # Virtual environment
```

---

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Zaid-dev2000/mablog.git
   cd mablog
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the API:**
   Visit `http://127.0.0.1:8000/` in your browser or use tools like Postman.

---

## API Endpoints

| Endpoint                  | HTTP Method | Description                          |
|---------------------------|-------------|--------------------------------------|
| `/users/`                 | POST        | Register a new user                 |
| `/users/<id>/`            | GET         | Retrieve user details               |
| `/users/<id>/`            | PUT         | Update user details                 |
| `/users/<id>/`            | DELETE      | Delete a user                       |
| `/posts/`                 | GET         | Retrieve all blog posts             |
| `/posts/`                 | POST        | Create a new blog post              |
| `/posts/<id>/`            | GET         | Retrieve a specific blog post       |
| `/posts/<id>/`            | PUT         | Update a specific blog post         |
| `/posts/<id>/`            | DELETE      | Delete a specific blog post         |
| `/posts/category/<category>/` | GET     | Retrieve blog posts by category     |
| `/posts/author/<author_id>/`  | GET     | Retrieve blog posts by author       |

---

## Deployment

This project is configured for deployment on platforms like **Heroku** and **PythonAnywhere**. Make sure to:
- Set environment variables for sensitive data like database credentials and secret keys.
- Use PostgreSQL for production.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/Zaid-dev2000/mablog).

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or feedback, please contact:
- **Name:** Zaid-dev2000
- **GitHub:** [Zaid-dev2000](https://github.com/Zaid-dev2000)
