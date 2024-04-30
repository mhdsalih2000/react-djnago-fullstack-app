# React + Django Simple Note Taking App

This is a simple note-taking application built using React for the frontend and Django for the backend. It implements SimpleJWT authentication for user authentication and authorization. Users can create, read, update, and delete notes.

## Features

- User authentication using SimpleJWT.
- Create, read, update, and delete notes functionality.
- Responsive UI for seamless user experience across devices.

## Prerequisites

- Node.js installed on your machine.
- Python and Django installed.
- Basic understanding of React and Django frameworks.

## Setup Instructions

1. Clone the repository:

    ```
    git clone 
    ```

2. Navigate to the project directory:

    ```
    cd react-django-note-app
    ```

3. Install frontend dependencies:

    ```
    cd frontend
    npm install
    ```

4. Install backend dependencies:

    ```
    cd ../backend
    pip install -r requirements.txt
    ```

5. Run migrations:

    ```
    python manage.py migrate
    ```

6. Create a superuser:

    ```
    python manage.py createsuperuser
    ```

7. Start the Django development server:

    ```
    python manage.py runserver
    ```

8. In a separate terminal, start the React development server:

    ```
    cd ../frontend
    npm start
    ```

9. Open your browser and navigate to `http://localhost:3000` to access the application.

## API Endpoints

- `/api/token/`: Obtain JWT authentication token.
- `/api/token/refresh/`: Refresh JWT authentication token.
- `/api/notes/`: List and create notes.
- `/api/notes/<note_id>/`: Retrieve, update, and delete notes.

## Technologies Used

### Frontend

- React
- React Router
- Axios

### Backend

- Django
- Django REST Framework
- djangorestframework-simplejwt

## Folder Structure
react-django-note-app/
│
├── frontend/ # Frontend React app

│ ├── public/

│ ├── src/

│ └── package.json

│
└── backend/ # Backend Django app

├── Backend(project flder)/

├── API(app)/

└── manage.py

