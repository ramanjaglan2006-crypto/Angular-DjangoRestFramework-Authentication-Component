# Full Stack Authentication Component

This project is a boilerplate for a full-stack web application featuring a robust authentication system. It uses **Django REST Framework** for the backend and **Angular** for the frontend.

## 🌟 Key Features

### Backend (Django REST Framework)
- **Custom User Model**: Scalable and flexible user management.
- **JWT Authentication**: Secure stateless authentication.
- **Social Auth**: Google and Facebook OAuth integration.
- **Service Layer**: Clean separation of business logic from views.
- **Centralized Error Handling**: Standardized API responses.

### Frontend (Angular)
- **Responsive UI**: Built with modern Angular practices.
- **Auth Guards**: Secure routes for authenticated users.
- **Token Management**: Automatic handling of JWT storage and refresh.

## 🛠️ Tech Stack

- **Backend**: Python, Django, DRF, JWT, SQLite/PostgreSQL
- **Frontend**: Angular, TypeScript, RXJS
- **DevOps**: Docker, Docker Compose

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- OR Python 3.9+ and NodeJS 14+

### Quick Start with Docker
```bash
docker-compose up --build
```
The backend will be available at `http://localhost:8000` and the frontend at `http://localhost:4200`.

### Manual Setup

#### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## 📂 Architecture Overview

The backend follows a modular architecture:
- `apps/`: Contains isolated business domains.
- `config/`: Centralized settings and URL routing.
- `services/`: Domain-specific business logic.
- `selectors/`: Data retrieval logic.

## 📝 License
MIT License
