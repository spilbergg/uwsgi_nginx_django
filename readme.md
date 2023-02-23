<h1 align="center">Привет! Это гайд по запуску проекта на Unix ОС</h1>

### Данный гайд представлен только в рамках этого проекта и только в учебных целях
### О проекте: запуск WEB-сервера с использованием UWSGI, NGINX и Django

---

### Для запуска проекта в системе должен быть установлен nginx, docker (необязательно, читать ниже)

Команда на установку nginx:

    sudo apt-get install nginx
Установку докера смотреть тут -> https://www.docker.com/

Запустить nginx:
    
    sudo /etc/init.d/nginx start  
или

    sudo service nginx start

### Перейдём к запуску самого приложения

Для это нужно создать папку и склонировать проект: 

         mkdir /home/имя_вашегокомьютера/proj1
         git clone https://github.com/spilbergg/uwsgi_nginx_django.git

Перейти в папку и установить виртуальное окружение:
        
        python3 -m env venv

Активировать виртуальное окружение:
        
        source venv/bin/activate

Установить зависимости:

        pip install -r requirements.txt
 
### Для запуска проекта с использование базы данных MySQL
 В корневой папке проекта запустить 
                
        docker-compose up -d
    
используя настройки db:
        
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'some_db',
                'USER': 'admin',
                'PASSWORD': 'admin',
                'HOST': '127.0.0.1',
                'PORT': '3306',
            }
        }
### Запуск проекта с использование sqlite3, для быстрого теста без использования докера

В proj1/settings.py раскомментировать настройки базы sqlite3, а MySQL закомментировать
    
            DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

Выполнить миграции в базу
        python manage.py migrate

<h3 align="center">Продолжим настройку конфигураций для **nginx**</h3>
    
1) В файле _proj1_nginx.conf_ (конфигурация для настройки nginx socket соединения) в корневой директрии проекта в строках 2, 18, 24

   **name** заменить на своё **имя комьютера**

2) Переместить конфиг proj_nginx.conf в папку nginx
        
       sudo cp proj1_nginx.conf /etc/nginx/sites-available/

3) Создать символьную ссылку на файл 
        
        sudo ln -s /etc/nginx/sites-available/proj1_nginx.conf /etc/nginx/sites-enabled/
4) В Файле uwsgi.ini в корневой директории проекта в путях имя spilbergg заменить на своё имя комьютера
   

5) Перезапустить nginx
        
        sudo service nginx restart

6) Собрать всю статику
        
        python manage.py collectstatic

7) Затем запустить uwsgi.ini (конфигурационные настройки uwsgi находятся в файле uwsgi.ini(корневой директории проекта)): 
        
        uwsgi uwsgi.ini

<h3 align="center">С настройками закончено</h3>

#### Осталось в браузере перейти по адресу: 
        127.0.0.1:8000



