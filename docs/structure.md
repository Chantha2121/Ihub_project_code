Project structure
==
    
    /iMIS/
    │
    ├── /app/                           # Main application folder
    │   ├── /static/                    # Static files (CSS, JavaScript, images)
    │   ├── /templates/                 # HTML templates
    │   ├── /blueprints/                # Blueprint modules (for feature-specific routes)
    │   │   ├── __init__.py             # Initializes the blueprint module
    │   │   ├── auth/                   # Example: Blueprint for authentication
    │   │   │   ├── __init__.py         # Initializes the auth blueprint
    │   │   │   ├── routes.py           # Routes related to authentication
    │   │   │   └── forms.py            # Forms for authentication
    │   │   └── blog/                   # Example: Blueprint for a blog
    │   │       ├── __init__.py         # Initializes the blog blueprint
    │   │       ├── routes.py           # Routes related to blog functionality
    │   │       └── models.py           # Models related to blog
    │   │
    │   ├── /extensions/                # Flask extensions initialization
    │   │   ├── __init__.py             # Initializes the extensions module
    │   │   ├── db.py                   # Database initialization (SQLAlchemy, etc.)
    │   │   └── login.py                # Flask-Login setup
    │   │
    │   ├── /models/                    # Database models
    │   │   ├── __init__.py             # Initializes the models module
    │   │   ├── user.py                 # User model
    │   │   └── post.py                 # Post model (if not using blueprints)
    │   │
    │   ├── /services/                  # Business logic and services
    │   │   ├── __init__.py             # Initializes the services module
    │   │   ├── email_service.py        # Email sending service
    │   │   └── payment_service.py      # Payment processing service
    │   │
    │   ├── /utils/                     # Utility functions and helpers
    │   │   ├── __init__.py             # Initializes the utils module
    │   │   ├── decorators.py           # Custom decorators
    │   │   └── helpers.py              # General helper functions
    │   │
    │   ├── config.py                   # Configuration settings
    │   ├── main.py                     # Main application entry point
    │   └── __init__.py                 # Application factory function
    │
    ├── /tests/                         # Test suite
    │   ├── __init__.py                 # Initializes the test suite
    │   ├── test_auth.py                # Tests for authentication
    │   ├── test_blog.py                # Tests for blog functionality
    │   └── test_models.py              # Tests for models
    │
    ├── /migrations/                    # Database migration scripts (e.g., Flask-Migrate)
    │   └── versioning files...         # Auto-generated migration files
    │
    ├── .env                            # Environment variables (never commit to version control)
    ├── .flaskenv                       # Flask environment settings (for development)
    ├── requirements.txt                # Python dependencies
    ├── README.md                       # Project documentation
    └── wsgi.py                         # WSGI entry point for production servers