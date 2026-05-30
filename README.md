<<<<<<< HEAD
# instagram
=======
Instagram API

Overview

This project is a RESTful backend built with Django 6.0.5 and Django REST Framework, featuring:





JWT authentication



Swagger/OpenAPI documentation



User profiles



Posts, comments, likes, saved posts



Stories



Follows



Direct messaging



OTP-based verification



Redis caching

Tech Stack





Framework: Django 6.0.5



API: Django REST Framework



Authentication: SimpleJWT (Bearer token)



API Schema: drf-spectacular



Database: SQLite



Cache: Redis via django-redis

Project Structure





accounts/: authentication, OTP, user profiles



posts/: posts, comments, likes, saved posts, hashtags



stories/: story management



directs/: direct conversations and messages



follows/: follow system



core/: shared/core app



src/: Django project settings and root urls

Features

Accounts





User profile management



OTP send/verify endpoints



Public and private profile endpoints

Posts





Create and manage posts



Like/unlike posts



Comment on posts and replies



Save posts



Hashtag search/filtering

Stories





Create and retrieve stories



Archive stories

Direct Messages





Direct conversations



Send messages with text or file attachments

Follows





Follow/unfollow functionality

Authentication

This API uses JWT authentication.

Header Format

Authorization: Bearer <your_access_token>


Token Lifetime





Access token: 15 minutes



Refresh token: 7 days

API Documentation

Swagger/OpenAPI docs are available via drf-spectacular.





Schema Title: Instagram



Version: 1.0.0



Description: Finally Project

Database





Default Database: SQLite



ENGINE: "django.db.backends.sqlite3"



NAME: BASE_DIR / "db.sqlite3"

Cache

Redis cache configuration:





Host: localhost



Port: 6379



DB: 0

Installation





Clone the repository:

git clone <repo-url>
cd <project-folder>




Create a virtual environment:

python -m venv venv
source venv/bin/activate




Install dependencies:

pip install -r requirements.txt




Apply migrations:

python manage.py migrate




Run the server:

python manage.py runserver


API Endpoints

Accounts





GET /accounts/all-profiles/



GET /accounts/all-profiles/{id}/



GET /accounts/profile/



GET /accounts/profile/{id}/



POST /accounts/send-otp/



POST /accounts/verify-otp/

Posts





GET /posts/all-posts/



GET /posts/all-posts/{id}/



POST /posts/all-posts/{id}/like/



GET /posts/comments/



GET /posts/comments/{id}/



GET /posts/post/



GET /posts/post/{id}/



GET /posts/saved/



GET /posts/saved/{id}/



GET /posts/tag/

Stories





GET /stories/stories/



GET /stories/stories/{id}/



GET /stories/stories/archive/

Notes





Search by hashtag is supported in posts.



Like/unlike is implemented as a toggle action.



The comment model supports nested replies.



Direct messages support file attachments.

Run Command

python manage.py runserver


License

This project does not currently include a license.
>>>>>>> 901ae28 (finally-project)
