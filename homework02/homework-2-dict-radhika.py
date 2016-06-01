#Radhika PC
#5/25/2016
#Homework 2- dictionaries

movie = { 'title': 'spy', 'release': '2015', 'director': 'Paul Feig', 'budget': '65000000' , 'revenue': '233125712'  }

print("My favorite movie is", movie['title'], "which was released in", movie['release'], "and was directed by", movie['director'])
#flop or success ?

if int(movie['budget']) < int(movie['revenue']):
    print("Wow,that was a good investment!")
else:
    print("It was a flop!")

# population of NYC
#Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000
NYC = { 'Manhattan': '1.6', 'Brooklyn': '2.6', 'Bronx': '1.4', 'Queens': '2.3' , 'Staten Island': '0.47'  }
#Display the population of Brooklyn.
print("The population of Brooklyn is", float(NYC['Brooklyn']))
#Display the combined population of all five boroughs.
total_population = float(NYC['Manhattan']) + float(NYC['Brooklyn']) + float(NYC['Bronx']) + float(NYC['Queens']) + float(NYC['Staten Island'])
print("The total NYC population is", total_population, "million")
#Display what percent of NYC's population lives in Manhattan.
Manhattan_percent = float(NYC['Manhattan']) / total_population * 100
print(Manhattan_percent, "% of total polution lives in Manhattan")
