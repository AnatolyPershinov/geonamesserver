## Run the app
    python script.py
## Get city by geonamesId
### Request
    GET /city/[geonamesId]
    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/city/452692
### Response
    Content-Length: 228
    Content-Type: application/json; charset=utf-8
    Date: Sun, 19 Sep 2021 11:44:58 GMT
    Server: Python/3.9 aiohttp/3.7.4.post0
    {"geonamesId": 452692, "name": "Svetlitsa", "alternative names": "Svetlica,Svetlitsa,\u0421\u0432\u0435\u0442\u043b\u0438\u0446\u0430", "latitude": 57.23779, "longitude": 33.0692, "population": 500, "time zone": "Europe/Moscow"}
## Get page
### Request
    GET /page-[pnum]?size=[size]
    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/page-1?size=2
### Response
    Content-Length: 442
    Content-Type: application/json; charset=utf-8
    Date: Sun, 19 Sep 2021 11:47:44 GMT
    Server: Python/3.9 aiohttp/3.7.4.post0
    [{"geonamesId": 452692, "name": "Svetlitsa", "alternative names": "Svetlica,Svetlitsa,\u0421\u0432\u0435\u0442\u043b\u0438\u0446\u0430", "latitude": 57.23779, "longitude": 33.0692, "population": 500, "time zone": "Europe/Moscow"}, {"geonamesId": 452741, "name": "Kletino", "alternative names": "Kletino,\u041a\u043b\u0435\u0442\u0438\u043d\u043e", "latitude": 57.10337, "longitude": 33.44257, "population": 150, "time zone": "Europe/Moscow"}]
## Compare two cities
### Request
    GET /compare?city1=[city1]&city2=[city2]
    curl -i -H 'Accept: application/json'http://127.0.0.1:8000/compare?city1=Москва&city2=Тюмень
### Response
    Content-Length: 987
    Content-Type: application/json; charset=utf-8
    Date: Sun, 19 Sep 2021 11:48:57 GMT
    Server: Python/3.9 aiohttp/3.7.4.post0
    [{"geonamesId": 524894, "name": "Moskva", "alternative names": "Maskva,Moscou,Moscow,Moscu,Mosc\u00fa,Moskau,Moskou,Moskovu,Moskva,M\u0259skeu,\u041c\u043e\u0441\u043a\u0432\u0430,\u041c\u04d9\u0441\u043a\u0435\u0443", "latitude": 55.76167, "longitude": 37.60667, "population": 11503501, "time zone": "Europe/Moscow"}, {"geonamesId": 1488747, "name": "Tyumenskaya Oblast\u2019", "alternative names": "Oblast de Tioumen,Tiumen,Tjumen,Tjumen',Tjumenskaja Oblast',Tjumenskaja oblast',Tyumen,Tyumen Oblast,Tyumen' Oblast,Tyumenskaya,Tyumenskaya Oblast',Tyumenskaya Oblast\u2019,Tyumen\u2019 Oblast,\u0422\u044e\u043c\u0435\u043d\u0441\u043a\u0430\u044f \u041e\u0431\u043b\u0430\u0441\u0442\u044c,\u0422\u044e\u043c\u0435\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c,\u0422\u044e\u043c\u0435\u043d\u044c", "latitude": 57.33333, "longitude": 68.5, "population": 1316577, "time zone": "Asia/Yekaterinburg"}, {"northern": "Tyumenskaya Oblast\u2019"}, {"time_dif": 2}]