Тестове завдання для fullstack розробника
-----------------------------------------
[Лум-відео з детальним поясненням про те, що треба зробити](https://www.loom.com/share/9d880138e06649dc83a3c9cd33d69cca)

Необхідно реалізувати функціонал live messaging для існуючого інбоксу рекрутера. Є репозиторій з інбоксом у вигляді списку повідомлень та сторінки переписки, яка зараз працює як HTML-форма. Сторінка переписки має працювати як live messaging.

### Технічні вимоги:

*   **Backend:** Python, Django
*   **Frontend:** Jinja2, Vanilla JS, [HTMX](https://htmx.org/) (за бажанням)

### Бізнес-логіка:

*   Live messaging замість HTML-форми
*   Функціонал має працювати як у списку повідомлень, так і на сторінці переписки
*   Повідомлення повинні мати статус прочитаного або непрочитаного (і на фронті, і на беці). Для непрочитаних має бути відповідний background на фронті
*   Має бути можливість відмітити повідомлення як непрочитане (на сторінці переписки)
*   Нове повідомлення має відмічатись як прочитане після наведення курсору або після фокусу у формі відповіді (на сторінці переписки)


Можна імітувати відправку повідомлення від кандидата через Python команди з терміналу або створити окремий view для відправки повідомлень (як зручніше).

### Результат:

*   посилання на гітхаб репозиторій
*   коротеньке [лум відео](loom.com), не більше 5 хвилин, з демо рішення та поясненням як все працює

## Installation

### Prerequisites 

- Python 3.9
- Docker  

### Local setup

After cloning the repo:

1. Setup env

```bash
# Python virtual env
python3 -m venv venv
source venv/bin/activate
```

2. Build and run the docker container
```
docker-compose build
docker-compose up -d
```

3. Prepare the database 

run `docker ps` and get the CONTAINER ID of the postgres:image
You should see something like this, the `e180ffc7d5d6` is the container id of the pg container.

```
CONTAINER ID   IMAGE                COMMAND                  CREATED       STATUS       PORTS                    NAMES
9432a9884aad   djinni-sandbox-web   "python app/manage.p…"   7 hours ago   Up 7 hours   0.0.0.0:8000->8000/tcp   djinni-sandbox-web-1
e180ffc7d5d6   postgres:latest      "docker-entrypoint.s…"   7 hours ago   Up 7 hours   0.0.0.0:5432->5432/tcp   djinni-sandbox-db-1
```

Then run this command to write backup.sql onto djinni_sandbox db

```
cat backup.sql | docker exec -i YOUR_CONTAINER_ID psql --user admin djinni_sandbox
```
4. Check if the installation succeeds by opening the [http://localhost:8000/]()

Good to go! 👍👍
