#Radhika PC
#5/25/2016
#Homework 2- dictionaries

movie = { 'title': 'spy', 'release': '2015', 'director': 'Paul Feig', 'budget': '65000000' , 'revenue': '233125712'  }

# TA-COMMENT: (-0.5) We can add entries to a dictionary AFTER making it. We wanted to see:
# movie['budget'] = 65000000
# rather than "hard coding" budget and revenue into the initial dictionary.

print("My favorite movie is", movie['title'], "which was released in", movie['release'], "and was directed by", movie['director'])
#flop or success ?

# TA-COMMENT: (-0.5) This is not what Soma's directions ask for. His directions state: If the movie cost more to make than it made in theaters, print "It was a flop". If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."
if int(movie['budget']) < int(movie['revenue']):
    print("Wow,that was a good investment!")
else:
    print("It was a flop!")

# population of NYC
#Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000

# TA-COMMENT: You didn't have to store the numbers as strings; that would have saved you some work later (float() wouldn't be necessary).
NYC = { 'Manhattan': '1.6', 'Brooklyn': '2.6', 'Bronx': '1.4', 'Queens': '2.3' , 'Staten Island': '0.47'  }
#Display the population of Brooklyn.
print("The population of Brooklyn is", float(NYC['Brooklyn']))
#Display the combined population of all five boroughs.
total_population = float(NYC['Manhattan']) + float(NYC['Brooklyn']) + float(NYC['Bronx']) + float(NYC['Queens']) + float(NYC['Staten Island'])

# TA-COMMENT: What would have been a more programmatic way of handling the above question?

print("The total NYC population is", total_population, "million")
#Display what percent of NYC's population lives in Manhattan.
Manhattan_percent = float(NYC['Manhattan']) / total_population * 100
print(Manhattan_percent, "% of total polution lives in Manhattan")
