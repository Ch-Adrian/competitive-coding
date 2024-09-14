

cities = {"Białystok": 0, "Olsztyn": 1, "Warszawa": 2, "Lublin": 3, "Bydgoszcz": 4, "Gdańsk": 5, "Łódź": 6, "Poznań": 7, "Szczecin": 8, "Gorzów Wielkopolski": 9, "Wrocław": 10, "Opole": 11, "Katowice": 12, "Kielce": 13, "Kraków": 14, "Rzeszów": 15}
amount, starting_point = input().split(' ')
amount = int(amount)
system = [[] for _ in range(len(cities)) ]

def delete_way(city1, city2):
    for idx, city in enumerate(system[cities[city1]]):
        if city[0] == cities[city2]:
            system.pop(idx)
    for idx, city in enumerate(system[cities[city2]]):
        if city[0] == cities[city1]:
            system.pop(idx)

def concatenate_cities(city1, city2):
    new_name = city1+city2
    delete_way(city1, city2)
    cities[new_name] = len(cities)
    for city_id in cities:
        tmp_idx = -1
        tmp_city = -1
        for idx, city in enumerate(system[city_id]):
            if city[0] == cities[city1]:
                city[0] = cities[new_name]
                if tmp_idx == -1

            if city[0] == cities[city2]:
                city[0] = cities[new_name]


for city_nr in range(1, amount+1):
    for i in range(amount - city_nr):
        city1, city2, time = input().split(' ')
        time = int(time)
        system[cities[city1]].append((cities[city2], time))
        system[cities[city2]].append((cities[city1], time))
    
    
        
