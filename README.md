# crm-app-django
A Customer-Relationship Management App made in Django which stores records of customers in MySQL database.</br>
This webapp does basic CRUD Operations like:
- Create: Create a new record of a customer.
- Read: Display records of customers.
- Update: Update records of a customer with new data.
- Delete: Delete a record.
</br></br>
It has a Register and a Login page for authentication.

## Installation
Install packages using `pip install -r requirements.txt`.  
Run the app using `python manage.py runserver`.
</br></br>

#### .env file
Create a .env file to store django secret key and mysql password
```
DJANGO_SECRET_KEY = 'secret_key'
MYSQL_PASSWORD = 'your_password'
```
