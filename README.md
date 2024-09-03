# LittleLemon-Website
This project is the final assignment of the Meta Backend Developer Professional Certificate on Coursera

# Project Structure
The project is composed of two apps, `api` and `restaurant`. The `api` app serves API endpoints of the project, while the `restaurant` app serves its front-end. 
<br> <br>
![landpage](https://github.com/user-attachments/assets/ad3aa0bc-27c8-4a07-8772-0a0bb94832d1)

# Installation

Activate the virtual environment

```jsx
pipenv shell
```
<br>

Install the dependencies
```jsx
pipenv install
```

# Setup
The default database settings are

```jsx
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'admindjango',
        'PASSWORD' : 'employee@123!',
    }
}
```
💡 Change those settings according to your local setup.
<br>
<br>

Apply the migrations
```jsx
cd littlelemon
python manage.py migrate
```
<be>

# Run the project
```jsx
python manage.py runserver
```
Open the website by click or paste `http://127.0.0.1:8000/` to your browser

# API Endpoints
Separate guide is available [here](https://github.com/DoDucNhan/LittleLemon-Website/blob/main/littlelemon/api/README.md). User information and tokens can be found in the user_notes.txt


