# personal-website

personal website hoosted on vercel built using django, mongodb, and redis

# building

make virtual environment installing dependencies 
```sh
pip install virtualenv
virtualenv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

setup mongodb and redis in setting.py and save credentials in .env file under `blog_portfolio` like below and generate new django key
```env
DATABASES_USER=dsfavxc12
DATABASES_KEY=JMOFavsgasdg12310
REDIS_USER=fdshrga
REDIS_KEY=fasdarewga234562347ghefdgb
SECRET_KEY=asdui235320-23masn12mnflasd
```

make migration
```sh
python manage.py makemigrations
pytoon manage.py migrate
```

generate staticfiles
```sh
python manage.py collectstatic
python manage.py compress
```
