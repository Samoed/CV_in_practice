# CV_in_practice
## Установка
Для запуска приложений надо установить зависимости с помощью pdm
```shell
pdm install --prod
```
или `requrenments.txt`
```shell
pip install -r requirements.txt
```
## Запуск
Для запуска надо выполнить команду
```shell
python src/app.py
```
Приложение будет выглядеть так:
![](img/demo.png)

## Разработка
Для разработки надо установить все библиотеки и скрипты для форматирования кода
```shell
pdm install
pre-commit install --install-hooks
```

## Эксперименты

|          | precision  | recall | mAP50 | mAP50-95 | fitness    | inference speed / sec  |
| -------- | --------   | -------|-------| -------  | -------    |    -------             |
| YOLOv8s  | 0.672      |  0.496 | 0.566 | 0.413    | 0.428      |    2.56                |
| YOLOv8n  | 0.618      |  0.446 | 0.469 | 0.336    | 0.349      |    1.80                |