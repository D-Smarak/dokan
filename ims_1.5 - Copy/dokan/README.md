# inventory-management
This is a inventory management system

# How to Setup
1. Clone Project

git clone 


2. Go To Project Directory

cd inventory-management

3. Create Virtual Environment

python3 -m venv venv

4. Active Virtual Environment

source venv/bin/activate
./venv/Scripts/activate

5. Install Requirements File

pip install -r requirements.txt

6. Migrate Database

python manage.py migrate

7. Create Super User

python manage.py createsuperuser

8. Run Project

python manage.py runserver




Additional commands on error:

```
To bypass Script running error:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

```

To upgrade pip:
python.exe -m pip install --upgrade pip
