# django-admin-lte3
**django-admin-lte3** is preconfigured theme project with **popular open source admin dashboard & control panel theme AdminLTE** with **django3**.
The Aim is to reduce the theme integration time with django and use the templates with less Headache.

This Project is built by [Codewithakshay](http://codewithakshay.in).
___
# Table of content
*  Features
*  Requirements
*  Installation
*  Generate Dajngo SECRET_KEY
*  Run the project
*  Theme Credit

___
# Features!
* Login, signup, forgot password page
* AdminLte dashboard version v1,v2, v3
* Widgets
* Charts (charts.js)
* Easily integrate admintlte components
___
## Requirements
* python3
* Django version 3.1.4
___
### Installation
```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ git clone https://github.com/akshaysharma1801/django-admin-lte3.git
$ pip install -r requirements.txt
```
___
### Generate Dajngo SECRET_KEY
To run the project you have to create a new secret key. open python terminal with virtualenv activated.
```sh
$ from django.core.management.utils import get_random_secret_key
$ get_random_secret_key()
```
Copy this key and paste into the setting.py SECRET_KEY variable.
___
### Run the project
```sh
$ python manage.py runserver
```
::<a href="#smileys--emotion">Smileys &amp; Emotion</a>
### Theme Credit
[ADMINLTE](https://adminlte.io/)
___
__Back to top__
<a class="link-gray" href="#url">link-gray</a>

