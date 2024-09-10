
#Math operators
#from math import ceil, floor
#Documentation from Microsoft learning path: Python for beginners

#Manipulate list data 
#Assumer you have a list with rainfall amounts for various month.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

#get all planets after earth
planets_after_earth = planets[3:8]
print(planets_after_earth)
#slice creates a new list and not modify the existing one. 

#join together again 
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']
regular_satelite_moons = amalthea_group + galilean_moons

## Remove any leading/trailing spaces from each moon name
regular_satelite_moons = [moon.strip() for moon in regular_satelite_moons]
#Sort
regular_satelite_moons.sort()
print("the regular satelite moons of jupiter are", regular_satelite_moons)

#exerciese work with list data --- 
#list of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'jupiter', 'Saturn', 'Uranus', 'Neptune']

#Get user input
user_planet = input("Enter planet name here: ")

#find the index of the users plante in the list 
planet_index = planets.index(user_planet)


# Display planets closer to the sun than the user's planet
print("Here are the planets closer than ", + user_planet + ':')

#display planets further
planet_index = planets.index(user_planet)

#NOT WORKING CORRETLY
