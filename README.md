# Flask API

Basic flask API with sqlite, nice and easy.


## Install

`pip install Flask`

## Run main

To run server enter `python main.py`
now it can be accessed from `loclhost:105` or `127.0.0.1:105` in web browser.
> default port for Flask app is 5000

## Blueprints

Blueprints allow us to separate various endpoints into subdomains.

- home.py
- contact.py
- app.py

### Run blueprint

`python app.py`

### Access on:

`localhost:5000/home/hello`
`localhost:5000/contact/hello`