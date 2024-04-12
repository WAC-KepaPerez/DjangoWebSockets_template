# Django Channels WebSocket Project

This README outlines the steps necessary to set up a Django project using Django Channels to handle WebSocket connections that send messages every 3 seconds for a total of 5 times.

## Prerequisites

- Python 
- Django 
- Channels 3.x
 -Daphne

## Installation

1. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. **Install Django, daphne and Channels**:

    ```bash
    pip install django channels daphne
    ```

3. **Create a new Django project and application**:

    ```bash
    django-admin startproject myproject
    cd myproject
    python manage.py startapp myapp
    ```

4. **Configure settings**:

    - Add 'daphne' to `INSTALLED_APPS` in `settings.py`.
    ```python
    #settings.py

    INSTALLED_APPS = [
        'daphne',
        ...
    ]
    ```
    - Set `ASGI_APPLICATION` to `'myproject.asgi.application'`.
    ```python
    #settings.py

    ASGI_APPLICATION = 'DjWebSockets.asgi.application'
    ```

5. **Set up ASGI application**:

    - Create/edit `asgi.py` in your project directory with the following content:
    ```python
    import os
    from django.core.asgi import get_asgi_application
    from channels.routing import ProtocolTypeRouter, URLRouter
    from channels.auth import AuthMiddlewareStack
    import myapp.routing

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                myapp.routing.websocket_urlpatterns
            )
        ),
    })
    ```

6. **Define WebSocket Consumer**:

    - Create `consumers.py` in your app directory with an `EchoConsumer` class.

7. **Configure URL routing for WebSockets**:

    - Create `routing.py` in your app directory with the WebSocket URL patterns.

    ```python
    from django.urls import re_path
    from .consumers import EchoConsumer

    websocket_urlpatterns = [
        re_path(r'^ws/somepath/$', EchoConsumer.as_asgi()),
    ]
    ```

8. **Run migrations and start the server**:

    ```bash
    python manage.py migrate #if you have db connection
    python manage.py runserver
    ```

## Testing WebSocket

- Connect and test the WebSocket using browser console or a client like Postman:

    ```javascript
    const ws = new WebSocket('ws://127.0.0.1:8000/ws/somepath/');
    ws.onmessage = function(event) {
        console.log('Message from server:', event.data);
    };
    ```

Ensure you follow these instructions in order for a successful setup.
