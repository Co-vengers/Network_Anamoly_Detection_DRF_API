# Network Anomaly Detection

A full-stack web application for uploading network datasets, training anomaly detection models, and making predictions.  
Built with Django (DRF) for the backend and React for the frontend.

---

## Features

- User registration and JWT authentication
- Dataset upload and management
- Model training (with Celery task queue)
- Prediction interface
- Protected routes for authenticated users
- Simple logout functionality

---

## Tech Stack

- **Backend:** Django, Django REST Framework, Celery
- **Frontend:** React
- **Broker:** Redis or RabbitMQ (for Celery)
- **Database:** MySQL

---

## Setup Instructions

### Backend

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd network_anamoly_detection
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Edit `.env` with your database credentials.

5. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Start the message broker (Redis or RabbitMQ):**
   ```bash
   # For Redis
   brew install redis
   brew services start redis

   # For RabbitMQ
   brew install rabbitmq
   brew services start rabbitmq
   ```

9. **Start Celery worker:**
   ```bash
   celery -A nad_api worker --loglevel=info
   ```

---

### Frontend

1. **Navigate to the frontend directory:**
   ```bash
   cd nad-frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

---

## Usage

- Register a new user at `/register`
- Login at `/login` to obtain JWT tokens
- Access the dashboard and other protected routes after authentication
- Use the navigation bar to upload datasets, train models, and make predictions
- Use the logout button to end your session

---

## Project Structure

```
network_anamoly_detection/
├── nad_api/           # Django backend project
│   ├── celery.py
│   ├── settings.py
│   └── ...
├── detection/         # Django app for core logic
├── nad-frontend/      # React frontend
│   ├── src/
│   └── ...
└── .env               # Environment variables
```

---

## License

MIT License

---

## Notes

- Ensure your message broker (Redis or RabbitMQ) is running before starting Celery.
- Update CORS and database settings as needed for your environment.
- For production, set `DEBUG = False` and configure allowed hosts and secrets properly.
