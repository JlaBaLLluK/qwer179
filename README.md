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
[Unit]
Description=<Описание>
After=network.target

[Service]
User=<имя-пользователя>
Group=www-data
WorkingDirectory=<путь-до-папки-с-проектом>
Environment="PATH=<путь-до-папки-с-виртульаным-окрежнием>/bin"
ExecStart=<путь-до-папки-с-виртульаным-окрежнием>/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
