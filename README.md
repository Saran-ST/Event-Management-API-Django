**~~Event Management API**

The Event Management API is a Django REST Framework–based backend system that allows users to create, view, and manage events efficiently.
It also includes features for RSVP management, user reviews, and JWT authentication, with a modern Swagger UI for easy testing and exploration.

**# Features**

* Full CRUD operations for events
* RSVP management for event attendees
* Review system for event feedback
* JWT Authentication (login and token refresh)
* Built-in Swagger UI and ReDoc documentation
* Access to Django Admin for backend data management
  
## 🧩 Tech Stack
-----------------------------------------------------------------
| Component          | Technology                               |
|--------------------|------------------------------------------|
| **Backend**        | Django, Django REST Framework            |
| **Authentication** | JWT (via `rest_framework_simplejwt`)     |
| **Documentation**  | Swagger & ReDoc (via `drf-yasg`)         |
| **Database**       | SQLite (default and lightweight)         |
-----------------------------------------------------------------

**⚙️ Setup Instructions**

Follow these steps to set up and run the project locally:

1️⃣ Clone the repository
git clone [https://github.com/YOUR-USERNAME/event-management-assignment.git](https://github.com/Saran-ST/Event-Management-API-Django)
cd event-management-assignment

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate    # For Windows
source venv/bin/activate  # For macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply database migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (optional, for admin access)
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver

Once the server starts, you can visit the following in your browser:
http://127.0.0.1:8000/swagger/     — Swagger UI

http://127.0.0.1:8000/redoc/       — ReDoc

## 🌐 API Endpoints
--------------------------------------------------------------------------------------------------
| **Endpoint**           | **Method**              | **Description**                             |
|------------------------|------------------------|----------------------------------------------|
| /api/events/           | GET / POST             | List all events or create a new event        |
| /api/events/{id}/      | GET / PUT / DELETE     | Retrieve, update, or delete an event         |
| /api/rsvps/            | GET / POST             | View or create RSVP entries                  |
| /api/reviews/          | GET / POST             | View or add reviews for an event             |
| /api/token/            | POST                   | Obtain JWT authentication token              |
| /api/token/refresh/    | POST                   | Refresh JWT access token                     |
| /swagger/              | -                      | Interactive Swagger documentation            |
| /redoc/                | -                      | ReDoc documentation page                     |
--------------------------------------------------------------------------------------------------

## 🖼️ API Demonstration Screenshots  

Below are screenshots showcasing the working features of the Event Management API using Swagger UI:
----------------------------------------------------------------------------------------------
| **Feature**                                | **Screenshot**                                | 
|--------------------------------------------|---------------------------------------------- |
| Swagger UI - Interactive API Docs          | screenshots/swagger_UI-overview[1].png        |
| GET /api/events/{id} - List all events     | screenshots/get-event-with-eventid.png        |
| POST /api/events/ - Create a new event     | screenshots/create-event.png                  |
| PUT /api/events/{id}/ - Update an event    | screenshots/update-event.png                  |
| DELETE /api/events/{id}/ - Delete an event | screenshots/delete-event.png                  |
| POST /api/rsvps/ - Add a new RSVP          | screenshots/create-rsvp.png                   |
| POST /api/reviews/ - Add a review          | screenshots/create-review.png                 |
| JWT Authentication - Obtain Token          | screenshots/jwt_token.png                     |
| ReDoc - Documentation of API               | screenshots/redoc-overview.png                |
----------------------------------------------------------------------------------------------
