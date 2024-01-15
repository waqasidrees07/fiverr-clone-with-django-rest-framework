# Fiverr Clone
python 3.8

django 4.2.3

**Run Project**

clone project

**create virtual environment**

```py -m venv virtualenv```

**activate virtual environment**

```virtualenv\Scripts\activate```

**go to backend directory**

```cd backend```

**install packages**

```pip install -r requirements.txt```

**setup database**

create ```.env``` file

```
database_name =
database_user =
database_password =
database_host =
database_port =

// enter email details 
email_host = "smtp.gmail.com"
email_port = 587
email_host_user =
email_host_password = "your_email_smtp_password"
```

**migrate models with database**
```
py manage.py makemigrations
py manage.py migrate
```


