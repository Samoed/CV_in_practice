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