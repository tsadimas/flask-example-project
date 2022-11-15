# how to run this project

* clone
```bash
git clone 
```

# in order to install mysqlclient dependency, install the corresponding libpython-dev, e,g,
```bash
sudo apt install libpython3.10-dev
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
## Database env variables (sqlite, postgres, mysql)
```bash
SQLALCHEMY_DATABASE_URI=sqlite:///./students.sqlite3
SQLALCHEMY_DATABASE_URI=postgresql://demouser:pass123@192.168.135.121/demodb
SQLALCHEMY_DATABASE_URI: mysql://demo:demo@db01/demo

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

# Docker
```bash
docker build -t myflask .
```
run
```bash
docker run --env-file .env -p 5000:5000 myflask
```


# install packages for mysql
```bash
sudo apt install libmysqlclient-dev
```


Links
* [bootstrap-flask](https://github.com/helloflask/bootstrap-flask)
* [flask-wtf](https://flask-wtf.readthedocs.io/en/1.0.x/)