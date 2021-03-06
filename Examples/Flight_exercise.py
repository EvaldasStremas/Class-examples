available_flights = [
    {"from": "City Y", "to": "City X", "price": 60, "flight id": "000"},
    {"from": "City X", "to": "City Z", "price": 78, "flight id": "001"},
    {"from": "City Y", "to": "City T", "price": 91, "flight id": "002"},
    {"from": "City Z", "to": "City Y", "price": 58, "flight id": "003"},
    {"from": "City E", "to": "City X", "price": 100, "flight id": "004"},
    {"from": "City T", "to": "City W", "price": 49, "flight id": "005"},
    {"from": "City Z", "to": "City T", "price": 45, "flight id": "006"},
    {"from": "City X", "to": "City W", "price": 205, "flight id": "007"},
    {"from": "City Z", "to": "City T", "price": 56, "flight id": "008"},
    {"from": "City W", "to": "City T", "price": 40, "flight id": "009"},
    {"from": "City Y", "to": "City M", "price": 50, "flight id": "010"},
    {"from": "City X", "to": "City W", "price": 45, "flight id": "011"},
]

class flights:

    def get_city_t_ids(self, available_flights):
        available_destinations = []

        for i in range(len(available_flights)):
            res = available_flights[i].get('to')
            if res == 'City T': 
                available_destinations.append(available_flights[i].get('flight id'))

        return available_destinations

    def all_available_city_destinations(self, available_flights):
        all_a_d = []

        for i in range(len(available_flights)):
            all_city = available_flights[i].get('to')
            all_a_d.append(all_city)
            
        all_a_d = set(all_a_d)

        return all_a_d

    def from_x_to_w(self, available_flights):
        x_cities_list = []
        to_w_city_list = []

        # Get all from City X cities
        for i in range(len(available_flights)):
            if available_flights[i].get('from') == 'City X':
                x_cities_list.append(available_flights[i])

        # Get all to City W cities
        for i in range(len(x_cities_list)):
            if x_cities_list[i].get('to') == 'City W':
                to_w_city_list.append(x_cities_list[i])

        return to_w_city_list

    def get_lowest_price_line(self, available_flights):
        price_list = []

        for i in range(len(available_flights)):
            price_list.append(available_flights[i].get('price'))
            price_list.sort()
            lowest_value = price_list[0]

            if available_flights[i].get('price') == lowest_value:
                lowest_price_line = available_flights[i]
            
        # print(lowest_price_line)
        return lowest_price_line

f = flights()
print('All available IDs flight to "City T":')
print(f.get_city_t_ids(available_flights))
print('All available cities:')
print(f.all_available_city_destinations(available_flights))
print('Cheapest trip from "City X" to "City W":')
print(f.get_lowest_price_line(f.from_x_to_w(available_flights)))