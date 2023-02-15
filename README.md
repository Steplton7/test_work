# test_work

### Описание
Django + Stripe
 
### Технологии
Python 
Django 
Stripe
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source ./venv/Scripts/activate
``` 
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Выполните миграции:
```
python3 manage.py migrate
```
- Создайте супер пользователя:
```
python3 manage.py createsuperuser
```
- Затем [зарегистрируйте](https://dashboard.stripe.com/login_success?redirect=%2F) учетную запись Stripe (если вы еще этого не сделали) и перейдите к [панели управления](https://dashboard.stripe.com/test/dashboard). Нажмите «Разработчикам».
- Затем на левой боковой панели нажмите «Ключи API».
-В нижней части файла settings.py добавьте следующие две строки, включая ваш собственный секретный и публичный ключ.
```
STRIPE_PUBLISHABLE_KEY = '<your test publishable key here>'
STRIPE_SECRET_KEY = '<your test secret key here>'
```
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```