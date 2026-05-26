# Django REST Framework - Authentication Component

A professional, scalable, and clean Django background project providing authentication and user profile management.

## 🚀 Features

- **Custom User Model**: Extended `AbstractUser` for flexibility.
- **JWT Authentication**: Secure token-based authentication using `django-rest-framework-simplejwt`.
- **Modular Architecture**: Clean separation of concerns with `apps`, `config`, `services`, and `selectors`.
- **Profile Management**: Automatic profile creation on user registration via signals.
- **Password Reset**: Integrated password reset flow with email notification.
- **Social OAuth2**: Built-in support for Google and Facebook login.
- **Standardized API**: Consistent response formatting and centralized error handling.
- **Environment Management**: Decoupled configuration using `.env`.
- **Dockerized**: Ready for development and production with Docker & Docker Compose.
- **Testing Setup**: Configured with `pytest` and `pytest-django`.

## 📁 Project Structure

```
backend/
├── apps/               # Business logic applications
│   ├── authentication/ # JWT, Login, Register, Social Auth
│   ├── core/           # Shared models, views, exceptions, responses
│   ├── profiles/       # User profile management
│   └── users/          # Custom User model, services, selectors
├── config/             # Project configuration
│   └── settings/       # Modular settings (base, dev, prod)
├── services/           # Cross-app business services
├── utils/              # Utility functions and helpers
├── tests/              # Global test suite
├── Dockerfile          # Container definition
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## 🛠️ Setup Instructions

### Local Development

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Copy `.env.example` to `.env` and fill in the required values.
   ```bash
   cp .env.example .env
   ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

### Using Docker

```bash
docker-compose up --build
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/auth/register/` | POST | Register a new user |
| `/api/v1/auth/login/` | POST | Obtain JWT token pair |
| `/api/v1/auth/token/refresh/` | POST | Refresh JWT access token |
| `/api/v1/users/me/` | GET/PUT | Retrieve/Update current user |
| `/api/v1/profiles/me/` | GET/PUT | Retrieve/Update current profile |

## 🧪 Running Tests

```bash
pytest
```

## 📝 License

This project is licensed under the MIT License.
