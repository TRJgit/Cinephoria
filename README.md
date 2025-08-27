# Cinephoria: Your Personal Movie Database

Cinephoria is a web-based application built with Django that allows users to browse, search, and get information about movies. It's your own personal movie database where you can explore a collection of films, view their details, and even contribute by adding new movies to the database.

## Features

  * **Browse Movies:** Explore a curated list of movies from different languages like Tamil, English, and Hindi.
  * **Movie Details:** Get comprehensive information about each movie, including:
      * Synopsis
      * Director
      * Cast
      * Genre
      * Duration
      * IMDB and Rotten Tomatoes ratings
      * Release Year
  * **Add New Movies:** Contribute to the database by adding new movies and their details.
  * **Admin Panel:** A powerful admin panel to manage the movie database.

## Technologies Used

  * **Backend:** Django, Python
  * **Frontend:** HTML, CSS, JavaScript
  * **Database:** SQLite

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

  * Python 3.x
  * Django

### Installation

1.  **Clone the repo**
    ```sh
    git clone https://github.com/your_username_/Cinephoria.git
    ```
2.  **Navigate to the project directory**
    ```sh
    cd Cinephoria/moviesite
    ```
3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the development server**
    ```sh
    python manage.py runserver
    ```
5.  Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

The project is organized as a standard Django application:

```
moviesite/
├── main/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   └── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── moviesite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```