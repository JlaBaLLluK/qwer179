# Flask application
# Инструкция по развертыванию:
## 1. Склонировать репозиторий с проектом: 
git clone https://github.com/JlaBaLLluK/qwer179
## 2. Настроить интерпретатор Python в настройках IDE.
## 3. Установить все зависимости из файла requirements.txt
pip install -r requirements.txt
## 4. Деактивировать виртуальное окружения с помощбю команды.
deactivate
## 5. Создать служебный файл для автоматического запуска Gunicron
sudo nano /etc/systemd/system/<имя-файла.service>
## 6. Заполнить это файл следующими настройками:
[Unit] <br>
Description=<Описание><br>
After=network.target<br>

[Service] <br>
User=<имя-пользователя><br>
Group=www-data<br>
WorkingDirectory=<путь-до-папки-с-проектом><br>
Environment="PATH=<путь-до-папки-с-виртульаным-окрежнием>/bin"<br>
ExecStart=<путь-до-папки-с-виртульаным-окрежнием>/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app<br>

[Install] <br>
WantedBy=multi-user.target

## 7. Активировать созданный файл.
sudo systemctl start <имя-созданного-файла><br>
sudo systemctl enable <имя-созданного-файла>

## 8. Проверить, правильно ли все создалось.
sudo systemctl status myproject<br>
Если есть какие-либо ошибки, проверить созданный файл и повторить еще раз.

## 9. Установить nginx.
sudo apt install nginx

## 10. Создать файл конфигурации nginx.
sudo nano /etc/nginx/sites-available/<имя-файла>

## 11. Заполнить файл следующими настройками:
server { <br>
    listen 80; <br>
    server_name <ваш-домен-или-IP>; <br>

    location / {
        include proxy_params;
        proxy_pass http://unix:<путь-до-проекта>myproject.sock;
    }
}

