# Django Library Management Project [Demo Video](https://drive.google.com/file/d/1NEH8tsMDDuKiVK8cmha4HerE_n7rVIqC/view?usp=sharing)


## Click the link below to see the live version.

https://djangolibrary.mzhasan00.repl.co/


## Or, follow the steps to install in your local machine

### 1. Create a virtual environment

From the **root** directory run:

```bash
python -m venv venv
```

### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

### 4. Run migrations

From the **root** directory run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 5. Create an admin user to access the Django Admin interface

From the **root** directory run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

## Run the application

From the **root** directory run:

```bash
python manage.py runserver
```

## View the application

Go to http://127.0.0.1:8000/ to view the application.