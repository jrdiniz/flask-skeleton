# Flask Skeleton

Just one more Flask (https://flask.palletsprojects.com/) boilerplate

## Frontend 

 - Bootstrap v4.3.1 - https://getbootstrap.com/
 - Font Awesome - https://fontawesome.com/
 - Jquery v3.5.0 - https://jquery.com/
 - Popper v1.14.7 - https://popper.js.org/

## Libraries

 - python-dotenv - https://github.com/theskumar/python-dotenv
 - gunicorn - https://gunicorn.org/

## How to use this project

Clone de repository inside of directory of project that you will start

```
git clone https://github.com/jrdiniz/flask-skeleton.git
```

 - Rename folder ```skeleton``` to name of your project
 - Rename the imports inside the file ```skeleton\__init__.py``` and ```wsgi.py``` 
 - Create ```.env``` to set enverionment variables:
    > FLASK_APP=<application_name>  
    > FLASK_ENV=development|production  
 - Create virtualenv using Pipenv ```pipenv install``` or using pip to install in your virtualenv ```pip install -r requirements.txt```

After that you will be able to run in development mode  ```flask run``` 

## Deploy using gunicorn (local)

``` $ gunicorn -b 0.0.0.0:5000 wsgi:app -w 4 -t 60 --log-file log/instance.log```

## Deploy using docker

## Deploy on Heroku
