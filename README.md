# django-weather
Weather app made with Django framework using the OpenWeatherMap API and Geo localization with GeoIP2.

# Setup
First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:rafaellima47/django-weather.git
    $ cd django-weather
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Apply the migrations:

    $ python manage.py migrate


Download the binaries of 'GeoLite2-city.mmdb' at https://dev.maxmind.com/geoip/geolite2-free-geolocation-data and Add it to the geoip directory:

    $ ls geoip/
    GeoLite2-City.mmdb


Signup and get your API key at https://openweathermap.org/api

Them assign your key to the variable API_KEY in config.py

```python
API_KEY = "your_api_key"
```


You can now run the development server:

    $ python manage.py runserver
