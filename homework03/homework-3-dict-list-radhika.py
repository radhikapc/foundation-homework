#Radhika PC
#5/31/2016
#Homework 2- dictionaries

#Make a list of dictionaries of five places across the world

cities_info = [
{ 'name': 'Moscow', 'latitude': 55.755826, 'longitude': 37.617300 },
{ 'name': 'Tehran', 'latitude': 35.689197, 'longitude': 51.388974 },
{ 'name': 'Falkland Islands', 'latitude': -51.7962536, 'longitude': -59.523613 },
{ 'name': 'Seoul', 'latitude': 36.069247, 'longitude': 120.318393 },
{ 'name': 'Santiago', 'latitude': 42.878213, 'longitude': -8.544844 }
]

tree = { 'name': 'Great Banyan', 'species': 'Moraceae', 'age': '250', 'location_name': 'culcutta' , 'latitude': 22.579335, 'longitude': 88.371582 }

for cities in cities_info:
    if int(cities['latitude']) > 0:
        print(cities['name'], "is above the equator")
    else:
        print(cities['name'], "is below the equator")
        if cities['name']=='Falkland Islands':
            print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    if int(cities['latitude']) > int(tree['latitude']):
        print(cities['name'], "is north of", tree['name'])
    else:
        print(cities['name'], "is south of", tree['name'])
