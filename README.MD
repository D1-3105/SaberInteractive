## Run script
Запуск в случае docker: 

`docker-compose up -d`

Запуск в случае localhost (uvicorn):

`python -m uvicorn core.v1:app`

PyTest:

`pytest core`

Приложению нужны файлы:
- `.env` (в случае запуска от localhost)
- `.env-docker` (в случае запуска в Docker)

По дефолту скрипт в докере слушает порт 8085.
## Swagger
Сваггер доступен по url `/api/doc/`

## ENV EXAMPLE
```
STORAGES=./builds/builds.yml,./builds/tasks.yml
TEST_STORAGES=./builds/test_builds.yml,./builds/test_tasks.yml
```
## Docker env example
```
STORAGES=/builds/builds.yml,/builds/tasks.yml
TEST_STORAGES=/builds/test_builds.yml,/builds/test_tasks.yml
```

## При выполнении задания возник вопрос по алгоритму:

Интуитивно понятно, что все зависимости должны быть загружены за 1 билд 1 раз,
однако, в тестовых примерах есть несколько билдов, содержащих на уровне build:tasks повторяющиеся
задачи. Я решил исключать повторяющиеся зависимости на уровне обхода зависимостей ветки задач билда.
