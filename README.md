# 📁 Image Captioning API

## 📖 Кратко о проекте
Этот проект представляет собой веб-приложение на Python, использующее FastAPI для автоматической генерации подписей к изображениям с помощью модели машинного обучения. Приложение принимает изображение через API, анализирует его и возвращает текстовое описание. Данные о сгенерированных подписях сохраняются в базе данных PostgreSQL.

## 🧾 TODO список (основные положения)
- [x] Настроить инициализацию проекта FastAPI с использованием Uvicorn для асинхронной обработки запросов.
- [x] Создать модели SQLAlchemy для хранения истории сгенерированных подписей.
- [x] Использовать SQLAlchemy для работы с PostgreSQL.
- [x] Реализовать CRUD-операции для работы с историей подписей.
- [x] Интегрировать модель машинного обучения для генерации подписей (Salesforce/blip-image-captioning-large).
- [x] Документировать API с использованием Swagger/OpenAPI.
- [x] Настроить Docker и docker-compose для локального запуска проекта.
- [x] Написать README.md с инструкциями по запуску проекта и описанием функциональности.

## 💻 Запуск проекта

Клонирование репозитория:
```bash
git clone https://github.com/SamvelMkhitarian/image_description.git
cd image_description
```

Создание виртуального окружения (venv):
```bash
python3 -m venv venv
```
Активация виртуального окружения (venv):

Linux / Mac:
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```
Установка зависимостей:

# Установка Poetry (если не установлен)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
# Клонирование репозитория
```bash
git clone https://github.com/SamvelMkhitarian/image_description.git
cd image_description
```
# Установка зависимостей через Poetry
```bash
poetry install
```
# Активация виртуального окружения
```bash
poetry shell
```
Настройка переменных окружения:

Создайте файл .env на основе .env.example и укажите необходимые значения, такие как настройки подключения к базе данных PostgreSQL.

Запуск проекта с помощью docker-compose:
```bash
docker-compose up --build
```
Приложение будет доступно по адресу: http://localhost:8000

📜 Документация API

Документация доступна по адресу http://localhost:8000/docs, где можно ознакомиться с доступными эндпоинтами и их параметрами.

🛑 Остановка сервера

Для остановки сервера нажмите Ctrl + C в консоли.

