#Radhika PC
#5/31/2016
#Homework 2- dictionaries
#Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'
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
