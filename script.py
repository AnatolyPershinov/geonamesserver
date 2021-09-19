from aiohttp import web
from operator import attrgetter, itemgetter

class City:
    def __init__(self, geonamesId, name, alt_names, lat, long, population, time_zone):
        self.geonamesId = int(geonamesId)
        self.name = name
        self.alt_names = alt_names
        self.latitude = float(lat)
        self.longitude = float(long)
        self.population = int(population)
        self.time_zone = time_zone

    def check_altname(self, alt_name):
        return alt_name in self.alt_names

    def json(self):
        return {
            "geonamesId":self.geonamesId,
            "name": self.name,
            "alternative names": self.alt_names,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "population": self.population,
            "time zone": self.time_zone
        }

    def __repr__(self):
        return "%d  %s  %s  %f  %f  %d  %s\n" % (self.geonamesId, self.name, self.alt_names,
                                                self.latitude, self.longitude, self.population, self.time_zone)       

class Cities:
    def __init__(self):
        
        self.cities = list()

    def add_city(self, city):
        self.cities.append(city)

    def find_by_id(self, id):
        for city in self.cities:
            if id == city.geonamesId:
                return city

    def create_page(self, number, size):
        pages = list()
        for k in range(0, len(self.cities), size):
            pages.append(self.cities[k:k+size])
        pages.append(self.cities[-size:])
        return pages[number-1]

    def find_by_name(self, name):
        result = list()
        for city in self.cities:
            if city.check_altname(name) or name == city.name:
                result.append(city)
        return result

    def set_timezones(self, file):
        self.time_zones = dict()
        with open("timezones.txt", "r", encoding="UTF-8") as f:
            content= f.read().split("\n")
            for row in content:
                row = row.split("-")
                self.time_zones[row[0]] = int(row[1])
        f.close()

    def __repr__(self):
        result = ""
        for i in self.cities:
            result += i.__repr__()
        return result

cities_list = Cities()

with open("RU.txt", "r", encoding="UTF-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        row = line.strip().split("\t")
        if row[-5] != "" and row[-5] != "0":
            cities_list.add_city(City(
                geonamesId=row[0], 
                name=row[1],  
                alt_names=row[3], 
                lat=row[4], 
                long=row[5],
                population=row[-5],
                time_zone=row[-2]
                )
            )
    f.close()

cities_list.set_timezones("timezones.txt")

routes = web.RouteTableDef()

@routes.get("/city/{geonamesid}")
async def get_city_by_id(request):
    geonamesid = request.match_info['geonamesid']
    result = cities_list.find_by_id(int(geonamesid))
    if result == None:
        return web.Response(text="requested city not found")
    return web.json_response(result.json())

@routes.get("/page-{page_n}")
async def get_pages(request):
    page_size = request.rel_url.query['size']
    page_number = request.match_info['page_n']
    try:
        page = cities_list.create_page(number=int(page_number), size=int(page_size))
    except Exception as exc:
        print(exc)
        return web.Response(text="Wrong request")
    res = list()
    for row in page:
        res.append(row.json())
    return web.json_response(res)
        
@routes.get("/compare")
async def compare_two_cities(request):
    city1_name = request.rel_url.query['city1']
    city2_name = request.rel_url.query['city2']
    if city1_name == city2_name: 
        if len(cities_list.find_by_name(city1_name)) > 1:
            res = sorted(cities_list.find_by_name(city1_name), key=attrgetter("population"))
            city1 = res[-1]
            city2 = res[0]
        else:
            return web.Response(text=f"There is only one city with this name")
    else:
        try:
            city1 = sorted(cities_list.find_by_name(city1_name), key=attrgetter("population"))[-1]
            city2 = sorted(cities_list.find_by_name(city2_name), key=attrgetter("population"))[-1]
        except Exception:
            return web.Response(text="Incorrect request parameters")

    result = [city1.json(), city2.json()]
    if city1.latitude > city2.latitude:
        result.append({"northern":city1.name})
    else:
        result.append({"northern":city2.name}) 
    timezones = (cities_list.time_zones[city1.time_zone], cities_list.time_zones[city2.time_zone])
    if timezones[0] == timezones[1]:
        result.append({"time_dif": 0})
    else:
        result.append({"time_dif":abs(timezones[0]-timezones[1])})
    return web.json_response(result)


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8000, host="127.0.0.1")
