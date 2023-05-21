# Kalvad-Test


## Requirements

- Python3.6+
- Django3.2+
- Pillow9.4.0+



## How To Install

```sh
Clone git repo:
git clone https://github.com/hashem-muhammad/Kalvad-Test.git
```

You can follow this step to install environment
```sh
Python
https://www.python.org/downloads/
```

```sh
Install Pillow
pip install Pillow
```
```sh
Install Django4.0+
pip install Django
```

if the cloned file is (.zip) you should unzip it using any tool you prefer it
## Prepare Project



```sh
inside Kalvad-Test (project name) where manage.py file exists run the following commands:
python manage.py makemigrations
python manage.py migrate
those commands to create tables in database and initial it
```

```sh
python manage.py create_products
this command to create a default values for products
```

```sh
python manage.py createsuperuser
to create user as admin and login to our system and admin dashboard
```



## Run Project And Server
inside Kalvad-Test (project name) where manage.py file exists run the following command:
```sh
python manage.py runserver
this is will run server with default config: http://127.0.0.1:8000/
if you want to customize it use:
python manage.py runserver 0.0.0.0:8001
where: 0.0.0.0 IP address(use what you want) and 8001 is port number
```


#### URL

- cart http://127.0.0.1:8000/
- admin http://127.0.0.1:8000/admin


## Thanks for your time
