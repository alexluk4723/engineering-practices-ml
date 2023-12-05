# Интсрукция по созданию проекта
1. Установка `poetry`, если еще его нет (я через `pip` устанавливал, можно иначе):
```bash
pip install poetry
```

2. Создаем проект
```bash
poetry new hello-world
```
и прыгаем в него.

3. В автоматически созданном файле `pyproject.toml` заполняем нужные поля (описание, информацию о себе и др.)

4. Чтобы добавить *dev-зависмости* (форматтеры `isort`, `black` и линтер `ruff`) нужно выполнить команду
```bash
poetry add --group=dev isort black ruff
```
Тут в `pyproject.toml` добавилась информация про эти зависимости и создался файл `poetry.lock`

5. Теперь в `pyproject.toml` можно сконфигурировать эти форматтеры и линтеры.

6. Дальше можно добавить python-файлы в автоматически созданную папку `hello_world` (название проекта)

7. И `numpy` понадобится 
```bash
poetry add --extras numpy
```

8. Для сборки проекта
```bash
poetry build
```

# Pre-commit

1. Аналогично добавляем dev зависиомость
```bash
poetry add --group=dev pre-commit
```
2. Потом
```bash
poetry run pre-commit install
```
3. И добавляем файл `.pre-commit-config.yaml` и настройки в него
4. Для запуска можно так
```bash
poetry run pre-commit run --show-diff-on-failure --all-files
```
# Formatters & linters

Можно запукать для файла
```bash
poetry run <formatter/linter name> <filename>
```
Например, для применения форматтера `black` к файлу `main.py` :
```bash
poetry run black hello_world/main.py
```
А также для всего проекта сразу с помощью `.`
```bash
poetry run <formatter/linter name> .
```


