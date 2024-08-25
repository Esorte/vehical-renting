DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'car_rental_service',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'db',  # This refers to the 'db' service in docker-compose.yml
        'PORT': '5432',
    }
}
