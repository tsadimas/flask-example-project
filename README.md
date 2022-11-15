## how to run this project

* clone
```bash
git clone https://github.com/tsadimas/flask-example-project.git
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
export FLASK_APP=app.main.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1; flask run -h 0.0.0.0 -p 8000
```
or
```bash
gunicorn app.main:app  --bind 0.0.0.0:5000
```
#### Database env variables (sqlite, postgres, mysql)
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

## Docker
```bash
docker build -t myflask .
```
run
```bash
docker run --env-file .env -p 5000:5000 myflask
```

## Docker-compose

```bash
docker-compose up --build
```

### install packages for mysql
in order to install mysqlclient dependency, install the corresponding libpython-dev, e,g,
```bash
sudo apt install libmysqlclient-dev
sudo apt install libpython3.10-dev
```