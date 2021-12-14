# Body Mass Index(BMI)

BMI project is a calculator which calculates your body mass index and gives you a BMI result

<hr style="border:2px solid gray"> </hr>

## Features

* Users can register and login
* this project has CRS and SSR views
* API has doc and swagger


<a href="https://ibb.co/zZJyPmb"><img src="https://i.ibb.co/5LFNs1v/2021-12-14-23-29.png" alt="2021-12-14-23-29" border="0"></a>

<a href="https://ibb.co/XDNxQgf"><img src="https://i.ibb.co/m015jwr/2021-12-14-23-29-1.png" alt="2021-12-14-23-29-1" border="0"></a>
<a href="https://ibb.co/gvp2xZY"><img src="https://i.ibb.co/hXj6SF0/2021-12-14-23-29-2.png" alt="2021-12-14-23-29-2" border="0"></a>

<a href="https://ibb.co/DQXqq4n"><img src="https://i.ibb.co/1TVSSZx/2021-12-14-23-30.png" alt="2021-12-14-23-30" border="0"></a>

<a href="https://ibb.co/27Thwk6"><img src="https://i.ibb.co/TBs2ZgT/2021-12-14-23-32.png" alt="2021-12-14-23-32" border="0"></a>





<hr style="border:2px solid gray"> </hr>

## Installation

### First step

create BMI directory:

    mkdir BMI

go to BMI directory:

    cd BMI

---

### Second step

clone the project:

    git clone https://github.com/MrMohammadY/bmi.git

create virtualenv in BMI directory:

    virtualenv bmi_venv

now active your virtualenv:

    source bmi_venv/bin/activate

---

### Third step

go to project by:

    cd bmi

install package with:

    pip install -r requirements.txt

---

### Fourth step

**In this step you should create database in postgresql(don't change create database in other rdbms!)**

---

### Fifth step

in bmi directory you should create .env file for some django settings(.env files is hidden files):

    touch .env

and fill this argument in env file:

- SECRET_KEY = '\<django secret key (you can generate from this [site](https://djecrety.ir/)) >'
- DEBUG = True
- ALLOWED_HOSTS = ['*']
- DB_NAME='\<your database name>'
- DB_USER='\<your user access to database>'
- DB_PASSWORD='\<user password>'
- DB_HOST='localhost'
- DB_PORT=5432

---

### Sixth step

now make migrations with:

    python manage.py makemigrations

and after that applying migrations:

    python manage.py migrate

---

### In the last

you can now run project by:

    python manage.py runserver