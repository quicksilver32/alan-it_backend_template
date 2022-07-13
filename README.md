# Основные команды
`python -m venv venv` - Инициализировать виртуальное окружение\
`venv/Scripts/activate` - Активировать виртуальное окружение\
`deactivate` - Декативировать виртуальное окружение (если оно активно)\
*При активном виртуальном окружении:*\
`pip install -r requirements.txt` - Установить необходимые пакеты
*Применение миграций:*\
`python manage.py migrate`\
*Запуск сервера выполняется при активном виртуальном окружении:*\
`python manage.py runserver 8080`