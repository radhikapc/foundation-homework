# Grade: 13 / 14

#Radhika PC
#5/31/2016
#Homework3
#Make a list called "countries" with 7 different countries and NOT be in order


nations =['India','Pakistan','Bangladesh','SriLanka','Nepal','Bhutan','Afghanistan']
#Using a for loop, print each element of the list
for nation in nations:
    print(nation)
#Sort the list permanently.

# TA-COMMENT: (-0.5) This technically does not sort of our original list permanently -- if we were to print(nations), it would not be sorted. To sort a list permanently, you should use nations.sort().

sorted_nations= sorted(nations)
print(sorted_nations)
#Display the first element of the list
print("The first element of the list is",sorted_nations[0])
#Display the second-to-last element of the list using a line of code that will work no matter what the size of the list
print("The second to last element of the list is", sorted_nations[len(sorted_nations)-2])
#Delete one of the countries from the list using its name

# TA-COMMENT: (-0.5) You removed the last element, but you didn't delete one of the countries using its name like the directions specified. This works: sorted_nations.remove("Afghanistan")
sorted_nations.pop()
for sorted_nation in sorted_nations:
    print(sorted_nation)

tree = { 'name': 'Great Banyan', 'species': 'Moraceae', 'age': '250', 'location_name': 'culcutta' , 'latitude': 22.579335, 'longitude': 88.371582 }
#print statement
print(tree['name'], "is a", tree['age'], "years old tree that is in", tree['location_name'])

#The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC
NY_latitude = 40.7128
NY_longitude = 74.0059
if tree['latitude'] > NY_latitude:
    print(tree['name'],"in", tree['location_name'], "is north of NYC")
else:
    print(tree['name'],"in", tree['location_name'], "is south of NYC")
#Ask the user how old they are.
your_age=input("How old are you?")

tree_age = int(tree['age'])

#If they are younger than the tree, display "{name} was {XXX} years old when you were born."
if int(your_age) < tree_age:
    difference = tree_age - int(your_age)
    print(tree['name'], "was", difference, "years old when you were born")
#If they are older than the tree, display "you are {XXX} years older than {name}.
else:
    new_diff = int(your_age) - tree_age
    print("You are", new_diff, "years older than", tree['name'])


cities_info = [
{ 'name': 'Moscow', 'latitude': 55.755826, 'longitude': 37.617300 },
{ 'name': 'Tehran', 'latitude': 35.689197, 'longitude': 51.388974 },
{ 'name': 'Falkland Islands', 'latitude': -51.7962536, 'longitude': -59.523613 },
{ 'name': 'Seoul', 'latitude': 36.069247, 'longitude': 120.318393 },
{ 'name': 'Santiago', 'latitude': 42.878213, 'longitude': -8.544844 }

# TA-COMMENT: I think Soma meant Santiago, Chile -- this is actually an town called Santiago in Spain.

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
