#Radhika PC
#5/31/2016
#Homework3
#Make a list called "countries" with 7 different countries and NOT be in order
nations =['India','Pakistan','Bangladesh','SriLanka','Nepal','Bhutan','Afghanistan']
#Using a for loop, print each element of the list
for nation in nations:
    print(nation)
#Sort the list permanently.
sorted_nations= sorted(nations)
print(sorted_nations)
#Display the first element of the list
print("The first element of the list is",sorted_nations[0])
#Display the second-to-last element of the list using a line of code that will work no matter what the size of the list
print("The second to last element of the list is", sorted_nations[len(sorted_nations)-2])
#Delete one of the countries from the list using its name
sorted_nations.pop()
for sorted_nation in sorted_nations:
    print(sorted_nation)
