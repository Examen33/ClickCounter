# Обрезка ссылок с помощью Битли

Этот проект предназначен для подсчета кликов по сокращенным ссылкам с использованием API VK. Цель проекта — автоматизировать процесс сокращения ссылок и отслеживания кликов через консольное приложение.


## Возможности

- Сокращение URL-адресов с использованием API VK.
- Получение и отображение статистики кликов по сокращенным URL-адресам.
- Полностью консольное приложение для бесшовной интеграции в рабочие процессы, основанные на использовании терминала.

## Используемые технологии

- **Python**: Основной язык программирования, используемый для разработки консольного приложения.
- **API VK**: Используется для сокращения ссылок и получения статистики кликов.
- **requests**: Простая библиотека HTTP для Python, используемая для выполнения API-запросов.
- **python-dotenv**: Модуль для чтения пар ключ-значение из файла `.env` и установки их как переменные окружения.

## Установка и настройка

### Шаг 1: Клонирование репозитория

Для начала клонируйте публичный репозиторий:

```sh
git clone https://github.com/
```

### Шаг 2: Создание виртуального окружения

Создайте виртуальное окружение и активируйте его:

- Для macOS и Linux:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
- Для Windows:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

### Шаг 3: Установка зависимостей

Установите необходимые зависимости:

```sh
python -m pip install -r requirements.txt
```

### Шаг 4: Настройка переменных окружения

Создайте файл `.env` в корне проекта и добавьте в него ваш токен API VK:

```env
VK_TOKEN=your_token_here
```

## Использование

Запустите скрипт с аргументом URL для сокращения или уже сокращенной ссылкой для получения статистики:

```sh
python main.py <URL> 
```