# Асинхронный парсер пепов
Скрипт парсит все ссылки пепов со страницы https://peps.python.org.
Переходит по ним и оттуда парсит номер, название и статус документа.

Сохраняет все в `.csv` - файл(например: `pep_2023-07-06T14-05-19.csv`)
в папку `results/`. Так же создает еще один файл где считает какое колличество
и каких статусов нашлось и в конце подсчитывает их общее число. Сохраняет все в
`.csv` - файл(например: `status_summary_2023-07-06_19-05-34.csv`)
в папку `results/` в корень проекта.

## Как запустить проект

***Клонировать репозиторий и перейти в него в командной строке:***

```bash
    git@github.com:AndreyKilanov/scrapy_parser_pep.git
 ```
```bash
    cd scrapy_parser_pep/
```
***Создать и активировать виртуальное окружение:***
```bash
    python -m venv venv
```
***Установить зависимости:***
```bash
    pip install -r requirements.txt
```
### ***Запустить парсер командой:***
```bash
    scrapy crawl pep
```

_Author: Andrey Kilanov_
 <img src="https://github.com/enricostara/telegram.link/blob/master/telegram.link.png" width="20"/>
[telegram](https://t.me/AndyFebruary)

_Stack: Python 3.10, Scrapy_
