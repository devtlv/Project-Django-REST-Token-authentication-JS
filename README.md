# Django & JavaScript Integration: Token-based Authentication with Django REST API

## Overview

This Django project (`django_js`) aims to demonstrate the integration of a Django REST API with JavaScript, utilizing token-based authentication.

### Objectives

- **Token Authentication**: Learn how to authenticate users using tokens in Django.
- **REST API and JavaScript**: Understand how to make API requests from JavaScript to Django.

## Installation Steps

### Setting up Django and Required Libraries

1. Install Django CORS Headers:  
    ```bash
    pip install django-cors-headers
    ```

2. After the installation, include `corsheaders` and `rest_framework.authtoken` to your `INSTALLED_APPS` in `django_js/settings.py`.

    ```python
    INSTALLED_APPS = [
        # ...other installed apps,
        "corsheaders",  # add this
        "rest_framework",  # add this
        "rest_framework.authtoken"  # add this
    ]
    ```

### Configure CORS and Database

1. **CORS Configuration**: CORS headers are necessary to allow the frontend (here, `fetch.html`) to access the API from different origins.

    Update `CORS_ALLOWED_ORIGINS` in your `settings.py`:

    ```python
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:8000',
        'http://localhost',
        'null'
    ]
    ```

2. **Database Migrations**: After adding the required configurations and apps, migrate your database to create the necessary tables.

    ```bash
    python manage.py migrate
    ```

## Token Authentication in Django

### Setting Up Automatic Token Generation

1. **Receiver for Token**: A receiver listens to a signal and performs some action. In our case, we will generate a new token whenever a new user is created.

    **File**: `django_js/todo/signals.py`

    ```python
    from django.dispatch import receiver
    from django.db.models.signals import post_save
    from django.contrib.auth.models import User
    from rest_framework.authtoken.models import Token

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
    ```

### Integrating Token Authentication in API Views

1. **File**: `django_js/todo/views.py`

    Add `TokenAuthentication` and `IsAuthenticated` to your API views to enforce token authentication.

    ```python
    from rest_framework.authentication import TokenAuthentication
    from rest_framework.permissions import IsAuthenticated

    class TodoView(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        ...
    ```

## Frontend (JavaScript) Integration

1. **File**: `django_js/fetch.html`

    When you make a request to the Django API, include the token in the headers of the request.

    ```javascript
    const token = 'your_token_here';
    fetch(url, {
        headers: {
            'Authorization': `Token ${token}`
        }
    })
    ```
