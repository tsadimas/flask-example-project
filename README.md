# how to run this project

* clone
```bash
git clone 
```
* create virtual environment, activate and install requirements
```bash
python3 -m venv fvenv
source fvenv/bin/activate
pip install -r requirements.txt
```
* run
```bash
python app/main.py
```
or
```bash
export FLASK_APP=app.main.py; flask run -h 0.0.0.0 -p 8000
```
or
```bash
gunicorn app.main:app  --bind 0.0.0.0:5000
```

## env variables
* copy .env.example
```bash
cp .env.example .env
```
define the variables
```bash
SQLALCHEMY_DATABASE_URI
```