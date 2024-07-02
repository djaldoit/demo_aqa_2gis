<p align="left">
  <a href="https://demoblaze.com">
  <picture>
<img alt="2gis" src="https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-znachok-dva-gis-na-prozrachnom-fone-10.png" width="600" height="150">
    </picture>
  </a>
</p>
<h1 align="center">
  Demo auto-test 2GIS
</h1>

<p align="center">
2GIS (2 ГИС) – бесплатное программное обеспечение, предназначенное для навигации по городу. В приложении имеется подробное описание для каждой организации, включающее в себя адрес, телефон, детальную информацию и маршрут проезда. Карты некоторых городов выполнены в 3D и имеют условные обозначения для удобного поиска.

## Используемые инструменты в проекте
<img title="Python" src="resources/icons/python.svg" height="30" width="30"/> <img title="Jenkins" src="resources/icons/selene.png" height="30" width="30"/>  <img title="Pytest" src="resources/icons/pytest.svg" height="40" width="40"/> <img title="Allure Report" src="resources/icons/allure-report.png" height="40" width="40"/> <img title="Selenoid" src="resources/icons/selenoid.png" height="40" width="40"/> <img title="Jenkins" src="resources/icons/jenkins.svg" height="40" width="40"/> <img title="GitHub" src="resources/icons/github.svg" height="40" width="40"/> <img title="Pycharm" src="resources/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="resources/icons/telegram.png" height="40" width="40"/> 

----
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
### 1. Склонировать репозиторий
```
git clone https://github.com/lrayne/demoblaze-tests.git
```
### 2. Запуск
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```

----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/demo_2gis/">Ссылка на проект в Jenkins</a>

#### Параметры сборки
* `build` - Build сборки
* `comment` - комментарий


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/demo_2gis/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать Build сборки
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure отчет


<details><summary>Общие результаты</summary>
  
![This is an image](resources/allure-report-remote.png)
</details>

<details><summary>Список тест кейсов</summary>
  
![This is an image](resources/allure-report-local.png)
</details>

<details><summary>Пример Telegram отчета</summary>
  
![This is an image](resources/telegram-notification.png)
</details>

<details><summary>Пример видео отчета о прохождении ui-теста</summary>
  
<video src='resources/route_video.mp4' width=180/>
</details>

